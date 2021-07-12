import singer

from target_bigquery.schema import build_schema, prioritize_one_data_type_from_multiple_ones_in_anyOf, convert_field_type

from tests.schema_old import build_schema_old

from target_bigquery.simplify_json_schema import simplify
from tests import unittestcore

from tests.rsc.input_json_schemas import *

from tests.utils import convert_list_of_schema_fields_to_list_of_lists, compare_old_vs_new_schema_conversion

import os

class TestStream(unittestcore.BaseUnitTest):

    def setUp(self):
        super(TestStream, self).setUp()

    def test_flat_schema(self):

        schema_0_input = schema_simple_1

        msg = singer.parse_message(schema_0_input)

        schema_1_simplified = simplify(msg.schema)

        schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)

        schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical?

        assert schema_2_built_new_method == schema_3_built_old_method

        for f in schema_2_built_new_method:
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

    def test_prioritize_one_data_type_from_multiple_ones_in_anyOf_string(self):

        test_input = {
                'anyOf': [
                    {
                        'type': [
                            'integer',
                            'null'
                        ]
                    },
                    {
                        'type': [
                            'boolean',
                            'null'
                        ]
                    },
                    {
                        'type': [
                            'string',
                            'null'
                        ]
                    }
                    ,
                    {
                        'type': [
                            'number',
                            'null'
                        ]
                    }
                ]
            }

        prioritized_data_type = prioritize_one_data_type_from_multiple_ones_in_anyOf(test_input)

        assert prioritized_data_type == "string"

        converted_data_type = convert_field_type(test_input)

        assert converted_data_type == "STRING"

    def test_prioritize_one_data_type_from_multiple_ones_in_anyOf_float(self):


        test_input = {
            'anyOf': [
                {
                    'type': [
                        'number',
                        'null'
                    ]
                },
                {
                    'type': [
                        'integer',
                        'null'
                    ]
                }
                ,
                {
                    'type': [
                        'boolean',
                        'null'
                    ]
                }
            ]
        }

        prioritized_data_type = prioritize_one_data_type_from_multiple_ones_in_anyOf(test_input)

        assert prioritized_data_type == "number"

        converted_data_type = convert_field_type(test_input)

        assert converted_data_type == "FLOAT"

    def test_prioritize_one_data_type_from_multiple_ones_in_anyOf_integer(self):

        test_input = {
            'anyOf': [

                {
                    'type': [
                        'integer',
                        'null'
                    ]
                }
                ,
                {
                    'type': [
                        'boolean',
                        'null'
                    ]
                }
            ]
        }

        prioritized_data_type = prioritize_one_data_type_from_multiple_ones_in_anyOf(test_input)

        assert prioritized_data_type == "integer"

        converted_data_type = convert_field_type(test_input)

        assert converted_data_type == "INTEGER"






    def test_nested_schema_1(self):

        schema_0_input = schema_nested_1

        msg = singer.parse_message(schema_0_input)

        schema_1_simplified = simplify(msg.schema)

        schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)

        schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical?
        assert schema_2_built_new_method == schema_3_built_old_method

        for f in schema_2_built_new_method:
            if f.name in ("date_start", "date_stop"):
                self.assertEqual(f.field_type.upper(), "TIMESTAMP")

    def test_nested_schema_2(self):

        schema_0_input = schema_nested_2

        msg = singer.parse_message(schema_0_input)

        schema_1_simplified = simplify(msg.schema)

        schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)

        schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of columns and case
        schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

        schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

        assert schema_built_new_method_sorted == schema_built_old_method_sorted

    def test_several_nested_schemas(self):

        list_of_schema_inputs = [test_schema_collection_anyOf_problem_column,
                                 schema_nested_1,
                                 schema_nested_1_subset_items_problem,
                                 schema_nested_2,
                                 schema_nested_3_shopify,
                                 bing_ads_campaigns,
                                 bing_ads_ad_extension_detail_report,
                                 bing_ads_ad_group_performance_report,
                                 bing_ads_ad_performance_report,
                                 bing_ads_age_gender_audience_report,
                                 bing_ads_audience_performance_report,
                                 bing_ads_campaign_performance_report,
                                 bing_ads_geographic_performance_report,
                                 bing_ads_goals_and_funnels_report,
                                 bing_ads_keyword_performance_report,
                                 bing_ads_search_query_performance_report,
                                 recharge_addresses,
                                 recharge_charges,
                                 recharge_orders
                                 ]

        for next_schema_input in list_of_schema_inputs:

            schema_0_input = next_schema_input

            msg = singer.parse_message(schema_0_input)

            schema_1_simplified = simplify(msg.schema)

            schema_2_built_new_method = build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                         add_metadata=True)

            schema_3_built_old_method = build_schema_old(msg.schema, key_properties=msg.key_properties, add_metadata=True)

            # are results of the two methods above identical? ignore order of columns and case
            schema_built_new_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_2_built_new_method)

            schema_built_old_method_sorted = convert_list_of_schema_fields_to_list_of_lists(schema_3_built_old_method)

            assert schema_built_new_method_sorted == schema_built_old_method_sorted

            # TODO: check data types



    def test_several_nested_schemas_amazon(self):

        filepath = os.path.join(os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'), 'input_json_schemas_amazon.json')

        compare_old_vs_new_schema_conversion(filepath)







