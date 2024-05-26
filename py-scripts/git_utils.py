import os, subprocess

def run_command(command, cwd=None):
    process = subprocess.Popen(command, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode().strip(), error.decode().strip()

def is_git_repo(directory):
    return run_command("git rev-parse --is-inside-work-tree", cwd=directory)[0] == 'true'

def get_current_branch(directory):
    return run_command("git rev-parse --abbrev-ref HEAD", cwd=directory)[0]

def checkout_branch(directory, branch):
    return run_command(f"git checkout {branch}", cwd=directory)

def pull_latest(directory):
    return run_command("git pull --all", cwd=directory)
    
def clone_repo(repo_url, destination):
    return run_command(f"git clone {repo_url} {destination}")

def apply_to_repositories(base_directory, callback):
    # Get all subdirectories in the base directory
    subdirs = [os.path.join(base_directory, d) for d in os.listdir(base_directory) if os.path.isdir(os.path.join(base_directory, d))]

    # Iterate over each subdirectory
    for subdir in subdirs:
        # Check if the subdirectory is a Git repository
        if is_git_repo(subdir):
            callback(subdir)
        else:
            print(f"{subdir} is not a Git repository")