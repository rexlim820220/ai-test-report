# tests/test_gitlab_tools.py

import pytest
from ai_test_report.basic import GitLabClient

def test_missing_gitlab_config(monkeypatch):
    monkeypatch.setenv("GITLAB_URL", "")
    monkeypatch.setenv("GITLAB_TOKEN", "")
    with pytest.raises(AssertionError):
        GitLabClient()