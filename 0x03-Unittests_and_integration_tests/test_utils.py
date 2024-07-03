#!/usr/bin/env python3
# AUTH: BNV
"""
Unit tests for the utils.access_nested_map function.
"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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
        Test access_nested_map with various inputs to ensure it returns the
        expected results.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_message):
        """
        Test access_nested_map to ensure it raises KeyError for invalid paths.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test case to verify the behavior of get_json function.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json with the test_url
        result = get_json(test_url)

        # Assertions:
        # Check if requests.get was called with test_url
        mock_get.assert_called_once_with(test_url)
        # Check if get_json returned the expected payload
        self.assertEqual(result, test_payload)
