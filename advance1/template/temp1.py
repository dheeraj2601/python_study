from string import Template
 
t = Template('x is $x')
 
print (t.substitute({'x' : 1}))

 
# List Student stores the name and marks of three students
Student = [('Ram',50,90), ('Ankit',60,78), ('Bob',70,92)]
 
# We are creating a basic structure to print the name and
# marks of the students.
t = Template('Hi $name, roll no $roll you have got $marks marks')
 
for i in Student:
     print (t.substitute(name = i[0], roll = i[1], marks = i[2]))



