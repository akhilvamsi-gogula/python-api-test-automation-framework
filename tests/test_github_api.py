import logging
import requests

logger = logging.getLogger("api_tests.github")


class TestGitHubUser:
    """
    Tests focused on the authenticated GitHub user and basic profile behavior.
    """

    def test_get_authenticated_user_returns_200(self, github_base_url, github_headers):
        """
        Verify that the authenticated /user endpoint is reachable and returns 200.
        """
        url = f"{github_base_url}/user"
        logger.info("Calling GitHub endpoint: %s", url)

        response = requests.get(url, headers=github_headers)

        logger.info("Status for /user: %s", response.status_code)
        assert response.status_code == 200

    def test_authenticated_user_profile_shape(self, github_base_url, github_headers):
        """
        Validate core fields and types in the authenticated user profile.
        """
        url = f"{github_base_url}/user"
        logger.info("Fetching authenticated user profile: %s", url)

        response = requests.get(url, headers=github_headers)
        data = response.json()

        logger.info("User profile keys (subset): %s", list(data.keys())[:8])

        required_keys = ["login", "id", "type", "html_url"]
        for key in required_keys:
            assert key in data, f"Missing expected key '{key}' in user profile"

        assert isinstance(data["login"], str)
        assert isinstance(data["id"], int)
        assert data["type"] == "User"

    def test_authenticated_user_is_expected_account(self, github_base_url, github_headers):
        """
        Verify that the authenticated user matches the expected GitHub login.
        """
        expected_login = "akhilvamsi-gogula"
        url = f"{github_base_url}/user"
        logger.info("Checking authenticated user identity at: %s", url)

        response = requests.get(url, headers=github_headers)
        data = response.json()

        logger.info("Authenticated login returned: %s", data.get("login"))
        assert data["login"] == expected_login

    def test_list_repos_contract(self, github_base_url, github_headers):
        """
        Validate repository list structure for the authenticated user.

        Checks:
        - Endpoint returns a list
        - Each repo contains core fields needed for automation
        """
        url = f"{github_base_url}/user/repos"
        logger.info("Listing repos via: %s", url)

        response = requests.get(url, headers=github_headers)
        logger.info("Status for /user/repos: %s", response.status_code)
        assert response.status_code == 200

        repos = response.json()
        assert isinstance(repos, list)

        if repos:
            sample = repos[0]
            logger.info("Sample repo name: %s, visibility: %s", sample.get("name"), sample.get("visibility"))

            required_repo_keys = ["name", "full_name", "private", "html_url", "default_branch"]
            for key in required_repo_keys:
                assert key in sample, f"Missing key '{key}' in repository payload"

    def test_invalid_user_returns_client_error(self, github_base_url):
        """
        Negative test: requesting a clearly invalid username should return a client error.
        GitHub may respond with 404 (Not Found) or 403 (Forbidden) depending on context,
        but in both cases the resource is not available to the caller.
        """
        invalid_user = "this-user-does-not-exist-xyz-12345"
        url = f"{github_base_url}/users/{invalid_user}"
        logger.info("Calling invalid user endpoint: %s", url)

        response = requests.get(url)

        logger.info("Status for invalid user '%s': %s", invalid_user, response.status_code)
        assert response.status_code in (404, 403)

    def test_unauthenticated_request_to_user_fails(self, github_base_url):
        """
        Security behavior test: /user endpoint requires authentication.
        """
        url = f"{github_base_url}/user"
        logger.info("Calling /user without authentication: %s", url)

        response = requests.get(url)

        logger.info("Unauthenticated status code: %s", response.status_code)
        assert response.status_code in (401, 403)

    def test_response_headers_and_performance(self, github_base_url, github_headers):
        """
        Validate response headers and basic performance for /user.
        """
        url = f"{github_base_url}/user"
        logger.info("Measuring response headers and time for: %s", url)

        response = requests.get(url, headers=github_headers)

        content_type = response.headers.get("Content-Type", "")
        elapsed = response.elapsed.total_seconds()

        logger.info("Content-Type: %s", content_type)
        logger.info("Elapsed seconds: %.3f", elapsed)

        assert "application/json" in content_type
        assert elapsed < 2.0