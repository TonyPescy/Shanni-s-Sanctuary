#######################################################################################################################################
# Title: Shanni's Sanctuary
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
# Author: Tony Pescatore and Nick Pescatore
# Description: Basic text based adventure game with simple visuals and simple combat.  The goal is to make it to the end alive.
#######################################################################################################################################


#######################################################################################################################################
#Random
import random
random.seed(69)
#######################################################################################################################################

#######################################################################################################################################
# Constants + starting values (CLASS?)
hp = 100    #players hitpoints CREATE SIMPLE VISUAL WITH GRAPHICS
#######################################################################################################################################

#######################################################################################################################################
# Finds room and plays out scenario USES DIVIDE AND CONQUER SORTING METHOD  (MAKE INTO CLASSES)
def roomDesc(x):
    if x == 1:
        roomName = "Small Health Potion"
        return roomName
    if x == 2:
        roomName = "Large Health Potion"
        return roomName
    if x == 3:
        roomName = "Antitoxin"
        return roomName
    if x == 4:
        roomName = "Portable Ward"
        return roomName
    if x == 5:
        roomName = "Light Armor"
        return roomName
    if x == 6:
        roomName = "Heavy Armor"
        return roomName
    if x == 7:
        roomName = "Sturdy Shield"
        return roomName
    if x == 8:
        roomName = "Magic Shield"
        return roomName
    if x == 9:
        roomName = "Buckler"
        return roomName
    if x == 10:
        roomName = "Ancient Sword"
        return roomName
    if x == 11:
        roomName = "Poison Floor"
        return roomName
    if x == 12:
        roomName = "Poison Darts"
        return roomName
    if x == 13:
        roomName = "Arrow Trap"
        return roomName
    if x == 14:
        roomName = "Spiked Pit Fall"
        return roomName
    if x == 15:
        roomName = "Arcane Missles"
        return roomName
    if x == 16:
        roomName = "Log Trap"
        return roomName
    if x == 17:
        roomName = "Fireball"
        return roomName
    if x == 18:
        roomName = "Pendulum Axe"
        return roomName
    if x == 19:
        roomName = "Snake Pit"
        return roomName
    if x == 20:  
        roomName = "Magic Bolts"
        return roomName
    if x == 21:
        roomName = "Honorable Duelist"
        return roomName
    if x == 22:
        roomName = "Decayed Ancient Captain"
        return roomName
    if x == 23:
        roomName = "Golem"
        return roomName
    if x == 24:
        roomName = "Mummy"
        return roomName
    if x == 25:
        roomName = "Cyclops"
        return roomName
    if x == 26:
        roomName = "Harpies" #random number 1-3 of them
        return roomName
    if x == 27:
        roomName = "Skeleton Archers" #random number 1-2 of them
        return roomName
    if x == 28:
        roomName = "Skeleton Swordsmen" #random number 1-4 of them
        return roomName
    if x == 29:
        roomName = "Minotaur"
        return roomName
    if x == 30:
        roomName = "Siren"
        return roomName
    if x == 31:
        roomName = "TBD"
        return roomName
    if x == 32:
        roomName = "TBD"
        return roomName
    if x == 33:
        roomName = "TBD"
        return roomName
    if x == 34:
        roomName = "TBD"
        return roomName
    if x == 35:
        roomName = "TBD"
        return roomName
    if x == 36:
        roomName = "TBD"
        return roomName
    if x == 37:
        roomName = "TBD"
        return roomName
    if x == 38:
        roomName = "TBD"
        return roomName
    if x == 39:
        roomName = "TBD"
        return roomName
    if x == 40:  
        roomName = "TBD"
        return roomName
    if x == 41:
        roomName = "Empty0"
        return roomName
    if x == 42:
        roomName = "Empty1"
        return roomName
    if x == 43:
        roomName = "Empty2"
        return roomName
    if x == 44:
        roomName = "Empty3"
        return roomName
    if x == 45:
        roomName = "Empty4"
        return roomName
    if x == 46:
        roomName = "Empty5"
        return roomName
    if x == 47:
        roomName = "Empty6"
        return roomName
    if x == 48:
        roomName = "Empty7"
        return roomName
    if x == 49:
        roomName = "Empty8"
        return roomName
    if x == 50:
        roomName = "Empty9"
        return roomName
#######################################################################################################################################

#######################################################################################################################################
#Code

def intro():    #intro to the game 
    print("You are walking down the side walk of the city you've spent your entire life in, during that time nothing much has changed.  It was always a small city, but now that you've grown up it seems to have gotten smaller and much duller.  You know every inch of this city like the back of your hand, you could walk the streets blindfolded and make it to work on time.  However today was odd, a peculiar weight was on you shoulders, maybe work was getting to you?  But that can't be making you feel this way can it?.")
    answer = str(input("That's when something catches your eye, something you never saw before.  A large overgrown pyramid in the center of the street, how have you never noticed this before?  A voice speaks to you, it comes from within your own mind, it's beckoning you forth.  Come closer it says, egging you on and on.  Do you listen to what the voice says?  Yes or no? ").lower())
    if answer == "n" or "no":
        print("Your body does not listen to you, instead it does the opposite and begins towards the massive black pyramid.")
    elif answer == "yes" or "y":
        print("Your begin towards the massive black pyramid, unaware of the implications it will have for your future... or if there will be one to come back to. ")
    else:
        print("Please enter yes or no")
        intro()

    

def userName(): #Gets players name
    name = str(input("The voice within asks:  'What is your name?' "))
    name = name[0].upper() + name[1:]
    return name
#userName() TEST

def entrance(name): #entrance to the sanctuary, this decides if user wishes to play the game or not
    answer = str(input(name + ", do you wish to enter Shanni's Sanctuary?  Yes or no? "))
    answer = answer.lower()
    if answer == "no":  #if user says no
        print("No?  Shanni is disappointed with your cowardice, but acknoledges your intellect.  She shall let you live and return to your life, as that is more hellish than what lies within.")
        print("You turn away slowly as the invisble weight appears to be lifted from your shoulders.  As you begin away from the sanctuary you take one last look at its devilish stone before it is blown into dust by the wind.")
        #return answer
    else:   #if user says yes
        print("Yes?  Shanni is delighted with your stupidity, it's not everyday she gets a sacrifice so eager.  Please enter.")
        print("The weight one your shoulders grows heavier as you walk into the black abyss beyond the door.")
        print("Welcome to Shanni's Sanctuary " + name + ", good luck in there, you'll need it.")
        #return answer

def roomGenerator():
    scenario = roomDesc(random.randint(0, 50))

roomGenerator()

#print(entrance(userName())) TEST

#######################################################################################################################################
#FINAL

def main():
    intro()
    entrance(userName())
    roomGenerator()

main()
#######################################################################################################################################