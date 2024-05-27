import argparse
from git_utils import fetch_prune, get_local_branches, get_remote_branches, track_branch

def fetch_prune_and_create_all_branches(directory, remote="origin"):
    # Fetch and prune the remote branches
    fetch_prune(directory)
    
    # Get the list of branches
    local_branches = set(get_local_branches(directory))
    remote_branches = set(get_remote_branches(directory, remote))

    branches_to_create = remote_branches - local_branches
    
    # Checkout each remote branch
    for branch in branches_to_create:
        if branch == "HEAD":
            continue
        remote_branch = f"{remote}/{branch}"
        print(f"Tracking branch {branch} from {remote_branch}...")
        output, error = track_branch(directory, branch, remote_branch)
        if error:
            print(f"Error tracking branch {branch}: {error}")
        else:
            print(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch, prune, and checkout all remote branches.")
    parser.add_argument('--remote', default='origin', help="Name of the remote to operate on (default: origin)")

    args = parser.parse_args()
    base_directory = "."  # Replace with your base directory path if different

    try:
        fetch_prune_and_create_all_branches(base_directory, args.remote)
        print("All remote branches checked out successfully.")
    except Exception as e:
        print(f"Error: {e}")
