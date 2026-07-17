# Python API Test Automation Framework

Production-style API test automation framework built with Python, Pytest, and Requests to validate live public REST APIs. This project demonstrates authenticated API testing, CRUD workflow validation, response assertions, reusable fixtures, environment-based secret handling, HTML test reporting, and CI integration with GitHub Actions.

---

## Why This Project Exists

Modern backend and QA teams rely on automated checks to verify that APIs are secure, reliable, and fast. This repository is a compact but realistic example of such a framework:

- Uses **real APIs**, not mocks (GitHub REST API, JSONPlaceholder).
- Covers **authentication**, **CRUD operations**, **negative scenarios**, and **basic performance**.
- Produces a **HTML report** and **structured logs** that are easy to review.
- Runs automatically in **GitHub Actions** with **coverage reporting**.
- Is organized to be extended into larger suites and CI/CD pipelines.

---

## Tech Stack

- Python
- Pytest
- Requests
- python-dotenv
- pytest-html
- pytest-cov
- Standard Python logging
- GitHub Actions (CI)

---

## APIs Covered

### GitHub REST API

Authenticated tests against the GitHub API validate:

- Authenticated user endpoint (`GET /user`).
- User profile contract (required fields and types).
- Identity consistency for the configured account.
- Repository listing and basic repository payload structure.
- Security behavior for unauthenticated access to `/user`.
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
├── requirements.txt                # Dependencies (including pytest-html, pytest-cov)
├── .env.example                    # Example environment variables
├── .github/
│   └── workflows/
│       └── api-tests.yml           # GitHub Actions workflow for CI
├── .gitattributes                  # Linguist overrides (exclude generated HTML from stats)
├── .gitignore                      # Ignored files (venv, logs, local report, env, coverage)
└── README.md
```

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

Use `.env.example` as a template. The token is **not** committed to Git; it is loaded at runtime via `python-dotenv`, and tests fail fast if the variable is missing.

On GitHub, create a personal access token with minimal scopes required to read user and repository details, and keep it secret.

---

## Running the Test Suite Locally

Run all tests with logging and HTML reporting:

```bash
pytest
```

To include coverage in the local run:

```bash
pytest \
  --cov=. \
  --cov-report=term-missing \
  --cov-report=xml:coverage.xml \
  --html=report.html \
  --self-contained-html
```

- `report.html` can be opened in a browser to inspect test results and logs.
- `coverage.xml` can be used by coverage tools or CI.

---

## Continuous Integration (GitHub Actions)

This project includes a GitHub Actions workflow in `.github/workflows/api-tests.yml` that:

- Triggers on `push` and `pull_request` to the `main` branch.
- Checks out the code.
- Sets up Python.
- Installs dependencies from `requirements.txt`.
- Runs pytest with coverage:
  - `--cov=.` for coverage over the whole project.
  - `--cov-report=term-missing` for a detailed summary in logs.
  - `--cov-report=xml:coverage.xml` to generate a coverage report file.
  - `--html=report.html --self-contained-html` to generate an HTML test report.
- Uploads `report.html` and `coverage.xml` as artifacts for each workflow run.

The workflow reads `GITHUB_TOKEN` from a repository secret (`GITHUB_TOKEN_API_TESTS`), which keeps credentials out of the codebase while still enabling authenticated API tests in CI.

---

## Example Test Coverage

### GitHub API

- Auth check: `GET /user` returns status 200 and a valid profile.
- Contract checks: core fields (`login`, `id`, `type`, `html_url`) and types.
- Identity check: authenticated user matches the expected GitHub login.
- Repository listing: `GET /user/repos` returns a list with key fields (`name`, `full_name`, `private`, `html_url`, `default_branch`).
- Negative scenario: invalid username returns a client error (403/404).
- Security: unauthenticated `GET /user` returns 401/403.
- Basic performance: response times for `/user` remain under a defined threshold.

### JSONPlaceholder API

- Collection contract: non-empty list of posts with required fields.
- Single-resource contract: `GET /posts/1` returns correctly typed fields.
- Create contract: `POST /posts` echoes key fields and returns an `id`.
- Update contract: `PUT /posts/1` returns updated values for the resource.
- Delete behavior: `DELETE /posts/1` returns a success status.
- Negative scenario: high ID returns a client error or an empty object.
- Query behavior: `GET /posts?userId=1` returns posts where `userId == 1`.

---

## Design Choices and Extensibility

This framework is intentionally small but structured to grow:

- **Fixtures in `conftest.py`** provide a single source of truth for base URLs and authentication.
- **Logging** is configured for both console and file output, and integrates with the HTML report.
- **HTML reporting** and **coverage** are wired into CI, making it easy to monitor test health over time.

Possible extensions:

- JSON schema validation for responses.
- Additional APIs or microservices under test.
- Pytest markers (smoke, regression, performance).
- More CI jobs (matrix builds, different Python versions).

---

## Author

**Akhil Vamsi Krishna Gogula**  
GitHub: [akhilvamsi-gogula](https://github.com/akhilvamsi-gogula)