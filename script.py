import subprocess
import os

# gitgub repo link
git_clone_url = "git clone https://github.com/salvadihari/Git_python.git"


def subprocess_cmd(command):
    subprocess.run(command)


def git_dir():

    get_split_url_dir = git_clone_url.split("/")
    print("",get_split_url_dir)
    get_dir = get_split_url_dir[-1].split(".")[-2]
    print("work_dir is: ", get_dir)
    repo_dir = os.getcwd() + "\\" + get_dir
  #  print("repo_dir:", repo_dir)
   # print(os.getcwd())
    os.chdir(get_dir)
    print(os.getcwd())


    output = subprocess.run('git log > abcd.txt', shell=True)
    print("output.txt file is generated with gitlog commits: ",output)

    os.listdir()
    print(os.listdir())


subprocess_cmd(git_clone_url)
git_dir()
