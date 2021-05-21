import subprocess
import os

# gitgub repo link
git_clone_url = "git clone https://github.com/salvadihari/Git_python"
git_log_file = "git log > gitlog.txt"


def subprocess_cmd(command):
    subprocess.Popen(command)
    subprocess.Popen(git_log_file)


def git_dir():

    get_split_url_dir = git_clone_url.split("/")[-1]
    dir = os.getcwd() + "/" + get_split_url_dir
    print("git cloned repo dir is :", dir)

    os.chdir(get_split_url_dir)

    os.getcwd()
    print(os.getcwd())






subprocess_cmd(git_clone_url)
git_dir()


