import re
import singer

LOGGER = singer.get_logger()


def validate_json_schema_completeness(schema_input):
    """
    Background
        - We already do have schema validation implemented with json schema library.
        - However, we had situations when a schema had empty properties, but existing json schema validator didn't flag
            it as invalid/incomplete (it happened with Shopify schema).

    The purpose of this function is
        - to flag schema as invalid if it is incomplete.

    :param schema_input: JSON schema. It can be dictionary/JSON object or string.

    What the function does

        Clean input:
            - If it's not a string, we'll convert it to string.

        Validation steps:
            - If schema has empty {} inside its "properties", "type" or "items", fail schema completeness validation check.
                - To help the end user, we'll tell them which part of schema has empty {} (properties, type or items).
            - If schema has empty {} elsewhere, a warning is logged.

        Rationale for our validation steps:
            - empty props, type or items clearly indicate invalid/incomplete schema
            - {} elsewhere also indicates invalid/incomplete schema, it may cause pipeline failure,
                but we want to relax the rules a bit
                and we don't want to be too heavy-handed
    """

    # convert to string
    schema_input_as_string = str(schema_input)

    # strip spaces from schema file (which is treated as text)
    schema_input_no_spaces = re.sub(' |\n', '', schema_input_as_string)

    # regex match for patterns of incomplete schema
    # the purpose of the dictionary below is to create a more user-friendly error message and point the end user to the
    # correponding part of their schema (props, type, items or elsewhere)
    completeness_validation_dict_exception = {"properties": re.compile(r'\"properties\"\:\{\}'),
                                              "type": re.compile(r'\"type\"\:\[\]'),
                                              "items": re.compile(r'\"items\"\:\{\}')
                                              }

    completeness_validation_dict_warning = {
        "object/dictionary": re.compile(r'\{\}')
    }

    # raise exception
    for schema_element, pattern_not_valid in completeness_validation_dict_exception.items():

        if pattern_not_valid.search(schema_input_no_spaces):
            raise ValueError("JSON schema is invalid/incomplete. It has empty {}".format(schema_element))

    # give warning
    for schema_element, pattern_not_valid in completeness_validation_dict_warning.items():

        if pattern_not_valid.search(schema_input_no_spaces):
            LOGGER.warning("the pipeline might fail because of undefined fields: {}")
