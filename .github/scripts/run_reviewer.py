import os

import openai
from jira import JIRA

# Keys
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_EMAIL = os.getenv("JIRA_EMAIL")
JIRA_SERVER = os.getenv("JIRA_SERVER")
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")

# Other data
PR_TITLE = os.getenv("PR_TITLE")
GIT_DIFF = os.getenv("GIT_DIFF")

# Get Data from Jira
jira = JIRA(basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN), server=JIRA_SERVER)
issue_id = PR_TITLE.split("]")[0].strip("[")
issue = jira.issue(issue_id)
jira_summary = issue.fields.summary
jira_description = issue.fields.description

# Prompt Open AI to generate a review
openai.api_key = OPEN_AI_API_KEY
prompt = f""""You are an expert code reviewer, I want to review a PR which is a fix for a Jira ticket.
    The Jira summary is: {jira_summary}
    The Jira description is: {jira_description}
    The PR diff is: {GIT_DIFF}
    Write a review about the PR, comment about the correctness, quality, and completeness of the code
    and please give three suggestions for improvements to the code you're reviewing.
    """
chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
)

# Print the review (This will be captured by the action and posted as a comment on the PR)
print(chat_completion.choices[0].message.content.replace('`', '&#96;'))
