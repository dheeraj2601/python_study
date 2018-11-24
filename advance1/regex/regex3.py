'''
matches 
\d - any integer
\D - any non-integer

\s - whitespace character
\S - whitespace non-character

\w - alphabet
\W - non-alphabet
'''


import re

p = re.compile('\d')
print (p.findall("hello the time is 11:30 am"))

p = re.compile('\d+[:]*')
print (p.findall("hello the time is 11:30 am"))
