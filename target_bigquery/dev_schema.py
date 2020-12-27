# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 16:20:49 2020

@author: Ruslan Bergenov
"""
import singer
from google.cloud.bigquery import SchemaField

METADATA_FIELDS = {
    "_time_extracted": {"type": ["null", "string"], "format": "date-time", "bq_type": "timestamp"},
    "_time_loaded": {"type": ["null", "string"], "format": "date-time", "bq_type": "timestamp"}
}


def prioritize_one_data_type_from_multiple_ones_in_anyOf(field_property):
    """
    In simplified JSON schema, anyOf columns are gone.

    There's one instance when input JSON schema has no anyOf, but anyOf gets added:

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

    # return key with minimum value
    # return the highest priority data type
    # https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    return min(anyOf_data_types, key=anyOf_data_types.get)


def convert_field_type(field_property):

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

    else:

        field_type_BigQuery = conversion_dict[field_property["type"][0]]

    return field_type_BigQuery


def determine_field_mode(field_name, field_property):

    if field_name in required_fields:

        field_mode = 'REQUIRED'

    elif "items" in field_property:

        field_mode = 'REPEATED'

    else:

        field_mode = 'NULLABLE'

    return field_mode


def dev_build_schema(schema, key_properties=None, add_metadata=True, force_fields={}):

    global required_fields

    required_fields = set(key_properties) if key_properties else set()

    schema_BigQuery = []

    for field_name, field_property in schema.get("properties", schema.get("items", {}).get(
            "properties")).items():

        schema_BigQuery.append(SchemaField(name=field_name,
                                           field_type=convert_field_type(field_property),
                                           mode=determine_field_mode(field_name, field_property),
                                           description=None,
                                           fields=(),
                                           policy_tags=None)
                               )

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




