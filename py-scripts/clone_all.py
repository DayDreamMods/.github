import os
import requests
from git_utils import clone_repo, run_command

def get_github_token():
    token = run_command("gh auth token")[0]
    if not token:
        raise ValueError("GitHub token not found. Ensure you are authenticated with gh CLI.")
    return token

def fetch_repositories(org, token):
    headers = {
        "Authorization": f"token {token}"
    }
    api_url = f"https://api.github.com/orgs/{org}/repos?per_page=100"
    response = requests.get(api_url, headers=headers)
    response.raise_for_status()
    return response.json()

def clone_repositories(org, repos):
    org_dir = os.path.join(os.getcwd(), org)
    if not os.path.exists(org_dir):
        os.makedirs(org_dir)
    
    total_repos = len(repos)
    for i, repo in enumerate(repos, 1):
        clone_url = repo['clone_url']
        repo_name = repo['name']
        print(f"Cloning {repo_name} ({i} of {total_repos})...")
        clone_repo(clone_url, os.path.join(org_dir, repo_name))
    print("All repositories cloned successfully.")

if __name__ == "__main__":
    organization = "RedEyeMods"
    
    try:
        token = get_github_token()
        repositories = fetch_repositories(organization, token)
        clone_repositories(organization, repositories)
    except Exception as e:
        print(f"Error: {e}")
