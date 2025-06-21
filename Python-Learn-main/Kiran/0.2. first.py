#
'''
'''
print("Please complete the total python course")

# Variables
kiran = 1000
print(kiran)
#assign single value to mutiple variables
a=b=c=10
print(a,b,c)
#mutiple values and variables
a,b,c = 1,2,3
print(a,b,c)

#memory Location idetification by using id funcation
a=10
print(id(a))

#DataTypes - TYPE will mention which datatype
#int
a= 10
print(type(a))
#float
b = 2.2
#Boolean True =1 Flase =0
d=True
e=False
#Complex
s=1+3j

#Type conversion
a = 10
b=float(a) 
print(b)

#INPUT Funcation

a=int(input("enter the number:  "))
print(a)

#Simple Interset
#PTR/100

p = 10
t = 20
r = 2.2

a = (p*t*r)/100

print(a)

p = 1200
r = 5.4
n= 30
t= 2

a = p*(1 + (r/100))**t

ci = a-p

print(ci)