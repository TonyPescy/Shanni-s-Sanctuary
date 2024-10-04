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


# switch loadout starts
# Asks players if they wish to switch weapons, armor, or shields if they are able
# Parameters:   player - Character object - current player
# Return:       player - Character object - player with updated loadout
#               weapon_index - list - list of all weapon indexes, used for hot swapping weapons during combat
def switch_loadout(player):
    # lists of indexes for items
    weapon_index = []
    shield_index = []
    armor_index = []
    # gets counts of all item in loadout (armor, shield, and weapon) that player has at start of combat
    for i in range(0, len(player.inventory) - 1):
        if player.inventory[i].identifier == 1:
            weapon_count += 1
            weapon_index.append[i]
        elif player.inventory[i].identifier == 2:
            shield_count += 1
            shield_index.append[i]
        elif player.inventory[i].identifier == 3:
            armor_count += 1
            armor_index.append[i]
    
    # weapon swap
    if weapon_count > 0:    # fists are not considered part of the inventory, therefore items above 0 mean there are more weapon options
        # lists all options
        print('Currents weapons in inventory:')
        for i in range(1, weapon_count):
            print(f'{i}. {player.inventory[weapon_index[i - 1]].name}, Damage: {player.inventory[weapon_index[i - 1]].damage}, Durability: {player.inventory[weapon_index[i - 1]].durability} ')
        print(f'You currently have {player.weapon.name} equipped.')
        choice = input('Please enter the number of the weapon you would like to have equipped: ')
        player.weapon = player.inventory[weapon_index[choice - 1]]
    
    # shield swap
    if shield_count > 1:
        # lists all options
        print('Currents shields in inventory:')
        for i in range(1, shield_count):
            print(f'{i}. {player.inventory[shield_index[i - 1]].name}, Armor Remaining: {player.inventory[shield_index[i - 1]].defence} ')
        print(f'You currently have {player.shield.name} equipped.')
        choice = input('Please enter the number of the shield you would like to have equipped: ')
        player.shield = player.inventory[shield_index[choice - 1]]
    
    # armor swap
    if armor_count > 1:
        # lists all options
        print('Currents armors in inventory:')
        for i in range(1, armor_count):
            print(f'{i}. {player.inventory[armor_index[i - 1]].name}, Armor Remaining: {player.inventory[armor_index[i - 1]].defence} ')
        print(f'You currently have {player.armor.name} equipped.')
        choice = input('Please enter the number of the armor you would like to have equipped: ')
        player.armor = player.inventory[armor_index[choice - 1]]

    return player, weapon_index
# switch loadout ends

