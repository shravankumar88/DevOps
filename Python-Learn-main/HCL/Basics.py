#Creating Single and multi-single strings

#Print(" " ) or print(' ') or print( """" """")
# Print("Double quoate") or Print('Single Quoate') or Print("pythonn" + 'is' + """awesome""") 

print (' I am a single quoates string')
print (" I am a single quoates string")
print("python " + 'is ' + """awesome""") #concate the string

#quotes matters
#print('I'm learning python') 
print ("I'm learning python")
print('John said "Hello there!"')

#if we want to use the single quote and wants to print we can use BACKSLASH to print
print ('I\'m learning python')
print("John said \"Hello there!\"")

#new line add
print("Hello Sir! \nHow are you?")

#For multi line use triple code
print(''' this  is  a 
      long line''')

#Input function - where we provide the input for the function

question = "what you are learing "
#answer = input()
#print(question + answer)

#Formating Operations with strings

#Manual Concatation
my_vars = 'barks'
print('my dog ' + my_vars +'!') 

# Instead of using manual we can use a method f
print(f'A dog {my_vars}!')

print('A dog {}!'.format(my_vars))

print("John asked \t'How are your?'") #tab space 

print('C:\\users\\Q') #if we need a backslash we need to use two \\a

