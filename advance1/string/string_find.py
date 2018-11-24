''' find(“string”, beg, end) :- This function is used to find the position of the substring within a string.It takes 3 arguments, substring , starting index( by default 0) and ending index( by default string length).

    It returns “-1 ” if string is not found in given range.
    It returns first occurrence of string if found.
'''

'''
 rfind(“string”, beg, end) :- This function has the similar working as find(), but it returns the position of the last occurrence of string.
'''

# Python code to demonstrate working of 
# find() and rfind()
str = "geeksforgeeks is for geeks"
str2 = "geeks"
 
# using find() to find first occurrence of str2
# returns 8
print ("The first occurrence of str2 is at : ", end="")
print (str.find( str2) )
print (str.find( str2, 4) )
 
# using rfind() to find last occurrence of str2
# returns 21
print ("The last occurrence of str2 is at : ", end="")
print ( str.rfind( str2, 4) )


# Python code to demonstrate working of 
# startswith() and endswith()
str = "geeksforgeeks"
str1 = "geeks"
 
# using startswith() to find if str starts with str1
if    str.startswith(str1):
        print ("str begins with str1")
else :  print ("str does not begin with str1")
 
# using endswith() to find if str ends with str1
if str.endswith(str1):
       print ("str ends with str1")
else : print ("str does not end with str1")

str = "GeeksforGeeks"
str1 = "geeks"
 
# checking if all characters in str are upper cased
if str.isupper() :
       print ("All characters in str are upper cased")
else : print ("All characters in str are not upper cased")
 
# checking if all characters in str1 are lower cased
if str1.islower() :
       print ("All characters in str1 are lower cased")
else : print ("All characters in str1 are not lower cased")

# Python code to demonstrate working of 
# upper(), lower(), swapcase() and title()

'''
title() :- This function converts the string to its title case i.e the first letter of every word of string is upper cased and else all are lower cased.
'''
str = "GeeksForGeeks is fOr GeeKs"
 
# Coverting string into its lower case
str1 = str.lower();
print (" The lower case converted string is : " + str1)
 
# Coverting string into its upper case
str2 = str.upper();
print (" The upper case converted string is : " + str2)
 
# Coverting string into its swapped case
str3 = str.swapcase();
print (" The swap case converted string is : " + str3)
 
# Coverting string into its title case
str4 = str.title();
print (" The title case converted string is : " + str4)



str = "geeksforgeeks is for geeks"
  
# Printing length of string using len()
print (" The length of string is : ", len(str));
 
# Printing occurrence of "geeks" in string
# Prints 2 as it only checks till 15th element
print (" Number of appearance of ""geeks"" is : ",end="")
print (str.count("geeks", 0, len(str)))









