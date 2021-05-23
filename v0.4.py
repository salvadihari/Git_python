
import subprocess
import os
import shutil

# gitgub repo link
git_clone_url = "git clone https://github.com/salvadihari/Git_python.git"

get_split_url_dir = git_clone_url.split("/")
print("splitting the url at / ",get_split_url_dir)
get_dir = get_split_url_dir[-1].split(".")[-2]
print("work_dir is: ", get_dir)

dir_path = os.getcwd() + "/" + get_dir
print("dir_path is: ", dir_path)


def subprocess_cmd(command):
    subprocess.run(command, stdout=subprocess.PIPE, shell=True)
    
    return change_dir()


def del_dir():

    try:
        shutil.rmtree(dir_path, ignore_errors=False, onerror=None)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))
        return subprocess_cmd(git_clone_url)


def change_dir():

    cd_dir = os.chdir(dir_path)
    print("we are in cloned dir now: ", cd_dir)

    output = subprocess.run('git log > abcd.txt', shell=True)
    print("output.txt file is generated with gitlog commits: ",output)




del_dir()
subprocess_cmd(get_dir)
#subprocess_cmd(git_clone_url)
change_dir()
