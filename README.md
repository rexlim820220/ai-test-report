# AI Test Report

This project aims to integrate tools like Pytest, pandas, Jinja2, and Chart.js to create a visualized automated testing report system. It helps software teams quickly understand test results and share knowledge effectively.

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
│       ├── fun.py              ← Feature module
│       └── basic/              ← Utility functions
│           ├── __init__.py
│           ├── common_tools.py
│           ├── err_tools.py
│           ├── log_tools.py
│       ├── resources/
│           └── chart.js
│       ├── reports/
│           ├── test_results.xlsx
│           ├── test_report.html
│           └── chart_template.html
├── tests/
│   ├── test_login.py
│   ├── test_write.py
│   ├── test_view.py
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

## Contact

This project is developed by the Pegatron System Integration Testing Team. If you have any questions, suggestions, or contributions, feel free to reach out to us!

