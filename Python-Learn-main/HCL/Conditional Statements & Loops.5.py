# Basic prg 3
# dictionary example
num_dict = dict()
num_dict[1] = 1
num_dict[2] = 2 ** 2
num_dict[3] = 3 ** 3
print(num_dict)

# Get two strings and print the common letters . For this we used INTERSECTION function here to get the common charaters
string_1 = input("Enter the first string: ")
string_2 = input("Enter the second string: ")

set_1 = set(string_1)
set_2 = set(string_2)

common_char = set_1.intersection(set_2)
print("\n Common Letters: ", list(common_char))

#WAP to given list into two halves
list_num = [10,11,12,13,14,15,16]
len_of_lists = len(list_num)

half = int(len_of_lists / 2)
list_num1 = list_num[:half]
list_num2 = list_num[half:]

print("\n First half : %s" %list_num1)
print("\n Second half: %s" %list_num2)

#WAP to accept the input and check postive, negative or zero
num = float(input("Entar a number: "))
if num >=0:
    if num == 0:
        print("Zero")
    else:
        print("Postive Number")
else:
    print("Negative Number")

#WAP to check the type of a given number
#var = input("Enter anything to know the type: ") we cann`t define like this beacuse bydefault it string and there is such funcation to define all`
var = 32.4
if (type(var) == int):
    print("Type of the variable is integer")
elif (type(var) == float):
    print("Type of the variable is float")
elif (type(var) == complex):
    print("Type of the variable is complex")
else:
    print("Type of the variable is Unknown")
    
#WAP to check whether it is even or odd. %D operator will repalce the num
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("%d is Even" % num)
else:
    print("%d is Odd" % num)
    
#WAP Let's write code to make a calculator.We'll accept two numbers as inputs from the userand store it in variables num1 and num2 respectively.\
# We'll also accept an operator from the user to perform the desired operation.

num1 = float(input("Enter the first number: "))

operator = input("Operator: ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print("Addition: ", num1 + num2)
elif operator == "-":
    print("Subtraction: ", num1 - num2)
elif operator == "*":
    print("Mulitplication: ", num1 * num2)
elif operator == "/":
    print("Division: ", num1 / num2)
else:
    print("This is not a valid operator")
    
#WAP to check the divisibility of a given number by 5,7 or both.

num_1= int(input("Enter a number:"))
if num_1 %5 == 0 and num_1 %7 == 0:
    print("This number is divisible by both 5 and 7")
elif num_1 %5 == 0:
    print("This number is divisibkle by 5")
elif num_1 %7 == 0:
    print("This number is divisibkle by 7")
else:
    print("Thi snumber is neither divisble by 5 nor 7")

#WAP to check the Vowel and Consontant
letter = input("Enter a letter of the alphabet")
letter = letter.lower()
if letter in ('a','e','i,','o','u'):
    print("%s is a vowel." %letter)
elif letter == "y":
    print("Y is ambiquos. It depends where it is used.")
else:
    print("%s is a consontant" % letter)
    print(letter + (" is a cosontant"))
    
#WAP to check the string is a palindrome or not. Step -1: The -1 after the colon indicates a step size of -1. 
# In slicing, a step size defines how many elements to skip between included elements in the resulting sublist (or reversed string in this case). 
# A step of -1 means you iterate through the original string in reverse order, starting from the last element and going towards the beginning.
original_string = "Hello, world!"
reversed_string = original_string[::-1]
print(reversed_string)  # Output: "!dlrow ,olleH"

str_value = input("Enter the string :  ")
reversed_str = str_value[::-1]
if(str_value == reversed_str):
    print("the string is palindrome")
else:
    print("The string is not a palindrome")

#WAP Company Bonus for 10 Y an in middle of 5 to 10
salary = int(input("Enter the  annaul salary :  "))
yeras_service = int(input("Enter the years of the service:  "))
if yeras_service >= 10:
    print("Bonus is: ", .15 * salary)
elif yeras_service >=5 and yeras_service < 10:
    print("Bouns is: ", .05 * salary)
else:
    print("NO Bonus")