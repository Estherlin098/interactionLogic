#this is the Week 2 example

#this is a boolean
they = False
# print (they)

#this is a string
myName = "Esther"

#this is a number
hello = 1
number = 3

var1 = 1
var2 = 4

#this adds things together
#print (myName,hello + number,var1 + var2,"1")

#this is an array
array = (1,"string",myName)
x = 0
# print (array)
# print (array[1])
# print(array[x])

#this is object
myObject = {"firstObject": "Esther", "secondObejct": "Mona", "thirdObject": "Bruno"}
# print (myObject)
# print (myObject["secondObejct"])

myFavoriteFood = [["sushi", "soup", "gummy bears"], ["pizza", "sushi"]]
x = 0
y = 1
#print (myFavoriteFood[x][y])

myDic = {
    "name": "Silly",
    "size": "big",
    "color": "brown",
    "hasTail": True,
    "numberOfLegs": 4
}

print (myDic)
print (myDic["name"])

myCom = {
    "type": "Mac",
    "years": 2015,
    "whose": "Esther",
    "Working": False
}

print (myCom["type"])

########################
from os import system
import random
#from PIL import Image # library for images


sayings = ['Next up is ', 'Introducing ', 'Put your hands together for ']

classmates = ['Bruno', 'Jordan', 'Esther']

chosenIntroduction = random.choice(sayings)
chosenClassmate = random.choice(classmates)

command = 'say ' + chosenIntroduction + chosenClassmate

system(command)
print(command)

# creating a object
#im = Image.open('./classmates/' + chosenClassmate + '.png')

# show the image
#im.show()



