# src/ai_test_report/basic/gitlab_tools.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_user_merge_requests():
    """Get the number of Merge Request activities of the user"""
    GITLAB_URL = os.getenv("GITLAB_URL")
    GITLAB_USER = os.getenv("GITLAB_USER")
    GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")

    assert GITLAB_URL , "GitLab URL config is missing"
    assert GITLAB_USER, "GitLab user config is missing"
    assert GITLAB_TOKEN , "GitLab token config is missing"

    HEADERS = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    verify_ssl = os.getenv("GITLAB_VERIFY_SSL", "true").lower() == "true"
    url = f"{GITLAB_URL}/merge_requests?author_username={GITLAB_USER}&scope=all"

    response = requests.get(url, headers=HEADERS, verify=verify_ssl)
    if response.status_code == 200:
        return GITLAB_USER, response.json()
    else:
        return GITLAB_USER, {"error": response.text}

def get_project_pipeline_stats(project_id):
    """Get the pipeline success rate information of the specified project""" 
    GITLAB_URL = os.getenv("GITLAB_URL")
    GITLAB_USER = os.getenv("GITLAB_USER")
    GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")

    assert GITLAB_URL , "GitLab URL config is missing"
    assert GITLAB_USER, "GitLab user config is missing"
    assert GITLAB_TOKEN , "GitLab token config is missing"

    HEADERS = {"PRIVATE-TOKEN": GITLAB_TOKEN}
    verify_ssl = os.getenv("GITLAB_VERIFY_SSL", "true").lower() == "true"
    url = f"{GITLAB_URL}/projects/{project_id}/pipelines"

    response = requests.get(url, headers=HEADERS, verify=verify_ssl)
    if response.status_code == 200:
        pipelines = response.json()
        success = sum(1 for p in pipelines if p["status"] == "success")
        failed = sum(1 for p in pipelines if p["status"] == "failed")
        return {"success": success, "failed": failed, "total": len(pipelines)}
    else:
        return {"error": response.text}
