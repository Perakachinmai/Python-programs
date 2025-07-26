#Arithmetic operators

num1=10
num2=2
print(num1 + num2)  # Addition
print(num1 - num2)  # Subtraction   
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Division
print(num1 % num2)  # Modulus
print(num1 ** num2) # Exponentiation
print(num1 // num2) # Floor Division

#compound assignment operators
num=10
#num=num+5
num += 5
num -= 2
num *= 3
num /= 2
num %= 4
num **= 2
num //= 3
print(num )

#Comparison operators/reational operators
num1=3
num2=2
print(num1 == num2)  # Equal to
print(num1 != num2)  # Not equal to 
print(num1 > num2)   # Greater than
print(num1 < num2)   # Less than
print(num1 >= num2)  # Greater than or equal to
print(num1 <= num2)  # Less than or equal to


#Logical operators
a=10
b=5
c=3
d=8
print(a > b and b<c)  # Logical AND
#result_and=a>b and b<c # T and F -> F
#print(result_and)
#result_or=a>b or b<c # T or F -> T
#print(result_or)
#result_not= a>b # -> T
#print(not result_not) # T -> F
print(a > b or b < c)   # Logical OR
print(not (a > b))      # Logical NOT


#membership operators
text="python is easy"
is_z_present = "z" in text  # Check if 'z' is in text
print(is_z_present)  # Output: False

list1 = [1, 2, 3, 4, 5]
is_6_present = 6 in list1  # Check if 3 is in list1
print(is_6_present)  # Output: False

is_z_not_present = "z" not in text  # Check if 'z' is not in text
print(is_z_not_present)  # Output: True

#identity operators
num1= 10
num2= 10
print(num1 is num2)  # Check if num1 and num2 are the same object
print(num1 is not num2)  # Check if num1 and num2 are not the same object
print(id(num1))  # Get the identity of num1
print(id(num2))  # Get the identity of num2

num1_list = [1, 2, 3]
num2_list = [1, 2, 3]
print(id(num1_list))  # Get the identity of num1_list
print(id(num2_list))  # Get the identity of num2_list
print(num1_list is num2_list)  # Check if num1_list and num2_list are the same object
print(num1_list is not num2_list) # Check if num1_list and num2_list are not the same object

#bitwise operators
a=5 #  # Binary: 0101
b=3 #  # Binary: 0011
print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)     # Bitwise NOT
print(a << 1)  # Left shift
print(a >> 1)  # Right shift

b=3 #0000000000000011
print(3 << 2) #0000000000001100 -> 12
print(3<<1) #0000000000000110 -> 6
print(3<<3) #0000000000110000 -> 24

b=3 #0000000000000011
print(3 >> 2) #0000000000000000 -> 0
print(3>>1) #0000000000000001 -> 1
print(8>>2) #0000000000000010 -> 2 

c=-4 #1111111111111100
print(-4 >> 2) #1111111111111111 -> -1
