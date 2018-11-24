# Python code to demonstrate working of 
# strip(), lstrip() and rstrip()
str = "---geeks-for--geeks---"
 
# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') )
 
# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') )
 
# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )




''' 
min(“string”) :- This function returns the minimum value alphabet from string.
max(“string”) :- This function returns the maximum value alphabet from string.
'''

# Python code to demonstrate working of 
# min() and max()
str = "geeksforgeeks"
 
# using min() to print the smallest character
# prints 'e'
print ("The minimum value character is : " + min(str));
 
# using max() to print the largest character
# prints 's'
print ("The maximum value character is : " + max(str));

from string import maketrans

str = "geeksforgeeks"
 
str1 = "gfo"
str2 = "abc"
 
# using maktrans() to map elements of str2 with str1
mapped = maketrans( str1, str2 );
 
# using translate() to translate using the mapping
print ("The string after translation using mapped elements is : ")
print  (str.translate(mapped)) ;












