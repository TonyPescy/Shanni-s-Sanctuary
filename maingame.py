#######################################################################################################################################
# Title: Maingame
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
# Author: Tony Pescatore and Nick Pescatore
# Description: Basic text based adventure game with simple visuals and simple combat.  The goal is to make it to the end alive.
#######################################################################################################################################


#######################################################################################################################################
# Imports
# import os
import Encounter
import Rooms
# import Character
import random

#random.seed(69)     # Hahahaha funni number
#######################################################################################################################################

#######################################################################################################################################
#Code

############################################################################################################
#FINAL

def main():
    #Encounter.intro()
    #player_name = Encounter.user_name()
    #Encounter.entrance(player_name)

    # Randomize rooms in layout
    rm_lst = list(random.sample(range(50), 31))
    print(rm_lst)
    print ("\n")

    rm_lst2 = list(random.sample(range(50), 31))
    print(rm_lst2)
    print("\n")
    
    # Read room descriptions from text file and puts it into list.  This list is used in room_creation function
    rm_dsc_lst = Rooms.Room.room_desc_read()
    print(rm_dsc_lst)

main()
#######################################################################################################################################