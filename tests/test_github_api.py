import requests

BASE_URL = "https://api.github.com"

def test_get_authenticated_user_returns_200(github_headers):
    response = requests.get(f"{BASE_URL}/user", headers=github_headers)
    assert response.status_code == 200

def test_authenticated_user_has_login(github_headers):
    response = requests.get(f"{BASE_URL}/user", headers=github_headers)
    data = response.json()
    assert "login" in data
    assert isinstance(data["login"], str)

def test_invalid_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/this-user-does-not-exist-xyz-12345")
    assert response.status_code == 404

def test_list_repos_returns_list(github_headers):
    response = requests.get(f"{BASE_URL}/user/repos", headers=github_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_response_content_type_is_json(github_headers):
    response = requests.get(f"{BASE_URL}/user", headers=github_headers)
    assert "application/json" in response.headers["Content-Type"]

def test_response_time_under_2_seconds(github_headers):
    response = requests.get(f"{BASE_URL}/user", headers=github_headers)
    assert response.elapsed.total_seconds() < 2.0