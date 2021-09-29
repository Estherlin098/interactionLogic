# this is week 4 class (for and while loops)

# for x in range (1,50): # add one every time
#     if x > 5:
#         break
#     else:
#         print ("the number is " + str(x) + " and x is smaller than 5")

# fruit = ['a', 'b', 'c']
# for singleFruit in fruit:
#     print (singleFruit)

# print("---------------------------------")
# numbersOfStudents = 21
# for x in range (0,numbersOfStudents): #print within this range from 0-21
#     print(x)

# print("---------------------------------")
# for x in range(len(fruit)): # loop 3 times - the numbers of items in fruit
#     print("x is " + str(x))
#     print("Fruit is " + fruit[x]) # fruit[x] - fruit[1]

# print("---------------------------------")
# animal = ['elephant', "zebra", "bird"] # this is an array
# for eachAnimal in range(len(animal)): # the numbers of loop is the length is animal list
#     print(animal[eachAnimal]) # the start of the for loop is 0

# print("---------------------------------")
# list = {
#     'hello': 2,
#     'my name': 3,
#     'Esther': 4
# }
# print(len(list))
# print("---------------------------------")

# listTwo = ["firstItem", ["secondItem"], [["1", "2", "3"]]]
# print(len(listTwo))



# print("---------------------------------")
# for eachItem in range(len(list)):
#     print (eachItem)

# print("---------------------------------")
# def countNumber(theNumber): # print out the command line 10 timees
#     print("count: " + str(theNumber))

# for theNumber in range(1,10):
#     countNumber(theNumber)

# for x in range(0,3):  
#     for y in range(0,5): # loop y in each x
#         print(x,y)

# global x # define global x that can be shared in the file
# x = 0

# def increaseCount():
#     global x # borrowing the global x here
#     x += 1

# while x < 10:
#     increaseCount()
#     print (x)


# recursion: the function recall itself - it happends forever

# from turtle import *
# for i in range(500): # this "for" loop will repeat these functions 500 times
#     forward(i)
#     left(91)

# from turtle import *
# import random

# for n in range(60):
#     penup()
#     goto(random.randint(-400, 400), random.randint(-400, 400))
#     pendown()

#     red_amount   = random.randint( 0,  30) / 100.0
#     blue_amount  = random.randint(50, 100) / 100.0
#     green_amount = random.randint( 0,  30) / 100.0
#     pencolor((red_amount, green_amount, blue_amount))

#     circle_size = random.randint(10, 40)
#     pensize(random.randint(1, 5))

#     for i in range(6):
#         circle(circle_size)
#         left(60)


# from turtle import *

# fillcolor('purple')
# pensize(10)
# pencolor('black')
# forward(100)

# begin_fill()
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# forward(100)
# left(90)
# end_fill()


# from turtle import *

# colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
# bgcolor('red')

# for x in range(350):
#     pencolor(colors[x % 6])
#     width(x / 100 + 1)
#     forward(x)
#     left(59)


# Step 1: Make all the "turtle" commands available to us.
import turtle

# Step 2: Create a new turtle. We'll call it "bob"
bob = turtle.Turtle() #name the turtle as bob

# Step 3: Move in the direction Bob's facing for 50 pixels
bob.forward(50)

# Step 4: We're done!
turtle.done()