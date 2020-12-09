import singer

from target_bigquery.schema import build_schema
from target_bigquery.simplify_json_schema import simplify
from tests import unittestcore
import collections

from tests.input_json_schemas import *

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

    def test_nested_schema_v2(self):

        schema = schema_nested_2

        msg = singer.parse_message(schema)

        schema = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        self.assertTrue(True)

    def test_nested_schema_v3(self):
        schema = schema_nested_3

        msg = singer.parse_message(schema)

        schema = build_schema(msg.schema, key_properties=msg.key_properties, add_metadata=True)

        self.assertTrue(True)

