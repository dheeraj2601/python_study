import os

#os.chdir("advance1/os")
#print (os.getcwd())

myvars = {}

myfile = open("config.txt", 'r')
for line in myfile:
    name, xyx, var = line.partition("=")
    #name, var = line.partition("=")[::2]
    print (name)
    print (var)
    var = var.rstrip()
    myvars[name.strip()] = var

print (myvars["ip"])
print (myvars["port"])
myfile.close()


str = "   dheeraj   "
print (str.strip())
print (str.rstrip())
print (str)

'''
server
192.168.5.6

port
80

ip
172.23.110.5

172.23.110.5
80
dheeraj
   dheeraj
   dheeraj   
'''

server=192.168.5.6
port=80
ip=172.23.110.5

