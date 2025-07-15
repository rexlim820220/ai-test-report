# src/ai_test_report/__main__.py

import yaml
import pandas as pd
from pathlib import Path
from jinja2 import Template
from datetime import datetime
from ai_test_report.basic import setup_logger
from ai_test_report.basic import GitLabClient

logger = setup_logger()

BASE_DIR = Path(__file__).parent.resolve()
REPORT_DIR = BASE_DIR / "reports"

def load_config():

    config_path = Path(__file__).parent / "config.yml"
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def generate_summary(excel_path, chart_path, result_dir, member_mr_dict, pipeline_stats):
    logger.info("Generate visual test summaries and graphs")

    results = []
    for file_path in Path(result_dir).glob("test_*.py"):
        test_case_name = file_path.stem
        status = "Pass" if "login" in test_case_name else "Fail"
        results.append({"case": test_case_name, "status": status})

    df = pd.DataFrame(results)
    df.to_excel(excel_path, index=False)

    summary = df["status"].value_counts().to_dict()
    pass_count = summary.get("Pass", 0)
    fail_count = summary.get("Fail", 0)

    template_args = {
        "pass_count": pass_count,
        "fail_count": fail_count,
        "user_labels": [],
        "user_values": [],
        "pipeline_success": 0,
        "pipeline_failed": 0,
        "pipeline_canceled": 0,
        "pipeline_others": 0,
    }

    if member_mr_dict:
        labels = list(member_mr_dict.keys())
        values = list(member_mr_dict.values())

        template_args["user_labels"] = labels
        template_args["user_values"] = values

        df_mr = pd.DataFrame.from_dict(member_mr_dict, orient="index", columns=["MergeRequests"])
        df_mr.index.name = "Username"
        with pd.ExcelWriter(excel_path, mode="a", if_sheet_exists="overlay") as writer:
            df_mr.to_excel(writer, sheet_name="GitLab_MRs")

    if pipeline_stats:
        template_args["pipeline_success"] = pipeline_stats.get("success", 0)
        template_args["pipeline_failed"] = pipeline_stats.get("failed", 0)
        template_args["pipeline_canceled"] = pipeline_stats.get("canceled", 0)
        known = sum([template_args[k] for k in ["pipeline_success", "pipeline_failed", "pipeline_canceled"]])
        template_args["pipeline_others"] = max(pipeline_stats.get("total", 0) - known, 0)

    chart_template_path = REPORT_DIR / "chart_template.html"
    with open(chart_template_path, 'r', encoding='utf-8') as f:
        template = Template(f.read())

    output_html = template.render(**template_args)
    with open(chart_path, 'w', encoding='utf-8') as f:
        f.write(output_html)

    logger.info(f"Rendered chart HTML.")

def main():
    config = load_config()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    html_path = REPORT_DIR / f"test_report_{timestamp}.html"
    excel_path = REPORT_DIR / f"test_results_{timestamp}.xlsx"
    chart_path = REPORT_DIR / f"chart_{timestamp}.html"

    member_mr_dict, pipeline_stats = {}, {}

    try:
        gitlab_api = GitLabClient()
        members = gitlab_api.get_group_members()
        logger.info(f"Retrieved {len(members)} group members from GitLab.")

        for member in members:
            username = member["username"]
            try:
                mr_data = gitlab_api.get_user_merge_requests(username)
                member_mr_dict[username] = len(mr_data)
                logger.info(f"Amount of merge requests for user {username}: {len(mr_data)}")
            except Exception as e:
                logger.warning(f"Failed to get MR for {username}: {e}")
                member_mr_dict[username] = 0

        pipeline_stats = gitlab_api.get_project_pipeline_stats()

    except Exception as e:
        logger.warning(f"Access GitLab data failed: {e}")

    generate_summary(excel_path, chart_path, config["test_case_dir"], member_mr_dict, pipeline_stats)

    logger.info("Test report completed")
    logger.info(f"HTML report: {html_path}")
    logger.info(f"Chart Summary: {chart_path}")
    logger.info(f"Excel file: {excel_path}")

if __name__ == "__main__":
    main()