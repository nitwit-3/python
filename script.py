#! /bin/python3 
# Variables and Methods 
import sys
	
quote="All is fair in love and war!" #variable
print(quote)
print(quote.upper()) #Method Uppercase
print(quote.lower()) #Method Lowercase
print(quote.title()) #Method Titlecase
name = "Brian" #string
age = 30 #int int(30)
gpa = 3.7 #float float(3.7)
print(int(age)) 
print(int(30.9))

print ("my name is " + name + " and i am " + str(age) + " years old")
age += 1
print(age)
birthday = 1 
age += birthday
print(age)

print('\n')
#function
print("here is an example function:")

def who_am_i(): #this is  a function
	name= "Brian"
	age= 30
	print ("my name is " + name + " and i am " + str(age) + " years old")
who_am_i()

def add_one_hundred(num): #adding parameters
	print (num + 100)
add_one_hundred(100)

def add(x,y): #multiple parameters
	print(x + y)
add(7,7)

def multiply(x,y):
	return x*y #store a value for later
multiply(7,7)

def new_line():
	print('\n')
new_line()

#Boolean Expressions (True or False)
print("Boolean expressions:")

bool1 = True
bool2 = 3*3 == 9 
bool3 = False
bool4 = 3*3 != 9 

print(bool1,bool2,bool3,bool4)
print(type(bool1))

new_line()

#Relational and Boolean Operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7 

test_and = (7 > 5) and (5 < 7) #True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) #True
test_or2 = (7 > 5) or (5 > 7) #True

test_not = not True #False
new_line()
#Conditional Statement

def drink(money):
	if money>=2:
		return "You got yourself a drink!"
	else:
		return "NO drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age,money):
	if (age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with more money."
	elif (age < 21) and (money > 5):
		return "Nice try kid."
	else:
		return "You're too poor and too young"

print (alcohol(21,5))
print (alcohol(21,4))
print (alcohol(20,4))

new_line()
#lists - have brackets []

movies = ["When Harry met Sally", "Hangover", "The perks of being a wallflower", "the excorcise"] 
print (movies[1]) # list always start from 0, this will return Hangover
print (movies[0])
print (movies[1:3]) # ranges 
print (movies[1:])
print (movies[:1])
print (movies[-1]) #last one if you dont know how many in your list.

print (len(movies))
movies.append("JAWS")
print (movies)

movies.pop() # deletes last in list
print(movies)

movies.pop(0) # deletes fist in list 
print(movies)

new_line()
#Tuples - Do not Change, have parentheses ()
grades = ("a", "b", "c", "d", "f")
print(grades[1])

new_line()	
#looping

#for loops- start to finish of an a repeated jester
vegatables = ["cucumber", "spinach", "cabbage"]
for x in vegatables:
	print(x)

#While loops - execute as long as true 

	i = 1
	while i < 10:
		print(i)
		i += 1
sys.exit()
