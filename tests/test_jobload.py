from tests import unittestcore
import unittest

"""
Tests:
Load truncate tables with partition fields (should fail)
Load truncate tables without partition (rows should == expected #)
Load append tables with partition field of int or string (should fail)

"""



class TestJobLoad(unittestcore.BaseUnitTest):
    @unittest.skip("Skipped")
    def test_simple_stream(self):
        from target_bigquery import main

        self.set_cli_args(
            stdin="./rsc/simple_stream.json",
            config="../sandbox/target-config.json",
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
            stdin="./rsc/simple_stream.json",
            config="../sandbox/target-config.json",
            tables="./rsc/simple_stream_table_config.json",
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
            stdin="./rsc/complex_stream.json",
            config="../sandbox/target-config.json",
            processhandler="load-job"
        )

        ret = main()
        self.assertEqual(ret, 0, msg="Exit code is not 0!")

        self.delete_dataset()
        print(self.get_state())

