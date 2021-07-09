# https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory
import unittest
import os

loader = unittest.TestLoader()
tests_dir = os.path.abspath(".")
suite = loader.discover(tests_dir)

runner = unittest.TextTestRunner()

if __name__ == "__main__": # this line prevents tests from running twice
    runner.run(suite)


#TODO: CI/CD
# how do I run a test which uses a sensitive file from gitignored sandbox directory???
# how do I change the name on the status badge?
