import logging
import unittest
from cython_example_proj import c_hello

"""
Some basic tests
"""


class TestSTL(unittest.TestCase):

    def c_hello(self):
        c_hello()

if __name__ == '__main__':
    unittest.main()
