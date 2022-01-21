from git import Repo

PATH_OF_GIT_REPO = r'D:\code\SP\KR\kr_sp_backup\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():

    repo = Repo(PATH_OF_GIT_REPO)
    repo.git.add(update=True)
    repo.git.add("D:\code\SP\KR\compiler.py")
    repo.index.commit(COMMIT_MESSAGE)
    origin = repo.remote(name='origin')
    origin.push()

git_push()