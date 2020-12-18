import singer

from target_bigquery.schema import build_schema
from target_bigquery.simplify_json_schema import simplify
from tests import unittestcore
import collections

from tests.input_json_schemas import *

from tests.input_json_schemas_Bing_Ads_problem_column import problem_schema

from tests.utils import convert_list_of_schema_fielts_to_list_of_lists





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

    def test_nested_schema_simplify_then_build_v1_fails(self):

        # msg = singer.parse_message(schema_nested_1)
        # fails (2nd method doesn't build schema, because in simplified JSON schema anyOf data type appears in column Age)

        msg = singer.parse_message(schema_nested_1_subset_1_contains_age) # fails (same reason as above)
        # msg = singer.parse_message(schema_nested_1_subset_2_no_age) # succeeds (I removed age column)

        schema_input = msg.schema

        # schema conversion method 1: "Convert".
        # Method is taken from Adswerve fork of GitHub repo target-bigquery, dev-schema-fix branch
        schema_built_method_1 = build_schema(schema_input, key_properties=msg.key_properties, add_metadata=True)

        # schema conversion method 2: "Simplify and convert".
        # Simplification was taken from target-postgres repo. Conversion is the same as in method 1 above
        schema_simplified = simplify(schema_input)
        schema = build_schema(schema_simplified, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of columns
        assert collections.Counter(schema_built_method_1) == collections.Counter(schema)

        for f in schema:
            if f.name in ("date_start", "date_stop"):
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

            # TODO: Actually check nested fields and their data type

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




    def test_nested_schema_simplify_then_build_bing_ads(self):

        #TODO: fix error here
        # hypothesis: the error might be caused by a bug in Bing Ads tap
        # the input JSON schema for KeyValueOfstringbase is not correct, it doesn't match API documentation

        # msg = singer.parse_message(bing_ads_accounts)
        # fails because of KeyValueOfstringbase column. Both methods fail on it

        msg = singer.parse_message(problem_schema)

        # breaks at simplification stage

        # schema = 'KeyValueOfstringbase'
        #             def get_type(schema):
        #         """
        #         Given a JSON Schema dict, extracts the simplified `type` value
        #         :param schema: dict, JSON Schema
        #         :return: [string ...]
        #         """
        # >       t = schema.get('type', None)
        # E       AttributeError: 'str' object has no attribute 'get'

        # msg = singer.parse_message(bing_ads_campaigns) #success

        # msg = singer.parse_message(bing_ads_ad_extension_detail_report)  #success

        # msg = singer.parse_message(bing_ads_search_query_performance_report) #success

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