''' 
Arithmetic OPERATORS - +,-,*,//,**,/,%
    Contorl Stmts
        Conditional Stmt(Decision Making) = if, if - else, if - elif- else, nested if - else
        Transfer Stmt (Jumping stmts) = break, contuine, pass
        Iterative Stmt (Looping Stmts) = for, while
    syntax
        if condition:
            Stmt
        elif condition:
            Stmt
        else:
            Stmt
'''

jyothi = 29
indra = 12
if jyothi > indra:  # jyothi < indra: else will print
    print("this is if")
elif jyothi > indra:
    print("elif is True")
else:
    print("if this is false")
    

user_name = 'kiran'
password = "kiran123"
user = input("ENter the User Name: ")
pass_word = input("Enter the pasword: ")
if user == user_name or password == pass_word: #and
    print("success")
else:
    print("Incorrect") 

#nested if
a = 10
b = 30
if a<b:
    print("this is outter if")
    if a>b:
        print("this is inner if")
    else:
        print("this is inner else")
else:
    print("this is outter else")
    
#short hand if
a = 20
b = 30
if a<b: print("this is if")

#short hand if else
a = 20
b=30
print("this is if") if a<b else print("this is else")


''' While Loop
While condition:
    statments(print,if,elif,else,for)
'''

# while True:
#     print("this is loop")
    
shiva =30
while shiva>20:
    print("this is loop", shiva)
    shiva-=1 #siva=siva+1
else:
    print("this is else")