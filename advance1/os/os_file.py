import os
fd = "GFG.txt"
 
# popen() is similar to open()
file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)
#os.rename(fd, "dk.txt")
