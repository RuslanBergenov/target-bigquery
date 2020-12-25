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


def convert_field_type(field_property):
    conversion_dict = {"string": "STRING",
                       "number": "FLOAT",
                       "integer": "INTEGER",
                       "boolean": "BOOLEAN",
                       "date-time": "TIMESTAMP",
                       "date": "DATE",
                       "time": "TIME"
                       }

    if field_property["type"][0] == "string" and "format" in field_property:

        field_type_BigQuery = conversion_dict[field_property["format"]]

    else:

        field_type_BigQuery = conversion_dict[field_property["type"][0]]

    return field_type_BigQuery


def determine_field_mode(field_name):
    # required_fields = msg.key_properties

    if field_name in required_fields:

        field_mode = 'REQUIRED'
    else:

        field_mode = 'NULLABLE'

    return field_mode


def dev_build_schema(schema, key_properties=None, add_metadata=True, force_fields={}):

    global required_fields

    required_fields = set(key_properties) if key_properties else set()

    schema_BigQuery = []

    for field_name, field_property in schema.get("properties", schema.get("items", {}).get(
            "properties")).items():
        # print (field_name,
        #        field_property,
        #        # properties.get("type")[0],
        #        # conversion_dict[properties.get("type")[0]],
        #        '\n')

        schema_BigQuery.append(SchemaField(name=field_name,
                                           field_type=convert_field_type(field_property),
                                           mode=determine_field_mode(field_name),
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




