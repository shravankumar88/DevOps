#Change the order of precedence of opertors in an expression #eg 10 -4 *2
#Summarize the memership opertors in python
#Convert a string to a list of charaters

a = 10
b = 4
c = 2
result = (a - b) * c
print("Result : ", result)

color_list = ["Black", "Green", "Pick", " Yellow"]

if "Black" and "Pick" in color_list:
    print("Color is listed")
else:
    print("Color is not listed")
    
str = input("Enter a string : ")
convert_list = list(str)
print("Hope it works: ", convert_list)

if 'bin' in {'float' : 1.2 , 'bin': 0b010}:
    print('a')
    print('b')
print('c')

value = 4 

# a = str(value)
# b = a + “^” + “2”
# c = a + “^” + “3”

# print(value, “+”, b, “+”, c)

a = "40.6"
b = "60.4"
c = a +b
print(c)

a = [1, 'one', {2: 'two'}, 3]
b = len(a)

if b == 4:
   print('Length of this list is 4')
   if b == 5:
       print('Length of this list is 5')
   else:
         print(b)

if None:
            print('Hi')         