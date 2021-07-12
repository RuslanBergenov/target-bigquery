from tests import unittestcore
import os
import unittest

class TestJobLoad(unittestcore.BaseUnitTest):

    def test_simple_stream(self):
        from target_bigquery import main
        self.set_cli_args(
            stdin=os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'simple_stream.json'),
            config=os.environ.get("TARGET_CONFIG"),
            processhandler="load-job"
        )

        ret = main()
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

        self.delete_dataset()
        print(self.get_state())

    @unittest.skip("Skipped")
    def test_simple_stream_with_tables_config(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'simple_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            tables=os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'simple_stream_table_config.json'),
            processhandler="load-job"
        )

        ret = main()
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

        self.delete_dataset()
        print(self.get_state())

    @unittest.skip("Skipped")
    def test_complex_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin=os.path.join(
                os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tests'), 'rsc'),
                'complex_stream.json'),
            config=os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sandbox'),
                                'target-config.json'),
            processhandler="load-job"
        )

        ret = main()
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

        self.delete_dataset()
        print(self.get_state())

