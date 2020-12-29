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
                     input_schema_field.description, input_schema_field.fields, input_schema_field.policy_tags))

    elif len(input_schema_field.fields) > 0:

        processed_subfields = []

        for field in input_schema_field.fields:
            processed_subfields.append(convert_schema_field_to_list(field))

        return list((input_schema_field.name, input_schema_field.field_type.upper(), input_schema_field.mode.upper(),
                     input_schema_field.description, sorted(processed_subfields),
                     input_schema_field.policy_tags))


def convert_list_of_schema_fielts_to_list_of_lists(input_schema_fields_list):
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