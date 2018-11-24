import re

def find1(string):
	regex = r"([A-Z][a-z]+) (\d+)"
	match = re.search(regex, string)

	print (match)
	if match == None:
		print ("invalid")
		return

	print ("Data : ", match.group())
	print ("Month : ", match.group(1))
	print ("Day : ", match.group(2))

find1("January 26")
print ()
find1("hello Sep 6")
