"""
the purpose of this script is to convert JSON schema to BigQuery schema.
"""

from google.cloud.bigquery import SchemaField
import re

METADATA_FIELDS = {
    "_time_extracted": {"type": ["null", "string"], "format": "date-time", "bq_type": "timestamp"},
    "_time_loaded": {"type": ["null", "string"], "format": "date-time", "bq_type": "timestamp"}
}


def cleanup_record(schema, record):
    nr = {}

    if not isinstance(record, dict) and not isinstance(record, list):
        return record

    for key, value in record.items():
        nkey = bigquery_transformed_key(key)

        if isinstance(value, dict):
            nr[nkey] = cleanup_record(schema, value)

        elif isinstance(value, list):
            nr[nkey] = []
            for o in value:
                nr[nkey].append(cleanup_record(schema, o))

        else:
            nr[nkey] = value

    return nr


def bigquery_transformed_key(key):

    """
    :param key: JSON field name
    :return: cleaned up JSON field name
    """

    for pattern, repl in [(r"-", "_"), (r"\.", "_")]:
        key = re.sub(pattern, repl, key)

    if re.match(r"^\d", key):
        key = "_" + key

    return key


def prioritize_one_data_type_from_multiple_ones_in_anyOf(field_property):

    """
    :param field_property: JSON field property, which has anyOf and multiple data types
    :return: one BigQuery SchemaField field_type, which is prioritized

    Simplification step removes anyOf columns from original JSON schema.

    There's one instance when original JSON schema has no anyOf, but anyOf gets added:

    original JSON schema:

     "simplification_stage_adds_anyOf": {
      "type": [
        "null",
        "integer",
        "string"
      ]
    }

     This is a simplified JSON schema where anyOf got added during
     simplification stage:

      {'simplification_stage_added_anyOf': {
            'anyOf': [
                {
                    'type': [
                        'integer',
                        'null'
                    ]
                },
                {
                    'type': [
                        'string',
                        'null'
                    ]
                }
            ]
        }
        }

    The VALUE of this dictionary will be the INPUT for this function.

    This simplified case needs to be handled.

    Prioritization needs to be applied:
        1) STRING
        2) FLOAT
        3) INTEGER
        4) BOOLEAN

    OUTPUT of the function is one JSON data type with the top priority
    """

    prioritization_dict = {"string": 1,
                           "number": 2,
                           "integer": 3,
                           "boolean": 4}

    anyOf_data_types = {}

    for i in range(0, len(field_property['anyOf'])):

        data_type = field_property['anyOf'][i]['type'][0]

        anyOf_data_types.update({data_type: prioritization_dict[data_type]})

    # return key with minimum value, which is the highest priority data type
    # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    return min(anyOf_data_types, key=anyOf_data_types.get)


def convert_field_type(field_property):

    """
    :param field_property: JSON field property
    :return: BigQuery SchemaField field_type
    """

    conversion_dict = {"string": "STRING",
                       "number": "FLOAT",
                       "integer": "INTEGER",
                       "boolean": "BOOLEAN",
                       "date-time": "TIMESTAMP",
                       "date": "DATE",
                       "time": "TIME",
                       "object": "RECORD",
                       "array": "RECORD"
                       }

    if "anyOf" in field_property:

        prioritized_data_type = prioritize_one_data_type_from_multiple_ones_in_anyOf(field_property)

        field_type_BigQuery = conversion_dict[prioritized_data_type]

    elif field_property["type"][0] == "string" and "format" in field_property:

        field_type_BigQuery = conversion_dict[field_property["format"]]

    elif (("items" in field_property) and ("properties" not in field_property["items"])):

        field_type_BigQuery = conversion_dict[field_property['items']['type'][0]]

    else:

        field_type_BigQuery = conversion_dict[field_property["type"][0]]

    return field_type_BigQuery


def determine_field_mode(field_name, field_property):

    """
    :param field_name: one nested JSON field name
    :param field_property: one nested JSON field property
    :return: BigQuery SchemaField mode
    """

    if field_name in required_fields:

        field_mode = 'REQUIRED'

    elif "items" in field_property:

        field_mode = 'REPEATED'

    else:

        field_mode = 'NULLABLE'

    return field_mode


def build_field(field_name, field_property):

    """
    :param field_name: one nested JSON field name
    :param field_property: one nested JSON field property
    :return: one BigQuery nested SchemaField
    """

    if not ("items" in field_property and "properties" in field_property["items"]) and not ("properties" in field_property):

        return (SchemaField(name=bigquery_transformed_key(field_name),
                            field_type=convert_field_type(field_property),
                            mode=determine_field_mode(field_name, field_property),
                            description=None,
                            fields=(),
                            policy_tags=None)
                )

    elif ("items" in field_property and "properties" in field_property["items"]) or ("properties" in field_property):

        processed_subfields = []

        # https://www.w3schools.com/python/ref_dictionary_get.asp
        for subfield_name, subfield_property in field_property.get("properties",
                                                                   field_property.get("items", {}).get("properties")
                                                                   ).items():

            processed_subfields.append(build_field(subfield_name, subfield_property))

        return (SchemaField(name=bigquery_transformed_key(field_name),
                            field_type=convert_field_type(field_property),
                            mode=determine_field_mode(field_name, field_property),
                            description=None,
                            fields=processed_subfields,
                            policy_tags=None)
                )


def build_schema(schema, key_properties=None, add_metadata=True, force_fields={}):

    """

    :param schema: input simplified JSON schema
    :param key_properties: JSON schema fields which will become required BigQuery column
    :param add_metadata: do we want BigQuery metadata columns (e.g., when data was uploaded?)
    :param force_fields: TODO: add explanation. force_fields are from table_config dictionary.
    :return: a list of BigQuery SchemaFields, which represents one BigQuery table
    """

    global required_fields

    required_fields = set(key_properties) if key_properties else set()

    schema_BigQuery = []

    for field_name, field_property in schema.get("properties", schema.get("items", {}).get(
            "properties")).items():

        schema_BigQuery.append(build_field(field_name, field_property))

    if add_metadata:

        for field_name in METADATA_FIELDS:
            schema_BigQuery.append(SchemaField(name=field_name,
                                               field_type=METADATA_FIELDS[field_name]["bq_type"],
                                               mode='NULLABLE',
                                               description=None,
                                               fields=(),
                                               policy_tags=None)
                                   )

    return schema_BigQuery


