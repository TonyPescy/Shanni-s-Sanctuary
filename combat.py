#######################################################################################################################################
# Title: Combat
# Author: Tony Pescatore
# Description: Holds functions used for combat
#######################################################################################################################################

# imports
import library as lib
import random as rand

# set loadout starts
# Asks players if they wish to switch weapons, armor, or shields if they are able
# Parameters:   player - Character object - current player
# Return:       player - Character object - player with updated loadout
#               weapon_index - list - list of all weapon indexes, used for hot swapping weapons during combat
#               cons_index - list - list of all item indexes, used for using items during combat
def set_loadout(player):
    # lists of indexes and counts for items
    weapon_index, weapon_count, shield_index, shield_count, armor_index, armor_count, cons_index = lib.loadout_count(player)
    
    # weapon swap
    if weapon_count > 1:    # fists are not considered part of the inventory, therefore items above 0 mean there are more weapon options
        # lists all options
        print('Current weapons in inventory:')
        for i in range(1, weapon_count + 1):
            print(f'{i}. {player.inventory[weapon_index[i - 1]].name}, Damage: {player.inventory[weapon_index[i - 1]].damage}, Durability: {player.inventory[weapon_index[i - 1]].durability} ')
        print(f'You currently have {player.weapon.name} equipped.')
        if weapon_count > 1:
            while True:
                choice = input('Please enter the number of the weapon you would like to have equipped: ')
                try:
                    choice = int(choice)
                    if choice > 0 and choice <= weapon_count:  # choice entered was valid
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
                choice = int(choice)
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
                choice = int(choice)
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
#               cons_index - updated cons list
def use_cons(player, cons_index):
    # asks player what item they would like to use, from their item list
    # lists all item options
    print('Current items in inventory:')
    for i in range(1, len(cons_index) + 1):
        print(f'{i}. {player.inventory[cons_index[i - 1]].name}')
    while True:
        choice = input('Please enter the number of the consumable you would like to use: ')
        try:
            choice = int(choice)
            if choice > 0 and choice <= len(cons_index):  # choice entered was valid
                break
        except: # choice was not entered correctly
            print('Please enter a number corresponding to an item above.')
            continue    # retries for choice 

    consumable_to_be_used = player.inventory[cons_index[choice - 1].name]
    player.inventory.pop(cons_index[choice - 1])    # removes consumable from inventory when used
    cons_index.pop(choice - 1)                      # removes item from list of consumables indexes

    match consumable_to_be_used:   # matches consumable to be used with all consumables
        case 'Small Health Potion':     # heals player for a max of 30 hp
            player.hp += 30
            if player.hp > 200:     # checks if potion over heals player
                overheal = player.hp - 200
                player.hp = 200     # sets hp to max
                print(f'You recovered {30 - overheal} hp!')    # tells player how much they healed, with overheal calculated
            else:   # no overheal
                print('You recovered 30 hp!')    # tells player how much they healed
            return player, cons_index

        case 'Medium Health Potion':    # heals player for a max of 60 hp
            player.hp += 60
            if player.hp > 200:     # checks if potion over heals player
                overheal = player.hp - 200
                player.hp = 200     # sets hp to max
                print(f'You recovered {60 - overheal} hp!')    # tells player how much they healed, with overheal calculated
            else:   # no overheal
                print('You recovered 60 hp!')    # tells player how much they healed
            return player, cons_index

        case 'Large Health Potion':    # heals player for a max of 100 hp
            player.hp += 100
            if player.hp > 200:     # checks if potion over heals player
                overheal = player.hp - 200
                player.hp = 200     # sets hp to max
                print(f'You recovered {100 - overheal} hp!')    # tells player how much they healed, with overheal calculated
            else:   # no overheal
                print('You recovered 100 hp!')    # tells player how much they healed
            return player, cons_index

        case 'Cleanse Potion':      # removes player debuff
            if player.debuff == 'NONE': # if player has no debuff to cure
                print('Nothing happened! (You had no ailments)')
            else:
                player.debuff = 'NONE'
                player.debuff_stack = 0
                print(f'You were cured of {player.debuff}!')
                return player, cons_index
        
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
            return player, cons_index

        case 'Potion of Strength':      # overwrites current buffs
            if player.buff != 'strengthened':
                player.buff = 'strengthened'
                player.buff_stack = 1   # starts player strengthened counter
                print(f'You became strengthened, you deal 5 additional damage!')
            else:
                player.buff_stack += 1  # adds stack which adds more damage for each strength potion
                print(f'Even more strength courses through your veins, you deal {5*player.buff_stack} additional damage!')
            return player, cons_index
        
        case 'Potion of Hardness':
            if player.armor == 'NONE' and player.shield == 'NONE':      # player does not have anything to use it on
                print('There was nothing to use it on... You just wasted your potion of hardness!')
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
            return player, cons_index
                
        case 'Portable Ward':
            if player.warded == False:      # if player has no initial ward
                player.buff = 'warded'
                player.buff_stack = 2
                print("You have become warded!")
                return player, cons_index
            else:                           #  if player has a ward already
                player.buff_stack += 2
                print("Your ward grows stronger around you!")
                return player, cons_index
# use consumable end


# status check start
# Applies and allows status effects to playout
# Parameters:   char - object - Character that status is on
# Return:       char - object - character after status has been applied
#               skip_turn - boolean - Determines if character misses thier turn or not
def status_check(char):
    # initializing varibles for use inside match case statement
    turn_skip = False
    # status check
    if char.debuff != 'NONE':  # if char has dubuff apllied
        match char.debuff:

            case 'crushed':     # lowers chars attack
                # temp_dmg -= char.debuff_stack # subtracts damage from char when crushed based in bumer of stacks REMOVED AND ADDED TO DAMAGE CALC STEP
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
                print(f'{char.name} lost 5 health points due to its \'{char.debuff}\' affliction!')
                print(f'{char.name} has {char.hp} health points remaining!')
                char.debuff_stack -= 1
                if char.debuff_stack == 0:  # debuff has run out
                    char.debuff = 'NONE'
                    print(f'{char.name} has lost its affliction!')
                else:                       # prints how much is left of the debuff
                    print(f'{char.name} has {char.debuff_stack} turns left on its affliction!')

            case 'acidic' | 'burned':  # lose 10 hp, ignores armor
                char.hp -= 10
                print(f'{char.name} lost 10 health points due to its \'{char.debuff}\' affliction!')
                print(f'{char.name} has {char.hp} health points remaining!')
                char.debuff_stack -= 1
                if char.debuff_stack == 0:  # debuff has run out
                    char.debuff = 'NONE'
                    print(f'{char.name} has lost its affliction!')
                else:                       # prints how much is left of the debuff
                    print(f'{char.name} has {char.debuff_stack} turns left on its affliction!')

            case 'gored':  # lose 15 hp, ignores armor
                char.hp -= 15
                print(f'{char.name} lost 15 health points due to its \'{char.debuff}\' affliction!')
                print(f'{char.name} has {char.hp} health points remaining!')
                char.debuff_stack -= 1
                if char.debuff_stack == 0:  # debuff has run out
                    char.debuff = 'NONE'
                    print(f'{char.name} has lost its affliction!')
                else:                       # prints how much is left of the debuff
                    print(f'{char.name} has {char.debuff_stack} turns left on its affliction!')

    if char.buff != 'NONE':
        match char.buff:

            # TEMP_DMG CALCULATED AT DMG CALC SO NO NEED FOR THIS AS IT ONLY DOES TEMP_DMG
            # case 'strengthened':    # buffs char damage based on stack
                # temp_dmg += (5*char.buff_stack)

            case 'warded':          # prevents damage to char
                if char.buff_stack == 0:    # ward ended last turn
                    char.buff = 'NONE'
                    char.warded = False
                else:
                    char.warded = True
                    char.buff_stack -= 1
    
    return char, turn_skip
# status check end            

# weapon switch start
# Allows player to switch weapons during combat if they wish
# Parameters:   player - object - players character
#               wep_index - list - list of location of all weapons in inventory
# Return:       player - object - player after weapon was swapped
def weapon_switch(player, wep_index):
    print('Current weapons in inventory:')
    for i in range(1, len(wep_index) + 1):
        print(f'{i}. {player.inventory[wep_index[i - 1]].name} - DMG: {player.inventory[wep_index[i - 1]].damage} - DUR: {player.inventory[wep_index[i - 1]].durability} - INF: {player.inventory[wep_index[i - 1]].infusion}')
    while True:
        choice = input('Please enter the number of the weapon you would like to use: ')
        try:
            choice = int(choice)
            if choice > 0 and choice <= len(wep_index):  # choice entered was valid
                break
        except: # choice was not entered correctly
            print('Please enter a number corresponding to a weapon above.')
            continue    # retries for choice 
    player.weapon = player.inventory[wep_index[choice - 1]]     # assigns weapon to player weapon slot

    return player
# weapon switch end


# deal damage start
# Performs damage calculations and applies them to characters
# Parameters:   attacker - object - attacker character
#               target - object - target of the attack
# Return:       attacker - object - attacker after the attack
#               target - object - target after the attack
def deal_damage(attacker, target):

    # checks if target is warded, which would render this process useless
    if target.warded == True:
        print(f'{target.name} is warded! The attacks bounce off!')
        return attacker, target     # ends function as target would not take damage

    # damage calculation
    temp_dmg = attacker.weapon.damage
    if attacker.weapon.infusion == 'magic':
        temp_dmg += 5
    elif attacker.weapon.infusion == 'magic +1':
        temp_dmg += 15
    if attacker.buff == 'strengthened':
        temp_dmg += (attacker.buff_stack*5)
    if attacker.debuff == 'crushed':
        temp_dmg -= (attacker.debuff_stack*5)
    if temp_dmg < 5:
        temp_dmg = 5    # 5 in minimum amount of damage dealt
    
    # debuff application
    # checks if target can receive a debuff
    if target.debuff == 'NONE':
        # checks if attacker has infusion that causes status affect
        if attacker.weapon.infusion != 'None' or attacker.weapon.infusion != 'magic +1' or attacker.weapon.infusion != 'magic': 
            # apply status effects based on infusion
            match attacker.weapon.infusion:
                case 'crusher':
                    target.debuff = 'crushed'
                    target.debuff_stack = 4    # Starts at 4, instead of the max of 3, because it will lose a stack before its calculations can be used. This ensures it will function according to the max of 3
                case 'slime':
                    target.debuff = 'slimed'
                    target.debuff_stack = 5
                case 'serrated':
                    target.debuff = 'lacerated'
                    target.debuff_stack = 10
                case 'gore':
                    target.debuff = 'gored'
                    target.debuff_stack = 7
                case 'acid':
                    target.debuff = 'acidic'
                    target.debuff_stack = 8
                case 'venom':
                    target.debuff = 'poisoned'
                    target.debuff_stack = 8
                case 'fiery':
                    target.debuff = 'burned'
                    target.debuff_stack = 10
        
    # damage application
    # damage is applied as follows: shield --> armor --> health points
    # damage over flows from shield to armor to health
    while temp_dmg > 0:     # stops the damage application loop once damage runs out
        if target.shield != 'NONE':     # checks to see if target has a shield, only runs if they have one
            target.shield.defence -= temp_dmg
            if target.shield.defence < 0:     # overflow damage, shield destroyed
                temp_dmg = abs(target.shield.defence)
                print(f'{target.name}\'s shield has been destroyed by the attack! (overflow)')
                lib.item_removal(target, target.shield)     # removes destroyed shield
            elif target.shield.defence == 0:  # no overflow but shield destroyed
                temp_dmg = 0
                print(f'{target.name}\'s shield has been destroyed by the attack!')
                lib.item_removal(target, target.shield)     # removes destroyed shield
                return attacker, target
            else:   # shield is not destroyed after attack, no overflow
                print(f'{attacker.name} dealt {temp_dmg} damage to {target.name}\'s shield!')
                temp_dmg = 0
                return attacker, target
            
        if target.armor != 'NONE':  # checks to see if target has any armor, only runs if they have some
            target.armor.defence -= temp_dmg
            if target.armor.defence < 0:     # overflow damage, armor destroyed
                temp_dmg = abs(target.armor.defence)
                print(f'{target.name}\'s armor has broken from the attack! OVERFLOW')
                lib.item_removal(target, target.armor)     # removes destroyed armor
            elif target.armor.defence == 0:  # no overflow but armor destroyed
                temp_dmg = 0
                print(f'{target.name}\'s armor has broken from the attack!')
                lib.item_removal(target, target.armor)     # removes destroyed armor
                return attacker, target
            else:   # armor is not destroyed after attack, no overflow
                print(f'{attacker.name} dealt {temp_dmg} damage to {target.name}\'s armor!')
                temp_dmg = 0
                return attacker, target
            
        # damage below is dealt directly to health points of target
        # only able to proceed if target has no armor or shield remaining or they were destroyed
        target.hp -= temp_dmg
        if target.hp <= 0:     # target has died
            print(f'{target.name} has died from their injuries!')
            temp_dmg = 0        # reset damage
            return attacker, target
        
        else:               # targets is still alive
            print(f'{attacker.name} dealt {temp_dmg} damage to {target.name}!')
            # POSSIBLY MAKE CHECKS ON TARGET.HP AND CHANGE THE PRINT ACCORIDNG TO HOW MUCH HP THEY HAVE LEFT?
            print(f'{target.name} still has {target.hp} health points remaining!')      # TEMP UNTIL ABOVE IS DONE
            temp_dmg = 0        # reset damage
            return attacker, target


# player_wep_use start
# Everytime a player uses a weapon this will change its durability accordingly
# Parameters:   user - character object - the user of the weapon
# Return:       
# 




# combat_loop start
# Basic loop that combat will follow
# Parameters:   enemy_list - List of objects - List of all enemies in combat
#               player - object - Player character
# Return:       
#               
# NOTES: Combat can be trimmed and optimized alot with match cases annd better ordering of operations. This is especially true for when there are 
# multiple enemies in the combat. 
# PLAN: Reduce repeat code as much as possible - Break it down into more functions, better system for swapping and targetting together.
def combat_loop(enemy_list, player):
    num_of_enemies = len(enemy_list)
    # loadout swap
    # weapons can be switched later, armor and shields can only be done here
    player, weapon_index, cons_index = set_loadout(player)   # gets a list of the weapon and item indexes in player inventory for swapping weaopons and using items in combat
    
    # initializing varibles for use inside while loop
    turn_skip = False

    match num_of_enemies:
        # combat with one enemy
        case 1:
            enemy = enemy_list[0]
            while enemy.hp > 0 and player.hp > 0:
                player, turn_skip = status_check(player)  # checks player status' and applies buffs/debuffs
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
                            player, cons_index = use_cons(player)
                        elif player_action == 'attack' and turn_skip != True:
                            player, enemy = deal_damage(player, enemy)

                    else:       # player does not have any items to use
                        # player attack
                        if len(weapon_index) > 1:   # more than 1 weapon in player inventory
                            print(f'Your current weapon is: {player.weapon.name} - DMG: {player.weapon.damage} - DUR: {player.weapon.durability} - INF: {player.weapon.infusion}')
                            while True: 
                                swap = input('Do you want to swap weapon? (Enter yes or no): ').lower()
                                try:
                                    if swap == 'yes' or swap == 'no':  # swap input entered was valid
                                        break
                                except: # swap input was not entered correctly
                                    print('Please enter yes or no.')
                                    continue    # retries for swap input 
                            if swap == 'no':    # weapon not swapped
                                player, enemy = deal_damage(player, enemy)
                            else:               # weapon is to be swapped
                                player = weapon_switch(player, weapon_index)
                                player, enemy = deal_damage(player, enemy)

                        else:                       # player only has 1 weapon to use /  no swap available 
                            player, enemy = deal_damage(player, enemy)

                # enemy turn will always run after all player actions have been completed, or if player turn has been skipped
                # since enemy goes after player, we must add a check to ensure enemy has not died before they attack
                if enemy.hp <= 0:
                    break
                else:
                    # enemy turn
                    enemy, player = deal_damage(enemy, player)
                    # restart combat loop
                    continue

        # combat with two enemies
        case 2:
            enemy1 = enemy_list[0]
            enemy2 = enemy_list[1]
            enemy_total_hp = enemy1.hp + enemy2.hp
            while enemy_total_hp > 0 and player.hp > 0: # ensures the player or at least 1 enemy is still alive

                player, turn_skip = status_check(player)  # checks player status' and applies buffs/debuffs
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
                            player, cons_index = use_cons(player)
                        elif player_action == 'attack' and turn_skip != True:
                            player, enemy = deal_damage(player, enemy)

                    else:       # player does not have any items to use
                        # player attack
                        if len(weapon_index) > 1:   # more than 1 weapon in player inventory
                            print(f'Your current weapon is: {player.weapon.name} - DMG: {player.weapon.damage} - DUR: {player.weapon.durability} - INF: {player.weapon.infusion}')
                            while True: 
                                swap = input('Do you want to swap weapon? (Enter yes or no): ').lower()
                                try:
                                    if swap == 'yes' or swap == 'no':  # swap input entered was valid
                                        break
                                except: # swap input was not entered correctly
                                    print('Please enter yes or no.')
                                    continue    # retries for swap input

                            if enemy1.hp > 0 and enemy2.hp > 0:     # asks for player to target an enemy if there are more than 1 alive
                                while True:     # player chooses which enemy to attack this round
                                    print(f'1. {enemy1.name} - HP: {enemy1.hp}')
                                    print(f'2. {enemy2.name} - HP: {enemy2.hp}')
        
                                    target = input('Please enter the enemy you would like to target (Enter 1 or 2): ').lower()
                                    try:
                                        if target == '1' or swap == '2':  # target input entered was valid

                                            break
                                    except: # target input was not entered correctly
                                        print('Please enter 1 or 2.')
                                        continue    # retries for target input 
                            else:   # determines what enemy player will target when the other enemy has died
                                match enemy1.hp > 0:
                                    case True:      # enemy1 is the last alive enemy
                                        target = '1'
                                    case False:     # enemy2 is the last alive enemy
                                        target = '2'

                            if swap == 'no':        # weapon not swapped
                                match target:
                                    case '1':       # enemy1 was chosen as target
                                        player, enemy1 = deal_damage(player, enemy1)    # player attacks enemy1
                                    case '2':       # enemy2 chosen as target
                                        player, enemy2 = deal_damage(player, enemy2)    # player attacks enemy2
                            else:                   # weapon is to be swapped
                                player = weapon_switch(player, weapon_index)
                                match target:
                                    case '1':       # enemy1 was chosen as target
                                        player, enemy1 = deal_damage(player, enemy1)    # player attacks enemy1
                                    case '2':       # enemy2 chosen as target
                                        player, enemy2 = deal_damage(player, enemy2)    # player attacks enemy2

                        # no weapon swap
                        else:       # player only has 1 weapon to use /  no swap available
                            if enemy1.hp > 0 and enemy2.hp > 0:     # asks for player to target an enemy if there are more than 1 alive
                                while True:     # player chooses which enemy to attack this round
                                    print(f'1. {enemy1.name} - HP: {enemy1.hp}')
                                    print(f'2. {enemy2.name} - HP: {enemy2.hp}')
        
                                    target = input('Please enter the enemy you would like to target (Enter 1 or 2): ').lower()
                                    try:
                                        if target == '1' or swap == '2':  # target input entered was valid

                                            break
                                    except: # target input was not entered correctly
                                        print('Please enter 1 or 2.')
                                        continue    # retries for target input 
                            else:   # determines what enemy player will target when the other enemy has died
                                match enemy1.hp > 0:
                                    case True:      # enemy1 is the last alive enemy
                                        target = '1'
                                    case False:     # enemy2 is the last alive enemy
                                        target = '2'
                            match target:
                                    case '1':       # enemy1 was chosen as target
                                        player, enemy1 = deal_damage(player, enemy1)    # player attacks enemy1
                                    case '2':       # enemy2 chosen as target
                                        player, enemy2 = deal_damage(player, enemy2)    # player attacks enemy2
                        
                        # Enemy(s) turn
                        if enemy1.hp > 0 and enemy2.hp > 0: # only occurs if both enemies are alive
                            enemy1, player = deal_damage(enemy1, player)    # enemy1 attacks player
                            enemy2, player = deal_damage(enemy2, player)    # enemy2 attacks player
                        else:   # one of the enemies have died
                            match enemy1.hp > 0:
                                case True:  # enemy1 is the only enemy alive
                                    enemy1, player = deal_damage(enemy1, player)    # enemy1 attacks player
                                case False: # enemy2 is the only enemy alive
                                    enemy2, player = deal_damage(enemy2, player)    # enemy2 attacks player

        case 3:
            print('needs implementation')






    # Universal print statments, only reached when all enemies have been killed or player has been killed
    if enemy.hp > 0:
        print('Enemy survived the encounter with ' + str(enemy.hp) + ' health points left!')
        print('You Died!')
    elif player.hp > 0:
        print(player.name + ' survived the encounter with ' + str(player.hp) + ' health points left!')