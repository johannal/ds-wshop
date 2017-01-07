# Using mako's sample json file
# get age for a human. allow 
# user to input the name

# steps
# 0 get name from user
# 1 get file from mako.cc
# 2 look in people for human with name matching input
# 3 print age for that human

import requests #grab data from internet

name = input("whose age do u want? ")

jsonresponse = requests.get("http://mako.cc/cdsw.json")

characters = jsonresponse.json() #converts string into python object

people = characters['people']

for person in people:
    if person['name'] == name: # input var name
        print("{0} is {1} years old".format (person['name'], person['age']))
    