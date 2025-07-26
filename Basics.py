print(10)
#print(a)
print("abcd")
#script mode
a=10
b=20
print (a+b)

import keyword
print(keyword.kwlist)

from math import sqrt
print(sqrt(16))

#2name="python" -> it will give an error

#store data -> type of data  
student_name="bubbu"
print(type(student_name))
print(id(student_name))
student_age=3
print(type(student_age))
print(id(student_age))
student_gpa=10
print(type(student_gpa))
print(id(student_gpa))

#2 students data

student_name_1="bubbu"
print(type(student_name_1))
print(id(student_name_1))

student_name_2="bubbu1"
print(id(student_name_2))

studet_1_age=3
print(type(studet_1_age))
print(id(studet_1_age)) 

student_2_age=3
print(id(student_2_age))

student_gpa=9.1
print(type(student_gpa))
print(id(student_gpa))

#define some complex data
list_1=[1,2,3,4,5]
list_2=[1,2,3,4,5]
#print(type(list_1))
print(id(list_1))
#print(type(list_2))
print(id(list_2))

x="python"
y=" is"
z=" awesome"
#print(x, y, z)
print(x + y + z) #string concatenation

x=10
y=20
print(x + y) ##addition operatorf


x=10
y=20
print(x + y) 
z="awesome"
#print(x+z) -> type error:unsupported operand type(s) for +: 'int' and 'str'
print(x,z)

x,y,z = "one", "two", "three"
print(x, y, z)

"""x,y,z = "one", "two", "three" , "four" #too many values to unpack (expected 3)
print(x, y, z) -> it will give an error 
#right side and left side should be same"""


x=y=z="one"
#print(x, y, z)
print(x)
print(y)
print(z)

