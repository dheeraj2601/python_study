import os
import time
import subprocess

curdir = os.getcwd()
print (curdir)

os.mkdir('dk_test.txt')
output = subprocess.call('ls', shell=True)

print ("resultcode : ", output)
time.sleep (5)

os.rename ('dk_test.txt', 'dk2.txt')
time.sleep (2)
print (subprocess.call('ls'))
