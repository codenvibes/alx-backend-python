<h1 align="center"><b>0X03. UNITTESTS AND INTEGRATION TESTS</b></h1>
<div align="center"><code>UnitTests</code> <code>Back-end</code> <code>Integration tests</code></div>

<br>
<div align="center"><img alt="" src="https://github.com/codenvibes/alx-backend-python/blob/master/0x03-Unittests_and_integration_tests/images/f088970b450e82c881ea.gif"></div>
<br>

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be [mocked](https://github.com/codenvibes/alx-backend-python/blob/master/0x03-Unittests_and_integration_tests/notes/mocking.md#mocking), especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with
```
$ python -m unittest path/to/test_file.py
```

<br>
<hr>
<h3><a href="https://github.com/codenvibes/alx-backend-python/tree/master/0x03-Unittests_and_integration_tests/notes">Notes</a></h3>
<hr>


<!--==================================================-->
<br>

## Resources
<details>
<summary><b><a href="https://docs.python.org/3/library/unittest.html">unittest — Unit testing framework</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://docs.python.org/3/library/unittest.mock.html">unittest.mock — mock object library</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock">How to mock a readonly property with mock?</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://pypi.org/project/parameterized/">parameterized</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href="https://pypi.org/project/parameterized/">Memoization</a></b></summary><br>


<br><p align="center">※※※※※※※※※※※※</p><br>
</details>



<!--==================================================-->
<br>

## Learning Objectives
<details>
<summary><b><a href=" "> </a>The difference between unit and integration tests.</b></summary><br>

**Unit testing is a type of automated testing where code is written to test a small isolated unit of the application. That small unit can be a function, a module or a component.**

**Integration tests focus on testing the interaction between multiple components or systems to ensure they work together as expected.**


### Unit Tests
1. **Scope**:
   - Unit tests focus on testing individual components or functions of the code in isolation.
   - The primary goal is to ensure that each unit of the codebase works as expected.

2. **Isolation**:
   - Unit tests isolate the piece of code being tested from other parts of the application.
   - They often use mock objects, stubs, or fakes to replace dependencies.

3. **Speed**:
   - Unit tests are typically fast to execute because they test small parts of the code in isolation without involving external systems like databases or web services.

4. **Granularity**:
   - They are fine-grained and test the smallest possible units of code, such as methods or functions.

5. **Purpose**:
   - Unit tests help identify bugs in the logic of individual units and provide quick feedback to developers.
   - They facilitate refactoring and help maintain code quality by ensuring each part of the code works correctly on its own.

### Integration Tests
1. **Scope**:
   - Integration tests focus on testing the interaction between multiple components or systems.
   - The primary goal is to ensure that different units work together as expected.

2. **Isolation**:
   - Integration tests do not isolate components; they test the integrated behavior of the system.
   - They often involve actual databases, web services, or other external systems to verify that the integration works correctly.

3. **Speed**:
   - Integration tests are generally slower than unit tests because they involve multiple components and possibly external systems.

4. **Granularity**:
   - They are more coarse-grained compared to unit tests and test the interaction and data flow between units.

5. **Purpose**:
   - Integration tests help identify issues in the way different parts of the system interact with each other.
   - They ensure that the integrated components function together as expected and catch errors that unit tests might miss due to their isolated nature.

### Summary
- **Unit Tests**: Test individual components in isolation, fast, fine-grained, identify logic errors within units.
- **Integration Tests**: Test the interaction between components, slower, coarse-grained, identify issues in the integration and data flow between units.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<details>
<summary><b><a href=" "> </a>Common testing patterns such as mocking, parametrizations and fixtures</b></summary><br>

Testing patterns are strategies used to make tests more readable, maintainable, and effective. Here are some common testing patterns and techniques:

### Mocking
Mocking is the practice of replacing real objects with mocks, which simulate the behavior of real objects. This is useful for isolating the unit of code under test and for simulating different scenarios.

- **Purpose**: To isolate the unit of code being tested and to simulate different conditions or behaviors.
- **Common Libraries**: `unittest.mock` in Python, `Mockito` in Java, `Sinon.js` in JavaScript.

**Example (Python with unittest.mock)**:
```python
from unittest.mock import MagicMock
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.json()

def test_fetch_data():
    mock_response = MagicMock()
    mock_response.json.return_value = {"key": "value"}
    
    with unittest.mock.patch('requests.get', return_value=mock_response):
        result = fetch_data('http://example.com')
        assert result == {"key": "value"}
```

### Parametrization
Parametrization is the practice of running the same test with different inputs. This helps in verifying that the code works correctly for a range of input values and scenarios.

- **Purpose**: To test the same functionality with different inputs efficiently.
- **Common Libraries**: `pytest` in Python, `JUnit` in Java, `Jest` in JavaScript.

**Example (Python with pytest)**:
```python
import pytest

@pytest.mark.parametrize("input, expected", [
    ("abc", 3),
    ("", 0),
    ("hello", 5),
])
def test_string_length(input, expected):
    assert len(input) == expected
```

### Fixtures
Fixtures are used to set up a known state before tests run and to clean up afterward. They can provide context or data needed for tests and help ensure tests are isolated and repeatable.

- **Purpose**: To prepare a consistent and reusable environment for tests.
- **Common Libraries**: `pytest` in Python, `JUnit` in Java, `Mocha` in JavaScript.

**Example (Python with pytest)**:
```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_sample_data(sample_data):
    assert sample_data["name"] == "John"
    assert sample_data["age"] == 30
```

### Summary of Common Testing Patterns
1. **Mocking**: Replaces real objects with mock objects to isolate the unit of code being tested.
2. **Parametrization**: Runs the same test with different inputs to ensure the code works correctly for a variety of cases.
3. **Fixtures**: Sets up and tears down the test environment to provide a consistent context for tests.

By using these testing patterns, you can create more robust, maintainable, and effective tests that help ensure the quality of your code.

<br><p align="center">※※※※※※※※※※※※</p><br>
</details>


<!--==================================================-->
<br>

## Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using <code>python3</code> (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly <code>#!/usr/bin/env python3</code>
- A <code>README.md</code> file, at the root of the folder of the project, is mandatory
- Your code should use the <code>pycodestyle</code> style (version 2.5)
- All your files must be executable
- All your modules should have a documentation (<code>python3 -c 'print(__import__("my_module").__doc__)'</code>)
- All your classes should have a documentation (<code>python3 -c 'print(__import__("my_module").MyClass.__doc__)'</code>)
- All your functions (inside and outside a class) should have a documentation (<code>python3 -c 'print(__import__("my_module").my_function.__doc__)'</code> and <code>python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'</code>)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

<!--==================================================-->
<br>

## Required Files
<h3><code>utils.py</code> (or <a href="https://intranet-projects-files.s3.amazonaws.com/webstack/utils.py" target="_blank" title="download">download</a>)</h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre><code>
#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -&gt; Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    Example
    -------
    &gt;&gt;&gt; nested_map = {"a": {"b": {"c": 1}}}
    &gt;&gt;&gt; access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -&gt; Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -&gt; Callable:
    """Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    &gt;&gt;&gt; my_object = MyClass()
    &gt;&gt;&gt; my_object.a_method
    a_method called
    42
    &gt;&gt;&gt; my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
</code>
</pre>
</details>

<h3><code>client.py</code> (or <a href="https://intranet-projects-files.s3.amazonaws.com/webstack/client.py" target="_blank" title="download">download</a>)</h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre><code>
#!/usr/bin/env python3
"""A github org client
"""
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class GithubOrgClient:
    """A Githib org client
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -&gt; None:
        """Init method of GithubOrgClient"""
        self._org_name = org_name

    @memoize
    def org(self) -&gt; Dict:
        """Memoize org"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -&gt; str:
        """Public repos URL"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -&gt; Dict:
        """Memoize repos payload"""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -&gt; List[str]:
        """Public repos"""
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -&gt; bool:
        """Static: has_license"""
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license
</code>
</pre>
</details>

<h3><code>fixtures.py</code> (or <a href="https://intranet-projects-files.s3.amazonaws.com/webstack/fixtures.py" target="_blank" title="download">download</a>)</h3>

<details>
<summary>Click to show/hide file contents</summary>
<pre><code>
#!/usr/bin/env python3

TEST_PAYLOAD = [
  (
    {"repos_url": "https://api.github.com/orgs/google/repos"},
    [
      {
        "id": 7697149,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
        "name": "episodes.dart",
        "full_name": "google/episodes.dart",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
        "html_url": "https://github.com/google/episodes.dart",
        "description": "A framework for timing performance of web apps.",
        "fork": False,
        "url": "https://api.github.com/repos/google/episodes.dart",
        "forks_url": "https://api.github.com/repos/google/episodes.dart/forks",
        "keys_url": "https://api.github.com/repos/google/episodes.dart/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/episodes.dart/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/episodes.dart/teams",
        "hooks_url": "https://api.github.com/repos/google/episodes.dart/hooks",
        "issue_events_url": "https://api.github.com/repos/google/episodes.dart/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/episodes.dart/events",
        "assignees_url": "https://api.github.com/repos/google/episodes.dart/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/episodes.dart/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/episodes.dart/tags",
        "blobs_url": "https://api.github.com/repos/google/episodes.dart/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/episodes.dart/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/episodes.dart/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/episodes.dart/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/episodes.dart/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/episodes.dart/languages",
        "stargazers_url": "https://api.github.com/repos/google/episodes.dart/stargazers",
        "contributors_url": "https://api.github.com/repos/google/episodes.dart/contributors",
        "subscribers_url": "https://api.github.com/repos/google/episodes.dart/subscribers",
        "subscription_url": "https://api.github.com/repos/google/episodes.dart/subscription",
        "commits_url": "https://api.github.com/repos/google/episodes.dart/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/episodes.dart/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/episodes.dart/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/episodes.dart/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/episodes.dart/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/episodes.dart/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/episodes.dart/merges",
        "archive_url": "https://api.github.com/repos/google/episodes.dart/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/episodes.dart/downloads",
        "issues_url": "https://api.github.com/repos/google/episodes.dart/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/episodes.dart/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/episodes.dart/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/episodes.dart/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/episodes.dart/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/episodes.dart/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/episodes.dart/deployments",
        "created_at": "2013-01-19T00:31:37Z",
        "updated_at": "2019-09-23T11:53:58Z",
        "pushed_at": "2014-10-09T21:39:33Z",
        "git_url": "git://github.com/google/episodes.dart.git",
        "ssh_url": "git@github.com:google/episodes.dart.git",
        "clone_url": "https://github.com/google/episodes.dart.git",
        "svn_url": "https://github.com/google/episodes.dart",
        "homepage": None,
        "size": 191,
        "stargazers_count": 12,
        "watchers_count": 12,
        "language": "Dart",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 22,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
          "key": "bsd-3-clause",
          "name": "BSD 3-Clause \"New\" or \"Revised\" License",
          "spdx_id": "BSD-3-Clause",
          "url": "https://api.github.com/licenses/bsd-3-clause",
          "node_id": "MDc6TGljZW5zZTU="
        },
        "forks": 22,
        "open_issues": 0,
        "watchers": 12,
        "default_branch": "master",
        "permissions": {
          "admin": False,
          "push": False,
          "pull": True
        }
      },
      {
        "id": 7776515,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
        "name": "cpp-netlib",
        "full_name": "google/cpp-netlib",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
        "html_url": "https://github.com/google/cpp-netlib",
        "description": "The C++ Network Library Project -- header-only, cross-platform, standards compliant networking library.",
        "fork": True,
        "url": "https://api.github.com/repos/google/cpp-netlib",
        "forks_url": "https://api.github.com/repos/google/cpp-netlib/forks",
        "keys_url": "https://api.github.com/repos/google/cpp-netlib/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/cpp-netlib/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/cpp-netlib/teams",
        "hooks_url": "https://api.github.com/repos/google/cpp-netlib/hooks",
        "issue_events_url": "https://api.github.com/repos/google/cpp-netlib/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/cpp-netlib/events",
        "assignees_url": "https://api.github.com/repos/google/cpp-netlib/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/cpp-netlib/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/cpp-netlib/tags",
        "blobs_url": "https://api.github.com/repos/google/cpp-netlib/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/cpp-netlib/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/cpp-netlib/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/cpp-netlib/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/cpp-netlib/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/cpp-netlib/languages",
        "stargazers_url": "https://api.github.com/repos/google/cpp-netlib/stargazers",
        "contributors_url": "https://api.github.com/repos/google/cpp-netlib/contributors",
        "subscribers_url": "https://api.github.com/repos/google/cpp-netlib/subscribers",
        "subscription_url": "https://api.github.com/repos/google/cpp-netlib/subscription",
        "commits_url": "https://api.github.com/repos/google/cpp-netlib/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/cpp-netlib/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/cpp-netlib/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/cpp-netlib/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/cpp-netlib/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/cpp-netlib/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/cpp-netlib/merges",
        "archive_url": "https://api.github.com/repos/google/cpp-netlib/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/cpp-netlib/downloads",
        "issues_url": "https://api.github.com/repos/google/cpp-netlib/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/cpp-netlib/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/cpp-netlib/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/cpp-netlib/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/cpp-netlib/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/cpp-netlib/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/cpp-netlib/deployments",
        "created_at": "2013-01-23T14:45:32Z",
        "updated_at": "2019-11-15T02:26:31Z",
        "pushed_at": "2018-12-05T17:42:29Z",
        "git_url": "git://github.com/google/cpp-netlib.git",
        "ssh_url": "git@github.com:google/cpp-netlib.git",
        "clone_url": "https://github.com/google/cpp-netlib.git",
        "svn_url": "https://github.com/google/cpp-netlib",
        "homepage": "http://cpp-netlib.github.com/",
        "size": 8937,
        "stargazers_count": 292,
        "watchers_count": 292,
        "language": "C++",
        "has_issues": False,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 59,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
          "key": "bsl-1.0",
          "name": "Boost Software License 1.0",
          "spdx_id": "BSL-1.0",
          "url": "https://api.github.com/licenses/bsl-1.0",
          "node_id": "MDc6TGljZW5zZTI4"
        },
        "forks": 59,
        "open_issues": 0,
        "watchers": 292,
        "default_branch": "master",
        "permissions": {
          "admin": False,
          "push": False,
          "pull": True
        }
      },
      {
        "id": 7968417,
        "node_id": "MDEwOlJlcG9zaXRvcnk3OTY4NDE3",
        "name": "dagger",
        "full_name": "google/dagger",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
        "html_url": "https://github.com/google/dagger",
        "description": "A fast dependency injector for Android and Java.",
        "fork": True,
        "url": "https://api.github.com/repos/google/dagger",
        "forks_url": "https://api.github.com/repos/google/dagger/forks",
        "keys_url": "https://api.github.com/repos/google/dagger/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/dagger/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/dagger/teams",
        "hooks_url": "https://api.github.com/repos/google/dagger/hooks",
        "issue_events_url": "https://api.github.com/repos/google/dagger/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/dagger/events",
        "assignees_url": "https://api.github.com/repos/google/dagger/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/dagger/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/dagger/tags",
        "blobs_url": "https://api.github.com/repos/google/dagger/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/dagger/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/dagger/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/dagger/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/dagger/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/dagger/languages",
        "stargazers_url": "https://api.github.com/repos/google/dagger/stargazers",
        "contributors_url": "https://api.github.com/repos/google/dagger/contributors",
        "subscribers_url": "https://api.github.com/repos/google/dagger/subscribers",
        "subscription_url": "https://api.github.com/repos/google/dagger/subscription",
        "commits_url": "https://api.github.com/repos/google/dagger/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/dagger/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/dagger/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/dagger/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/dagger/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/dagger/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/dagger/merges",
        "archive_url": "https://api.github.com/repos/google/dagger/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/dagger/downloads",
        "issues_url": "https://api.github.com/repos/google/dagger/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/dagger/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/dagger/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/dagger/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/dagger/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/dagger/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/dagger/deployments",
        "created_at": "2013-02-01T23:14:14Z",
        "updated_at": "2019-12-03T12:39:55Z",
        "pushed_at": "2019-11-27T21:20:38Z",
        "git_url": "git://github.com/google/dagger.git",
        "ssh_url": "git@github.com:google/dagger.git",
        "clone_url": "https://github.com/google/dagger.git",
        "svn_url": "https://github.com/google/dagger",
        "homepage": "https://dagger.dev",
        "size": 59129,
        "stargazers_count": 14492,
        "watchers_count": 14492,
        "language": "Java",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 1741,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 148,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
          "spdx_id": "Apache-2.0",
          "url": "https://api.github.com/licenses/apache-2.0",
          "node_id": "MDc6TGljZW5zZTI="
        },
        "forks": 1741,
        "open_issues": 148,
        "watchers": 14492,
        "default_branch": "master",
        "permissions": {
          "admin": False,
          "push": False,
          "pull": True
        }
      },
      {
        "id": 8165161,
        "node_id": "MDEwOlJlcG9zaXRvcnk4MTY1MTYx",
        "name": "ios-webkit-debug-proxy",
        "full_name": "google/ios-webkit-debug-proxy",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
        "html_url": "https://github.com/google/ios-webkit-debug-proxy",
        "description": "A DevTools proxy (Chrome Remote Debugging Protocol) for iOS devices (Safari Remote Web Inspector).",
        "fork": False,
        "url": "https://api.github.com/repos/google/ios-webkit-debug-proxy",
        "forks_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/forks",
        "keys_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/teams",
        "hooks_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/hooks",
        "issue_events_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/events",
        "assignees_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/tags",
        "blobs_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/languages",
        "stargazers_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/stargazers",
        "contributors_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/contributors",
        "subscribers_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/subscribers",
        "subscription_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/subscription",
        "commits_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/merges",
        "archive_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/downloads",
        "issues_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/deployments",
        "created_at": "2013-02-12T19:08:19Z",
        "updated_at": "2019-12-04T02:06:43Z",
        "pushed_at": "2019-11-24T07:02:13Z",
        "git_url": "git://github.com/google/ios-webkit-debug-proxy.git",
        "ssh_url": "git@github.com:google/ios-webkit-debug-proxy.git",
        "clone_url": "https://github.com/google/ios-webkit-debug-proxy.git",
        "svn_url": "https://github.com/google/ios-webkit-debug-proxy",
        "homepage": "",
        "size": 680,
        "stargazers_count": 4630,
        "watchers_count": 4630,
        "language": "C",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": False,
        "has_pages": False,
        "forks_count": 395,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 24,
        "license": {
          "key": "other",
          "name": "Other",
          "spdx_id": "NOASSERTION",
          "url": None,
          "node_id": "MDc6TGljZW5zZTA="
        },
        "forks": 395,
        "open_issues": 24,
        "watchers": 4630,
        "default_branch": "master",
        "permissions": {
          "admin": False,
          "push": False,
          "pull": True
        }
      },
      {
        "id": 8459994,
        "node_id": "MDEwOlJlcG9zaXRvcnk4NDU5OTk0",
        "name": "google.github.io",
        "full_name": "google/google.github.io",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
        "html_url": "https://github.com/google/google.github.io",
        "description": None,
        "fork": False,
        "url": "https://api.github.com/repos/google/google.github.io",
        "forks_url": "https://api.github.com/repos/google/google.github.io/forks",
        "keys_url": "https://api.github.com/repos/google/google.github.io/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/google.github.io/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/google.github.io/teams",
        "hooks_url": "https://api.github.com/repos/google/google.github.io/hooks",
        "issue_events_url": "https://api.github.com/repos/google/google.github.io/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/google.github.io/events",
        "assignees_url": "https://api.github.com/repos/google/google.github.io/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/google.github.io/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/google.github.io/tags",
        "blobs_url": "https://api.github.com/repos/google/google.github.io/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/google.github.io/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/google.github.io/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/google.github.io/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/google.github.io/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/google.github.io/languages",
        "stargazers_url": "https://api.github.com/repos/google/google.github.io/stargazers",
        "contributors_url": "https://api.github.com/repos/google/google.github.io/contributors",
        "subscribers_url": "https://api.github.com/repos/google/google.github.io/subscribers",
        "subscription_url": "https://api.github.com/repos/google/google.github.io/subscription",
        "commits_url": "https://api.github.com/repos/google/google.github.io/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/google.github.io/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/google.github.io/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/google.github.io/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/google.github.io/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/google.github.io/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/google.github.io/merges",
        "archive_url": "https://api.github.com/repos/google/google.github.io/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/google.github.io/downloads",
        "issues_url": "https://api.github.com/repos/google/google.github.io/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/google.github.io/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/google.github.io/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/google.github.io/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/google.github.io/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/google.github.io/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/google.github.io/deployments",
        "created_at": "2013-02-27T16:21:19Z",
        "updated_at": "2019-12-03T01:38:02Z",
        "pushed_at": "2019-12-03T01:37:58Z",
        "git_url": "git://github.com/google/google.github.io.git",
        "ssh_url": "git@github.com:google/google.github.io.git",
        "clone_url": "https://github.com/google/google.github.io.git",
        "svn_url": "https://github.com/google/google.github.io",
        "homepage": None,
        "size": 8,
        "stargazers_count": 38,
        "watchers_count": 38,
        "language": "HTML",
        "has_issues": False,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": False,
        "has_pages": True,
        "forks_count": 44,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": None,
        "forks": 44,
        "open_issues": 0,
        "watchers": 38,
        "default_branch": "master",
        "permissions": {
          "admin": False,
          "push": False,
          "pull": True
        }
      },
      {
        "id": 8566972,
        "node_id": "MDEwOlJlcG9zaXRvcnk4NTY2OTcy",
        "name": "kratu",
        "full_name": "google/kratu",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
        "html_url": "https://github.com/google/kratu",
        "description": None,
        "fork": False,
        "url": "https://api.github.com/repos/google/kratu",
        "forks_url": "https://api.github.com/repos/google/kratu/forks",
        "keys_url": "https://api.github.com/repos/google/kratu/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/kratu/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/kratu/teams",
        "hooks_url": "https://api.github.com/repos/google/kratu/hooks",
        "issue_events_url": "https://api.github.com/repos/google/kratu/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/kratu/events",
        "assignees_url": "https://api.github.com/repos/google/kratu/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/kratu/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/kratu/tags",
        "blobs_url": "https://api.github.com/repos/google/kratu/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/kratu/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/kratu/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/kratu/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/kratu/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/kratu/languages",
        "stargazers_url": "https://api.github.com/repos/google/kratu/stargazers",
        "contributors_url": "https://api.github.com/repos/google/kratu/contributors",
        "subscribers_url": "https://api.github.com/repos/google/kratu/subscribers",
        "subscription_url": "https://api.github.com/repos/google/kratu/subscription",
        "commits_url": "https://api.github.com/repos/google/kratu/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/kratu/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/kratu/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/kratu/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/kratu/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/kratu/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/kratu/merges",
        "archive_url": "https://api.github.com/repos/google/kratu/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/kratu/downloads",
        "issues_url": "https://api.github.com/repos/google/kratu/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/kratu/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/kratu/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/kratu/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/kratu/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/kratu/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/kratu/deployments",
        "created_at": "2013-03-04T22:52:33Z",
        "updated_at": "2019-11-15T22:22:16Z",
        "pushed_at": "2017-08-06T05:44:34Z",
        "git_url": "git://github.com/google/kratu.git",
        "ssh_url": "git@github.com:google/kratu.git",
        "clone_url": "https://github.com/google/kratu.git",
        "svn_url": "https://github.com/google/kratu",
        "homepage": None,
        "size": 1777,
        "stargazers_count": 280,
        "watchers_count": 280,
        "language": "JavaScript",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 32,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
          "spdx_id": "Apache-2.0",
          "url": "https://api.github.com/licenses/apache-2.0",
          "node_id": "MDc6TGljZW5zZTI="
        },
        "forks": 32,
        "open_issues": 0,
        "watchers": 280,
        "default_branch": "master",
        "permissions": {
          "admin": False,
          "push": False,
          "pull": True
        }
      },
      {
        "id": 8858648,
        "node_id": "MDEwOlJlcG9zaXRvcnk4ODU4NjQ4",
        "name": "build-debian-cloud",
        "full_name": "google/build-debian-cloud",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
        "html_url": "https://github.com/google/build-debian-cloud",
        "description": "Script to create Debian Squeeze &amp; Wheezy Amazon Machine Images (AMIs) and Google Compute Engine images",
        "fork": True,
        "url": "https://api.github.com/repos/google/build-debian-cloud",
        "forks_url": "https://api.github.com/repos/google/build-debian-cloud/forks",
        "keys_url": "https://api.github.com/repos/google/build-debian-cloud/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/build-debian-cloud/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/build-debian-cloud/teams",
        "hooks_url": "https://api.github.com/repos/google/build-debian-cloud/hooks",
        "issue_events_url": "https://api.github.com/repos/google/build-debian-cloud/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/build-debian-cloud/events",
        "assignees_url": "https://api.github.com/repos/google/build-debian-cloud/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/build-debian-cloud/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/build-debian-cloud/tags",
        "blobs_url": "https://api.github.com/repos/google/build-debian-cloud/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/build-debian-cloud/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/build-debian-cloud/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/build-debian-cloud/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/build-debian-cloud/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/build-debian-cloud/languages",
        "stargazers_url": "https://api.github.com/repos/google/build-debian-cloud/stargazers",
        "contributors_url": "https://api.github.com/repos/google/build-debian-cloud/contributors",
        "subscribers_url": "https://api.github.com/repos/google/build-debian-cloud/subscribers",
        "subscription_url": "https://api.github.com/repos/google/build-debian-cloud/subscription",
        "commits_url": "https://api.github.com/repos/google/build-debian-cloud/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/build-debian-cloud/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/build-debian-cloud/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/build-debian-cloud/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/build-debian-cloud/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/build-debian-cloud/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/build-debian-cloud/merges",
        "archive_url": "https://api.github.com/repos/google/build-debian-cloud/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/build-debian-cloud/downloads",
        "issues_url": "https://api.github.com/repos/google/build-debian-cloud/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/build-debian-cloud/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/build-debian-cloud/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/build-debian-cloud/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/build-debian-cloud/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/build-debian-cloud/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/build-debian-cloud/deployments",
        "created_at": "2013-03-18T16:32:00Z",
        "updated_at": "2019-09-23T11:54:00Z",
        "pushed_at": "2014-06-17T18:52:10Z",
        "git_url": "git://github.com/google/build-debian-cloud.git",
        "ssh_url": "git@github.com:google/build-debian-cloud.git",
        "clone_url": "https://github.com/google/build-debian-cloud.git",
        "svn_url": "https://github.com/google/build-debian-cloud",
        "homepage": "",
        "size": 986,
        "stargazers_count": 32,
        "watchers_count": 32,
        "language": "Shell",
        "has_issues": False,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": False,
        "has_pages": False,
        "forks_count": 22,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 5,
        "license": {
          "key": "other",
          "name": "Other",
          "spdx_id": "NOASSERTION",
          "url": None,
          "node_id": "MDc6TGljZW5zZTA="
        },
        "forks": 22,
        "open_issues": 5,
        "watchers": 32,
        "default_branch": "master",
        "permissions": {
          "admin": False,
          "push": False,
          "pull": True
        }
      },
      {
        "id": 9060347,
        "node_id": "MDEwOlJlcG9zaXRvcnk5MDYwMzQ3",
        "name": "traceur-compiler",
        "full_name": "google/traceur-compiler",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
        "html_url": "https://github.com/google/traceur-compiler",
        "description": "Traceur is a JavaScript.next-to-JavaScript-of-today compiler",
        "fork": False,
        "url": "https://api.github.com/repos/google/traceur-compiler",
        "forks_url": "https://api.github.com/repos/google/traceur-compiler/forks",
        "keys_url": "https://api.github.com/repos/google/traceur-compiler/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/traceur-compiler/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/traceur-compiler/teams",
        "hooks_url": "https://api.github.com/repos/google/traceur-compiler/hooks",
        "issue_events_url": "https://api.github.com/repos/google/traceur-compiler/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/traceur-compiler/events",
        "assignees_url": "https://api.github.com/repos/google/traceur-compiler/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/traceur-compiler/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/traceur-compiler/tags",
        "blobs_url": "https://api.github.com/repos/google/traceur-compiler/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/traceur-compiler/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/traceur-compiler/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/traceur-compiler/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/traceur-compiler/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/traceur-compiler/languages",
        "stargazers_url": "https://api.github.com/repos/google/traceur-compiler/stargazers",
        "contributors_url": "https://api.github.com/repos/google/traceur-compiler/contributors",
        "subscribers_url": "https://api.github.com/repos/google/traceur-compiler/subscribers",
        "subscription_url": "https://api.github.com/repos/google/traceur-compiler/subscription",
        "commits_url": "https://api.github.com/repos/google/traceur-compiler/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/traceur-compiler/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/traceur-compiler/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/traceur-compiler/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/traceur-compiler/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/traceur-compiler/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/traceur-compiler/merges",
        "archive_url": "https://api.github.com/repos/google/traceur-compiler/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/traceur-compiler/downloads",
        "issues_url": "https://api.github.com/repos/google/traceur-compiler/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/traceur-compiler/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/traceur-compiler/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/traceur-compiler/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/traceur-compiler/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/traceur-compiler/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/traceur-compiler/deployments",
        "created_at": "2013-03-27T18:05:40Z",
        "updated_at": "2019-12-02T16:45:54Z",
        "pushed_at": "2018-05-28T04:37:54Z",
        "git_url": "git://github.com/google/traceur-compiler.git",
        "ssh_url": "git@github.com:google/traceur-compiler.git",
        "clone_url": "https://github.com/google/traceur-compiler.git",
        "svn_url": "https://github.com/google/traceur-compiler",
        "homepage": "",
        "size": 27487,
        "stargazers_count": 8033,
        "watchers_count": 8033,
        "language": "JavaScript",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 604,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 296,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
          "spdx_id": "Apache-2.0",
          "url": "https://api.github.com/licenses/apache-2.0",
          "node_id": "MDc6TGljZW5zZTI="
        },
        "forks": 604,
        "open_issues": 296,
        "watchers": 8033,
        "default_branch": "master",
        "permissions": {
          "admin": False,
          "push": False,
          "pull": True
        }
      },
      {
        "id": 9065917,
        "node_id": "MDEwOlJlcG9zaXRvcnk5MDY1OTE3",
        "name": "firmata.py",
        "full_name": "google/firmata.py",
        "private": False,
        "owner": {
          "login": "google",
          "id": 1342004,
          "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
          "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/google",
          "html_url": "https://github.com/google",
          "followers_url": "https://api.github.com/users/google/followers",
          "following_url": "https://api.github.com/users/google/following{/other_user}",
          "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/google/subscriptions",
          "organizations_url": "https://api.github.com/users/google/orgs",
          "repos_url": "https://api.github.com/users/google/repos",
          "events_url": "https://api.github.com/users/google/events{/privacy}",
          "received_events_url": "https://api.github.com/users/google/received_events",
          "type": "Organization",
          "site_admin": False
        },
        "html_url": "https://github.com/google/firmata.py",
        "description": None,
        "fork": False,
        "url": "https://api.github.com/repos/google/firmata.py",
        "forks_url": "https://api.github.com/repos/google/firmata.py/forks",
        "keys_url": "https://api.github.com/repos/google/firmata.py/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/firmata.py/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/firmata.py/teams",
        "hooks_url": "https://api.github.com/repos/google/firmata.py/hooks",
        "issue_events_url": "https://api.github.com/repos/google/firmata.py/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/firmata.py/events",
        "assignees_url": "https://api.github.com/repos/google/firmata.py/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/firmata.py/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/firmata.py/tags",
        "blobs_url": "https://api.github.com/repos/google/firmata.py/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/firmata.py/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/firmata.py/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/firmata.py/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/firmata.py/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/firmata.py/languages",
        "stargazers_url": "https://api.github.com/repos/google/firmata.py/stargazers",
        "contributors_url": "https://api.github.com/repos/google/firmata.py/contributors",
        "subscribers_url": "https://api.github.com/repos/google/firmata.py/subscribers",
        "subscription_url": "https://api.github.com/repos/google/firmata.py/subscription",
        "commits_url": "https://api.github.com/repos/google/firmata.py/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/firmata.py/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/firmata.py/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/firmata.py/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/firmata.py/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/firmata.py/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/firmata.py/merges",
        "archive_url": "https://api.github.com/repos/google/firmata.py/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/firmata.py/downloads",
        "issues_url": "https://api.github.com/repos/google/firmata.py/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/firmata.py/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/firmata.py/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/firmata.py/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/firmata.py/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/firmata.py/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/firmata.py/deployments",
        "created_at": "2013-03-27T23:20:35Z",
        "updated_at": "2019-09-23T11:54:02Z",
        "pushed_at": "2013-03-27T23:34:35Z",
        "git_url": "git://github.com/google/firmata.py.git",
        "ssh_url": "git@github.com:google/firmata.py.git",
        "clone_url": "https://github.com/google/firmata.py.git",
        "svn_url": "https://github.com/google/firmata.py",
        "homepage": None,
        "size": 160,
        "stargazers_count": 15,
        "watchers_count": 15,
        "language": "Python",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 15,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
          "key": "apache-2.0",
          "name": "Apache License 2.0",
          "spdx_id": "Apache-2.0",
          "url": "https://api.github.com/licenses/apache-2.0",
          "node_id": "MDc6TGljZW5zZTI="
        },
        "forks": 15,
        "open_issues": 0,
        "watchers": 15,
        "default_branch": "master",
        "permissions": {
          "admin": False,
          "push": False,
          "pull": True
        }
      }
    ],
    ['episodes.dart', 'cpp-netlib', 'dagger', 'ios-webkit-debug-proxy', 'google.github.io', 'kratu', 'build-debian-cloud', 'traceur-compiler', 'firmata.py'],
    ['dagger', 'kratu', 'traceur-compiler', 'firmata.py'],
  )
]
</code>
</pre>
</details>


<!--==================================================-->
<br>

## Tasks
<details>
<summary>

### 0. Parameterize a unit test
`mandatory`

File: [test_utils.py]()
</summary>

<p>Familiarize yourself with the <code>utils.access_nested_map</code> function and understand its purpose. Play with it in the Python console to make sure you understand.</p>

<p>In this task you will write the first unit test for <code>utils.access_nested_map</code>.</p>

<p>Create a <code>TestAccessNestedMap</code> class that inherits from <code>unittest.TestCase</code>.</p>

<p>Implement the <code>TestAccessNestedMap.test_access_nested_map</code> method to test that the method returns what it is supposed to.</p>

<p>Decorate the method with <code>@parameterized.expand</code> to test the function for following inputs:</p>

<pre><code>nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")
</code></pre>

<p>For each of these inputs, test with <code>assertEqual</code> that the function returns the expected result.</p>

<p>The body of the test method should not be longer than 2 lines.</p>


</details>

<details>
<summary>

### 1. Parameterize a unit test
`mandatory`

File: [test_utils.py]()
</summary>

<p>Implement <code>TestAccessNestedMap.test_access_nested_map_exception</code>. Use the <code>assertRaises</code> context manager to test that a <code>KeyError</code> is raised for the following inputs (use <code>@parameterized.expand</code>):</p>

<pre><code>nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")
</code></pre>

<p>Also make sure that the exception message is as expected.</p>


</details>

<details>
<summary>

### 2. Mock HTTP calls
`mandatory`

File: [test_utils.py]()
</summary>

<p>Familiarize yourself with the <code>utils.get_json</code> function.</p>

<p>Define the <code>TestGetJson(unittest.TestCase)</code> class and implement the <code>TestGetJson.test_get_json</code> method to test that <code>utils.get_json</code> returns the expected result.</p>

<p>We don’t want to make any actual external HTTP calls. Use <code>unittest.mock.patch</code> to patch <code>requests.get</code>. Make sure it returns a <code>Mock</code> object with a <code>json</code> method that returns <code>test_payload</code> which you parametrize alongside the <code>test_url</code> that you will pass to <code>get_json</code> with the following inputs:</p>

<pre><code>test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}
</code></pre>

<p>Test that the mocked <code>get</code> method was called exactly once (per input) with <code>test_url</code> as argument.</p>

<p>Test that the output of <code>get_json</code> is equal to <code>test_payload</code>.</p>


</details>

<details>
<summary>

### 3. Parameterize and patch
`mandatory`

File: [test_utils.py]()
</summary>

<p>Read about memoization and familiarize yourself with the <code>utils.memoize</code> decorator.</p>

<p>Implement the <code>TestMemoize(unittest.TestCase)</code> class with a <code>test_memoize</code> method.</p>

<p>Inside <code>test_memoize</code>, define following class</p>

<pre><code class="python">class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()
</code></pre>

<p>Use <code>unittest.mock.patch</code> to mock <code>a_method</code>. Test that when calling <code>a_property</code> twice, the correct result is returned but <code>a_method</code> is only called once using <code>assert_called_once</code>.</p>


</details>

<details>
<summary>

### 4. Parameterize and patch as decorators
`mandatory`

File: [test_client.py]()
</summary>

<p>Familiarize yourself with the <code>client.GithubOrgClient</code> class.</p>

<p>In a new <code>test_client.py</code> file, declare the <code>TestGithubOrgClient(unittest.TestCase)</code> class and implement the <code>test_org</code> method.</p>

<p>This method should test that <code>GithubOrgClient.org</code> returns the correct value.</p>

<p>Use <code>@patch</code> as a decorator to make sure <code>get_json</code> is called once with the expected argument but make sure it is not executed.</p>

<p>Use <code>@parameterized.expand</code> as a decorator to parametrize the test with a couple of <code>org</code> examples to pass to <code>GithubOrgClient</code>, in this order:</p>

<ul>
<li><code>google</code></li>
<li><code>abc</code></li>
</ul>

<p>Of course, no external HTTP calls should be made.</p>


</details>

<details>
<summary>

### 5.  Mocking a property
`mandatory`

File: [test_client.py]()
</summary>

<p><code>memoize</code> turns methods into properties. Read up on how to mock a property (see resource).</p>

<p>Implement the <code>test_public_repos_url</code> method to unit-test <code>GithubOrgClient._public_repos_url</code>.</p>

<p>Use <code>patch</code> as a context manager to patch <code>GithubOrgClient.org</code> and make it return a known payload.</p>

<p>Test that the result of <code>_public_repos_url</code> is the expected one based on the mocked payload.</p>


</details>

<details>
<summary>

### 6. More patching
`mandatory`

File: [test_client.py]()
</summary>

<p>Implement <code>TestGithubOrgClient.test_public_repos</code> to unit-test <code>GithubOrgClient.public_repos</code>.</p>

<p>Use <code>@patch</code> as a decorator to mock <code>get_json</code> and make it return a payload of your choice.</p>

<p>Use <code>patch</code> as a context manager to mock <code>GithubOrgClient._public_repos_url</code> and return a value of your choice.</p>

<p>Test that the list of repos is what you expect from the chosen payload.</p>

<p>Test that the mocked property and the mocked <code>get_json</code> was called once.</p>


</details>

<details>
<summary>

### 7. Parameterize
`mandatory`

File: [test_client.py]()
</summary>

<p>Implement <code>TestGithubOrgClient.test_has_license</code> to unit-test <code>GithubOrgClient.has_license</code>.</p>

<p>Parametrize the test with the following inputs</p>

<pre><code>repo={"license": {"key": "my_license"}}, license_key="my_license"
repo={"license": {"key": "other_license"}}, license_key="my_license"
</code></pre>

<p>You should also parameterize the expected returned value.</p>


</details>

<details>
<summary>

### 8. Integration test: fixtures
`mandatory`

File: [test_client.py]()
</summary>

<p>We want to test the <code>GithubOrgClient.public_repos</code> method in an integration test. That means that we will only mock code that sends external requests.</p>

<p>Create the <code>TestIntegrationGithubOrgClient(unittest.TestCase)</code> class and implement the <code>setUpClass</code> and <code>tearDownClass</code> which are part of the <code>unittest.TestCase</code> API.</p>

<p>Use <code>@parameterized_class</code> to decorate the class and parameterize it with fixtures found in <code>fixtures.py</code>. The file contains the following fixtures:</p>

<pre><code>org_payload, repos_payload, expected_repos, apache2_repos
</code></pre>

<p>The <code>setupClass</code> should mock <code>requests.get</code> to return example payloads found in the fixtures.</p>

<p>Use <code>patch</code> to start a patcher named <code>get_patcher</code>, and use <code>side_effect</code> to make sure the mock of <code>requests.get(url).json()</code> returns the correct fixtures for the various values of <code>url</code> that you anticipate to receive.</p>

<p>Implement the <code>tearDownClass</code> class method to stop the patcher.</p>


</details>

<details>
<summary>

### 9. Integration tests
`#advanced`

File: [test_client.py]()
</summary>

<p>Implement the <code>test_public_repos</code> method to test <code>GithubOrgClient.public_repos</code>.</p>

<p>Make sure that the method returns the expected results based on the fixtures.</p>

<p>Implement <code>test_public_repos_with_license</code>  to test the <code>public_repos</code> with the argument <code>license="apache-2.0"</code> and make sure the result matches the expected value from the fixtures.</p>


</details>

