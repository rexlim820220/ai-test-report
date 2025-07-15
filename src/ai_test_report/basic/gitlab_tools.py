# src/ai_test_report/basic/gitlab_tools.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GitLabClient:
    def __init__(self):
        self.base_url = os.getenv("GITLAB_URL")
        self.token = os.getenv("GITLAB_TOKEN")
        self.group_id = os.getenv("GITLAB_GROUP_ID")
        self.headers = {"PRIVATE-TOKEN": self.token}
        self.project_id = os.getenv("GITLAB_PROJECT_ID")

        assert self.base_url, "GitLab URL config is missing"
        assert self.token   , "GitLab token config is missing"
        assert self.group_id, "GitLab GROUPID config is missing"
        assert self.project_id, "GitLab PROJECTID config is missing"

    def get_group_members(self):
        """Get the member list of the entire GitLab group"""
        url = f"{self.base_url}/groups/{self.group_id}/members/all"
        response = requests.get(url, headers=self.headers, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            raise RuntimeError(f"GitLab group member fetch failed: {response.status_code} → {response.text}")

    def get_user_merge_requests(self, user):
        """Get the number of Merge Request activities of the user"""

        url = f"{self.base_url}/merge_requests?author_username={user}&scope=all"
        response = requests.get(url, headers=self.headers, verify=False)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text}

    def get_project_pipeline_stats(self):
        """Get the pipeline success rate information of the specified project"""

        url = f"{self.base_url}/projects/{self.project_id}/pipelines"
        response = requests.get(url, headers=self.headers, verify=False)
        if response.status_code == 200:
            pipelines = response.json()
            success = sum(1 for p in pipelines if p["status"] == "success")
            failed = sum(1 for p in pipelines if p["status"] == "failed")
            return {"success": success, "failed": failed, "total": len(pipelines)}
        else:
            return {"error": response.text}
