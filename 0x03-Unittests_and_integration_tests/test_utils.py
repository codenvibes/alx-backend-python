#!/usr/bin/env python3
# AUTH: BNV
"""
Unit tests for the utils.access_nested_map function.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map with various inputs to ensure it returns the expected results.

        Parameters
        ----------
        nested_map : dict
            A nested dictionary to access.
        path : tuple
            A sequence of keys representing the path to the value.
        expected : any
            The expected value at the end of the path in the nested dictionary.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
