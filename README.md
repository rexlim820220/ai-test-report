# AI Test Report

AI Test Report is a command-line testing suite built to visualize team-wide GitLab contribution metrics using `Python`, `Chart.js`, `Jinja2`, and `Pytest`.

This project was developed to support internal reporting for technical departments and demonstrate AI-assisted data processing and visualization. It automates the execution and summarization of test cases while integrating GitLab REST API data such as CI/CD pipeline success rates and Merge Request activity.

This project aims to integrate tools like Pytest, pandas, Jinja2, and Chart.js to create a visualized automated testing report system. It helps Pegatron developers quickly understand test results and share knowledge effectively.

## Project Directory Structure

```plaintext
ai_test_report/
├── .git/
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
├── setup.cfg
├── tox.ini
├── src/
│   └── ai_test_report/
│       ├── __init__.py
│       ├── __main__.py         ← Main entry point (can be executed via CLI)
│       ├── config.yml          ← Configuration file for reports and resources
│       └── basic/              ← Utility functions
│          ├── __init__.py
│          ├── common_tools.py
│          ├── err_tools.py
│          ├── log_tools.py
│          └── gitlab_tools.py
│       ├── reports/
│           ├── test_results.xlsx
│           ├── test_report.html
│           └── chart_template.html
├── tests/
│   ├── test_login.py
│   ├── test_write.py
│   ├── test_view.py
│   └── test_gitlab_tools.py
├── reports/
```

---

## Installation & Execution Steps

### 1. Create a Virtual Environment `.venv`

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install Dependencies

Using `requirements.txt`:

```bash
(.venv) pip install -r requirements.txt
```

Or use `pyproject.toml` with tools like `pipx`, `hatch`, or `poetry`.

### 3. Compile and Register CLI Command in `.venv`

Install the package into `.venv` with:

```bash
(.venv) pip install -e .
```

Now you can run the command directly:

```bash
(.venv) ai_test_report
```

This will:
- Execute test cases
- Aggregate test results
- Generate an HTML test report, Excel summary, and Chart.js visual report

### 4. Run Unit Tests with Pytest

To validate offline components or simulate GitLab data responses, run:

```bash
(.venv) pytest tests/test_gitlab_tools.py --html=chart_test_report.html --self-contained-html
```

This test will:

- Use monkeypatch to mock GitLab group members, user MR data, and pipeline status
- Generate a realistic `chart_test_report.html` report containing:
  - Test result doughnut chart
  - Team Merge Request contribution bar chart
  - CI/CD pipeline status distribution chart

## Additional Support

- Customize report appearance: Edit `chart_template.html`
- Write test cases: Add new `test_*.py` files under the `tests/` directory

## Environment Variables

Note: To launch and build ai_test_report properly, define the following variables in your `.env` file:

- `GITLAB_TOKEN`: Personal access token for GitLab API
- `GITLAB_URL`: Base URL of your GitLab instance
- `GITLAB_GROUP_ID`: Label used in GitLab to represent a specific group

If these variables are missing, the CLI may fail to connect to GitLab or generate reports. Create your own `.env` file with these values before running the tool.

## Authors and acknowledgment

This project is developed by Pegatron Technology Group. All rights reserved.

