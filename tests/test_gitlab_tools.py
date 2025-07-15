# tests/test_gitlab_tools.py

import os
import pytest
from unittest.mock import patch
from ai_test_report.basic.gitlab_tools import GitLabClient
from ai_test_report.__main__ import generate_summary

MOCK_MEMBERS = [
    {"username": "Ackman_Liang"},
    {"username": "Stephen_Chen"},
    {"username": "Evan_Cheng"},
]

MOCK_MRS = {
    "Ackman_Liang": [{"id": 1}, {"id": 2}, {"id": 3}],
    "Stephen_Chen": [],
    "Evan_Cheng": [{"id": 4}],
}

MOCK_PIPELINES = [
    {"status": "success"},
    {"status": "failed"},
    {"status": "canceled"},
    {"status": "success"},
    {"status": "manual"},
]

@pytest.fixture
def mock_gitlab(monkeypatch):
    client = GitLabClient()

    monkeypatch.setattr(client, "get_group_members", lambda: MOCK_MEMBERS)
    monkeypatch.setattr(
        client,
        "get_user_merge_requests",
        lambda username: MOCK_MRS.get(username, [])
    )
    monkeypatch.setattr(
        client,
        "get_project_pipeline_stats",
        lambda project_id=None: {
            "success": 2,
            "failed": 1,
            "canceled": 1,
            "total": 5,
        }
    )
    return client

def test_generate_chart(monkeypatch, tmp_path, mock_gitlab):
    result_dir = tmp_path / "results"
    result_dir.mkdir()
    (result_dir / "test_login_flow.py").write_text("fake test script")
    (result_dir / "test_checkout_fail.py").write_text("fake test script")

    excel_path = tmp_path / "report.xlsx"
    chart_path = tmp_path / "chart.html"

    member_mr_dict = {}
    for m in MOCK_MEMBERS:
        username = m["username"]
        member_mr_dict[username] = len(MOCK_MRS.get(username, []))

    pipeline_stats = mock_gitlab.get_project_pipeline_stats()

    generate_summary(
        excel_path,
        chart_path,
        result_dir,
        member_mr_dict,
        pipeline_stats
    )

    assert chart_path.exists()
    html = chart_path.read_text()
    assert "Merge Request Activity" in html
    assert "Test Result Distribution" in html
    assert "Pipeline Status Distribution" in html

def test_missing_gitlab_config(monkeypatch):
    monkeypatch.setenv("GITLAB_URL", "")
    monkeypatch.setenv("GITLAB_TOKEN", "")
    with pytest.raises(AssertionError):
        GitLabClient()
