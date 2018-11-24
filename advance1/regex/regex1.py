import re

sentence = ''' hi this is Dheeraj  30 . along with him is Manoj of 31.
they are also joined by Suresh whose age is 35'''

print (sentence)

name = re.findall(r'\d{1,3}', sentence)
age = re.findall(r'[A-Z][a-z]*', sentence)

dic = {}

x = 0

for a in name:
	dic[a] = age[x]
	x+=1

print (dic)


