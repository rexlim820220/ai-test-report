# tests/test_gitlab_tools.py

import pytest
from ai_test_report.basic import get_user_merge_requests, get_project_pipeline_stats

def test_merge_request_failure(monkeypatch):
    monkeypatch.setenv("GITLAB_TOKEN", "")
    monkeypatch.setenv("GITLAB_URL", "")

    with pytest.raises(AssertionError):
        get_user_merge_requests()

def test_pipeline_fetch_failure(monkeypatch):
    monkeypatch.setenv("GITLAB_TOKEN", "")
    monkeypatch.setenv("GITLAB_URL", "")

    with pytest.raises(AssertionError):
        get_project_pipeline_stats("123")

