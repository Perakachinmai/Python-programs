#if condition
value=10

#check if given value is +ve
if value>0:
#print(f"Given {value}is Positive") #IndentationError: expected an indented block after 'if' statement on line 5
    print(f"Given {value} is positive")
 # print("Code will not execute") #IndentationError: unindent does not match any outer indentation level
    print("code will execute")

#condition for checking a number is in range or not(10 to 20)
num=20 #22 it will not give any output
if num>=10 and num<=20:
    print(f"Given num {num} is in range")


#check if given value is +ve or -ve
value=-10
if value>0:
        print(f"Given {value} is positive")
else:
    print(f"Given {value} is negative")

#input() -> for taking inputs
#print("enter your name:")
name = input("Enter your Name:")
print(f"Welcome: {name}")

#check vote Eligibility using if-else
age = int(input("Enter your age:"))
if age>=18:
     print(f"You can vote")
else:
     print(f"You cannot vote")
#TypeError: '>=' not supported between instances of 'str' and 'int' 


#check vote Eligibility using Ternary operator
#value_if_true if condition else value_if_false
age=int(input("enter your Age:"))
status="You can vote" if age>=18 else "You cannot vote"
print(status)


#elif ladder
avg_score=int(input("enter your Average score:"))
if avg_score>=90:
     print("A Grade")
elif avg_score>=75:
     print("B Grade")
elif avg_score>=60:
     print("C Grade")
elif avg_score>=50:
     print("D Grade")
elif avg_score>=35:
     print("E Grade")
else:
     print("Fail")

#Match-case
choice=int(input("enter your choice:"))
match choice:
    case 1:
          print("One")
    case 2:
          print("Two")
    case 3:
          print("Three")
    case 4:
          print("Four")
    case _:
          print("Invalid")

#Nested conditions Scenario
#club Entry --> if age is 21 or above and also a valid ID should be present
age=21
has_id=True #false ->you neeed an id to enter

if age>=21:
    if has_id:
        print("You are allowed to enter")
    else:
        print("You Need to ID to enter")
else:
     print("You are too Young to enter")
         

