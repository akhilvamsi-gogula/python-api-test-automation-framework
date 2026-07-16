import logging
import requests

logger = logging.getLogger("api_tests.jsonplaceholder")


class TestJsonPlaceholderPosts:
    """
    Tests for the JSONPlaceholder /posts resource.

    These simulate typical CRUD and query operations against a REST API.
    """

    def test_get_all_posts_shape(self, jsonplaceholder_base_url):
        """
        Verify that GET /posts returns a non-empty list of posts
        with required fields present in each item.
        """
        url = f"{jsonplaceholder_base_url}/posts"
        logger.info("Fetching all posts from: %s", url)

        response = requests.get(url)
        logger.info("Status for /posts: %s", response.status_code)
        assert response.status_code == 200

        posts = response.json()
        assert isinstance(posts, list)
        assert len(posts) > 0

        sample = posts[0]
        logger.info("Sample post id=%s, userId=%s", sample.get("id"), sample.get("userId"))

        required_keys = ["userId", "id", "title", "body"]
        for key in required_keys:
            assert key in sample, f"Missing expected key '{key}' in post payload"

    def test_get_single_post_details(self, jsonplaceholder_base_url):
        """
        Verify that GET /posts/1 returns a single post with a consistent schema.
        """
        url = f"{jsonplaceholder_base_url}/posts/1"
        logger.info("Fetching single post from: %s", url)

        response = requests.get(url)
        logger.info("Status for /posts/1: %s", response.status_code)
        assert response.status_code == 200

        data = response.json()
        logger.info("Post 1 title: %s", data.get("title"))

        assert data["id"] == 1
        assert isinstance(data["title"], str)
        assert isinstance(data["body"], str)
        assert isinstance(data["userId"], int)

    def test_create_post_contract(self, jsonplaceholder_base_url):
        """
        Verify that POST /posts creates a new post and echoes key fields back.
        """
        url = f"{jsonplaceholder_base_url}/posts"
        payload = {
            "title": "Test Post",
            "body": "Created by Pytest",
            "userId": 1,
        }
        logger.info("Creating post via POST %s with payload: %s", url, payload)

        response = requests.post(url, json=payload)
        logger.info("Status for POST /posts: %s", response.status_code)
        assert response.status_code == 201

        data = response.json()
        logger.info("Created post id: %s", data.get("id"))

        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]
        assert "id" in data

    def test_update_post_contract(self, jsonplaceholder_base_url):
        """
        Verify that PUT /posts/1 updates the post representation.
        """
        url = f"{jsonplaceholder_base_url}/posts/1"
        payload = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated body",
            "userId": 1,
        }
        logger.info("Updating post via PUT %s with payload: %s", url, payload)

        response = requests.put(url, json=payload)
        logger.info("Status for PUT /posts/1: %s", response.status_code)
        assert response.status_code == 200

        data = response.json()
        logger.info("Updated post title: %s", data.get("title"))

        assert data["title"] == payload["title"]
        assert data["body"] == payload["body"]
        assert data["userId"] == payload["userId"]
        assert data["id"] == payload["id"]

    def test_delete_post_behavior(self, jsonplaceholder_base_url):
        """
        Verify that DELETE /posts/1 returns a successful status code.
        """
        url = f"{jsonplaceholder_base_url}/posts/1"
        logger.info("Deleting post via DELETE %s", url)

        response = requests.delete(url)
        logger.info("Status for DELETE /posts/1: %s", response.status_code)

        assert response.status_code in (200, 204)

    def test_get_nonexistent_post_returns_404_or_empty(self, jsonplaceholder_base_url):
        """
        Negative test: requesting a high, non-existent ID.

        JSONPlaceholder may return 404 or an empty object.
        """
        url = f"{jsonplaceholder_base_url}/posts/99999"
        logger.info("Fetching likely nonexistent post via: %s", url)

        response = requests.get(url)
        logger.info(
            "Status for nonexistent post: %s, body: %s",
            response.status_code,
            response.text,
        )

        if response.status_code == 404:
            assert True
        else:
            data = response.json()
            assert data == {}

    def test_filter_posts_by_user(self, jsonplaceholder_base_url):
        """
        Verify that GET /posts?userId=1 filters posts by userId.
        """
        url = f"{jsonplaceholder_base_url}/posts"
        params = {"userId": 1}
        logger.info("Filtering posts with params %s via: %s", params, url)

        response = requests.get(url, params=params)
        logger.info("Status for filtered /posts: %s", response.status_code)
        assert response.status_code == 200

        posts = response.json()
        assert isinstance(posts, list)

        for post in posts:
            assert post["userId"] == 1