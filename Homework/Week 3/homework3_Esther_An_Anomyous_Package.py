# this is Esther Lin Week 3 Homework

# the Adventures of Tintin - An Anonymous Package

# this is a story about you, Tintin, and Snowy in the New York City. Your job is to help Tintin to save his father from the Joker by collecting keys around the city. 
# you can collect keys through completing tasks in the city or earning money to buy keys from a local Locksmith's owner.

import random # random numbers 

# globe value - define the player's characteristics
player = { 
    "money": 0,
    "keys": 0,
    "keysValue": 20
}    

# this gives users time to read the text
def userBreak(): 
    return (input("press return key to continue >"))

# print out the user's current money and received keys
def resourceCount():
    print("You currently have $" + str(player["money"]) + " and " + str(player["keys"]) + " key(s)!" )
    return(userBreak())

# this is the game result
def gameResult(): 
    print ("""
    
-----------------------------------
You made it! This is the final game result!

    """)

    # success: have 3 keys
    if player["keys"] == 3:
        print ("You now have $" + str(player["money"]) + ", and found 3 keys. It seems like you don’t to buy more keys!")
        print ("Congratulations! You have successfully opened the gem box and use the map to help saving Tintin’s father.")
    
    # less than 3 keys and have money to buy the rest of the keys
    elif player["keys"] < 3 and player["money"] >= 20:
        print ("You now have $" + str(player["money"]) + ", and found " + str(player["keys"]) + " keys. you need to buy " + str(3 - player["keys"]) + " key(s) from the Locksmith's owner. ")
        userBreak()
        addKeys = player["money"] / 20
        player["keys"] += addKeys
        
        # succesful: use money to purchase the remaining keys
        if player["keys"] >= 3:
            print ("Congratulations! You have successfully trade with the Locksmith’s owner, opened the gem box and use the map to help saving Tintin’s father. ")
        
        # game over: don't have enough money to buy 3 keys
        else:
            print ("It seems like you don’t have enough money to buy remaining keys, ($20 per key). Please play again to help save Tintin’s father. ")
    
    # game over: don't have enough money to buy 3 keys
    else:
        print ("You now have $" + str(player["money"]) + ", and found " + str(player["keys"]) + " keys.")
        print ("It seems like you don’t have enough money to buy remaining keys, ($20 per key). Please play again to help save Tintin’s father. ")
        print ("""
  ___   __   _  _ ____     __  _  _ ____ ____ 
 / __) / _\ ( \/ |  __)   /  \/ )( (  __|  _ \
( (_ \/    \/ \/ \) _)   (  O ) \/ /) _) )   /
 \___/\_/\_/\_)(_(____)   \__/ \__/(____|__\_)

        """)

    return()

# this is the last scene of the story
def giftShop(): 
    userInput = input("\nYou walk into the gift shop on the rooftop and talked to the staff there saying you are looking for keys or more clues to save Tintin’s father. The staff gives you two balls, and says “one ball contains a key, and one ball contains $10.” \nDo you choose the ball on his left hand or right hand? 'R'/'L' > ")
     
     # right: receive a key
    if (userInput.upper() == "R"):
        player["keys"] += 1
        print ("\nCongratulations! You got a key from the staff!")
    
    # left: receive $10
    else:
        player["money"] += 10
        print ("\nCongratulations! You received $10 from the staff!")
    
    resourceCount()
    return ()

# this is the fifth part of the story
def luckyDay (): 
    userInput = input("\nAt the rooftop, you see a man with a dice saying 'Is today your lucky day?' \nDo you want to pay $10 to play? \nHint: you may find a key from playing the dice! 'Y'/'N' > ")

    # roll the dice: -$10        
    if (userInput.upper() == "Y"):
        player["money"] -= 10
        userInput = input("\npress the return key to roll the dice >")
        dice = random.randint(1,6)
        print ("You rolled: " + str(dice) + " out of 6.")
        userBreak()

        # rolled 1-4: get nothing           
        if (dice < 5):
            print ("\nSmaller than 5? I guess today is not your lucky day...")
        
        # rolled 5-6: receive $20       
        elif (dice >= 4 and dice < 6):
            print ("\nBigger than 4? Today is your lucky day! \nCongratulations! You received $20!") 
            player["money"] += 20
        
        # rolled 6: receive a key
        else:
            player["keys"] += 1
            print ("\nYou got 6! Today is your super lucky day! Congratulations! You got a key") # if the user roll the dice and receive 6, the user will get a key
  
    resourceCount()
    return()

# this is the fourth part of the story
def rockefeller(): 
    userInput = input("\nYou arrived at the Rockefeller center. And Snowy suddenly starts barking at this young man with a black backpack. \nYou have three options, ['1' - tell Snowy to be quiet, '2' - call the police, '3' - talk to the man] > ")
    
    # option 1: get nothing
    if (userInput == "1"):
        print ("\nSnowy is not happy but he quiets down. Let's head to the rooftop now!")
    
    # option 2: receive a key
    elif (userInput == "2"):
        print ("\nThank god you called the police, the young man was carrying a gun in his backpack and you just save everyone in the building. The police gives you a gift bag and you found a key inside. \nCongratulations! You found a key!")
        player["keys"] += 1
    
    # option 3: receive $20
    else:
        print ("\nWhen you walk up to the man, he suddenly put a knife around your neck and tell everyone don’t move and give him all the valuables. Someone called the police and the police saved you. \nCongratulations! You received $20 from the police as a reward to be the bravest man in the world.")
        player["money"] += 20
    
    resourceCount()
    return()

# this is the third part of the story
def foodTruck(): 
    userInput = input("\nYou get off the train and see a food truck. You then realize you are really hungry. Do you want to buy a burger? 'Y'/'N' > ")

    # yes: receive a key
    if (userInput.upper() == "Y"):
        print ("\nYou open the burger wrap, you found out there’s a key under the wrap. \nCongratulations! You received a key!")
        player["keys"] += 1

    # no: get nothing
    else:
        print ("\nCongratulations! You saved $10 from not buying the food!")
    
    resourceCount()
    return()

# this is the second part of the story
def subwayScene(): 
    userInput = input("\nOn the subway, you find an empty seat and sit down. But later you see the old man with a lot of groceries, would you give up the seat for him? 'Y'/'N' > ")

    # yes: receive $10
    if (userInput.upper() == "Y"):
        print ("\nOld man: Thank you, friend! \nCongratulations, you received $10 from helping the old man.")
        player["money"] += 10
    
    # no: get nothing
    else:
        print ("\nIt seems like you are really tired! Resting more on the train will help you find more keys.")
    
    resourceCount()
    return()

# this is the first part of the story
def stairScene(): 
    print ("Here is the clue message from anomyous package:'Explore the city and head to the Rockefeller Center rooftop, you may find something there.'")
    userBreak ()
    print ("\nTintin: I'm wondering what's in the Rockefeller Center. Let's take the train and check it out!")
    userBreak ()

    userInput = input("\nTintin: Oh! I saw an old man who might need help carrying his groceries down the subway stairs, should we help? 'Y'/'N' > ")
    
    # yes: get nothing
    if (userInput.upper == "Y"):
        print ("\nOh, you are too late. Someone is helping him now.")
    
    # no: receive $10
    else:
        print ("\nYou see a $10 bill on the ground and picked it up. I guess, sometimes, bad karma leads to good things.\nCongratulations! You received $10!")
        player["money"] += 10
    
    resourceCount()
    return()

# this is the introduction of the story
def intro(): 
    
    print ("""
Welcome to The Adventures of Tintin - An Anonymous Package

-----------------------------------

After Tintin and Snowy's adventure in Tibet,they received an anonymous package containing a gem box and a clue. This gem box contains a map that would help them save Tintin's father from the Joker in New York City. 
Your job is to help Tintin collect three keys around the city to unlock the gem box and save Tintin's father. 

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢦⠙⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⢯⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⠛⢿⣿⣿⣿⣿⣿
⣿⣿⣿⢧⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡕⠂⠈⢻⣿⣿⣿⣿
⣿⣿⡅⣻⡿⢿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠿⢿⣿⡇⠀⠀⠈⣿⣿⣿⣿
⣿⣿⠀⠀⠀⠘⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⣹⣿⣿⣿
⣿⣿⠀⠀⠀⠀⣿⣿⡿⠿⠛⠻⣿⣿⣿⣿⡿⠟⠁⠈⠀⠉⠻⡆⠀⠀⠀⣿⣿⣿
⣿⣯⠄⠂⠀⠀⣿⡋⠀⢀⠀⠀⠀⠉⣿⣿⡀⠀⠀⠘⠓⣠⣶⣿⡀⠀⠀⠘⣿⣿
⣿⣫⡆⠀⠀⢀⣿⣷⣶⣄⠀⢀⣤⣴⣿⣿⣿⣶⣄⠀⣴⣿⣿⣿⠁⠀⠀⠀⠘⣿
⣿⣿⠁⠀⠀⡤⠙⢿⣿⣿⣷⣾⣿⡿⣿⣿⢿⠿⣿⣧⣿⣿⡿⢣⠀⠀⠀⠀⢠⣿
⣷⣌⠈⠀⠀⠀⠀⣆⠈⡉⢹⣿⣿⣆⡀⠀⠀⢠⣿⣿⣿⡿⢃⣼⠀⠀⠀⠀⣸⣿
⣿⣿⡇⠀⠀⠀⠀⠙⢿⣿⣆⠈⠛⠛⠛⠀⠀⠈⠉⠁⠀⢠⣿⠇⠀⠀⠀⠹⢿⡇
⣿⡫⠀⠀⠁⠀⠀⠀⠈⠻⣿⢢⣄⠀⠀⠀⠀⠀⣀⣠⣾⡾⠋⠀⠀⠀⠀⢀⠴⠋
⣿⣁⠄⠀⠀⠀⣀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⠿⡿⠋⠀⠀⠀⠀⠀⣀⠬⠆⢀
⣿⣿⣧⣄⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠠⠙
""")
    userBreak ()
    print ("""
There are the two ways you can retrieve the keys:

1. Find the key from completing tasks in the city using the clues found in the gem box
2. Earn as much money as possible to buy keys from a local Locksmith's owner ($20 per key)

-----------------------------------

    """)
    userBreak ()
    
    # ask for user's name
    userName = input("Now, introduce yourself to Tintin and Snowy, what's your name? ") 

    print ("Hello " + userName + "! This is Tintin, thank you for joining this adventure with us! ")
    print ("""
      _,, \n
    (/..\ \n
     \ -/ \n
    _\`.|_ \n
    /`H  I'\ \n
    ( (H  I- ) \n
     \/==O=\/ \n
    >    , \ \n
    /    /   \ \n
        /\    \ \n
       /  \   / _ \n
     ,"    `-.`'/ \n
    --.       \P Ojo. \n
    `""
    """)
    
    userBreak ()
    return()
     

def main():
    intro() # start the intro
    stairScene () # start the first scene of the story
    subwayScene() # start the second scene of the story
    foodTruck() # start the third scene of the story
    rockefeller() # start the fourth scene of the story
    luckyDay() # start the fifth scene of the story
    giftShop()  # start the last scenen of the story
    gameResult() # show game result


main() # this is the first thing that happens