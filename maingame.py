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
import Gui

#random.seed(69)     # Hahahaha funni number
#######################################################################################################################################

#######################################################################################################################################
#Code

############################################################################################################
#FINAL

def main():

    # Builds and displays gui for intro
    # name = Gui.username_gui()
    # print(name)                 # Test 1
    
    # intro_repeat = Gui.intro_gui(name)

    # if intro_repeat == True:            # repeats intro if needed
    #    Gui.intro_gui(name)

    # room creation testing

    random.seed(420)        # Hahaha funni number, for testing
    rm_desc_lst_nums = list(random.sample(range(50), 31))                             # Generates random room descriptions for all rooms, excludes special rooms with constant room descriptions

    room_array = Rooms.Room.room_creation(rm_desc_lst_nums)          # gives the random numbers that will be used to access the descriptions of the rooms

    # print(room_array[0].e_num)                          # prints out encounter number of first room
    # Encounter.room_encounters(room_array[0].e_num)      # prints out room description

    #Encounter.intro()
    #player_name, player_answer = Encounter.user_name_and_ans()
    #Encounter.entrance(player_name, player_answer)

    # Randomize rooms in layout
    #rm_lst = list(random.sample(range(50), 31))
    #print(rm_lst)
    #print ("\n")

    #rm_lst2 = list(random.sample(range(50), 31))
    #print(rm_lst2)
    #print("\n")
    
    # Read room descriptions from text file and puts it into list.  This list is used in room_creation function
    #rm_dsc_lst = Rooms.Room.room_desc_read()
    #print(rm_dsc_lst)

main()
#######################################################################################################################################
