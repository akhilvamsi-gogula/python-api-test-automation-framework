# Python API Test Automation Framework

Production-style API test automation framework built with Python, Pytest, and Requests to validate live public REST APIs. This project demonstrates authenticated API testing, CRUD workflow validation, response assertions, reusable fixtures, environment-based secret handling, and HTML test reporting.

---

## Why This Project Exists

Modern backend and QA teams rely on automated checks to verify that APIs are secure, reliable, and fast. This repository is a compact but realistic example of such a framework:

- Uses **real APIs**, not mocks (GitHub REST API, JSONPlaceholder).
- Covers **authentication**, **CRUD operations**, **negative scenarios**, and **basic performance**.
- Produces a **HTML report** and **structured logs** that non-developers can read.
- Is organized to be easily extended into CI/CD pipelines and larger suites.

This makes it suitable as a portfolio project for QA / SDET / backend testing roles.

---

## Tech Stack

- Python
- Pytest
- Requests
- python-dotenv
- pytest-html
- Standard Python logging

---

## APIs Covered

### GitHub REST API

Authenticated tests against the GitHub API validate:

- Authenticated user endpoint (`GET /user`).
- User profile contract (required fields and types).
- Identity consistency for the configured account.
- Repository listing and basic repository payload structure.
- Security behavior for unauthenticated access.
- Response headers and simple performance checks.

### JSONPlaceholder API

Public tests against JSONPlaceholder validate:

- List of posts (`GET /posts`) and payload shape.
- Single post details (`GET /posts/1`) and schema.
- Post creation contract (`POST /posts`).
- Update behavior (`PUT /posts/1`).
- Deletion behavior (`DELETE /posts/1`).
- Non-existent resource handling.
- Query parameter filtering (`GET /posts?userId=1`).

---

## Project Structure

```text
python-api-test-automation-framework/
├── tests/
│   ├── test_github_api.py          # Auth, profile, repos, security, headers, performance
│   └── test_jsonplaceholder.py     # CRUD, negative tests, query params
├── conftest.py                     # Shared fixtures: base URLs, GitHub token, headers
├── pytest.ini                      # Pytest configuration, HTML report, logging
├── requirements.txt                # Dependencies
├── .env.example                    # Example environment variables
├── .gitignore                      # Ignored files (venv, logs, local report, env)
└── README.md
```

Key design decisions:

- **Fixtures in `conftest.py`** give a single source of truth for base URLs and authentication, which is a common practice in production frameworks.
- **Tests grouped by API** keep responsibilities clear and make it easy to add more services later.
- **Logging and HTML reporting** provide observable, shareable test runs for teams.

---

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

#### macOS / Linux

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root:

```env
GITHUB_TOKEN=your_github_token_here
```

Use `.env.example` as a template. The token is **not** committed to Git; it is loaded at runtime via `python-dotenv`, and tests will fail fast if the variable is missing.

On GitHub, create a PAT (personal access token) with minimal scopes required for reading user and repository details.

---

## Running the Test Suite

Run all tests with logging and HTML reporting:

```bash
pytest
```

This uses the options defined in `pytest.ini`:

- `-v` for verbose test output.
- `--html=report.html --self-contained-html` for a single-file HTML report.
- `--capture=tee-sys` to show logs in the console and embed them into the report.

Logs are also written to `logs/test.log`.

Open `report.html` in a browser to review:

- Test summary.
- Per-test logs (URLs called, status codes, payload snippets).
- Execution times.

---

## Example Test Coverage

### GitHub API

- Auth check: `GET /user` returns `200` and a valid profile.
- Contract checks: core fields (`login`, `id`, `type`, `html_url`) and types.
- Identity check: authenticated user matches the expected GitHub login.
- Repository listing: `GET /user/repos` returns a list with key fields (`name`, `full_name`, `private`, `html_url`, `default_branch`).
- Negative scenario: invalid username returns `404`.
- Security: unauthenticated `GET /user` returns `401` or `403`.
- Basic performance: simple response-time assertion and JSON `Content-Type`.

### JSONPlaceholder API

- Collection contract: non-empty list of posts with required fields.
- Single-resource contract: `GET /posts/1` returns correctly typed fields.
- Create contract: `POST /posts` echoes key fields and returns an `id`.
- Update contract: `PUT /posts/1` returns updated values for the resource.
- Delete behavior: `DELETE /posts/1` returns a success status.
- Negative scenario: high ID returns `404` or an empty object, depending on service.
- Query behavior: `GET /posts?userId=1` returns posts where `userId == 1`.

---

## Design Choices and Extensibility

This framework is intentionally small but structured to grow:

- **Configuration via fixtures** makes it easy to add more environments (dev, stage, prod).
- **Logging** is centralized and formatted for both console and file output, which is a common pattern in serious test frameworks.
- **HTML reporting** can be plugged into CI pipelines (e.g. GitHub Actions, GitLab CI) for nightly or per-commit runs.

Possible extensions:

- JSON schema validation using `jsonschema` or Cerberus.
- More APIs (internal services, third-party payment or auth APIs).
- Pytest markers (smoke, regression, performance).
- GitHub Actions workflow to run tests on push and publish `report.html` as an artifact.

---

## Use Cases

This repository can be used to:

- Demonstrate API testing skills.
- Serve as a starting point for a team API automation framework.
- Practice designing positive, negative, security, and performance test scenarios.
- Validate integration behavior for live APIs.

---

## Author

**Akhil Vamsi Krishna Gogula**  
GitHub: [akhilvamsi-gogula](https://github.com/akhilvamsi-gogula)