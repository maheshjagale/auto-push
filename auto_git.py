from git import Repo

def push_to_github(repo_path):
    try:
        repo = Repo(repo_path)

        # Prompt for commit message
        commit_message = input("Enter commit message (or press Enter for default): ")
        if not commit_message:
            commit_message = "Automated commit"

        # Add and commit new/untracked/modified files
        if len(repo.untracked_files) > 0 or len(repo.git.diff("--name-only")) > 0:
            repo.git.add(all=True)
            repo.index.commit(commit_message)
        else:
            print("No changes to commit.")

        # Push if local branch is ahead of remote
        origin = repo.remote(name='origin')
        origin.fetch()
        if repo.head.commit != repo.commit('origin/main'):
            origin.push()
            print("Successfully pushed to GitHub!")
        else:
            print("No commits to push.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please resolve any issues and try again.")

if __name__ == "__main__":
    repo_path = "./"
    push_to_github(repo_path)

