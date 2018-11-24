x = "Geeks at work at Cal"
 
# Prints 3rd character beginning from 0
print (x[2])  
 
# Prints 7th character
print (x[6])  
 
# Prints 3rd character from rear beginning from -1
print (x[-3]) 



#slicing
print (x[2:5]) 

print (x[-5:-1])

#  find(“string”, beg, end) 
# returns first occurrence of string if found. returns “-1 ” if string is not found in given range.
str2 = "at"
print (x.find(str2,2))


# rfind : returns last occurrence of string
print (x.rfind(str2,2))



# islower(“string”) : This function returns true if all the letters in the string are lower cased, otherwise false.
print (x.islower())
print (str2.islower())
print (str2.isupper())


print (x.lower())
print (x.swapcase())
print (x.upper())





# strip() :- delete all the leading and trailing characters mentioned in its argument.

# lstrip() :- delete all the leading characters mentioned in its argument.

# rstrip() :- delete all the trailing characters mentioned in its argument.

str = "---geeksforgeeks---"
 
# using strip() to delete all '-'
print ( " String after stripping all '-' is : ", end="")
print ( str.strip('-') )
 
# using lstrip() to delete all trailing '-'
print ( " String after stripping all leading '-' is : ", end="")
print ( str.lstrip('-') )
 
# using rstrip() to delete all leading '-'
print ( " String after stripping all trailing '-' is : ", end="")
print ( str.rstrip('-') )



# replace()
str = "nerdsfornerds is for nerds"
 
str1 = "nerds"
str2 = "geeks"
 
# using replace() to replace str2 with str1 in str
# only changes 2 occurrences 
print ("The string after replacing strings is : ", end="")
print (str.replace( str1, str2, 2)) 





