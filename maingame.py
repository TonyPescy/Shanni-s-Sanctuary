#######################################################################################################################################
# Title: Maingame
# Author: Tony Pescatore and Nick Pescatore
# Description: Basic text based adventure game with simple visuals and simple combat.  The goal is to make it to the end alive.
#######################################################################################################################################


#######################################################################################################################################
# Imports
import Encounter as en
import Rooms as rm
import Character as char
import random as rand
# import Gui

#random.seed(69)     # Hahahaha funni number
#######################################################################################################################################

#######################################################################################################################################
#Code

############################################################################################################
#FINAL

def main():
    rand.seed(420)        # Hahaha funni number, for testing

    # Room Creation and randomize rooms in layout
    rm_lst = list(rand.sample(range(50), 31))
    # Read room descriptions from text file and puts it into list
    rm_dsc_lst = rm.Room.room_desc_read()

    # creates an array that has all randomly chosen rooms
    # Use as rooms_array[desried_room_num].desired_prop
    rooms_array = rm.Room.room_creation(rm_lst)

    # en.intro()
    # player_name, player_answer = en.user_name_and_ans()
    # en.entrance(player_name, player_answer)

    # creates character object for player
    # used in combat and the sort
    #player = char.Character(player_name)
    # print(player.name)

    # Entrance Encounter
    # print(rooms_array[30].num)
    # print(rooms_array[30].pathing)
    next_room = 0      # room starts at 0 because non-randomized descriptions are appened after the random ones
    rooms_array, next_room = en.room_encounters(next_room, rm_dsc_lst, -3, rooms_array)  # always starts at zero, later we will use next_room for first parameter
    print(next_room)

    # 'Random' Encounters and boss encounter
    # maybe a while statemnt that will run until the rooms equal the boxx encounter? (door will close in boss encounter)
    while next_room < 32:
        rooms_array, next_room = en.room_encounters(next_room, rm_dsc_lst, rooms_array[next_room].e_num, rooms_array)  # always starts at zero, later we will use next_room for first parameter
        print(next_room)

    # Exit Encounter
    en.room_encounters(next_room, rm_dsc_lst, -2, rooms_array) # final room, exit room
    

main()
#######################################################################################################################################
