import json
import openai
from github_ops import get_jira_ticket_id, get_pr_diff
from jira_ops import get_jira_data

try:
    with open("creds.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        OPEN_AI_API_KEY = data["OPEN_AI_API_KEY"]
except (FileNotFoundError, KeyError):
    print("Error: Please check your creds.json file")
    exit(1)

openai.api_key = OPEN_AI_API_KEY

def review_pr(pr_id: int):
    ticket_id = get_jira_ticket_id(pr_id)
    diff = get_pr_diff(pr_id)
    jira_summary, jira_description = get_jira_data(ticket_id)

    prompt = f""""You are an expert code reviewer, I want to review a PR which is a fix for a Jira ticket.
    The Jira summary is: {jira_summary}
    The Jira description is: {jira_description}
    The PR diff is: {diff}
    Write a review about the PR, comment about the correctness, quality, and completeness of the code
    and please give three suggestions for improvements to the code you're reviewing.
    """
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    return chat_completion.choices[0].message.content

print(review_pr(2))