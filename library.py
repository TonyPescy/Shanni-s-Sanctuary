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

# identifiers
WEAPON_ID = 1
SHIELD_ID = 2
ARMOR_ID = 3
CONSUMABLE_ID = 4

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


# set loadout starts
# Asks players if they wish to switch weapons, armor, or shields if they are able
# Parameters:   player - Character object - current player
# Return:       player - Character object - player with updated loadout
#               weapon_index - list - list of all weapon indexes, used for hot swapping weapons during combat
#               cons_index - list - list of all item indexes, used for using items during combat
def set_loadout(player):
    # lists of indexes for items
    weapon_index = []
    shield_index = []
    armor_index = []
    cons_index = []
    # gets counts of all item in loadout (armor, shield, and weapon) that player has at start of combat
    for i in range(0, len(player.inventory) - 1):
        if player.inventory[i].identifier == WEAPON_ID:
            weapon_count += 1
            weapon_index.append[i]
        elif player.inventory[i].identifier == SHIELD_ID:
            shield_count += 1
            shield_index.append[i]
        elif player.inventory[i].identifier == ARMOR_ID:
            armor_count += 1
            armor_index.append[i]
        elif player.inventory[i].identifier == CONSUMABLE_ID:
            cons_index.append[i]
    
    # weapon swap
    if weapon_count > 0:    # fists are not considered part of the inventory, therefore items above 0 mean there are more weapon options
        # lists all options
        print('Current weapons in inventory:')
        for i in range(1, weapon_count + 1):
            print(f'{i}. {player.inventory[weapon_index[i - 1]].name}, Damage: {player.inventory[weapon_index[i - 1]].damage}, Durability: {player.inventory[weapon_index[i - 1]].durability} ')
        print(f'You currently have {player.weapon.name} equipped.')
        while True:
            choice = input('Please enter the number of the weapon you would like to have equipped: ')
            try:
                if choice > 0 and choice < weapon_count:  # choice entered was valid
                    break
            except: # choice was not entered correctly
                print('Please enter a number corresponding to an item above.')
                continue    # retries for choice 
        player.weapon = player.inventory[weapon_index[choice - 1]]
    
    # shield swap
    if shield_count > 1:
        # lists all options
        print('Current shields in inventory:')
        for i in range(1, shield_count + 1):
            print(f'{i}. {player.inventory[shield_index[i - 1]].name}, Armor Remaining: {player.inventory[shield_index[i - 1]].defence} ')
        print(f'You currently have {player.shield.name} equipped.')
        while True:
            choice = input('Please enter the number of the shield you would like to have equipped: ')
            try:
                if choice > 0 and choice <= shield_count:  # choice entered was valid
                    break
            except: # choice was not entered correctly
                print('Please enter a number corresponding to an item above.')
                continue    # retries for choice 
        player.shield = player.inventory[shield_index[choice - 1]]
    
    # armor swap
    if armor_count > 1:
        # lists all options
        print('Current armors in inventory:')
        for i in range(1, armor_count + 1):
            print(f'{i}. {player.inventory[armor_index[i - 1]].name}, Armor Remaining: {player.inventory[armor_index[i - 1]].defence} ')
        print(f'You currently have {player.armor.name} equipped.')
        while True:
            choice = input('Please enter the number of the armor you would like to have equipped: ')
            try:
                if choice > 0 and choice <= armor_count:  # choice entered was valid
                    break
            except: # choice was not entered correctly
                print('Please enter a number corresponding to an item above.')
                continue    # retries for choice 
        player.armor = player.inventory[armor_index[choice - 1]]

    return player, weapon_index, cons_index
# set loadout ends

# use consumable start
# Prompts user to select consumable to use and applies the effect
# Parameters:   player - object - Player character
#               cons_index - list - list of all consumable indexes, used for using consumables during combat
#               enemy_list - list - list of all enemies in combat
# Return:       player - ohject - updated player character
def use_cons(player, cons_index):
    # asks player what item they would like to use, from their item list
    # lists all item options
    print('Current items in inventory:')
    for i in range(1, len(cons_index) + 1):
        print(f'{i}. {player.inventory[cons_index[i - 1]].name}')
    while True:
        choice = input('Please enter the number of the consumable you would like to use: ')
        try:
            if choice > 0 and choice <= len(cons_index):  # choice entered was valid
                break
        except: # choice was not entered correctly
            print('Please enter a number corresponding to an item above.')
            continue    # retries for choice 
    consumable_to_be_used = player.inventory[cons_index[choice - 1].name]
    player.inventory.pop(cons_index[choice - 1])        # removes consumable from inventory whenn used

    match consumable_to_be_used:   # matches consumable to be used with all consumables
        case 'Small Health Potion':     # heals player for a max of 30 hp
            player.hp += 30
            if player.hp > 200:     # checks if potion over heals player
                overheal = player.hp - 200
                player.hp = 200     # sets hp to max
                print(f'You recovered {30 - overheal} hp!')    # tells player how much they healed, with overheal calculated
            else:   # no overheal
                print('You recovered 30 hp!')    # tells player how much they healed
            return player

        case 'Medium Health Potion':    # heals player for a max of 60 hp
            player.hp += 60
            if player.hp > 200:     # checks if potion over heals player
                overheal = player.hp - 200
                player.hp = 200     # sets hp to max
                print(f'You recovered {60 - overheal} hp!')    # tells player how much they healed, with overheal calculated
            else:   # no overheal
                print('You recovered 60 hp!')    # tells player how much they healed
            return player

        case 'Large Health Potion':    # heals player for a max of 100 hp
            player.hp += 100
            if player.hp > 200:     # checks if potion over heals player
                overheal = player.hp - 200
                player.hp = 200     # sets hp to max
                print(f'You recovered {100 - overheal} hp!')    # tells player how much they healed, with overheal calculated
            else:   # no overheal
                print('You recovered 100 hp!')    # tells player how much they healed
            return player

        case 'Cleanse Potion':      # removes player debuff
            if player.debuff == 'NONE': # if player has no debuff to cure
                print('Nothing happened! (You had no ailments)')
            else:
                player.debuff = 'NONE'
                player.debuff_stack = 0
                print(f'You were cured of {player.debuff}!')
                return player
        
        case 'Bandages':        # Stops bleeding status' and heals for 15 hp
            if player.debuff == 'lacerated' or player.debuff == 'gored':    # bleeding status
                # removes debuff
                player.debuff = 'NONE'
                player.debuff_stack = 0
                print(f'You were cured of {player.debuff}!')
            player.hp += 15
            if player.hp > 200:     # checks if potion over heals player
                overheal = player.hp - 200
                player.hp = 200     # sets hp to max
                print(f'You recovered {15 - overheal} hp!')    # tells player how much they healed, with overheal calculated
            else:   # no overheal
                print('You recovered 15 hp!')    # tells player how much they healed
            return player

        case 'Potion of Strength':      # overwrites current buffs
            if player.buff != 'strengthened':
                player.buff = 'strengthened'
                player.buff_stack = 1   # starts player strengthened counter
                print(f'You became strengthened, you deal 5 additional damage!')
            else:
                player.buff_stack += 1  # adds stack which adds more damage for each strength potion
                print(f'Even more strength courses through your veins, you deal {5*player.buff_stack} additional damage!')
            return player
        
        case 'Potion of Hardness':
            if player.armor == 'NONE' and player.shield == 'NONE':      # player does not have anything to use it on
                print('You just wasted your potion of hardness! (There was nothing to use it on...)')
            elif player.armor != 'NONE' and player.shield == 'NONE':    # player only has armor
                player.armor.defence += 25
            elif player.armor == 'NONE' and player.shield != 'NONE':    # player only has a shield
                player.shield.defence += 25
            else:                                                       # player has both a shield and armor
                while True:
                    print('Here are the posssible targets for the Potion of Hardness:')
                    print(f'1. {player.armor.name}')
                    print(f'2. {player.shield.name}')
                    choice = input('What is the number of the item would you like to use your Potion of Hardness on?')
                    if choice > 2 or choice < 1:   # neither option was selected
                        print('Please enter 1 or 2.')
                        continue
                    else:
                        if choice == 1:     # if armor was selected
                            print(f'You chose to harden your {player.armor.name}!')
                            player.armor.defence += 25
                            break
                        else:   # if shield was selected
                            print(f'You chose to harden your {player.shield.name}!')
                            player.shield.defence += 25
                            break
            return player
                
        case 'Portable Ward':
            if player.warded == False:      # if player has no initial ward
                player.buff = 'warded'
                player.buff_stack = 2
                print("You have become warded!")
                return player
            else:                           #  if player has a ward already
                player.buff_stack += 2
                print("Your ward grows around you!")
                return player
# use consumable end


# status check start
# Applies and allows status effects to playout
# Parameters:   char - object - Character that status is on
# Return:       char - object - character after status has been applied
#               temp_dmg - int - damage that will be used for chars damage calculation
#               skip_turn - boolean - Determines if character misses thier turn or not
def status_check(char):
    # initializing varibles for use inside match case statement
    temp_dmg = 0
    turn_skip = False
    # status check
    if char.debuff != 'NONE':  # if char has dubuff apllied
        match char.debuff:

            case 'crushed':     # lowers chars attack
                temp_dmg -= char.debuff_stack # subtracts damage from char when crushed based in bumer of stacks
                char.debuff_stack -= 1
                if char.debuff_stack == 0:    # when debuff runs out
                    char.debuff = 'NONE'      # reset char debuff

            case 'slimed':      # chance to miss turn
                if char.debuff_stack == 5:  # max chance to miss turn, 50%
                    temp_int = rand.randrange(1, 10)
                    if temp_int <= 5:
                        turn_skip = True
                    else:
                        turn_skip = False
                    char.debuff_stack -= 1  # reduces slimed counter

                elif char.debuff_stack == 4:  # chance to miss turn 40%
                    temp_int = rand.randrange(1, 10)
                    if temp_int <= 4:
                        turn_skip = True
                    else:
                        turn_skip = False
                    char.debuff_stack -= 1  # reduces slimed counter

                elif char.debuff_stack == 3:  # chance to miss turn 30%
                    temp_int = rand.randrange(1, 10)
                    if temp_int <= 3:
                        turn_skip = True
                    else:
                        turn_skip = False
                    char.debuff_stack -= 1  # reduces slimed counter

                elif char.debuff_stack == 2:  # chance to miss turn 20%
                    temp_int = rand.randrange(1, 10)
                    if temp_int <= 2:
                        turn_skip = True
                    else:
                        turn_skip = False
                    char.debuff_stack -= 1  # reduces slimed counter

                elif char.debuff_stack == 1:  # chance to miss turn 10%
                    temp_int = rand.randrange(1, 10)
                    if temp_int <= 1:
                        turn_skip = True
                    else:
                        turn_skip = False
                    char.debuff_stack -= 1  # reduces slimed counter
                    char.debuff = 'NONE'    # final turn of slimed, so it is removed
                
            case 'lacerated' | 'poisoned':  # lose 5 hp, ignores armor
                char.hp -= 5
                char.debuff_stack -= 1
                if char.debuff_stack == 0:  # debuff has run out
                    char.debuff = 'NONE'

            case 'acidic' | 'burned':  # lose 10 hp, ignores armor
                char.hp -= 10
                char.debuff_stack -= 1
                if char.debuff_stack == 0:  # debuff has run out
                    char.debuff = 'NONE'
            
            case 'gored':  # lose 15 hp, ignores armor
                char.hp -= 15
                char.debuff_stack -= 1
                if char.debuff_stack == 0:  # debuff has run out
                    char.debuff = 'NONE'

    if char.buff != 'NONE':
        match char.buff:

            case 'strengthened':    # buffs char damage based on stack
                temp_dmg += (5*char.buff_stack)

            case 'warded':          # prevents damage to char
                if char.buff_stack == 0:    # ward ended last turn
                    char.buff = 'NONE'
                    char.warded = False
                else:
                    char.warded = True
                    char.buff_stack -= 1
    
    return char, temp_dmg, turn_skip
# status check end            


# combat start
# Basic loop that combat will follow
# Parameters:   enemy_list - List of objects - List of all enemies in combat
#               player - object - Player character
# Return:       
#               
def combat(enemy_list, player):
    num_of_enemies = len(enemy_list)
    # loadout swap
    # weapons can be switched later, armor and shields can only be done here
    player, weapon_index, cons_index = set_loadout(player)   # gets a list of the weapon and item indexes in player inventory for swapping weaopons and using items in combat
    
    # initializing varibles for use inside while loop
    temp_dmg = 0
    turn_skip = False


    match num_of_enemies:
        # combat with one enemy
        case 1:
            while enemy_list[0].hp > 0 or player.hp > 0:
                player, temp_dmg, turn_skip = status_check(player)  # checks player status' and applies buffs/debuffs
                # player turn
                if turn_skip != True:   # if player turn is not skipped, player turn is allowed to continue
                    if len(cons_index) > 0:         # if player has items

                        while True:         # repeats until valid choice is made
                            player_action = input('Would you like to attack or use a consumable? (Enter \'attack\' or \'consumable\'): ').lower()
                            try:
                                if player_action == 'consumable' or player_action == 'attack':  # choice entered was valid
                                    break
                            except: # choice was not entered correctly
                                print('Please enter \'attack\' or \'consumable\'.')
                                continue    # retries for player_action 

                        if player_action == 'consumable' and turn_skip != True:
                            # item gets used
                            # enemy turn
                            # continue to restart combat loop
                            print('ooo')
                        elif player_action == 'attack' and turn_skip != True:
                            #nothing happens?
                            print('zzzz')

                    else:       # player does not have any items to use
                        # what weapon do u want to use?
                        # deal damage
                        # enemy turn
                        # continue to repeat combat loop


                # enemy turn
                