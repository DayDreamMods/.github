import os
from git_utils import is_git_repo, get_current_branch, checkout_branch, pull_latest, apply_to_repositories

def update_repositories(repo_path):
    # Get the current branch
    current_branch = get_current_branch(repo_path)

    # Check out the main branch if not already on it
    if current_branch != "main":
        print("Switching to main branch")
        checkout_branch(repo_path, "main")

    print(f"Pulling '{repo_path}'")

    # Perform a git pull
    pull_output, pull_error = pull_latest(repo_path)
    if pull_error:
        print(f"Error pulling latest changes: {pull_error}")
    else:
        print(pull_output)


if __name__ == "__main__":
    base_directory = "."  # Replace with your base directory path if different
    apply_to_repositories(base_directory, update_repositories)
    print("All repositories updated successfully.")
