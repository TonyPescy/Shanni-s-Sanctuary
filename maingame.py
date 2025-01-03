#######################################################################################################################################
# Title: Maingame
# Author: Tony Pescatore and Nick Pescatore
# Description: Basic text based adventure game with simple combat.  The goal is to make it to the end alive.
#######################################################################################################################################


#######################################################################################################################################
# Imports
import Encounter as en
import Rooms as rm
import Character as char
import random as rand
import library as lib
import combat as com
#######################################################################################################################################

#######################################################################################################################################
#Code

############################################################################################################
#FINAL

# GIVE BREIF DESCRIPTION OF BUFF AND DEBUFF RULES
# BUFFS OVERWRITE EACH OTHER, BUT CAN STACK ON EACH OTHER
# DEBUFFS CAN ONLY BE APPLIED 1 AT A TIME AND CANNOT OVERWRITE EACH OTHER

def main():
    # game item, room, and other generation
    rooms_array, rm_dsc_lst, weapon_list, armor_list, shield_list, consume_list = lib.create_all()
    
    '''
    # combat tester
    player_name, player_answer = en.user_name_and_ans()
    player = char.Character.create_player(player_name, weapon_list, armor_list)

    player.weapon = weapon_list[5]
    player.armor = armor_list[2]
    player.shield = shield_list[2]
    player.inventory.append(weapon_list[5])
    player.inventory.append(armor_list[2])
    player.inventory.append(shield_list[2])

    test_char = char.Character.create_mino(weapon_list)
    test_char_2 = char.Character.create_hellknight(weapon_list, armor_list, shield_list)
    enemy1 = char.Character.create_mummy(weapon_list)
    e_list = [enemy1, test_char, test_char_2]
    com.combat_loop(e_list, player)
    '''


    # Beginning of game scenarios
    en.intro()
    player_name, player_answer = en.user_name_and_ans()
    en.entrance(player_name, player_answer)

    # creates character object for player with default values for player character
    # used in combat and the sort
    player = char.Character.create_player(player_name, weapon_list, armor_list, shield_list)
    # print(player.name)

    # Entrance Encounter
    next_room = 0      # room starts at 0 because non-randomized descriptions are appened after the random ones
    rooms_array, next_room, player = en.room_encounters(next_room, rm_dsc_lst, -3, rooms_array, player, weapon_list, armor_list, shield_list, consume_list)  # always starts at zero, later we will use next_room for first parameter
    print(next_room)

    # All 'random' encounters and boss encounter
    while next_room < 32:
        rooms_array, next_room, player = en.room_encounters(next_room, rm_dsc_lst, rooms_array[next_room].e_num, rooms_array, player, weapon_list, armor_list, shield_list, consume_list)  # always starts at zero, later we will use next_room for first parameter
        print(next_room)

    # Exit Encounter
    rooms_array, next_room, player = en.room_encounters(next_room, rm_dsc_lst, -2, rooms_array, player, weapon_list, armor_list, shield_list, consume_list) # final room, exit room
    

main()
#######################################################################################################################################
