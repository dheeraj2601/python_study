#create a new direcotory in another path

import os
import subprocess

ab = os.getcwd()
print (ab)

os.chdir('..');
subprocess.call('mkdir sys2', shell=True)





