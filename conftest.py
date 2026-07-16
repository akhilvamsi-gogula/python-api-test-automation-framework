import os
import pytest
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def github_token():
    token = os.getenv("GITHUB_TOKEN")
    assert token, "GITHUB_TOKEN is not set in .env"
    return token

@pytest.fixture(scope="session")
def github_headers(github_token):
    return {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }