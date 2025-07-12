# src/ai_test_report/basic/common_tools.py
import pandas as pd

def summarize_results(excel_path):
    """
    Load a test results Excel file and return summary statistics.
    """
    try:
        df = pd.read_excel(excel_path)
        status_counts = df["status"].value_counts().to_dict()
        total = len(df)
        passed = status_counts.get("Pass", 0)
        failed = status_counts.get("Fail", 0)
        error = status_counts.get("Error", 0)
        summary = {
            "total": total,
            "passed": passed,
            "failed": failed,
            "error": error
        }
        return summary
    except Exception as e:
        return {"error": str(e)}
