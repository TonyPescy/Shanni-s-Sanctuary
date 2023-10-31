#######################################################################################################################################
# Title: Encounter
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
# Author: Tony Pescatore and Nick Pescatore
# Description: All encounter descriptions and encounter interactions
#######################################################################################################################################

class Encounter():

    # Initializes basic parts of an encounter
    def __init__(self, e_num, e_desc, r_num, comp):
        self.e_num = e_num                      # Encounter number - Integer
        self.e_desc = e_desc                    # Encounter descrpition - String
        self.r_num = r_num                      # Number that encounter will be assigned to - Integer
        self.comp = False                       # Will determine if encounter has been beaten before or not - Boolean

# Special Encounters
# finEn
# bossEn

# Entrance Starts
# Entrance encounter - For going into the sanctuary
# Parameters:   name = players name
# Return:       N/A
def entrance(name):         # Entrance to the sanctuary, this decides if user wishes to play the game or not
    answer = str(input(name + ", do you wish to enter Shanni's Sanctuary?  Yes or no? "))
    answer = answer.lower()
    if answer == "no":      # If user says no
        print("No?  Shanni is disappointed with your cowardice, but acknoledges your intellect.  She shall let you live and return to your life, as that is more hellish than what lies within.")
        print("You turn away slowly as the invisble weight appears to be lifted from your shoulders.  As you begin away from the sanctuary you take one last look at its devilish stone before it is blown into dust by the wind.")
    elif answer == "yes":   # If user says yes
        print("Yes?  Shanni is delighted with your stupidity, it's not everyday she gets a sacrifice so eager.  Please enter.")
        print("The weight one your shoulders grows heavier as you walk into the black abyss beyond the door.")
        print("Welcome to Shanni's Sanctuary " + name + ", good luck in there, you'll need it.")
    else:                   # If no proper answer is given, program tries again
        print("Enter yes or no")
        entrance()
# Entrance Ends

# Introduction Starts
# Introduction encounter - For finding the sanctuary
# Parameters:   None
# Return:       N/A
def intro():            # Intro to the game 
    print("You are walking down the side walk of the city you've spent your entire life in, during that time nothing much has changed.  It was always a small city, but now that you've grown up it seems to have gotten smaller and much duller.  You know every inch of this city like the back of your hand, you could walk the streets blindfolded and make it to work on time.  However today was odd, a peculiar weight was on you shoulders, maybe work was getting to you?  But that can't be making you feel this way can it?.")
    answer = str(input("That's when something catches your eye, something you never saw before.  A large overgrown pyramid in the center of the street, how have you never noticed this before?  A voice speaks to you, it comes from within your own mind, it's beckoning you forth.  Come closer it says, egging you on and on.  Do you listen to what the voice says?  Yes or no? ").lower())
    if answer == "no":
        print("Your body does not listen to you, instead it does the opposite and begins towards the massive black pyramid.")
    elif answer == "yes":
        print("Your begin towards the massive black pyramid, unaware of the implications it will have for your future... or if there will be one to come back to. ")
    else:               # If no proper answer is given, program tries again
        print("Enter yes or no")
        intro()
# Introduction Ends