# AI Test Report

AI Test Report is a command-line testing suite built to visualize team-wide GitLab contribution metrics using `Python`, `Chart.js`, `Jinja2`, and `Pytest`.

This project was developed to support internal reporting for technical departments and demonstrate AI-assisted data processing and visualization. It automates the execution and summarization of test cases while integrating GitLab REST API data such as CI/CD pipeline success rates and Merge Request activity.

This project aims to integrate tools like Pytest, pandas, Jinja2, and Chart.js to create a visualized automated testing report system. It helps Pegatron developers quickly understand test results and share knowledge effectively.

## Project Directory Structure

```plaintext
ai_test_report/
├── .git/
├── .gitignore
├── .gitlab-ci.yml
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
pip install -r requirements.txt
```

Or use `pyproject.toml` with tools like `pipx`, `hatch`, or `poetry`.

### 3. Compile and Register CLI Command in `.venv`

If your `pyproject.toml` includes:

```toml
[project.scripts]
ai_test_report = "ai_test_report.__main__:main"
```

Install the package into `.venv` with:

```bash
pip install -e .
```

Now you can run the command directly:

```bash
ai_test_report
```

This will:
- Execute test cases
- Aggregate test results
- Generate an HTML test report, Excel summary, and Chart.js visual report

---

## Additional Support

- CI workflow: Refer to `.gitlab-ci.yml`
- Customize report appearance: Edit `chart_template.html`
- Write test cases: Add new `test_*.py` files under the `tests/` directory

---

## Authors and acknowledgment

This project is developed by Pegatron Technology Group. All rights reserved.

