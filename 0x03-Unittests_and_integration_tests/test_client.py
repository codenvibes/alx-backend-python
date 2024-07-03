#!/usr/bin/env python3
"""
Unit tests for the GithubOrgClient class and its methods.
"""
import unittest
from urllib import response
from parameterized import parameterized, parameterized_class
from unittest import mock
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """
        Test the org method of GithubOrgClient.

        Parameters:
        - org (str): The name of the organization to test.
        - mock_org (Mock): Mock object for get_json.

        This method tests that GithubOrgClient.org returns the correct
        organization data without making actual HTTP calls. It mocks the
        get_json function to return a predefined dictionary and verifies
        the behavior of the org method.
        """
        org_test = GithubOrgClient(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()

    def test_public_repos_url(self):
        """
        Test the _public_repos_url property of GithubOrgClient.

        This method uses patch.object to mock the org property and verifies
        that _public_repos_url returns the correct repository URL.
        """
        with patch.object(GithubOrgClient,
                          'org',
                          new_callable=PropertyMock) as m:
            m.return_value = {"repos_url": "89"}
            test_org = GithubOrgClient('holberton')
            test_repo_url = test_org._public_repos_url
            self.assertEqual(test_repo_url, m.return_value.get('repos_url'))
            m.assert_called_once()

    @patch('client.get_json', return_value=[{'name': 'Holberton'},
                                            {'name': '89'},
                                            {'name': 'alx'}])
    def test_public_repos(self, mock_repo):
        """
        Test the public_repos method of GithubOrgClient.

        Parameters:
        - mock_repo (Mock): Mock object for get_json.

        This method uses patch.object to mock the _public_repos_url property
        and verifies that public_repos returns the correct list of repository
        names.
        """
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value="https://api.github.com/") as m:
            test_client = GithubOrgClient('holberton')
            test_repo = test_client.public_repos()
            for idx in range(3):
                self.assertIn(mock_repo.return_value[idx]['name'], test_repo)
            mock_repo.assert_called_once()
            m.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test the has_license method of GithubOrgClient.

        Parameters:
        - repo (dict): The repository dictionary to check.
        - license_key (str): The license key to check for.
        - expected (bool): The expected result.

        This method verifies that has_license correctly identifies if a
        repository has the specified license key.
        """
        test_instance = GithubOrgClient('holberton')
        license_available = test_instance.has_license(repo, license_key)
        self.assertEqual(license_available, expected)


def requests_get(*args, **kwargs):
    """
    Mock function for requests.get.

    This function returns a mock response object with a predefined JSON payload
    based on the URL passed in args.
    """
    class MockResponse:
        """
        Mock response class for simulating requests.Response.
        """
        def __init__(self, json_data):
            self.json_data = json_data

        def json(self):
            return self.json_data

    if args[0] == "https://api.github.com/orgs/google":
        return MockResponse(TEST_PAYLOAD[0][0])
    if args[0] == TEST_PAYLOAD[0][0]["repos_url"]:
        return MockResponse(TEST_PAYLOAD[0][1])


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    [(TEST_PAYLOAD[0][0], TEST_PAYLOAD[0][1], TEST_PAYLOAD[0][2],
      TEST_PAYLOAD[0][3])]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration tests for GithubOrgClient class.
    """
    @classmethod
    def setUpClass(cls):
        """
        Set up the class with mocked requests.get.

        This method starts a patcher for requests.get to use the requests_get
        mock function and creates an instance of GithubOrgClient.
        """
        cls.get_patcher = patch('utils.requests.get', side_effect=requests_get)
        cls.get_patcher.start()
        cls.client = GithubOrgClient('google')

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the class by stopping the patcher.

        This method stops the patcher for requests.get started in setUpClass.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test the public_repos method of GithubOrgClient.

        This method verifies that public_repos returns the expected list of
        repository names.
        """
        self.assertEqual(self.client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """
        Test the public_repos method with a license filter.

        This method verifies that public_repos returns the correct list of
        repository names that have the specified license.
        """
        self.assertEqual(
            self.client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )
