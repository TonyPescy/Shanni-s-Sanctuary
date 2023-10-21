#######################################################################################################################################
# Title: Maingame
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
# Author: Tony Pescatore and Nick Pescatore
# Description: Basic text based adventure game with simple visuals and simple combat.  The goal is to make it to the end alive.
#######################################################################################################################################


#######################################################################################################################################
# Imports
import Encounter
import Rooms
import Character
import random
random.seed(69)
#######################################################################################################################################

#######################################################################################################################################
#Code  
def userName(): #Gets players name
    name = str(input("The voice within asks:  'What is your name?' "))
    name = name[0].upper() + name[1:]
    return name
#userName() TEST

############################################################################################################
#FINAL

def main():
    #Encounter.intro()
    #Encounter.entrance(userName())

    # Randomize rooms in layout
    roomList = list(random.sample(range(50), 30))
    print(roomList)

main()
#######################################################################################################################################