import os
import argparse
from git_utils import get_local_branches, get_remote_branches, delete_branch, fetch_prune

def delete_local_branches_not_on_remote(directory, remote="origin"):
    local_branches = set(get_local_branches(directory))
    remote_branches = set(get_remote_branches(directory, remote))

    branches_to_delete = local_branches - remote_branches

    if len(branches_to_delete) == 0:
        print("No branches to delete")

    for branch in branches_to_delete:
        print(f"Deleting local branch {branch}...")
        output, error = delete_branch(directory, branch)
        if error:
            print(f"Error deleting branch {branch}: {error}")
        else:
            print(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Delete local branches not present on a specified remote.")
    parser.add_argument('--remote', default='origin', help="Name of the remote to compare against (default: origin)")
    args = parser.parse_args()

    base_directory = "."  # Replace with your base directory path if different
    remote_name = "origin"  # Change this if your remote has a different name

    fetch_prune(base_directory)

    try:
        delete_local_branches_not_on_remote(base_directory, args.remote)
        print("Unused local branches deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")