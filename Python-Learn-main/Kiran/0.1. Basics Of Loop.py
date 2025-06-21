'''    Contorl Stmts
        Conditional Stmt(Decision Making) = if, if - else, if - elif- else, nested if - else
        Transfer Stmt (Jumping stmts) = break, contuine, pass
        Iterative Stmt (Looping Stmts) = for, while
            While Loop: Repeats the stmt or group of stmts while a given condition is TRUE. It tests the condition before executing the loop body.
            For Loop: Executes the code block mutiple times and abbreviates the code that manage the loop variable
            Nested Loop: We can iterate a loop inside another loop
'''

# For Loops
'''The first question to ask at this point, though is, what exactly is a for loop?One way to put it is that a for loop allows us to processthe elements in a sequence one at a time.
That is, it allows us to iterate over the contents of that sequence.And in the context of Python, you will know that sequences could be inthe forms of list, tuples, dictionaries, sets, and so on.'''

for letters in ['H','E','E','L','O']:
    print(letters)
    
for letters in "Hello":
    print(letters)

my_string = "Hello World"
for char in my_string:
    print(char)
    
for digit in "10":
    print(digit)

# Iterating Over Elements in a Tuple and Dictinoary

for country in "Germany", "India", "Israel": # LIST
    print(country)

dogs = ("Pug", "Doberman", "Golden Retriever") # TUPLE

for dog in dogs:
    print("It`s a ", dog)

dog_weight = (("Pug", 20), ("Doberman", 80), ("Golden Retriever", 55)) # TUPLES OF TUPLES

for i, (dog, weight) in enumerate(dog_weight): # It will return at each iteration not only the individual element, which is a tuple, but also an index for that element within the obj
    print("The dog ar index %d is a %s and it weights %s pounds" %(i, dog, weight))
    
''' %d: This is a format specifier for decimal integers. and %s: This is a format specifier for strings
The character after the % in the print statement corresponds to the type of variable you want to format. 
In this case, %d is used for an integer (the index), %s is used for a string (the dog's name), and %s is also used for the weight, which is presumably a string or could be a number that you want to convert to a string.
'''

friends = ["john", "sam", "jill"] #LIST
for friend in friends:
    print("Happy New Year, ", friend)

student_scores = {"john": 80,"sam" : 60, "jill":50, "bob" : 96} #Dictionary

for student in student_scores:
    print("student  ", student)

for student in student_scores.keys():
    print("key-students", student)

for student in student_scores.values():
    print("values ", student)
    
for student in student_scores.items():
    print("items ", student) # printed in tuple  format

for key in student_scores:
    print("KEy Value pair - ", key, ";", student_scores[key])

for student, score in student_scores.items():
    print("Student: ", student, "\tScore: ", score)
    
# Else for the loop
#Arthemtic Operators

numbers = [4,6,7,8,9]

for num in numbers:
    quotient = num // 2
    print(quotient, "is the quotient of", num, "/2")

mixed_list = [145, 10.5, 1+3j,
              True, "Python",
              (0, 1),[2, -5],
              {"class":"V", "Section":"A"}]

for item in mixed_list:
    print("Type of", item, "is ", type(item))
    
num_list = [2,4,6,8]
square = 0
for val in num_list:
    square = val ** 2
    print("Square of ", val, "is ", square)
    
#WAP to caluclate the string withour using len funcation
string = input("Enter the string: ")
count = 0
for i in string:
    count = count + 1
    print(count) # output will be 1 2 3 4 5 input=kumar

string = input("Enter the string: ")
count = 0
for i in string:
    count = len(string)
    print(count) # Output will be 5 5 5 5 5 input = kumar

numbers = [2,3,4,5]

for num in numbers:
    print(num)
else:
    print("No more items left in the list.")
    
#SET
characters = {"a", "c", "d", "f", "g"}
for chara in characters:
    print(chara)
else:
    print("No charaters left")

# Nested Loop
us_cities = ["New york", "Nashville", "Seattle"]
for city in us_cities:
    if city == "New york":
        print("city is present")

#iterate collection of intergers and see any even numbers with in the list

numbers = [11,33,44,55,66,34,67,89,88]
for num in numbers:
    if num % 2 == 0:
        print(num, "it is even number")
    else:
        print(num, "it is odd number")

#LISt Inside LIST
names = [["Mary", "Lisa", "Jessica"],["James","Jacob","Willaim"]]
for sublist in names:
    print(sublist)

for sublist in names:
    for name in sublist:
        print(name)

colors_list = ["red","green","black"]
objects_list = ["pen", "market", "pencil"]

for color in colors_list:
    for obj in objects_list:
        print(color, obj)