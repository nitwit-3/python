#! /bin/python3 
import sys #system functions and paramerters
from datetime import datetime as dt #import part of a import and set an alias 

print(dt.now())
my_name = "Brian"
print(my_name[0])
print(my_name[-1])
sentence = "This is a sentence"
print(sentence[:4])
print(sentence.split())
sentence_split = sentence.split()
sentence_join = ' '.join(sentence.split())
print(sentence_join)

quote = "He said, \"give me all your money\""
print(quote)
def new_line():
	print('\n')
new_line()

#Dictionaries - Key/value pairs - uses curly Cues {}
drinks = {"White Russian":7, "Old Fashion":10, "Lemon Drop": 8} #Drink is Key: price is value
print(drinks)
#employees{"Finance":["Bob", "Linda","Tina"], "IT":["Gene","louis","Teddy"]}
#print(employees)

#employees["Legal"] = ["Mr.Frodo"] #add a new value pair
#print(employees)

#employees.update({"Sales": ["Andie", "Ollie"]}) #add new key:value pair
#print(employees)

drinks ["White Russian"] = 8
print(drinks)

print(drinks.get("White.Russian"))

sys.exit()
