'''
c/c++
char * strtok(char str[], const char *delims);

#include <stdio.h>
#include <string.h>
 
int main()
{
    char str[] = "Geeks-for-Geeks";
 
    // Returns first token 
    char *token = strtok(str, "-");
   
    // Keep printing tokens while one of the
    // delimiters present in str[].
    while (token != NULL)
    {
        printf("%s\n", token);
        token = strtok(NULL, "-");
    }
 
    return 0;
}


'''

'''
 
  // regexp is the delimiting regular expression; 
  // limit is limit the number of splits to be made 
  str.split(regexp = "", limit = string.count(str)) 

'''

line = "Geek1 \nGeek2 \nGeek3";
print (line.split())
print (line.split(' ', 1))


