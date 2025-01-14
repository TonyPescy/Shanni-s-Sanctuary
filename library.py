#######################################################################################################################################
# Title: Library
# Author: Tony Pescatore
# Description: Holds functions to be used in other classes or to used from many other classes
#######################################################################################################################################

# imports
import Items as it
import Rooms as rm
import random as rand

# identifiers
WEAPON_ID = 1
SHIELD_ID = 2
ARMOR_ID = 3
CONSUMABLE_ID = 4

# OTHER CONSTANTS
INV_LEN = 5     # length of inventory

# seed
# rand.seed(420)        # Hahaha funni number, for testing

# get_inventory_len starts
# Gets number of non-null values that are in the inventory
# Parameters:   inventory - list - list of character items
# Return:       inventory_length - int - number of non-null values in the inventory


# weapon counter starts
# Counts all weapons in inventory and assigns a list to where they are located in the inventory
# Parameters:   player - object - player character
# Return:       weapon_index - lists - contains location of weapons in list
#               weapon_count - ints - number of weapons in inventory
def weapon_counter(player):
    # init
    weapon_count = 0
    # lists of indexes for items
    weapon_index = []
    # gets counts of weapons in inventory
    for i in range(0, INV_LEN):
        if player.inventory[i] == 'null':   # null value, no item at this index in inventory
            pass
        elif player.inventory[i].identifier == WEAPON_ID:
            weapon_count += 1
            weapon_index.append(i)
    return weapon_count, weapon_index
# weapon counter ends

# shield counter starts
# Counts all shield in inventory and assigns a list to where they are located in the inventory
# Parameters:   player - object - player character
# Return:       shield_index - lists - contains location of shields in list
#               shield_count - ints - number of shields in inventory
def shield_counter(player):
    # init
    shield_count = 0
    # lists of indexes for items
    shield_index = []
    # gets counts of all shields in inventory
    for i in range(0, INV_LEN):
        if player.inventory[i] == 'null':   # null value, no item at this index in inventory
            pass
        elif player.inventory[i].identifier == SHIELD_ID:
            shield_count += 1
            shield_index.append(i)
    return shield_count, shield_index
# shield counter ends

# weapon counter starts
# Counts all weapons in inventory and assigns a list to where they are located in the inventory
# Parameters:   player - object - player character
# Return:       armor_index - lists - contains location of armors in list
#               armor_count - ints - number of armors in inventory
def armor_counter(player):
    # init
    armor_count = 0
    # lists of indexes for items
    armor_index = []
    # gets counts of armor in inventory
    for i in range(0, INV_LEN):
        if player.inventory[i] == 'null':   # null value, no item at this index in inventory
            pass
        elif player.inventory[i].identifier == ARMOR_ID:
            armor_count += 1
            armor_index.append(i)
    return armor_count, armor_index
# weapon counter ends

# shield counter starts
# Counts all shield in inventory and assigns a list to where they are located in the inventory
# Parameters:   player - object - player character
# Return:       consumable_index - lists - contains location of consumables in list
def consumable_indexer(player):
    # lists of indexes for items
    consumable_index = []
    # gets indexes of consumables in inventory
    for i in range(0, INV_LEN):
        if player.inventory[i] == 'null':   # null value, no item at this index in inventory
            pass
        elif player.inventory[i].identifier == CONSUMABLE_ID:
            consumable_index.append(i)
    return consumable_index
# consumable indexer ends

# loadout count starts
# performs counts for all types of items
# Parameters:   player - object - player character
# Return:       x_index - lists - contains location of x (weapons, shield, armor, and consumables) in list
#               x_count - ints - number of x (weapons, shields, and armors) in inventory
def loadout_count(player):
    # initialization of item counts
    weapon_count = 0
    shield_count = 0
    armor_count = 0

    # lists of indexes for items
    weapon_index = []
    shield_index = []
    armor_index = []
    consumable_index = []
    # gets counts of all item in loadout (armor, shield, and weapon) that player has at start of combat
    for i in range(0, INV_LEN):                   # 5 is max size of inventory
        if player.inventory[i] == 'null':   # null value, no item at this index in inventory
            pass
        elif player.inventory[i].identifier == WEAPON_ID:
            weapon_count += 1
            weapon_index.append(i)
        elif player.inventory[i].identifier == SHIELD_ID:
            shield_count += 1
            shield_index.append(i)
        elif player.inventory[i].identifier == ARMOR_ID:
            armor_count += 1
            armor_index.append(i)
        elif player.inventory[i].identifier == CONSUMABLE_ID:
            consumable_index.append(i)
    return weapon_index, weapon_count, shield_index, shield_count, armor_index, armor_count, consumable_index
# loadout count ends

# item pickup starts
# Allows player to pickup up new weapons
# Parameters:   inventory - list - current inventory of player
#               new_item - object - new item to be added
# Return:       inventory - List - updated inventory
def item_pickup(inventory, new_item):
    # searching for empty item space
    for i in range(0, INV_LEN):      # iterates over every item in player inventory
        if inventory[i] == 'null':      # if there is an empty space in player inventory
            # replace empty space with new item
            inventory[i] = new_item
            return inventory    # returns inventory with newly picked up item
    # if this code is reached, that means that the inventory is completely filled with items so player must remove an item to make room for a new one
    for i in range(1, INV_LEN + 1):     # iterates over every item at +1 to list out all items for player to remove an item
        print(f'{i}. {inventory[i-1].name}')                    # prints all items in inventory
    print(f'6. {new_item.name} (Do not pick up this item). ')   # prints new item to be added
    while True:
        selection = input('Please select the number of the option you would like to select: ')  # player selects an item to remove
        selection = int(selection)      # casts selection to be an int for comparison
        if selection == 1 or selection == 2 or selection == 3 or selection == 4 or selection == 5:  # player removes an old item
            print(f'You dropped {inventory[selection].name}!')
            inventory[selection] = new_item         # new item replaces older item
            break
        elif selection == 6:
            print(f'You did not pick up {new_item.name}!')
            break
        else:
            continue    # continues selection loop if player makes invalid selection
    return inventory
# item pickup ends

# create all starts
# Game creates all aspects of the game; rooms, armors, weapons, shields, consumables, and enemies
# Parameters:   inventory - list - current inventory of player
#               new_item - object - new item to be added
# Return:       rm_list - List - List of all rooms selected in this playthrough
#               rm_dsc_lst - list - List of all possible room descriptions
#               w_list - List - list of all weapons
#               a_list - List - List of all armors
#               s_list - List - List of all shield
#               c_list - List - List of all consumables
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

    # enemy creation


    return rm_list, rm_dsc_lst, w_list, a_list, s_list, c_list
