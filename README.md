# Python API Test Automation Framework

Production-style API test automation framework built with Python, Pytest, and Requests to validate live public REST APIs. This project demonstrates authenticated API testing, CRUD workflow validation, response assertions, reusable fixtures, environment-based secret handling, and HTML test reporting.

## Project Overview

This repository showcases a practical API automation setup that mirrors common backend and QA engineering workflows. The suite covers:

- Authenticated API validation against the GitHub REST API
- CRUD and query-parameter testing against JSONPlaceholder
- Reusable Pytest fixtures for test setup
- Environment-based token management with `.env`
- HTML reporting for test execution results
- Clean project structure suitable for extension in CI/CD pipelines

## Tech Stack

- Python
- Pytest
- Requests
- python-dotenv
- pytest-html

## APIs Covered

### 1. GitHub REST API

Authenticated tests against the GitHub API verify:

- Authenticated user retrieval
- Response status validation
- JSON field validation
- Repository listing
- Content-Type validation
- Basic response-time assertion
- Negative scenario coverage for invalid users

### 2. JSONPlaceholder API

Public CRUD-style tests verify:

- Retrieve all posts
- Retrieve a single post
- Create a post
- Update a post
- Delete a post
- Negative scenario validation
- Query parameter filtering

## Project Structure

```text
python-api-test-automation-framework/
├── tests/
│   ├── test_github_api.py
│   └── test_jsonplaceholder.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/akhilvamsi-gogula/python-api-test-automation-framework.git
cd python-api-test-automation-framework
```

### 2. Create and activate a virtual environment

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_github_token_here
```

Use `.env.example` as a reference template.

## Running the Test Suite

Run all tests:

```bash
pytest
```

Run tests with verbose output and HTML report:

```bash
pytest --html=report.html --self-contained-html
```

## Example Test Coverage

### GitHub API

- Validate authenticated `GET /user`
- Verify presence and type of key response fields
- Validate `GET /user/repos`
- Assert JSON response headers
- Assert negative response for a non-existent user
- Measure basic API responsiveness

### JSONPlaceholder API

- Validate `GET /posts`
- Validate `GET /posts/1`
- Validate `POST /posts`
- Validate `PUT /posts/1`
- Validate `DELETE /posts/1`
- Validate invalid resource behavior
- Validate filtered queries with request parameters

## Design Choices

This project uses a small but scalable structure intended for real-world automation growth:

- `conftest.py` centralizes shared fixtures and API headers
- Test files are separated by API domain
- Secrets are kept out of source control
- The framework is easy to extend with markers, schema validation, logging, retries, and CI integration

## Sample Use Cases

This framework can be extended for:

- Regression testing of REST APIs
- Smoke testing in CI/CD pipelines
- Auth and header validation
- Contract and schema checks
- Performance sanity checks
- Portfolio demonstration for QA and SDET roles

## How This Project Demonstrates Hands-On Skills

This repository reflects practical skills expected in API testing and backend quality engineering roles:

- Writing maintainable Pytest test cases
- Validating live HTTP responses
- Managing authentication securely
- Designing positive and negative test scenarios
- Organizing reusable automation code
- Producing execution reports for visibility

## Next Improvements

Planned extensions for a more advanced version:

- JSON schema validation
- Pytest markers for smoke/regression grouping
- GitHub Actions CI execution
- Allure or richer reporting
- Request/response logging
- Config-driven environment management
