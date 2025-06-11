#Basic programs 1

#total savaing for any employee
salary = int(input("Enter salary amount: "))
expenses = int(input("Enter expenses: "))

savings = salary - expenses
print("My total savings in a month is: ", savings)

#n + nn + nnn

num = int(input("Enter a number: "))

temp1 = str(num)
print(temp1)
temp2 = temp1 + temp1
temp3 = temp1 + temp1 + temp1
total = num +(int(temp2) + int(temp3))
print(total)
print(temp1, '+' , temp2, '+', temp3, '=', total)

# Quotient and Remainder Q/R
num_1 = int(input("Enter first number :"))
num_2 = int(input("Enter Second number: "))

Quotient = int(num_1/num_2)
print("\nQuotient: ", Quotient)

Remainder = num_1 % num_2
print("Remainder: ", Remainder)

#Simple interset
principle = float(input("Enter the principle amount: "))
time = int(input("Enter the time(years): "))
rate = float(input("Enter the rate: "))
simple_int = (principle * time * rate) / 100
print("The Simple interset is: ", simple_int)

#Basic programs 2
cars_list = ['toyota camry', "Honda Accord", "Honda Civic", 'Toyoto Corolla']
cars_list_temp = cars_list[0]
cars_list[0] = cars_list[2]
cars_list[2] = cars_list_temp
print("List of cars after the swap: ",cars_list)

#Swap two elemets of the list without using a temp variable
cars_list = ['toyota camry', "Honda Accord", "Honda Civic", 'Toyoto Corolla']

car1 = 1
car2 = 2
cars_list[car1], cars_list[car2] = cars_list[car2], cars_list[car1]
print("list of cars after the swap: ", cars_list)

#check the duplicate elemets in list
list_student =["Sofia", "Ella","Samuael", "Ella", "Aiden", "Sofia"]
print("Student List :", list_student)
print("Number of students: ", len(list_student))
student_set = set(list_student)
print("\n New student list: ", list(student_set))
print("Length of modifies students list: ", len(student_set))
print("There are %s deuplcate elements"%(len(list_student) - len(student_set)))

#check the list with set using if else stmt
list_str = ["Sofia", "Ella","Samuael", "Ella", "Aiden", "Sofia"]
len_lit_str = len(list_str)
len_set_str = len(set(list_str))
if len_lit_str == len_set_str:
    print("there are no duplicates elements")
else:
    print("There are {} duplicate elements".format(len_lit_str - len_set_str))
    
#check the even or odd num
num_value = 50
print("the number stored in num_value is:", num_value)
if not num_value % 2 == 0:
    print("The numbber is odd number")
else:
    print("The number is an even number")

# input a list of numbers and it will generate List and Tuples
values = input("Enter some comma seperated numbers : ")
list_value = values.split(",")
tuple_value = tuple(list_value)
print("list" , list_value)
print("tuple", tuple_value)

#Sort the Alpabetic order
list_words = input("Enter the words with comma seperated: ")
words = list_words.split(",")
new_list_words = sorted(words)
print(new_list_words)

# sort the sentence
sentence = input("Enter the words with some white-space: ")
words = sentence.split(" ")
set_of_words = set(words)
sorted_set_of_words = sorted(set_of_words)
print(" ".join(sorted_set_of_words))

