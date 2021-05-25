import subprocess
import os
import datetime import datetime
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
        if os.path.exists(dir_path):
            print ("dir_path exist")
            shutil.rmtree(dir_path, ignore_errors=False, onerror=None)
            print("deleted existing repo dir")
            subprocess_cmd(git_clone_url)
        else:
            print ("dir_path does not exist")
            subprocess_cmd(git_clone_url)
    except OSError as e:
        print("Error: %s : %s" % (dir_path, e.strerror))


def change_dir():
    cd_dir = os.chdir(dir_path)
    print("we are in cloned dir now: ", os.getcwd())

    output = subprocess.run('git log > xyz.txt', shell=True)
    print("xyz.txt file is generated with gitlog commits: ",output)


def git_log():
    try:
        previous_line = ""
        with open("xyz.txt", 'r') as rf:
            r_lines = rf.readlines()

        with open("xyz.txt", 'w') as wf:
            for line in r_lines:
                if line.startswith("commit", 0):
                    wf.write("\n" + line)
                elif line.startswith("date", 0):
                    # Date:   Mon May 24 13:46:38 2021 +0530
                    d_str =(line.rstrip()).split("   ")
                    d_obj = datetime.strptime(d_str[-1], "%a %b %d %H:%M:%S %Y %z")
                    wf.write(d_str[0] + srt(d_obj) + "\n")
                elif previous_line.startswith("date"):
                    f.write("commit message: " + line.lstrip())
                elif not line.isspace():
                    wf.write(line.lstrip())
            else:
                pass
            previous_line = line
    except Exception as e:
        print(e)




del_dir()
change_dir()
git_log()
