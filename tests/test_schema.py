import singer

from target_bigquery.schema import build_schema, clean_up_schema_anyOf
from target_bigquery.simplify_json_schema import simplify
from tests import unittestcore
import collections

from tests.input_json_schemas import *

from tests.utils import convert_list_of_schema_fielts_to_list_of_lists

from tests.input_json_schemas_Bing_Ads_problem_column import problem_schema

from tests.input_json_schemas_age_anyOf_problem import test_schema_collection_anyOf_problem_column, test_schema_collection_anyOf_problem_column_short_version, test_schema_collection_anyOf_problem_column_removed


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

        # schema conversion method 1: "Convert".
        # Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_test = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert".
        # Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
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

        # schema conversion method 1: "Convert".
        # Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_test = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert".
        # Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
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

        msg = singer.parse_message(schema_nested_1_subset_1_contains_age)

        schema_input = msg.schema

        # schema conversion method 1: "Convert".
        # Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_built_method_1 = build_schema(schema_input, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert".
        # Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above

        schema_simplified = simplify(schema_input) #anyOf is introduced here for column "Age" of Bing Ads

        schema = build_schema(clean_up_schema_anyOf(schema_simplified), key_properties=msg.key_properties, add_metadata=True)
        # are results of the two methods above identical? ignore order of columns
        assert collections.Counter(schema_built_method_1) == collections.Counter(schema)

        for f in schema:
            if f.name in ("date_start", "date_stop"):
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

            # TODO: Actually check nested fields and their data type

    def test_nested_schema_simplify_then_build_age_anyOf_problem(self):

        msg = singer.parse_message(test_schema_collection_anyOf_problem_column)

        schema_input = msg.schema

        # schema conversion method 1: "Convert".
        # Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_built_method_1 = build_schema(schema_input, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert".
        # Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
        schema_simplified = simplify(schema_input) #anyOf is introduced here for column "Age" of Bing Ads

        schema_cleaned_up = clean_up_schema_anyOf(schema_simplified)

        schema_built_method_2 = build_schema(schema_cleaned_up, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of column

        schema_built_method_1_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_1)

        schema_built_method_2_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_2)

        assert schema_built_method_1_sorted == schema_built_method_2_sorted

        for f in schema_built_method_2:
             if f.name in ("date_start", "date_stop"):
                 self.assertEqual(f.field_type.upper(), "TIMESTAMP")

             # TODO: Actually check nested fields and their data type


    def test_build_schema_v1(self):

        msg = singer.parse_message(test_schema_collection_anyOf_problem_column)

        schema_input = {'type': ['object', 'null'], 'properties': {
            'simplification_stage_adds_anyOf': {
                'anyOf': [{'type': ['integer', 'null']}, {'type': ['string', 'null']}]
            }
        }
                        }

        schema_cleaned = clean_up_schema_anyOf(schema_input)

        schema_built_method_1 = build_schema(schema_cleaned, key_properties=msg.key_properties, add_metadata=True)

        self.assertTrue(schema_built_method_1)



    def test_nested_schema_simplify_then_build_v1_succeeds(self):

        # msg = singer.parse_message(schema_nested_1)
        # fails (2nd method doesn't build schema, because in simplified JSON schema anyOf data type appears in column Age)

        # msg = singer.parse_message(schema_nested_1_subset_1_contains_age) # fails (same reason as above)
        msg = singer.parse_message(schema_nested_1_subset_2_no_age) # succeeds (I removed age column)

        schema_input = msg.schema

        # schema conversion method 1: "Convert".
        # Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_built_method_1 = build_schema(schema_input, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert". S
        # implification was taken from target-postgres repo. Conversion is the same as in method 1 above
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

        # schema conversion method 1: "Convert".
        # Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_built_method_1 = build_schema(schema_input, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert".
        # Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
        schema_simplified = simplify(schema_input)
        schema_built_method_2 = build_schema(schema_simplified, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of column
        schema_built_method_1_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_1)

        schema_built_method_2_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_2)

        assert schema_built_method_1_sorted == schema_built_method_2_sorted

    def test_nested_schema_v3(self):
        schema = schema_nested_3_shopify

        msg = singer.parse_message(schema)

        schema = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        self.assertTrue(True)

    def test_nested_schema_simplify_then_build_v3(self):

        msg = singer.parse_message(schema_nested_3_shopify)

        schema_input = msg.schema

        # schema conversion method 1: "Convert".
        # Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_built_method_1 = build_schema(schema_input, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert".
        # was taken from target-postgres repo. Conversion is the same as in method 1 above
        schema_simplified = simplify(schema_input)
        schema_built_method_2 = build_schema(schema_simplified, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of column

        schema_built_method_1_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_1)

        schema_built_method_2_sorted = convert_list_of_schema_fielts_to_list_of_lists(schema_built_method_2)

        assert schema_built_method_1_sorted == schema_built_method_2_sorted
