#######################################################################################################################################
# Title: Library
# Author: Tony Pescatore
# Description: Holds functions to be used in other classes or to used from many other classes
#######################################################################################################################################

# imports
import sys
import Items as it
import Rooms as rm
import random as rand

# seed
rand.seed(420)        # Hahaha funni number, for testing

# item pickup starts
# Allows player to pickup up new weapons
# Parameters:   inventory - list - current inventory of player
#               new_item - object - new item to be added
# Return:       inventory - List - updated inventory
def item_pickup(inventory, new_item):
    if inventory.len() == 5:        # if inventory is full
        print('Your inventory is full! Please remove an item to continue.')
        for i in range(6):          # for every element in inventory
            print(i + '. Remove ' + inventory[i])

        print('6. Remove ' + new_item.name)
        while True:
            selection = input('Please select the number of the option you would like to select: ')  # player selects an item to remove
            if selection == 1 or selection == 2 or selection == 3 or selection == 4 or selection == 5:
                print('You dropped ' + inventory[selection])
                inventory[selection] = new_item         # new item replaces older item
                break
            elif selection == 6:
                print('You dropped ' + new_item)
                break
            else:
                continue
    
    else:           # if inventory has open slots
        inventory.append(new_item)

    return inventory

# create all starts
# Game creates all aspects of the game; rooms, armors, weapons, shields, consumables, and enemies
# Parameters:   inventory - list - current inventory of player
#               new_item - object - new item to be added
# Return:       rm_list - List - List of all rooms selected in this playthrough
#               rm_dsc_lst - list - List of all possible room descriptions
#               w_list - List - list of all weapons
#               a_list - List - List of all armors
#               s_list - List - List of all shield
def create_all():

    # rooms
    rm_nums = list(rand.sample(range(50), 31))  # randomize rooms in layout
    rm_list = rm.Room.room_creation(rm_nums)
    rm_dsc_lst = rm.Room.room_desc_read()

    # weapons
    w_list = it.Weapons.create_weapons()

    # armors
    a_list = it.Armors.create_armors()

    # shields
    s_list = it.Shields.create_shields()

    # consumables
    c_list = it.Consumables.create_consumables()

    return rm_list, rm_dsc_lst, w_list, a_list, s_list, c_list