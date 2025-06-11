#if-else stmt with complex datatypes
fruit_list = ["apple", "orange", "grapes", "banana", "avocado"]
#case1
if "grapes" in fruit_list:
    print("Yes, Grapes is in fruit_list")
else:
    print("NO, Grapes is in fruit_list")
#Case2
if "strawberry" in fruit_list:
    print("Yes, strawberry is in fruit_list")
elif "orange" in fruit_list:
    print("Yes, orange is in fruit_list")
else:
    print("Both strawberry and orange are not in the fruitlist")

#Case3 - Index based
if fruit_list[1] == "orange":
    print("True")
else:
    print("False")
#case 4- replace the index with LIST
if fruit_list[4] == "avocado":
    print("yes avacodo is at fourth index")
    print("Replacing avocado with strawberry at the fourth index")
    
    fruit_list[4] = "strawberry"
    print(fruit_list)
else:
    print("avacodo is not at the fourth index")
    
if fruit_list[4] == "avocado":
    print(f'yes " {fruit_list[4]} "is at fourth index')
    print("Replacing avocado with strawberry at the fourth index")
    
    fruit_list[4] = "strawberry"
    print(fruit_list)
else:
    print("avacodo is not at the fourth index")

#case 5 with TUPLE
car_tuple = ('toyota camry', "Honda Accord", "Honda Civic", 'Toyoto Corolla')
if "toyota camry" in car_tuple:
    print("car is present")
else:
    print("it is not listed")

#Case 5 chcking mutiple tuples with AND & OR Operator
if "toyota camry" in car_tuple and "Ducati" in car_tuple:
    print("car is present")
else:
    print("it is not listed")
    
if "toyota camry" in car_tuple or "Ducati" in car_tuple:
    print("car is present")
else:
    print("it is not listed")

#case 6 checking dictionary
salary_details = {"Lisa":25000,"Jason":45000,"Cooper":35000,"Elias":23000,"Jordan":77000}
if "Lisa" in salary_details:
    print("We have the salary details for Lisa")
else:
    print("We don`t have the salary details for Lisa")
#trying the varbile example 
# salary_details = {"Lisa":25000,"Jason":45000,"Cooper":35000,"Elias":23000,"Jordan":77000}
# if salary_details[3] == "Cooper":
#     print('index is working {}'.format(salary_details[4]))
# The code attempts to access elements in the dictionary salary_details using numeric indices ([3] and [4]). 
# However, dictionaries in Python are unordered collections, meaning they don't maintain a specific order for their elements. Consequently, accessing elements by numerical indices is unreliable and can lead to unexpected results.

salary_details = {"Lisa":25000,"Jason":45000,"Cooper":35000,"Elias":23000,"Jordan":77000}
if salary_details["Cooper"] == 35000:
  print('Salary of Cooper matches')
  
#Case 7 Adding new salary details to tuple
if "Cora" in salary_details:
    print("we have salary details for cora")
else:
    salary_details["Cora"] = 31000
    print("Cora annual income is %s"%salary_details["Cora"])

#case 8 Nested List
details = [['jane', 'Amanda', 'Emma'],
            [35,40,50],
            [20000,50000,40000]]

max_sal = max(details[2])
print(max_sal)
if (details[2][1] == max_sal):
    if(details[1][1] > 30):
        print(details[0][1], " has the hightest salasry and her age is gretear than 30")
    elif(details[1][1] == 30):
        print(details[0][1], "has the highest salary and she is 30 years old")
    else:
        print("Amanda has the highest salary and her age is less than 30")
else:
    print("amanda is not the highest paid employee")