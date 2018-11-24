import os
import subprocess


def main():
	a = os.getcwd()
	print (a)
	#os.mkdir('dk123.txt')
	#output = subprocess.call('ls', shell=TRUE)
        #print(output)
	directory = 'dk_test.txt'
	if (os.path.exists(directory) == True):
		os.mkdir(directory)
	output = subprocess.call('ls', shell=True)
	print(output)


if __name__ == "__main__":
	main()
