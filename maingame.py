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
# import Character
import random
random.seed(69)     # Hahahaha funni number
#######################################################################################################################################

#######################################################################################################################################
#Code

# Username Starts
# Gets the users name
# Parameters:   None
# Return:       Users name with first letter uppercase and all others lowercase
def user_name(): # Gets players name
    name = str(input("The voice within asks:  'What is your name?' "))
    name = name[0].upper() + name[1:].lower()       # Makes name look nice
    return name
# Username Ends
#userName() TEST

############################################################################################################
#FINAL

def main():
    #Encounter.intro()
    #Encounter.entrance(user_name())

    # Randomize rooms in layout
    room_list = list(random.sample(range(50), 31))
    print(room_list)

main()
#######################################################################################################################################