#######################################################################################################################################
# Title: Encounter
# Author: Tony Pescatore and Nick Pescatore
# Description: All encounter descriptions and encounter interactions
#######################################################################################################################################

# imports
import sys
import Rooms as rm
import random as rand
import Character as char
import combat as com
import library as lib

# Constants
DESC_ENTRY = 0      # will be used to access the first element of the room description array, it contains the exit description
DESC_EXIT = 1       # will be used to access the second element of the room description array, it contains the exit description

class Encounter():

    # Initializes basic parts of an encounter
    def __init__(self, e_num, e_desc, r_num):
        self.e_num = e_num                      # Encounter number - Integer
        self.e_desc = e_desc                    # Encounter descrpition - String
        self.r_num = r_num                      # Number that encounter will be assigned to - Integer

# Special Encounters
# finEn
# bossEn

# Username Starts
# Gets the users name
# Parameters:   None
# Return:       Users name with first letter uppercase and all others lowercase
def user_name_and_ans(): # Gets players name
    name = str(input("The voice within asks:  'What is your name?' "))
    name = name[0].upper() + name[1:].lower()       # Makes name look nice
    while True:
        answer = str(input(name + ", do you wish to enter Shanni's Sanctuary?  Yes or no? "))
        answer = answer.lower()
        if (answer == 'yes' or answer == 'no'):
            break
        else:
            print('Please enter yes or no.')
            continue
    return name, answer
# Username Ends

# Entrance Starts
# Entrance encounter - For going into the sanctuary
# Parameters:   name = players name
# Return:       N/A
def entrance(name, answer):         # Entrance to the sanctuary, this decides if user wishes to play the game or not
    while True:
        if answer == "no":      # If user says no
            print("No?  Shanni is disappointed with your cowardice, but acknowledges your intellect.  She shall let you live and return to your life, as that is more hellish than what lies within.")
            print("You turn away slowly as the invisble weight appears to be lifted from your shoulders.  As you begin away from the sanctuary you take one last look at its devilish stone before it is blown into dust by the wind.")
            sys.exit(1)
        elif answer == "yes":   # If user says yes
            print("Yes?  Shanni is delighted with your stupidity, it's not everyday she gets a sacrifice so eager.  Please enter.")
            print("The weight one your shoulders grows heavier as you walk into the black abyss beyond the door.")
            print("Welcome to Shanni's Sanctuary " + name + ", good luck in there, you'll need it.")
            break
        else:                   # If no proper answer is given, program tries again *This is a double check should not ever occur*
            answer = input("Enter yes or no ")
# Entrance Ends

# Introduction Starts
# Introduction encounter - For finding the sanctuary
# Parameters:   None
# Return:       N/A
def intro():            # Intro to the game 
    temp = 0        # temp for while loop to ensure yes or no is provided
    print("You are walking down the side walk of the city you've spent your entire life in, during that time nothing much has changed.  It was always a small city, but now that you've grown up it seems to have gotten smaller and much duller.  You know every inch of this city like the back of your hand, you could walk the streets blindfolded and make it to work on time.  However today was odd, a peculiar weight was on you shoulders, maybe leaving home for the city was getting to you?  But that can't be making you feel this way can it?.")
    answer = str(input("That's when something catches your eye, something you never saw before.  A large overgrown pyramid in the center of the street, how have you never noticed this before?  A voice speaks to you, it comes from within your own mind, it's beckoning you forth.  Come closer it says, egging you on and on.  Do you listen to what the voice says?  Yes or no? ").lower())
    while True:
        if answer.lower() == "no":
            print("Your body does not listen to you, instead it does the opposite and begins towards the massive black pyramid.")
            break
        elif answer.lower() == "yes":
            print("Your begin towards the massive black pyramid, unaware of the implications it will have for your future... or if there will be one to come back to. ")
            break
        else:               # If no proper answer is given, program tries again
            answer = input("Enter yes or no. ")
            
# Introduction Ends

# random encounters start
# Cases for each room in game and what to do with dictionary lookup
# each function will return the new room number based on direction inputted

# rm_entrance Starts
# rm_entrance - First encounter within the actual pyramid
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_entrance(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list):
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    print(desc[encounter_num_ind:])
    next_direction = rm.Room.get_player_move(rooms_arr[32].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[32].num)      # gets new room that player has selected
    print('As you you make your way north, those heavy wooden doors slam shut. Another barrier to ensure you do not escape Shanni\'s Sanctuary.')
    
    return rooms_arr, new_room, player
# room_entrance ends


# rm_1 Starts
# rm_1 - Room 1 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_1(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list):
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[0].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[0].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 1 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[0].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[0].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 1")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_1 ends

# rm_2 Starts
# rm_2 - Room 2 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_2(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[1].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[1].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 2 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[1].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[1].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 2")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_2 ends

# rm_3 Starts
# rm_3 - Room 3 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_3(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[2].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[2].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 3 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Northwest.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[2].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[2].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 3")              # all rooms will need a unique exit statement

    return rooms_arr, new_room, player
# rm_3 ends

# rm_4 Starts
# rm_4 - Room 4 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_4(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[3].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[3].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 4 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is West.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[3].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[3].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 4")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_4 ends

# rm_5 Starts
# rm_5 - Room 5 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_5(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[4].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[4].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 5 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is East.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[4].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[4].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 5")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_5 ends

# rm_6 Starts
# rm_6 - Room 6 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_6(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[5].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[5].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 6 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Northeast.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[5].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[5].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 6")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_6 ends

# rm_7 Starts
# rm_7 - Room 7 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_7(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[6].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[6].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 7 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Northwest.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[6].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[6].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 7")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_7 ends

# rm_8 Starts
# rm_8 - Room 8 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_8(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[7].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[7].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 8 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Northwest.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[7].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[7].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 8")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_8 ends

# rm_9 Starts
# rm_9 - Room 9 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_9(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[8].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[8].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 9 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Northeast.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[8].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[8].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 9")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_9 ends

# rm_10 Starts
# rm_10 - Room 10 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_10(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[9].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[9].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 10 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is East.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[9].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[9].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 10")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_10 ends

# rm_11 Starts
# rm_11 - Room 11 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_11(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[10].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[10].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 11 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[10].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[10].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 11")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_11 ends

# rm_12 Starts
# rm_12 - Room 12 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_12(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[11].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[11].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 12 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[11].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[11].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 12")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_12 ends

# rm_13 Starts
# rm_13 - Room 13 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_13(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[12].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[12].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 13 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Southwest.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[12].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[12].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 13")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_13 ends

# rm_14 Starts
# rm_14 - Room 14 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_14(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[13].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[13].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 14 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[13].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[13].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 14")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_14 ends

# rm_15 Starts
# rm_15 - Room 15 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_15(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[14].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[14].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 15 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Northwest.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[14].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[14].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 15")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_15 ends

# rm_16 Starts
# rm_16 - Room 16 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_16(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[15].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[15].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 16 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Northwest.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[15].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[15].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 16")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_16 ends

# rm_17 Starts
# rm_17 - Room 17 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_17(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[16].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[16].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 17 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Northwest.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[16].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[16].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 17")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_17 ends

# rm_18 Starts
# rm_18 - Room 18 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_18(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[17].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[17].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 18 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[17].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[17].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 18")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_18 ends

# rm_19 Starts
# rm_19 - Room 19 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_19(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[18].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[18].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 19 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is West.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[18].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[18].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 19")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_19 ends

# rm_20 Starts
# rm_20 - Room 20 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_20(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[19].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[19].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 20 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is Northeast.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[19].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[19].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 20")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_20 ends

# rm_21 Starts
# rm_21 - Room 21 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_21(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[20].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[20].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 21 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[20].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[20].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 21")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_21 ends

# rm_22 Starts
# rm_22 - Room 22 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_22(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[21].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[21].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 22 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[21].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[21].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 22")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_22 ends

# rm_23 Starts
# rm_23 - Room 23 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_23(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[22].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[22].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 23 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[22].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[22].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 23")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_23 ends

# rm_24 Starts
# rm_24 - Room 24 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_24(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[23].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[23].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 24 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is West.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[23].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[23].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 24")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_24 ends

# rm_25 Starts
# rm_25 - Room 25 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_25(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[24].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[24].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 25 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[24].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[24].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 25")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_25 ends

# rm_26 Starts
# rm_26 - Room 26 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_26(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[25].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[25].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 26 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[25].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[25].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 26")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_26 ends

# rm_27 Starts
# rm_27 - Room 27 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_27(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[26].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[26].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 27 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is West.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[26].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[26].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 27")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_27 ends

# rm_28 Starts
# rm_28 - Room 28 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_28(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[27].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[27].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 28 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is West.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[27].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[27].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 28")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_28 ends

# rm_29 Starts
# rm_29 - Room 29 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_29(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[28].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[28].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 29 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is West.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[28].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[28].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 29")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_29 ends

# rm_30 Starts
# rm_30 - Room 30 with random encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_30(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[29].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[29].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 30 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[29].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[29].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 30")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_30 ends

# rm_boss Starts
# rm_boss - Boss Room with boss encounter inside
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_boss(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    encounter_num = desc[:encounter_num_ind]  # selects number from room description
    print('ENCOUNTER SCENARIO NUMBER: ' + str(encounter_num))   # to be removed, helps keep track of unexpected errors
    if rooms_arr[31].re_entry != True:   # first time entering the room
        print(desc[encounter_num_ind+1:]) # prints random room description
        player = encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, consume_list)
        rooms_arr[31].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 31 (boss) has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    # select next room
    next_direction = rm.Room.get_player_move(rooms_arr[31].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[31].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF BOSS ROOM")              # all rooms will need a unique exit statement
    return rooms_arr, new_room, player
# rm_boss ends

# rm_exit Starts
# rm_exit - Exit room with exit story
# Parameters:   
#               desc - string - description for this room
#               rooms_arr - array - Array of all room objects
#               player - character object - player character
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#           new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def rm_exit(desc, rooms_arr, player, weapon_list, armor_list, shield_list, consume_list): 
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    print(desc[encounter_num_ind+1:])
    new_room = 'temp'   # place holder given for proper return statement
    return rooms_arr, new_room, player

encounter_dict = {
    0: rm_entrance,
    1: rm_1,
    2: rm_2,
    3: rm_3,
    4: rm_4,
    5: rm_5,
    6: rm_6,
    7: rm_7,
    8: rm_8,
    9: rm_9,
    10: rm_10, 
    11: rm_11,
    12: rm_12,
    13: rm_13,
    14: rm_14,
    15: rm_15,
    16: rm_16,
    17: rm_17,
    18: rm_18,
    19: rm_19,
    20: rm_20, 
    21: rm_21,
    22: rm_22,
    23: rm_23,
    24: rm_24,
    25: rm_25,
    26: rm_26,
    27: rm_27,
    28: rm_28,
    29: rm_29,
    30: rm_30, 
    31: rm_boss,
    32: rm_exit
}

# room_encounters to lookup and execute the function based on players room
# room_encounters - selects room encounter to play out according to the player current room
# Parameters:   
#               c_room - int - Current room the player is in
#               desc_arr - array - Array of all room descriptions
#               desc_arr_index - int - Index for current room 
#               rmms_arr - array - Array of all room objects
#               w_list/a_list/s_list - arrays- contains all weapons, armors, shields, and consumables that are need to run all scenarios
# Returns: returns the output of the corresponding function in the dictionary
#          new_room - int - Room that player will move into
#           rooms_arr - array - Returns modified room array
#           player - object - player character
def room_encounters(c_room, desc_arr, desc_arr_index, rms_arr, player, weapon_list, armor_list, shield_list, consume_list):
    # special room descriptions (static encounters) are checked else normal room encounters play out
    if c_room == 0:     # entrance
        return encounter_dict[c_room](desc_arr[desc_arr_index], rms_arr, player, weapon_list, armor_list, shield_list, consume_list)
    elif c_room == 31:      # exit
        return encounter_dict[c_room](desc_arr[desc_arr_index], rms_arr, player, weapon_list, armor_list, shield_list, consume_list)
    elif c_room == 32:      # boss
        return encounter_dict[c_room](desc_arr[-1], rms_arr, player, weapon_list, armor_list, shield_list, consume_list)
    else:
        return encounter_dict[c_room](desc_arr[desc_arr_index], rms_arr, player, weapon_list, armor_list, shield_list, consume_list)

# encounter scenarios start
# Description: These are to be used in the room encounter functions in their dictionary
# Returns:  It will return the player character as the player character and/or 
#           its items will most likely be changed during encounters
def encounter_scenario_1(player, w_list, a_list, s_list, c_list):    # venus mantrap
    mantrap = char.Character.create_vmt(w_list) # creates enemy for combat
    enemy_list = [mantrap]                      # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_2(player, w_list, a_list, s_list, c_list):    # harpies 1-3
    # random number of harpies created for combat
    num_of_harpies = rand.randint(1, 3) # 1-3 inclusive
    match num_of_harpies:
        case 1: # 1 harpy
            harpy = char.Character.create_harpies(1, w_list)
            enemy_list = [harpy]                    # list of all enemies to be used in combat function
        case 2: # 2 harpies
            harpy0, harpy1 = char.Character.create_harpies(2, w_list)
            enemy_list = [harpy0, harpy1]           # list of all enemies to be used in combat function
        case 3: # 3 harpies
            harpy0, harpy1, harpy2 = char.Character.create_harpies(3, w_list)
            enemy_list = [harpy0, harpy1, harpy2]   # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat
        

def encounter_scenario_3(player, w_list, a_list, s_list, c_list):    # sword skeletons 1-3
    # random number of skeletons created for combat
    num_of_skeletons = rand.randint(1, 3) # 1-3 inclusive
    match num_of_skeletons:
        case 1: # 1 skeleton
            skeleton = char.Character.create_skeleton('sword', w_list, a_list, s_list, 1)
            enemy_list = [skeleton]                    # list of all enemies to be used in combat function
        case 2: # 2 skeletons
            skeleton0, skeleton1 = char.Character.create_skeleton('sword', w_list, a_list, s_list, 2)
            enemy_list = [skeleton0, skeleton1]           # list of all enemies to be used in combat function
        case 3: # 3 skeletons
            skeleton0, skeleton1, skeleton2 = char.Character.create_skeleton('sword', w_list, a_list, s_list, 3)
            enemy_list = [skeleton0, skeleton1, skeleton2]           # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat
    

def encounter_scenario_4(player, w_list, a_list, s_list, c_list):    # bow skeletons 1-2
    # random number of skeletons created for combat
    num_of_skeletons = rand.randint(1, 2) # 1-2 inclusive
    match num_of_skeletons:
        case 1: # 1 skeleton
            skeleton = char.Character.create_skeleton('bow', w_list, a_list, s_list, 1)
            enemy_list = [skeleton]                    # list of all enemies to be used in combat function
        case 2: # 2 skeletons
            skeleton0, skeleton1 = char.Character.create_skeleton('bow', w_list, a_list, s_list, 2)
            enemy_list = [skeleton0, skeleton1]           # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_5(player, w_list, a_list, s_list, c_list):    # siren
    # MAY NEED SPECIAL ENCOUNTER LOOP OR SOMETHING
    # save for later!!!!!
    print('temp THIS IS SIREN ROUND')
    return player

def encounter_scenario_6(player, w_list, a_list, s_list, c_list):    # minotaur
    minotaur = char.Character.create_mino(w_list) # creates enemy for combat
    enemy_list = [minotaur]                      # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_7(player, w_list, a_list, s_list, c_list):    # decayed ancient captain
    decay_capt = char.Character.create_decay_capt(w_list, s_list)   # creates enemy for combat
    enemy_list = [decay_capt]                                       # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_8(player, w_list, a_list, s_list, c_list):    # mummy
    mummy = char.Character.create_mummy(w_list)     # creates enemy for combat
    enemy_list = [mummy]                            # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_9(player, w_list, a_list, s_list, c_list):    # cyclops
    cyclops = char.Character.create_cyclops(w_list, a_list)       # creates enemy for combat
    enemy_list = [cyclops]                                        # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_10(player, w_list, a_list, s_list, c_list):   # honorable duelist
    # asks player if they wish to pick up the rapier
    choice = str(input('Do you wish to pick up the rapier? Yes or no? ').lower())
    while True:     # repeats question until a correct response is gotten from user
        if choice == 'yes':     # player wishes to pickup rapier
            player.inventory = lib.item_pickup(player.inventory, w_list[4]) # item pickup function used on the rapier
            break
        elif choice == 'no':    # player does not pick up the rapier
            break
        else:   # If no proper answer is given, loop tries again
            choice = input("Please enter yes or no. ")
    duelist = char.Character.create_duelist(w_list, a_list, s_list)         # creates enemy for combat
    enemy_list = [duelist]                                                  # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_11(player, w_list, a_list, s_list, c_list):   # golem
    golem = char.Character.create_golem(w_list)                 # creates enemy for combat
    enemy_list = [golem]                                        # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_12(player, w_list, a_list, s_list, c_list):   # pristine ancient captain
    pristine_capt = char.Character.create_pristine_capt(w_list, a_list, s_list)         # creates enemy for combat
    enemy_list = [pristine_capt]                                                        # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_13(player, w_list, a_list, s_list, c_list):   # ancient spellspear
    spellspear = char.Character.create_spellspear(w_list, a_list, s_list)       # creates enemy for combat
    enemy_list = [spellspear]                                                      # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_14(player, w_list, a_list, s_list, c_list):   # hellknight
    # AT END OF ENCOUNTER U GAIN HIS SWORD
    hellknight = char.Character.create_hellknight(w_list, a_list, s_list)       # creates enemy for combat
    enemy_list = [hellknight]                                                   # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    # asks player if they wish to pick up the hellknights greatsword
    choice = str(input('Do you wish to pick up the hellknights greatsword? Yes or no?').lower())
    while True:     # repeats question until a correct response is gotten from user
        if choice == 'yes':     # player wishes to pickup greatsword
            player.inventory = lib.item_pickup(player.inventory, w_list[5]) # item pickup function used on the greatsword
            break
        elif choice == 'no':    # player does not pick up the greatsword
            break
        else:   # If no proper answer is given, loop tries again
            choice = input("Please enter yes or no. ")
    return player                                   # returns player after combat and decision about greatsword

def encounter_scenario_15(player, w_list, a_list, s_list, c_list):   # lost travelers (2)
    traveler0, traveler1 = char.Character.create_travelers(w_list, a_list)      # creates enemies for combat
    enemy_list = [traveler0, traveler1]                                         # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_16(player, w_list, a_list, s_list, c_list):   # forsaken mage
    mage = char.Character.create_mage(w_list, a_list)   # creates enemy for combat
    enemy_list = [mage]                                 # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_17(player, w_list, a_list, s_list, c_list):   # shadow
    shadow = char.Character.create_golem(player)                 # creates enemy for combat, uses player for equipment
    enemy_list = [shadow]                                        # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_18(player, w_list, a_list, s_list, c_list):   # overgrown toad
    toad = char.Character.create_toad(w_list)       # creates enemy for combat
    enemy_list = [toad]                             # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_19(player, w_list, a_list, s_list, c_list):   # hell hounds 1-2
    # random number of hell hounds created for combat
    num_of_hounds = rand.randint(1, 2) # 1-2 inclusive
    match num_of_hounds:
        case 1: # 1 hound
            hound = char.Character.create_hounds(w_list, 1)
            enemy_list = [hound]                    # list of all enemies to be used in combat function
        case 2: # 2 skeletons
            hound0, hound1 = char.Character.create_hounds(w_list, 2)
            enemy_list = [hound0, hound1]           # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_20(player, w_list, a_list, s_list, c_list):   # baby red dragon
    baby_dragon = char.Character.create_brd(w_list, a_list)         # creates enemy for combat
    enemy_list = [baby_dragon]                                      # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_21(player, w_list, a_list, s_list, c_list):    # poison floor
    # applies poison to player for 4 turns
    player.debuff = 'poisoned'
    player.debuff_stack = 4
    return player   # returns player after affliction is added

def encounter_scenario_22(player, w_list, a_list, s_list, c_list):    # poison dart room
    # player is hit with 0-5 poison darts
    hits = rand.randint(0, 5)  # how many darts hit player
    dmg_taken = hits * 5    # each dart does 5 damage
    player.hp -= dmg_taken
    player.debuff = 'poisoned'
    player.debuff_stack = hits  # poison lasts for as many turns as the player is hit
    return player   # returns player after affliction and damage is added

def encounter_scenario_23(player, w_list, a_list, s_list, c_list):    # arrow trap
    # player is hit with 0-4 arrows
    hits = rand.randint(0, 4)  # how many arrows hit player
    dmg_taken = hits * 10    # each arrow does 10 damage
    player.hp -= dmg_taken
    return player   # returns player after affliction and damage is added

def encounter_scenario_24(player, w_list, a_list, s_list, c_list):    # spike trap
    # player is hit with 1-3 spikes
    hits = rand.randint(1, 3)  # how many spikes pierce player
    dmg_taken = hits * 15    # each spike does 15 damage
    player.hp -= dmg_taken
    return player   # returns player after affliction and damage is dealt

def encounter_scenario_25(player, w_list, a_list, s_list, c_list):    # arcane missle library book
    choice = str(input('Do you wish to pick up the shimmering book? Yes or no?').lower())
    while True:     # repeats question until a correct response is gotten from user
        if choice == 'yes':     # player wishes to pickup the glowing book
            print('A blue missle erupts from the book when the shimmering shield is broken. Before you can react the missle slams into your chest, thwoing you to your back. ')
            player.hp -= 10     # magic missle does 10 damage
            break
        elif choice == 'no':    # nothing happens when player does not pick up the book
            break
        else:   # If no proper answer is given, loop tries again
            choice = input("Please enter yes or no. ")
    return player   # returns player after damage may have been done

def encounter_scenario_26(player, w_list, a_list, s_list, c_list):    # log trap
    # player is hit by a log trap
    player.hp -= 25  # log trap does 25 damage
    return player   # returns player after damage is dealt

def encounter_scenario_27(player, w_list, a_list, s_list, c_list):    # fireball seal
    # player is hit by fireball explosion
    player.hp -= 30     # fireball does 30 damage
    return player # returns player after damage is done

def encounter_scenario_28(player, w_list, a_list, s_list, c_list):    # snake pit 0-3 snake bites
    # player is bit by 0-3 poisonous snakes
    bites = rand.randint(0, 3)  # how many snakes bite player
    dmg_taken = bites * 10    # each bite does 10 damage
    player.hp -= dmg_taken
    if bites > 0:        # if player got bit
        player.debuff = 'poisoned'
        player.debuff_stack = bites
    return player   # returns player after affliction and damage is dealt

def encounter_scenario_29(player, w_list, a_list, s_list, c_list):    # coin flip door
    door_case = rand.randint(1, 2)    # selects a random number to decide which color will open the door
    choice = str(input('Which button would you like to pick? Red or blue? ')).lower()
    while True:
        if choice == 'blue' or 'red':       # valid response entered by player
            break
        else:       # response was invalid
            choice = str(input('Please enter red or blue. ')).lower()
    match door_case:
        case 1:         # if 1 is randomly selected, then blue is the right answer
            if choice == 'blue':
                print('The door opens slowly as gears grind loudly from within the door.')
                return player
            else:
                print('Electricity jolts through you body from the wrong selection. Despite the tense muscles you manage to quickly press the blue button, which frees you from the torture.')
                player.hp -= 10     # electricity does 10 damage
                return player
        case 2:         # if 2 is randomly selected, then red is the right answer
            if choice == 'red':
                print('The door opens slowly as gears grind loudly from within the door.')
                return player
            else:
                print('Electricity jolts through you body from the wrong selection. Despite the tense muscles you manage to quickly press the red button, which frees you from the torture.')
                player.hp -= 10     # electricity does 10 damage
                return player

def encounter_scenario_30(player, w_list, a_list, s_list, c_list):    # pendulum axes over chasm
    # player is scratched by pendulum axe
    player.hp -= 15     # axe does 15 damage
    return player # returns player after damage is done

def encounter_scenario_31(player, w_list, a_list, s_list, c_list):    # ancient sword in the stone
    choice = str(input('Do you pull the sword from the stone? Yes or no? ')).lower()
    while True:
        if choice == 'yes':       # player pulls sword from the stone
            player.inventory = lib.item_pickup(player.invetory, w_list[4])
            break
        elif choice == 'no':        # player does not pull the sword from the stone
            break
        else:       # response was invalid
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_32(player, w_list, a_list, s_list, c_list):    # heavy armor on display
    choice = str(input('Do you take the armor from the display? Yes or no? ')).lower()
    while True:
        if choice == 'yes':       # player uses the armor
            player.inventory = lib.item_pickup(player.invetory, a_list[2])
            break
        elif choice == 'no':        # player does not use the armor
            break
        else:       # response was invalid
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_33(player, w_list, a_list, s_list, c_list):    # apothecary 3-5 random potions
    num_of_potions = rand.randint(3, 5) # 3-5 random potions are in the apothecary
    # player has choice to check for or leave the potions
    choice = str(input('Do you check for potions from the apothecary? Yes or no? ')).lower()
    while True:
        if choice == 'yes':       # player takes the potions
            # 3 potion minimum
            # potion0
            potion0 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
            if potion0 < 4:         # the 1st four potions are the top 4 in the consumables list
                player.inventory = lib.item_pickup(player.invetory, c_list[potion0])    # player choses to keep and leave potion
            elif potion0 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                player.inventory = lib.item_pickup(player.invetory, c_list[potion0 + 1])    # player choses to keep and leave potion
            # potion1
            potion1 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
            if potion1 < 4:         # the 1st four potions are the top 4 in the consumables list
                player.inventory = lib.item_pickup(player.invetory, c_list[potion1])    # player choses to keep and leave potion
            elif potion1 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                player.inventory = lib.item_pickup(player.invetory, c_list[potion1 + 1])    # player choses to keep and leave potion
            # potion2
            potion2 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
            if potion2 < 4:         # the 1st four potions are the top 4 in the consumables list
                player.inventory = lib.item_pickup(player.invetory, c_list[potion2])    # player choses to keep and leave potion
            elif potion2 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                player.inventory = lib.item_pickup(player.invetory, c_list[potion2 + 1])    # player choses to keep and leave potion
            # Depends on how num_of_potions if the following potions are generated
            # potion3
            if num_of_potions == 4:
                potion3 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
                if potion3 < 4:         # the 1st four potions are the top 4 in the consumables list
                    player.inventory = lib.item_pickup(player.invetory, c_list[potion3])    # player choses to keep and leave potion
                elif potion3 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                    player.inventory = lib.item_pickup(player.invetory, c_list[potion3 + 1])    # player choses to keep and leave potion
            # potion4
            elif num_of_potions ==5:
                potion4 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
                if potion4 < 4:         # the 1st four potions are the top 4 in the consumables list
                    player.inventory = lib.item_pickup(player.invetory, c_list[potion4])    # player choses to keep and leave potion
                elif potion4 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                    player.inventory = lib.item_pickup(player.invetory, c_list[potion4 + 1])    # player choses to keep and leave potion
            break
        elif choice == 'no':        # player does not look for any potions
            break
        else:       # response was invalid
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_34(player, w_list, a_list, s_list, c_list):    # field hospital 1-3 cleanse potions and 2-4 bandages
    # cleanse potion generation and pickup
    num_of_cleanse = rand.randint(1, 3) # number of cleanse potions in the hospital
    choice = str(input(f'There are {num_of_cleanse} cleanse potions in the field hospital, do you want to grab them? Yes or no? ')).lower()
    while True:
        if choice == 'yes':     # player accepts the cleanse potions
            for i in range(num_of_cleanse - 1):
                player.inventory = lib.item_pickup(player.invetory, c_list[3])  # cleanse potions are at index 3 of consumable list
            break
        elif choice == 'no':    # player passes on the cleanse potions
            break
        else:       # invalid response
            choice = str(input('Please enter yes or no. ')).lower()
    # bandage generation and pickup
    num_of_bands = rand.randint(2, 4) # number of bandages in the hospital
    choice = str(input(f'There are {num_of_bands} bandages in the field hospital, do you want to grab them? Yes or no? ')).lower()
    while True:
        if choice == 'yes':     # player accepts the cleanse potions
            for i in range(num_of_bands - 1):
                player.inventory = lib.item_pickup(player.invetory, c_list[4])  # bandages are at index 4 of consumable list
            break
        elif choice == 'no':    # player passes on the bandages
            break
        else:       # invalid response
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_35(player, w_list, a_list, s_list, c_list):    # armory room with 1 or 3 weapons, armor, and shield(s)
    # armory room type generation - 0 == armory with only 1 salvaged item, 1 == armory with 1 of each item type
    choice = str(input('Do you wish to search for any items that can be salvaged from the armory? Yes or no? ').lower())
    while True:
        if choice == 'yes':     # player searches for salvagable items
            armory_type = rand.randint(0, 1)
            if armory_type == 1:    # only 1 salvaged item
                item_type = rand.randint(1, 3)  # 1 == weapon, 2 == armor, and 3 == shield item generated
                match item_type:
                    case 1:     # weapon salvaged
                        w_index = rand.randint(0, 7)
                        player.inventory = lib.item_pickup(player.invetory, w_list[w_index])  # player picks up weapon based on what is randomly found
                    case 2:     # armor salvaged
                        a_index = rand.randint(0, 2)
                        player.inventory = lib.item_pickup(player.invetory, a_list[a_index])  # player picks up armor based on what is randomly found
                    case 3:     # shield salvaged
                        s_index = rand.randint(0, 2)
                        player.inventory = lib.item_pickup(player.invetory, s_list[s_index])  # player picks up shield based on what is randomly found
            else:   # full armory type is generated - 0
                # weapons salvaged
                w_index = rand.randint(0, 7)
                player.inventory = lib.item_pickup(player.invetory, w_list[w_index])  # player picks up weapon based on what is randomly found
                # armor salvaged
                a_index = rand.randint(0, 2)
                player.inventory = lib.item_pickup(player.invetory, a_list[a_index])  # player picks up armor based on what is randomly found
                # shield salvaged
                s_index = rand.randint(0, 2)
                player.inventory = lib.item_pickup(player.invetory, s_list[s_index])  # player picks up shield based on what is randomly found
            break   # breaks while loop after items have been salvaged
        elif choice == 'no':    # player does not salavge items
            break   # breaks while loop after items have been salvaged
        else:       # invalid response from player
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_36(player, w_list, a_list, s_list, c_list):    # wizard tower with 1-2 random scrolls
    choice = str(input('Do you wish to take any scrolls you can read from the wizard tower? Yes or no? ').lower())
    while True:
        if choice == 'yes':     # player is looting the wizards tower
            num_of_scrolls = rand.randint(1, 2)
            match num_of_scrolls:
                case 1:     # 1 readable scroll found
                    scroll_found = rand.randint(6, 7)   # 6 and 7 are the indexes of the scrolls in the weapon list
                    player.inventory = lib.item_pickup(player.invetory, w_list[scroll_found])  # player picks up the scroll they found
                case 2:     # two scrolls are found - fireball and arcane missle
                    player.inventory = lib.item_pickup(player.invetory, w_list[6])  # player picks up a scroll they found
                    player.inventory = lib.item_pickup(player.invetory, w_list[7])  # player picks up a scroll they found
            break
        elif choice == 'no':    # player does not loot the tower
            break
        else:       # invalid response from player
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_37(player, w_list, a_list, s_list, c_list):    # treasure room with ornate magic shield and 1/3 chance for ornate weapon
    choice = str(input('Do you wish to loot the treasure room? Yes or no? ').lower())
    while True:
        if choice == 'yes':     # player is looting the treasure room
            # ornate shield pickup
            player.inventory = lib.item_pickup(player.invetory, s_list[2])      # sturdy shield = ornate shield
            # ornate sword pickup
            ornate_sword_roll = rand.randint(1, 3)  # ornate sword has a 1/3 chance to spawn in the treasure room
            if ornate_sword_roll == 3:      # player hit the 1 in 3 chance
                player.inventory = lib.item_pickup(player.invetory, w_list[1])      # ancient sword = ornate sword
            break
        elif choice == 'no':        # player does not loot
            break
        else:   # invalid response from player
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_38(player, w_list, a_list, s_list, c_list):    # travelers old storage room has 1 buckler, short sword, and light armor
    print('In the far corner of the room there lay a short sword, a buckler, and some light leather armor that luckily fits you.')
    choice = str(input('Do you wish to take the items? Yes or no? ').lower())
    while True:
        if choice == 'yes':     # player is looting the traveler's room
            player.inventory = lib.item_pickup(player.invetory, s_list[0])  # player picks up buckler
            player.inventory = lib.item_pickup(player.invetory, a_list[1])  # player picks up light armor
            player.inventory = lib.item_pickup(player.invetory, w_list[2])  # player pick ups short sword
            break
        elif choice == 'no':    # player leaves the items behind
            break
        else:       # invlaid response from player
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_39(player, w_list, a_list, s_list, c_list):    # apothecary with different description and 2-5 random potions
    num_of_potions = rand.randint(3, 5) # 3-5 random potions are in the apothecary
    # player has choice to check for or leave the potions
    choice = str(input('Do you check for potions from the apothecary? Yes or no? ')).lower()
    while True:
        if choice == 'yes':       # player takes the potions
            # 3 potion minimum
            # potion0
            potion0 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
            if potion0 < 4:         # the 1st four potions are the top 4 in the consumables list
                player.inventory = lib.item_pickup(player.invetory, c_list[potion0])    # player choses to keep and leave potion
            elif potion0 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                player.inventory = lib.item_pickup(player.invetory, c_list[potion0 + 1])    # player choses to keep and leave potion
            # potion1
            potion1 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
            if potion1 < 4:         # the 1st four potions are the top 4 in the consumables list
                player.inventory = lib.item_pickup(player.invetory, c_list[potion1])    # player choses to keep and leave potion
            elif potion1 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                player.inventory = lib.item_pickup(player.invetory, c_list[potion1 + 1])    # player choses to keep and leave potion
            # potion2
            potion2 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
            if potion2 < 4:         # the 1st four potions are the top 4 in the consumables list
                player.inventory = lib.item_pickup(player.invetory, c_list[potion2])    # player choses to keep and leave potion
            elif potion2 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                player.inventory = lib.item_pickup(player.invetory, c_list[potion2 + 1])    # player choses to keep and leave potion
            # Depends on how num_of_potions if the following potions are generated
            # potion3
            if num_of_potions == 4:
                potion3 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
                if potion3 < 4:         # the 1st four potions are the top 4 in the consumables list
                    player.inventory = lib.item_pickup(player.invetory, c_list[potion3])    # player choses to keep and leave potion
                elif potion3 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                    player.inventory = lib.item_pickup(player.invetory, c_list[potion3 + 1])    # player choses to keep and leave potion
            # potion4
            elif num_of_potions ==5:
                potion4 = rand.randint(0, 5)     # out of all the comsumable items there are 6 which are potions
                if potion4 < 4:         # the 1st four potions are the top 4 in the consumables list
                    player.inventory = lib.item_pickup(player.invetory, c_list[potion4])    # player choses to keep and leave potion
                elif potion4 >= 4:      # the 5th and 6th potion are at the index of potionX + 1
                    player.inventory = lib.item_pickup(player.invetory, c_list[potion4 + 1])    # player choses to keep and leave potion
            break
        elif choice == 'no':        # player does not look for any potions
            break
        else:       # response was invalid
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_40(player, w_list, a_list, s_list, c_list):    # library with emergency fireball scroll
    choice = str(input('Do you break the glass and take the scroll? Yes or no? ')).lower()
    while True:
        if choice == 'yes':        # player takes the fireball scroll
            player.inventory = lib.item_pickup(player.invetory, w_list[6])  # player picks up fireball scroll
            break
        elif choice == 'no':        # player skipped on the scroll
            break
        else:       # invalid response from player
            choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_41(player, w_list, a_list, s_list, c_list):    # infusion room
    # checks to see if player has any weapon to infuse
    w_count, w_ind = lib.weapon_counter(player)
    if w_count > 0:     # If player has a weapon
        choice = str(input('Do you want to infuse a weapon? Yes or no? ')).lower()
        while True:
            if choice == 'yes':        # player wishes to infuse one of their weapon(s)
                count = 0       # count is used to list the weapons in the for loop below
                for index in w_ind: # for each index in weapon index list
                    count += 1
                    print(f'{count}. {w_list[index].name} Damage: {w_list[index].damage} Current Infusion: {w_list[index].infusion}')
                chosen_wep = input('Please enter the number of the weapon you would like to infuse (infusions can be overwritten). ')
                while True:
                    try:        # catches type error for chosen_wep
                        if 0 < int(chosen_wep) <= w_count:       # if chosen weapon is a valid number within the range of player weapons
                            # list all infusion optionfs for the player weapon
                            print('1. Magic +1 - Desc: Deals an additional 15 damage.')
                            print('2. Fiery - Desc: Applies the \'burned\' status effect.')
                            print('3. Acid - Desc: Applies the \'acidic\' status effect.')
                            print('4. Gore - Desc: Applies the \'gored\' status effect.')
                            chosen_infusion = input('Please enter the number of the infusion you would like to apply. (1, 2, 3, or 4). ')
                            while True:
                                try:    # catches type error for chosen infusion
                                    if 0 < int(chosen_infusion) < 5:    # valid choice for infusion
                                        match chosen_infusion:
                                            case 1: # magic +1
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'magic +1'
                                                break
                                            case 2: # fiery
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'fiery'
                                                break
                                            case 3: # acid
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'acid'
                                                break
                                            case 4: # gore
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'gore'
                                                break
                                except:
                                    chosen_infusion = input('Please enter a number from the following: 1, 2, 3, or 4. ')
                                    continue
                            break
                    except:
                        chosen_wep = input('Please enter a number. ')
                        continue    # retires until valid number is given
                break
            elif choice == 'no':        # player skipped on infusing a weapon
                break
            else:       # invalid response from player
                choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_42(player, w_list, a_list, s_list, c_list):    # different infusion room
    # checks to see if player has any weapon to infuse
    w_count, w_ind = lib.weapon_counter(player)
    if w_count > 0:     # If player has a weapon
        choice = str(input('Do you want to infuse a weapon? Yes or no? ')).lower()
        while True:
            if choice == 'yes':        # player wishes to infuse one of their weapon(s)
                count = 0       # count is used to list the weapons in the for loop below
                for index in w_ind: # for each index in weapon index list
                    count += 1
                    print(f'{count}. {w_list[index].name} Damage: {w_list[index].damage} Current Infusion: {w_list[index].infusion}')
                chosen_wep = input('Please enter the number of the weapon you would like to infuse (infusions can be overwritten). ')
                while True:
                    try:        # catches type error for chosen_wep
                        if 0 < int(chosen_wep) <= w_count:       # if chosen weapon is a valid number within the range of player weapons
                            # list all infusion optionfs for the player weapon
                            print('1. Magic +1 - Desc: Deals an additional 15 damage.')
                            print('2. Fiery - Desc: Applies the \'burned\' status effect.')
                            print('3. Acid - Desc: Applies the \'acidic\' status effect.')
                            print('4. Gore - Desc: Applies the \'gored\' status effect.')
                            chosen_infusion = input('Please enter the number of the infusion you would like to apply. (1, 2, 3, or 4). ')
                            while True:
                                try:    # catches type error for chosen infusion
                                    if 0 < int(chosen_infusion) < 5:    # valid choice for infusion
                                        match chosen_infusion:
                                            case 1: # magic +1
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'magic +1'
                                                break
                                            case 2: # fiery
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'fiery'
                                                break
                                            case 3: # acid
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'acid'
                                                break
                                            case 4: # gore
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'gore'
                                                break
                                except:
                                    chosen_infusion = input('Please enter a number from the following: 1, 2, 3, or 4. ')
                                    continue
                            break
                    except:
                        chosen_wep = input('Please enter a number. ')
                        continue    # retires until valid number is given
                break
            elif choice == 'no':        # player skipped on infusing a weapon
                break
            else:       # invalid response from player
                choice = str(input('Please enter yes or no. ')).lower()
    return player

def encounter_scenario_43(player, w_list, a_list, s_list, c_list):    # other different infusion room
    # checks to see if player has any weapon to infuse
    w_count, w_ind = lib.weapon_counter(player)
    if w_count > 0:     # If player has a weapon
        choice = str(input('Do you want to infuse a weapon? Yes or no? ')).lower()
        while True:
            if choice == 'yes':        # player wishes to infuse one of their weapon(s)
                count = 0       # count is used to list the weapons in the for loop below
                for index in w_ind: # for each index in weapon index list
                    count += 1
                    print(f'{count}. {w_list[index].name} Damage: {w_list[index].damage} Current Infusion: {w_list[index].infusion}')
                chosen_wep = input('Please enter the number of the weapon you would like to infuse (infusions can be overwritten). ')
                while True:
                    try:        # catches type error for chosen_wep
                        if 0 < int(chosen_wep) <= w_count:       # if chosen weapon is a valid number within the range of player weapons
                            # list all infusion optionfs for the player weapon
                            print('1. Magic +1 - Desc: Deals an additional 15 damage.')
                            print('2. Fiery - Desc: Applies the \'burned\' status effect.')
                            print('3. Acid - Desc: Applies the \'acidic\' status effect.')
                            print('4. Gore - Desc: Applies the \'gored\' status effect.')
                            chosen_infusion = input('Please enter the number of the infusion you would like to apply. (1, 2, 3, or 4). ')
                            while True:
                                try:    # catches type error for chosen infusion
                                    if 0 < int(chosen_infusion) < 5:    # valid choice for infusion
                                        match chosen_infusion:
                                            case 1: # magic +1
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'magic +1'
                                                break
                                            case 2: # fiery
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'fiery'
                                                break
                                            case 3: # acid
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'acid'
                                                break
                                            case 4: # gore
                                                player.inventory[w_ind[chosen_wep - 1]].infusion = 'gore'
                                                break
                                except:
                                    chosen_infusion = input('Please enter a number from the following: 1, 2, 3, or 4. ')
                                    continue
                            break
                    except:
                        chosen_wep = input('Please enter a number. ')
                        continue    # retires until valid number is given
                break
            elif choice == 'no':        # player skipped on infusing a weapon
                break
            else:       # invalid response from player
                choice = str(input('Please enter yes or no. ')).lower()
    return player

# ALL ROOMS HERE (except the last two) DO NOT HAVE ANY SPECIAL EFECTS AND ARE CONSIDERED TO BE 'EMPTY ROOMS'
# THEY ALL ONLY RETURN PLAYER
def encounter_scenario_44(player, w_list, a_list, s_list, c_list):    # ancient masks
    return player

def encounter_scenario_45(player, w_list, a_list, s_list, c_list):    # cursed artifacts
    return player

def encounter_scenario_46(player, w_list, a_list, s_list, c_list):    # ancient ritual room with runes
    return player

def encounter_scenario_47(player, w_list, a_list, s_list, c_list):    # functioning observatory
    return player

def encounter_scenario_48(player, w_list, a_list, s_list, c_list):    # stained torture room
    return player

def encounter_scenario_49(player, w_list, a_list, s_list, c_list):    # ethereal bridge over abyss
    return player

def encounter_scenario_50(player, w_list, a_list, s_list, c_list):    # mirror of memories
    return player

def encounter_scenario_51(player, w_list, a_list, s_list, c_list):    # boss
    adult_drag = char.Character.create_ard(w_list, a_list) # creates enemy for combat
    enemy_list = [adult_drag]                      # list of all enemies to be used in combat function
    # combat
    player = com.combat_loop(enemy_list, player)    # updates player after combat, if they survive
    return player                                   # returns player after combat

def encounter_scenario_52(player, w_list, a_list, s_list, c_list):    # exit
    # nothing happens, it is just a description being read out
    # CHANGED, THIS IS NO LONGER EVEN CALLED
    print('temp FAILED EXIT ONE???, THIS SHOULD NEVER APPEAR')
    return player

encounter_scenario_dict = {
    1: encounter_scenario_1,
    2: encounter_scenario_2,
    3: encounter_scenario_3,
    4: encounter_scenario_4,
    5: encounter_scenario_5,
    6: encounter_scenario_6,
    7: encounter_scenario_7,
    8: encounter_scenario_8,
    9: encounter_scenario_9,
    10: encounter_scenario_10,
    11: encounter_scenario_11,
    12: encounter_scenario_12,
    13: encounter_scenario_13,
    14: encounter_scenario_14,
    15: encounter_scenario_15,
    16: encounter_scenario_16,
    17: encounter_scenario_17,
    18: encounter_scenario_18,
    19: encounter_scenario_19,
    20: encounter_scenario_20,
    21: encounter_scenario_21,
    22: encounter_scenario_22,
    23: encounter_scenario_23,
    24: encounter_scenario_24,
    25: encounter_scenario_25,
    26: encounter_scenario_26,
    27: encounter_scenario_27,
    28: encounter_scenario_28,
    29: encounter_scenario_29,
    30: encounter_scenario_30,
    31: encounter_scenario_31,
    32: encounter_scenario_32,
    33: encounter_scenario_33,
    34: encounter_scenario_34,
    35: encounter_scenario_35,
    36: encounter_scenario_36,
    37: encounter_scenario_37,
    38: encounter_scenario_38,
    39: encounter_scenario_39,
    40: encounter_scenario_40,
    41: encounter_scenario_41,
    42: encounter_scenario_42,
    43: encounter_scenario_43,
    44: encounter_scenario_44,
    45: encounter_scenario_45,
    46: encounter_scenario_46,
    47: encounter_scenario_47,
    48: encounter_scenario_48,
    49: encounter_scenario_49,
    50: encounter_scenario_50,
    51: encounter_scenario_51,
    52: encounter_scenario_52
}

# encounter_picker starts
# encounter_picker - selects encounter scenario from dictionary based on room
# Parameters:   player - object - player character
#               encounter_num - int - num spliced from encounter desc, used to select and play out any action in a room if there is any
#               weapon_list - list of objects - List of all weapons, used to create enemies in needed scenarios
#               armor_list - list of objects - List of all armor, used to create enemies in needed scenarios
#               shield_list - list of objects - List of all shields, used to create enemies in needed scenarios
# Returns:      player - object - player character
def encounter_picker(player, encounter_num, weapon_list, armor_list, shield_list, comsumable_list):
    return encounter_scenario_dict[int(encounter_num)](player, weapon_list, armor_list, shield_list, comsumable_list)    # returns encounter scenario output