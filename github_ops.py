import json
from github import Github
import requests

try:
    with open("creds.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        GITHUB_ACCESS_TOKEN = data["GITHUB_ACCESS_TOKEN"]
        GITHUB_USERNAME = data["GITHUB_USERNAME"]
        GITHUB_REPO = data["GITHUB_REPO"]
except (FileNotFoundError, KeyError):
    print("Error: Please check your creds.json file")
    exit(1)

g = Github(GITHUB_ACCESS_TOKEN)

def get_pr_diff(pr_id: int):
    repo = g.get_repo(GITHUB_REPO)
    diff_url = repo.get_pull(pr_id).diff_url
    return requests.get(diff_url, auth=(GITHUB_USERNAME,GITHUB_ACCESS_TOKEN)).text

# Test driven development 😂
diff = get_pr_diff(1)
assert diff == '''diff --git a/Dummy b/Dummy
new file mode 100644
index 0000000..ff24143
--- /dev/null
+++ b/Dummy
@@ -0,0 +1 @@
+This is a dummy file!
'''