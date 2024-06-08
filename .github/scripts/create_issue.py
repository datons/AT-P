import os
import requests
from datetime import datetime

def create_github_issue():
    token = os.getenv('GITHUB_TOKEN')
    repo_owner = os.getenv('GITHUB_REPOSITORY_OWNER')
    repo_name = os.getenv('GITHUB_REPOSITORY_NAME')
    run_id = os.getenv('GITHUB_RUN_ID')

    current_date = datetime.utcnow().strftime('%Y-%m-%d')
    report_url = f"https://github.com/{repo_owner}/{repo_name}/blob/solutions/notebooks/2_Strategies/1_Bollinger/reports/{current_date.split('-')[0]}/{current_date.split('-')[1]}/{current_date}_{run_id}.ipynb"
    issue_title = f"Daily Report for {current_date}"
    issue_body = f"The daily report has been generated. You can view it [here]({report_url})."

    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "title": issue_title,
        "body": issue_body
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 201:
        print(f"Created issue #{response.json()['number']}")
    else:
        print(f"Failed to create issue: {response.status_code}, {response.text}")

if __name__ == "__main__":
    create_github_issue()
