'''If-else Contorl Strcutures in Python

Conditions https://docs.python.org/3/reference/expressions.html#operator-precedence

== , != < > <=

if stmsts with Primitive datatype
'''
if 10 < 15:
    print("10 is less than 15")
    
if 46 > 40 +5:
    print("46 is greater than 45")
    
x_value = 65
y_value = 25
if x_value < y_value:
    print("vale of x is les thn value of y")
    
# in keyord will check whether the strig is present or not
my_string = "Hello python world"
if "python" in my_string:
    print("Yes, python is in my_string")
    
list_student = ["Ayden", "Gavin", "Ian", "Jose", "Jane"]
list_student

if "Jose" in list_student:
    print("student is present")
    
#if stmsts with complex datatype
tuple_teachers = ("Alice", "Alexa", "Robert", "Bella")
print (tuple_teachers)

if "Alexa" in tuple_teachers:
    print("teachers is present")

#dictonary
student_score = {"Ayden":60, "Gavin":85, "Ian":76, "Jose":70}
print(student_score)

if "Ayden" in student_score:
    print("Ayden score", student_score["Ayden"])

if "Ayden" == 60 in student_score :
    print("test")
    

#logical if stmt
a = 60
b = 35
if a > b and b < a:                     
    print("a is greater than b")
if a>b or b<a:
    print("At least one of the above conditions is true")

bike_price = 715
bike_is_electric = False
if bike_price > 500 or bike_is_electric == True:
    print("At least one of the above conditions is true bike")  
if not bike_is_electric:
    print("it is an human bike")

if not (a<b):
    print("x is not less than y")

#if-else Elif stmts
if 10 > 20:
    print("10 is greater than 20")
    print("if block activated")
else:
    print("10 is less than 20")
    print("else block activated")

# ternary operators(conditional expressions)
# evaluate someting based on a condition being true or not
num = 50
print("num before expression: ", num)
num = num - 20 if num > 20 else num + 20
print("num before expression: ", num)

num = 50
print("num before expression: ", num)
if num > 20:
    num = num - 20
else:
    num = num + 20
print("num before expression: ", num)

num = 100
print("num before expression: ", num)
if num < 50:
    result  = num / 5
else:
    result = num * 5
print("num before expression: ", result)

num = 100
result = num / 5 if num < 50 else num * 5
print("num before expression: ", result)

#elseif stmt
if 15 > 20:
    print("15 is greater than 20")
    print("if block activated")
elif 15 < 20:
    print("15 is less than 20")
    print("elif block activated")
else:
    print("Both are equal")
    print("else Bloack activated")
    
#Nested If-else stmt
x = 25
y = 35
z = 45
if x < y:
    print("the first condition is true")
    if x < z:
        print("Both conditions are true")
    else:
        print("the first condition is true and the second condition is false")
        
x = 55
if x < y:
    print("the first condition is true")
    if x < z:
        print("Both conditions are true")
    else:
        print("the first condition is true and the second condition is false")
else:
    print("the first condition is false")
        