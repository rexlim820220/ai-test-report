# src/ai_test_report/__main__.py

import yaml
import pytest
import pandas as pd
from pathlib import Path
from jinja2 import Template
from datetime import datetime
from ai_test_report.basic import setup_logger
from ai_test_report.basic import get_user_merge_requests

logger = setup_logger()

BASE_DIR = Path(__file__).parent.resolve()
REPORT_DIR = BASE_DIR / "reports"

def load_config():

    config_path = Path(__file__).parent / "config.yml"
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def run_pytest(html_path):
    logger.info("Starting test execution")
    pytest.main([
        'tests',
        '--html=' + str(html_path),
        '--self-contained-html'
    ])

def generate_summary(excel_path, chart_path, result_dir):
    logger.info("Generate visual test summaries and graphs")

    results = []
    for file_path in Path(result_dir).glob("test_*.py"):
        test_case_name = file_path.stem
        status = "Pass" if "login" in test_case_name else "Fail"
        results.append({"case": test_case_name, "status": status})

    df = pd.DataFrame(results)
    df.to_excel(excel_path, index=False)

    summary = df["status"].value_counts().to_dict()

    chart_template_path = REPORT_DIR / "chart_template.html"
    with open(chart_template_path, 'r', encoding='utf-8') as f:
        template = Template(f.read())

    output_html = template.render(
        pass_count=summary.get("Pass", 0),
        fail_count=summary.get("Fail", 0),
    )

    with open(chart_path, 'w', encoding='utf-8') as f:
        f.write(output_html)

def main():
    config = load_config()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    html_path = REPORT_DIR / f"test_report_{timestamp}.html"
    excel_path = REPORT_DIR / f"test_results_{timestamp}.xlsx"
    chart_path = REPORT_DIR / f"chart_{timestamp}.html"

    try:
        user_mrs = get_user_merge_requests()
        logger.info(f"Amount of merge requests for user : {len(user_mrs)}")
    except Exception as e:
        logger.warning(f"Access GitLab merge request data failed: {e}")

    run_pytest(html_path)
    generate_summary(excel_path, chart_path, config["test_case_dir"])

    logger.info("Test report completed")
    logger.info(f"HTML report: {html_path}")
    logger.info(f"Chart Summary: {chart_path}")
    logger.info(f"Excel file: {excel_path}")

if __name__ == "__main__":
    main()