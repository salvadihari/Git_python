import subprocess

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout.decode())

subprocess_cmd('echo working dir is; pwd; echo listing the dir files ; ls -l; echo creating a Git dir in pwd ; mkdir /home/hps/Git_python/Git; Git dir is created; ls -l /home/hps/Git_python/; now cd to Git dir ; cd /home/hps/Git_python/Git; cloning teh github repo ; git clone https://github.com/salvadihari/example-voting-app.git;cd to repo ; cd example-voting-app; echo listing the files in repo; ls -l; echo redirecting the git log commits to gitlog.txt; git log > gitlog.txt; now we can able to see the gitlog.txt file;ls -l')
