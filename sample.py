import subprocess

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    print(proc_stdout.decode())

subprocess_cmd('echo working dir is; pwd; echo listing the dir files ; ls -l; echo creating a dir in /home/; mkdir /home/Git; ls -l /home/; cd /home/Git; git clone https://github.com/salvadihari/example-voting-app.git; cd example-voting-app; echo listing the files in repo; ls -l; echo redirecting the git log commits to gitlog.txt; git log > gitlog.txt; ls -l')
