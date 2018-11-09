import unittest
import os
import time
import random
import subprocess

print(time.ctime(time.time()))
print(time.ctime(time.time()))
class unitTestFramework(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(),'FOO')
        print("inside test_upper")

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        print("inside test_isupper")

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(),['hello','world'])


if __name__ == "__main__":
    unittest.main()
