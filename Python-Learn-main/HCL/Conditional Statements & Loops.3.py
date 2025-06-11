#Type Conversions with Primitive Datatypes
#String -> Number, NUmber -> String , List -> Tuple

print(type(66))

print(float(66))

a = 66
print(type(a))

print(int(390.8))

a = ("66")
con = int(a)
print(type(con))

int ("12")
conv = str(int)
print(type(conv))

#Type Conversions with Complex Datatypes
old_num = "500"
new_num = "10"

remaining_num = int(old_num) - int(new_num)
print(remaining_num)

old_code = "40.6"
new_code = "60.4"
total_code = float(old_code) + float(new_code)
print(total_code)

value_str = "python world"
value_list = list(value_str)
print(value_list)

# list(1,2,3,4,5)
# print(list)

list((1,2,3,4,5))
print(list)

car_tuple = ('toyota camry', "Honda Accord", "Honda Civic", 'Toyoto Corolla')
print(car_tuple)
my_list = list(car_tuple)
print(my_list)

value_str = "python world"
value_tup = tuple(value_str)
print(value_tup)

nested_list = [['toyota camry', 50],["Honda Accord", 40], ["Honda Civic", 60], ['Toyoto Corolla', 70]]
nested_tuple = tuple(nested_list)
print(nested_tuple)

nested_list = [['toyota camry', 50],["Honda Accord", 40], ["Honda Civic", 60], ['Toyoto Corolla', 70]]
nested_tuple = tuple(nested_list[0])
print(nested_tuple)

pet_list = [('Dog', 1),('cat',2),('Cow',3),('Goat',4)]
pet_tuple = tuple(pet_list)
print(pet_tuple)

#tuple of tuple can be converted into dictinoary.
age_tuple = (('Leo', 18),('Aaron',25),('Eastern',34),('Jordan',45))
print(dict(age_tuple))

#we can`t have the LIST as a key in dictionary eaxmple below
# print(age_tuple = (('Leo', 18),('Aaron',25),('Eastern',34),(['Jordan','John'],45)))
age_tuple1 = (('Leo', 18),('Aaron',25),('Eastern',34),('Jordan',['John',45])) #List as a value in dictonary
print(dict(age_tuple1))

#List of List in Dictonary
age_list = [['Leo', 18],['Aaron',25],['Eastern',34]]
age_dict = dict(age_list)
print(age_dict)

#Type Converstions and Base Conversions

#SET - it will remove duplicates
print(set("apple"))

fruit_tuples = ("apple", "orange", "grapes", "banana", "avocado",  "avocado")
fruit_set = set(fruit_tuples)
print(fruit_set)

