import json
import singer
import copy

from tests.schema_old import build_schema_old

from target_bigquery.schema import build_schema

from target_bigquery.simplify_json_schema import simplify

from target_bigquery.validate_json_schema import validate_json_schema_completeness


def convert_schema_field_to_list(input_schema_field):
    """
    Helper function for unit testing.

    Help to compare two BigQuery schemas. Ignore order of columns and case.

    Recursive function which converts 1 nested BigQuery SchemaField (one column) to a sorted nested list,
    so it's easier to compare 2 BigQuery schemas, when they have a different sort order

    This is a helper function to assist in unit test,
    which compares outputs of two ways  of schema conversion from JSON to BigQuery.

    Steps:
        Goes through one SchemaField and its nested SchemaFields.
        Converts nested SchemaField to nested lists.
        Sorts the list and sublists.
        Uppercase field type and mode.

    Parameters
    ----------
    input_schema_field: SchemaField(SchemaField)

        Input one SchemaField (can be nested), representing one column.

        Example:

        >>> SchemaField('BiddingScheme','RECORD', 'NULLABLE', None, (SchemaField('Type', 'STRING', 'NULLABLE', None, (), None), SchemaField('InheritedBidStrategyType', 'STRING', 'NULLABLE', None, (),None), SchemaField('MaxCpc','RECORD', 'NULLABLE', None, (SchemaField('Money', 'INTEGER', 'REQUIRED', None, (), None),SchemaField('Amount', 'FLOAT', 'NULLABLE', None, (), None),), None)), None)

    Output - one nested list, representing one column
    ----------
    List[List]

        Example:

        ['BiddingScheme',
            'RECORD',
          'NULLABLE',
          None,
          [['InheritedBidStrategyType', 'STRING', 'NULLABLE', None, (), None],
           ['MaxCpc',
            'RECORD',
            'NULLABLE',
            None,
            [['Amount', 'FLOAT', 'NULLABLE', None, (), None],
             ['Money', 'INTEGER', 'REQUIRED', None, (), None]],
            None],
           ['Type', 'STRING', 'NULLABLE', None, (), None]],
          None]

    ----------

    """

    if len(input_schema_field.fields) == 0:

        return list((input_schema_field.name, input_schema_field.field_type.upper(), input_schema_field.mode.upper(),
                     input_schema_field.fields, input_schema_field.policy_tags))

    elif len(input_schema_field.fields) > 0:

        processed_subfields = []

        for field in input_schema_field.fields:
            processed_subfields.append(convert_schema_field_to_list(field))

        return list((input_schema_field.name, input_schema_field.field_type.upper(), input_schema_field.mode.upper(),
                    sorted(processed_subfields),
                     input_schema_field.policy_tags))


def convert_list_of_schema_fields_to_list_of_lists(input_schema_fields_list):
    """
    This is a helper function to assist in comparing output of two methods of schema conversion from JSON to BigQuery.

    Iterate through a list of SchemaFields and apply the function convert_schema_field_to_list to each SchemaField.



    Parameters
    ----------
    input_schema_fields_list:
        input a list of SchemaFields, representing a table

        Example:

        >>> [SchemaField('BiddingScheme','RECORD', 'NULLABLE', None, (SchemaField('Type', 'STRING', 'NULLABLE', None, (), None),SchemaField('InheritedBidStrategyType', 'STRING', 'NULLABLE', None, (),None), SchemaField('MaxCpc','RECORD', 'NULLABLE', None, (SchemaField('Money', 'INTEGER', 'REQUIRED', None, (), None),SchemaField('Amount', 'FLOAT', 'NULLABLE', None, (), None),), None)), None), SchemaField('AudienceAdsBidAdjustment', 'INTEGER', 'NULLABLE', None, (), None)]


    Output
    ----------
    sorted(list_of_lists) - List[List[List]]
        output a sorted list of nested lists, representing a table

        Example:

        [['AudienceAdsBidAdjustment', 'INTEGER', 'NULLABLE', None, (), None],
         ['BiddingScheme',
          'RECORD',
          'NULLABLE',
          None,
          [['InheritedBidStrategyType', 'STRING', 'NULLABLE', None, (), None],
           ['MaxCpc',
            'RECORD',
            'NULLABLE',
            None,
            [['Amount', 'FLOAT', 'NULLABLE', None, (), None],
             ['Money', 'INTEGER', 'REQUIRED', None, (), None]],
            None],
           ['Type', 'STRING', 'NULLABLE', None, (), None]],
          None]]

    """

    list_of_lists = []

    for schema_list_item in input_schema_fields_list:
        list_of_lists.append(convert_schema_field_to_list(schema_list_item))

    return sorted(list_of_lists)


def compare_old_vs_new_schema_conversion(catalog_schema_file, exclude_stream=None):

    """
    :param catalog_schema_file: input JSON schema / tap catalog json file
    :param exclude_stream:
    :param only_test_stream:

    convert JSON schema using old vs new method. Make sure results are identical. Ignore order of fields.
    """

    catalog = json.load(open(catalog_schema_file))

    for next_schema_input in catalog['streams']:

        if next_schema_input['tap_stream_id'] == exclude_stream:
            continue

        # make sure stream doesn't have empty (undefined object {}) type or properties
        validate_json_schema_completeness(next_schema_input)

        # clean up schema formatting
        schema_0_input = copy.deepcopy(next_schema_input)

        if "type" not in schema_0_input.keys():
            schema_0_input.update({"type": "SCHEMA"})

        if "key_properties" not in schema_0_input.keys():
            schema_0_input.update({"key_properties": "Id"})

        schema_0_input = str(schema_0_input)

        schema_0_input = schema_0_input.replace("\'", "\"").replace("True", "true").replace("False", "false").replace("None", "null")

        # convert schema using old vs. new method
        msg = singer.parse_message(schema_0_input)

        schema_1_simplified = simplify(msg.schema)

        schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                 add_metadata=True)

        schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of columns and case
        schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

        schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

        assert schema_built_new_method_sorted == schema_built_old_method_sorted

