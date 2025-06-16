#RangeFunction In For Loop
my_range = range(5)
print(my_range)

print(tuple(my_range))
print(list(my_range))

print(list(range(5, 10)))
print(list(range(-5, 5)))

# for i in range(3.5): # Range funcation will only work on integers not floats
#     print(i)

# for i in range("c", "y"): # Range funcation will only work on integers not string
#     print(i)

for i in range(6):
    print(i)

for i in range(3):
    print("Hello")

for _ in range(3): #When we use _ as the name of a avarible in python. The Value of the element is not going to accessed
    print(i)

#Setting Intervals In a Range
#Passing Mathmatic expressions in integers
for i in range(2 ** 2):
    print("Python")

for i in range(5, 8):
    print(i, "Square is", i ** 2)
print("End of loop")

#How to reverse the range
x = range(5)
y = "Welcome"

for i in reversed(x):
    print(i)

for i in reversed(y):
    print(i)

#Gap intervals for the range function

print(list(range(2,10,1))) # Output [2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2,10,2))) # [2, 4, 6, 8]
print(list(range(2,10,3)))
print(tuple(range(5,-10,-2)))
'''
Slicing in Python

Slicing is a powerful technique in Python that allows you to extract a sub-sequence from a sequence data type like strings, lists, tuples, and ranges. It provides a concise and efficient way to access specific portions of these sequences.

Syntax:

Python
sequence_name[start:stop:step] '''
start = -2
stop = -10
step = -2
for number in range(start, stop, step):
    print(number)

for i in range(1, 10):
    if i % 2 == 0:
        print("The number %s is divisible by 2" %i)
    else:
        print("The number %s is not divisible by 2" %i)
        

for i in range(1, 11): #ptuput will be 67 8 9 10
  if i > 5:
    print(i)

num_list = []
for i in range(1,21):
    if (i%3 ==0 or i %5 == 0):
        num_list.append(i)
print(num_list)

items = []

for i in range(100, 301):
    num_str = str(i)
    #print("num_str : ", num_str, items)
    first_digit = int(num_str[0])
    second_digit = int(num_str[1])
    thrid_digit = int(num_str[2])
    if(first_digit %2 ==0) and (second_digit %2 ==0) and (thrid_digit %2 ==0):
        items.append(num_str)
print(",".join(items))

for num1 in range(1, 10):
    print("num = ", num1, ";", end = " ")
    for num_2 in range(1,10):
        print("{:2d}".format(num1 * num_2), end = " ")
    print()

#Execrise1   
for i in range(1,10):
    cube = i ** 3
    print(cube)
    
orignal_list = [1, 2, 3, 4,5,6]
cubes_list = []

for i in orignal_list:
    cubes_list.append(i ** 3)
print("cubes_list",cubes_list)

#Execrise2
cars_list = [['volks','Mer','BMW'],['Honda','Toyo','Mazda']]
full_list = []

for cars1 in cars_list:
    print("cars1: ", cars1)
    for car in cars1:
        full_list.append(car)  #Add "car" to the end of the list
print(full_list)

#Execrise3
for i in range(2000,2100):
    if i % 4 == 0:
        
        print("first: ", i)

for i in range(2000,2100,4):
    print("second: ",i)

leap_year = range(2000,2100,4)
leap_list = list(leap_year)
print(leap_list)