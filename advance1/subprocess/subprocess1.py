import subprocess
#import time

cmd = 'date'
ab = subprocess.call(cmd, shell=True)
print ('return code : ', ab)


cmd2 = 'ls -lrt'
ab2 = subprocess.call(cmd2, shell=True)
print ('return code : ', ab2)

