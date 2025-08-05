#Implementation of loops

# while loop
# while condition:
#   statement
count=1
while count<=5:
    print(count)
    count+=1

# while True:
#   print("Infinite loop") ->it will execute infinite tyms

# Best use case to understand while
password="123"
user_input="" 

#validation
while user_input !=password:
    user_input=input("Enter Password ")
print("Access granted")

# for loop
#for element in sequence:   
#    statements
n="python"
print(dir(n))
for i in n:
    print(i)

# we cannot use for to iterate non iterable objects
#num=10
#for i in num:
#   print(i) #TypeError: 'int' object is not iterable
just_num=10
print(dir(just_num))

# we can use for to iterate iterable objects
list_num=[10]  #List ->iterable objects
print(dir(list_num))
for i in list_num:
   print(i) 

#Manual Work
print("Hi")

#say 10 times hi -Manually
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
print("Hi")

print("=======") #seperator

#say 10 times hi - Automated
for i in range(10):
    print("Hello")

for i in range(3,10):
    print("g")

for i in range(1,10,3):
    print(i)


#lets print even nums between 1-20 ->while
#1st approach
i=2
while i<=20:
    print(i)
    i+=2

print("=====")

#2nd approach
i=2
while i<=20:
    if i % 2==0:
        print(i)
    i+=1


#lets print even nums between 1-20 ->for
#1st approach
i=2
for i in range(2,21,2):
    print(i)

#Nested loops
#Maths Table
for i in range(1,4):
    for j in range(1,11):
        print(f"{i} x {j} ={i*j}")

print("=============")
#Nested while loop
#maths Table
i=1
while i<4:
    j=1
    while j < 3:
       print(f"{i} x {j} ={i*j}")
       j += 1
    i += 1 

#break demo
for i in range(5):
    if i==3:
        break #terminate the loop when i is 3   
    print(i)

#continue demo
for i in range(5):
    if i==3:
        continue #skip the 4th iteration when i is 3(based on index) 
    print(i)
   
   
#pass demo
if (5>9):
     pass