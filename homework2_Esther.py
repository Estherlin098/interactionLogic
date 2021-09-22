#this is Esther lin Week 2 Homework
#assignement 1: Pick four objects in everyday life and represent them as a data type.

idealLife = {
	"wake up": False,
	"location": "Honolulu",
	"house size": 1902,
	"pets": "100 Siamese"
}

#assignment 2: Create an object and verify it using https://jsonlint.com/
#when I run this object in jsonlint, I got the error saying the capalized 'True' is not defined, therefore, I changed it to lower case 'true' and it's valid json. 

tapestry = {
    "nature": True,
    "color": "blue and green",
    "size": 16,
    "about": "forest"
}

#assignment 3: Create your own story algorithm. You can modify an example from class (story maker) or create your own. 
#Remember to comment your code and use examples of: - user inputs - variables (int or float, string, boolean) - concatenation

#welcome messages
print ("-----------------------------------")
print("Welcome to Mad Lib!")
print("Answer the questions below to play.")
print ("-----------------------------------")


#define variables
food1 = input("Enter your favorite food: ")
name1 = input("Enter your name: ")
pet = input("What kind of pet do you have: ")
petname1 = input("Enter your pet's name: ")
food2 = input("Enter your least favorite food: ")
name2 = input("Enter your best friend's name: ")
color1 = input("Enter your favorite color: ")
snack1 = input("Enter your favorite snake: ")
fruit1 = input("Enter your favorite fruit: ")
gift1 = input("Enter your most wanted gift: ")


# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!


story = food1.capitalize() + " party at my house tonight! " + name1 + " is invited, and you can bring your pets " + pet + " " + petname1 + "!" \
" Your job is to mix " + food2 + " with sticky toufu together, and serve it to " + name2 + "." \
" It's dessert time! You decided to make a " + color1 + " cake with " + snack1 + " and " + fruit1 + "." \
" It's midnight and time to go home. Your friend " + name2 + " gave you a/an " + gift1 + "." \
" You were happy and gave " + name2 + " a hug."


#print out story
print(story)

#thought experiment: Imagine some future way to explain one of the data types we talked about in class. 
#Boolean:
#String:
#Number: 