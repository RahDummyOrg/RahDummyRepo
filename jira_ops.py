import json

from jira import JIRA

try:
    with open("creds.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        JIRA_API_TOKEN = data["JIRA_API_TOKEN"]
        JIRA_SERVER = data["JIRA_SERVER"]
        JIRA_EMAIL = data["JIRA_EMAIL"]
except (FileNotFoundError, KeyError):
    print("Error: Please check your creds.json file")
    exit(1)

jira = JIRA(basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN), server=JIRA_SERVER)


def get_jira_data(issue_id: str):
    issue = jira.issue(issue_id)
    return issue.fields.summary, issue.fields.description


# Test driven development 😂
title, description = get_jira_data("RAH-1")
assert title == "Test Task"
assert description == "This is a test Task"
