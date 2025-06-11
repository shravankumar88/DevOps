# It is a contorl flow stmt, which allows some code to be executed repeaedly until a specfic condition is met.
number = 20
while number < 20:
    print(number)

number = 20
while number < 25:
    print(number)
    break


number = 20
while number < 25:
    print(number)
    number +=1 

number = 20
while number <= (25+5):
    print("+",number)
    number += 1

num = 5
while num:
    print("Value of num is ", num)
    num =num -1
print("good bye")

name = "thomas"
while name == "thomas":
    print("%s is an amazing soccer player "% name)
    name = "Kingsley"

user_password = ""
while user_password != "Roan@95":
    user_password= input("Enter password: ")
print("\n Access Granted")

num = 1
while num <= 10:
    print(num ** 2)
    num +=1

num_value = int(input("enter a number: "))
name = input("Enter a name: ")
count =1
while count <= num_value:
    print(count, ":", name)
    count = count+1