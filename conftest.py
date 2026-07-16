import os
import logging

import pytest
from dotenv import load_dotenv

# Load environment variables from .env into process environment
load_dotenv()

# Session-level logger
logger = logging.getLogger("api_tests")


@pytest.fixture(scope="session")
def github_token():
    """
    Load the GitHub personal access token from environment.

    Fails fast if the token is missing, so tests do not make unauthenticated
    calls by accident.
    """
    token = os.getenv("GITHUB_TOKEN")
    assert token, "GITHUB_TOKEN is not set in .env or environment variables"
    logger.info("Loaded GitHub token from environment")
    return token


@pytest.fixture(scope="session")
def github_headers(github_token):
    """
    Shared headers for GitHub API calls.
    """
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    logger.info("Prepared GitHub headers for authenticated requests")
    return headers


@pytest.fixture(scope="session")
def github_base_url():
    """
    Base URL for GitHub REST API.
    """
    url = "https://api.github.com"
    logger.info("Using GitHub API base URL: %s", url)
    return url


@pytest.fixture(scope="session")
def jsonplaceholder_base_url():
    """
    Base URL for JSONPlaceholder fake REST API.
    """
    url = "https://jsonplaceholder.typicode.com"
    logger.info("Using JSONPlaceholder base URL: %s", url)
    return url