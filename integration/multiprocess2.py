import subprocess
import multiprocessing
import time

def fun1():
	command = ['python test_server.py']
    	output = subprocess.call(command, shell=True)
	#print output.communicate()
    	#output = output.decode()
    	#return output

def fun2():
	command = ['python web_server.py']
    	output = subprocess.call(command, shell=True)
	#print output.communicate()[0]

if __name__ == '__main__':
	p1 = multiprocessing.Process(name='p1', target=fun1)
	p2 = multiprocessing.Process(name='p2', target=fun2)
	p1.start()
	p2.start()

