import singer

from target_bigquery.schema import build_schema
from target_bigquery.simplify_json_schema import simplify
from tests import unittestcore
import collections

from tests.input_json_schemas import *


def convert_schema_field_to_list(input_schema_field):
    """
    This is a helper function to assist in comparing output of two methods of schema conversion from JSON to BigQuery.

    Input one SchemaField (can be nested), representing one column

    Go through one SchemaField and its nested SchemaFields. Convert from SchemaField to list. Sort the list and sublists

    Output a list
    """

    if len(input_schema_field.fields) == 0:

        return list((input_schema_field.name, input_schema_field.field_type, input_schema_field.mode,
                     input_schema_field.description, input_schema_field.fields, input_schema_field.policy_tags))

    elif len(input_schema_field.fields) > 0:

        processed_subfields = []

        for field in input_schema_field.fields:
            processed_subfields.append(convert_schema_field_to_list(field))

        return list((input_schema_field.name, input_schema_field.field_type, input_schema_field.mode,
                     input_schema_field.description, sorted(processed_subfields),
                     input_schema_field.policy_tags))


def convert_list_of_schema_fielts_to_list_of_lists(input_schema_fields_list):
    """
    This is a helper function to assist in comparing output of two methods of schema conversion from JSON to BigQuery.

    input a list of SchemaFields, representing a table

    apply function convert_schema_field_to_list to each SchemaField

    output a sorted list of lists

    """

    list_of_lists = []

    for schema_list_item in input_schema_fields_list:
        list_of_lists.append(convert_schema_field_to_list(schema_list_item))

    return sorted(list_of_lists)



class TestSimpleStream(unittestcore.BaseUnitTest):

    def setUp(self):
        super(TestSimpleStream, self).setUp()

    def test_flat_schema(self):

        schema = schema_simple_1

        msg = singer.parse_message(schema)

        schema = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        for f in schema:
            if f.name == "id":
                self.assertEqual(f.field_type.upper(), "STRING")

            elif f.name == "name":
                self.assertEqual(f.field_type.upper(), "STRING")

            elif f.name == "value":
                self.assertEqual(f.field_type.upper(), "INTEGER")

            elif f.name == "ratio":
                self.assertEqual(f.field_type.upper(), "FLOAT")

            elif f.name == "timestamp":
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

            elif f.name == "date":
                self.assertEqual(f.field_type.upper(), "DATE")


    def test_flat_schema_simplify_then_build_v1(self):

        schema = schema_simple_1

        msg = singer.parse_message(schema)

        # schema conversion method 1: "Convert". Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_test = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert". Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
        schema = simplify(msg.schema)
        schema = build_schema(schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of columns
        assert collections.Counter(schema_test) == collections.Counter(schema)

        for f in schema:
            if f.name == "id":
                self.assertEqual(f.field_type.upper(), "STRING")

            elif f.name == "name":
                self.assertEqual(f.field_type.upper(), "STRING")

            elif f.name == "value":
                self.assertEqual(f.field_type.upper(), "INTEGER")

            elif f.name == "ratio":
                self.assertEqual(f.field_type.upper(), "FLOAT")

            elif f.name == "timestamp":
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

            elif f.name == "date":
                self.assertEqual(f.field_type.upper(), "DATE")

    def test_flat_schema_simplify_then_build_v2(self):

        schema = schema_simple_2_short

        msg = singer.parse_message(schema)

        # schema conversion method 1: "Convert". Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_test = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert". Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
        schema = simplify(msg.schema)
        schema = build_schema(schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of columns
        assert collections.Counter(schema_test) == collections.Counter(schema)

        for f in schema:
            if f.name == "id":
                self.assertEqual(f.field_type.upper(), "STRING")

            elif f.name == "name":
                self.assertEqual(f.field_type.upper(), "STRING")

            elif f.name == "value":
                self.assertEqual(f.field_type.upper(), "INTEGER")

            elif f.name == "ratio":
                self.assertEqual(f.field_type.upper(), "FLOAT")

            elif f.name == "timestamp":
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

            elif f.name == "date":
                self.assertEqual(f.field_type.upper(), "DATE")


    def test_nested_schema_v1(self):

        schema = schema_nested_1

        msg = singer.parse_message(schema)

        schema = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        for f in schema:
            if f.name in ("date_start", "date_stop"):
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

            # TODO: Actually check nested fields and their data type

    def test_nested_schema_simplify_then_build_v1(self):

        # msg = singer.parse_message(schema_nested_1) # fails (2nd method doesn't build schema, because in simplified JSON schema anyOf data type appears in column Age)
        # msg = singer.parse_message(schema_nested_1_subset_1_contains_age) # fails (same reason as above)
        msg = singer.parse_message(schema_nested_1_subset_2_no_age) # succeeds (I removed age column)

        schema_input = msg.schema

        # schema conversion method 1: "Convert". Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_built_method_1 = build_schema(schema_input, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert". Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
        schema_simplified = simplify(schema_input)
        schema = build_schema(schema_simplified, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of columns
        assert collections.Counter(schema_built_method_1) == collections.Counter(schema)

        for f in schema:
            if f.name in ("date_start", "date_stop"):
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

            # TODO: Actually check nested fields and their data type


    def test_nested_schema_v2(self):

        schema = schema_nested_2

        msg = singer.parse_message(schema)

        schema = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        self.assertTrue(True)



    def test_nested_schema_simplify_then_build_v2(self):

        msg = singer.parse_message(schema_nested_2)

        schema_input = msg.schema

        # schema conversion method 1: "Convert". Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_built_method_1 = build_schema(schema_input, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert". Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
        schema_simplified = simplify(schema_input)
        schema_built_method_2 = build_schema(schema_simplified, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of column
        schema_built_method_1_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_1)

        schema_built_method_2_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_2)

        assert schema_built_method_1_sorted == schema_built_method_2_sorted

    def test_nested_schema_v3(self):
        schema = schema_nested_3

        msg = singer.parse_message(schema)

        schema = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        self.assertTrue(True)

    def test_nested_schema_simplify_then_build_v3(self):

        msg = singer.parse_message(schema_nested_3)

        schema_input = msg.schema

        # schema conversion method 1: "Convert". Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_built_method_1 = build_schema(schema_input, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert". Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
        schema_simplified = simplify(schema_input)
        schema_built_method_2 = build_schema(schema_simplified, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of column

        schema_built_method_1_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_1)

        schema_built_method_2_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_2)

        assert schema_built_method_1_sorted == schema_built_method_2_sorted