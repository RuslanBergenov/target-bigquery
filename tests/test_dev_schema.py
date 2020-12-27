import singer

from target_bigquery.dev_schema import dev_build_schema, prioritize_one_data_type_from_multiple_ones_in_anyOf, convert_field_type

from target_bigquery.schema import build_schema

from target_bigquery.simplify_json_schema import simplify
from tests import unittestcore
import collections

from tests.input_json_schemas import *

from tests.utils import convert_list_of_schema_fielts_to_list_of_lists

from tests.input_json_schemas_Bing_Ads_problem_column import problem_schema

from tests.input_json_schemas_age_anyOf_problem import test_schema_collection_anyOf_problem_column, test_schema_collection_anyOf_problem_column_short_version, test_schema_collection_anyOf_problem_column_removed


class TestStream(unittestcore.BaseUnitTest):

    def setUp(self):
        super(TestStream, self).setUp()

    def test_flat_schema(self):

        schema_0_input = schema_simple_1

        msg = singer.parse_message(schema_0_input)

        schema_1_simplified = simplify(msg.schema)

        schema_2_built_new_method = dev_build_schema(schema_1_simplified, key_properties=msg.key_properties,
                                                     add_metadata=True)

        schema_3_built_old_method = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        # are results of the two methods above identical? ignore order of columns
        assert collections.Counter(schema_2_built_new_method) == collections.Counter(schema_3_built_old_method)

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

    def test_prioritize_one_data_type_from_multiple_ones_in_anyOf(self):

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
                            'string',
                            'null'
                        ]
                    }
                ]
            }

        prioritized_data_type = prioritize_one_data_type_from_multiple_ones_in_anyOf(test_input)

        assert prioritized_data_type == "string"

        converted_data_type = convert_field_type(test_input)

        assert converted_data_type == "STRING"

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
            ]
        }

        prioritized_data_type = prioritize_one_data_type_from_multiple_ones_in_anyOf(test_input)

        assert prioritized_data_type == "number"

        converted_data_type = convert_field_type(test_input)

        assert converted_data_type == "FLOAT"

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









