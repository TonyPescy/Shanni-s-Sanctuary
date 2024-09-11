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

    # Room Creation
    # Randomize rooms in layout
    rm_lst = list(rand.sample(range(50), 31))
    # print(rm_lst)
    # Read room descriptions from text file and puts it into list
    rm_dsc_lst = rm.Room.room_desc_read()
    #print(rm_dsc_lst[5])

    # creates an array that has all randomly chosen rooms
    # Use as rooms_array[desried_room_num].desired_prop
    rooms_array = rm.Room.room_creation(rm_lst)
    # print(rooms_array)
    # print(rooms_array[3].e_num)

    #en.intro()
    #player_name, player_answer = en.user_name_and_ans()
    #en.entrance(player_name, player_answer)

    # creates character object for player
    #player = char.Character(player_name)
    #print(player.name)

    # Entrance Encounter
    # print(rm_dsc_lst[rooms_array[-3].e_num])
    next_direction = rm.Room.get_player_move(rooms_array[-3].pathing)

    print(next_direction)
    print(rooms_array[-3].num)
    temp = rm.Room.next_room(next_direction, rooms_array[-3].num)
    print(temp)
    # 'Random' Encounters

    # Boss Encounter

    # Exit Encounter

main()
#######################################################################################################################################
