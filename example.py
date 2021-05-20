import subprocess
import os




# gitgub repo link
git_clone = str("git clone https://github.com/salvadihari/Git_python")

def subprocess_cmd():

    # cloning the git repo
    subprocess.run(str(git_clone), shell=True)

    working_dir = os.getcwd()   

    # changin the dir
    dir_name = git_clone.split("/")
    target_dir = working_dir + "/" + dir_name[4]
    
    # 
    print("this is target dir :", target_dir)

    os.chdir(target_dir)
    
    # this is pwd
    print("this is pwd", os.getcwd())

    # exporting git log commits to gitlog.txt
    subprocess.run('git log > gitlog.txt', shell=True)
    
    # listing pwd to cehck gitlog.txt
    subprocess.run('ls -l', shell=True)

subprocess_cmd()
