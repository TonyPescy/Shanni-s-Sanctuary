#######################################################################################################################################
# Title: Encounter
# Author: Tony Pescatore and Nick Pescatore
# Description: All encounter descriptions and encounter interactions
#######################################################################################################################################

# imports
import sys
import Rooms as rm

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
    print("You are walking down the side walk of the city you've spent your entire life in, during that time nothing much has changed.  It was always a small city, but now that you've grown up it seems to have gotten smaller and much duller.  You know every inch of this city like the back of your hand, you could walk the streets blindfolded and make it to work on time.  However today was odd, a peculiar weight was on you shoulders, maybe work was getting to you?  But that can't be making you feel this way can it?.")
    answer = str(input("That's when something catches your eye, something you never saw before.  A large overgrown pyramid in the center of the street, how have you never noticed this before?  A voice speaks to you, it comes from within your own mind, it's beckoning you forth.  Come closer it says, egging you on and on.  Do you listen to what the voice says?  Yes or no? ").lower())
    while True:
        if answer.lower() == "no":
            print("Your body does not listen to you, instead it does the opposite and begins towards the massive black pyramid.")
            break
        elif answer.lower() == "yes":
            print("Your begin towards the massive black pyramid, unaware of the implications it will have for your future... or if there will be one to come back to. ")
            break
        else:               # If no proper answer is given, program tries again
            answer = input("Enter yes or no ")
            
# Introduction Ends

# random encounters start
# Cases for each room in game and what to do with dictionary lookup
# each function will return the new room number based on direction inputted

# IN ROOM DESCRIPTIONS.TXT FOR EVERY ENTRY ADD A DELIMITER "~" THAT CAN BE READ SO THAT WE CAN HAVE FLAVORED ROOM ENTER AND EXIT DESCRIPTIONS

# rm_entrance Starts
# rm_entrance - First encounter within the actual pyramid
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - Room that player will move into
#               rooms_arr - array - Returns modified room array Note: rooms_arr does not change here as rm_entrance cannot be entered again
def rm_entrance(desc, rooms_arr):
    print(desc)
    next_direction = rm.Room.get_player_move(rooms_arr[32].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[32].num)      # gets new room that player has selected
    print('As you you make your way north, those heavy wooden doors slam shut. Another barrier to ensure you do not escape Shanni\'s Sanctuary.')
    
    return rooms_arr, new_room
# room_entrance ends


# rm_1 Starts
# rm_1 - Room 1 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_1(desc, rooms_arr):
    encounter_num_ind = desc.find(' ')  # finds index at the end of the room description number which allows for correct combat scenario
    combat_scenario = desc[:encounter_num_ind]  # selects number from room description
    print(desc[encounter_num_ind:])
    if rooms_arr[0].re_entry != True:   # first time entering the room
        #COMBAT GOES HERE
        rooms_arr[0].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 1 has been already entered and conquered
    else:       # room has been entered before
        print('As you have been here before, Shanni bestows the gift of guidance upon you. She states the best direction to go from here is North.')
    next_direction = rm.Room.get_player_move(rooms_arr[0].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[0].num)      # gets new room that player has selected
    print("THIS IS UR EXIT OF ROOM 1")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_1 ends

# rm_2 Starts
# rm_2 - Room 2 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_2(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[1].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[1].num)      # gets new room that player has selected
    rooms_arr[1].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 2 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 2")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_2 ends

# rm_3 Starts
# rm_3 - Room 3 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_3(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[2].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[2].num)      # gets new room that player has selected
    rooms_arr[2].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 3 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 3")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_3 ends

# rm_4 Starts
# rm_4 - Room 4 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_4(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[3].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[3].num)      # gets new room that player has selected
    rooms_arr[3].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 4 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 4")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_4 ends

# rm_5 Starts
# rm_5 - Room 5 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_5(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[4].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[4].num)      # gets new room that player has selected
    rooms_arr[4].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 5 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 5")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_5 ends

# rm_6 Starts
# rm_6 - Room 6 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_6(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[5].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[5].num)      # gets new room that player has selected
    rooms_arr[5].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 6 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 6")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_6 ends

# rm_7 Starts
# rm_7 - Room 7 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_7(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[6].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[6].num)      # gets new room that player has selected
    rooms_arr[6].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 7 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 7")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_7 ends

# rm_8 Starts
# rm_8 - Room 8 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_8(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[7].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[7].num)      # gets new room that player has selected
    rooms_arr[7].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 8 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 8")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_8 ends

# rm_9 Starts
# rm_9 - Room 9 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_9(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[8].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[8].num)      # gets new room that player has selected
    rooms_arr[8].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 9 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 9")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_9 ends

# rm_10 Starts
# rm_10 - Room 10 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_10(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[9].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[9].num)      # gets new room that player has selected
    rooms_arr[9].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 10 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 10")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_10 ends

# rm_11 Starts
# rm_11 - Room 11 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_11(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[10].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[10].num)      # gets new room that player has selected
    rooms_arr[10].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 11 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 11")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_11 ends

# rm_12 Starts
# rm_12 - Room 12 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_12(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[11].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[11].num)      # gets new room that player has selected
    rooms_arr[11].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 12 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 12")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_12 ends

# rm_13 Starts
# rm_13 - Room 13 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_13(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[12].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[12].num)      # gets new room that player has selected
    rooms_arr[12].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 13 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 13")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_13 ends

# rm_14 Starts
# rm_14 - Room 14 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_14(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[13].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[13].num)      # gets new room that player has selected
    rooms_arr[13].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 14 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 14")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_14 ends

# rm_15 Starts
# rm_15 - Room 15 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_15(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[14].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[14].num)      # gets new room that player has selected
    rooms_arr[14].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 15 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 15")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_15 ends

# rm_16 Starts
# rm_16 - Room 16 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_16(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[15].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[15].num)      # gets new room that player has selected
    rooms_arr[15].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 16 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 16")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_16 ends

# rm_17 Starts
# rm_17 - Room 17 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_17(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[16].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[16].num)      # gets new room that player has selected
    rooms_arr[16].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 17 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 17")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_17 ends

# rm_18 Starts
# rm_18 - Room 18 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_18(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[17].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[17].num)      # gets new room that player has selected
    rooms_arr[17].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 18 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 18")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_18 ends

# rm_19 Starts
# rm_19 - Room 19 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_19(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[18].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[18].num)      # gets new room that player has selected
    rooms_arr[18].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 19 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 19")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_19 ends

# rm_20 Starts
# rm_20 - Room 20 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_20(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[19].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[19].num)      # gets new room that player has selected
    rooms_arr[19].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 20 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 20")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_20 ends

# rm_21 Starts
# rm_21 - Room 21 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_21(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[20].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[20].num)      # gets new room that player has selected
    rooms_arr[20].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 21 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 21")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_21 ends

# rm_22 Starts
# rm_22 - Room 22 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_22(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[21].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[21].num)      # gets new room that player has selected
    rooms_arr[21].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 22 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 22")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_22 ends

# rm_23 Starts
# rm_23 - Room 23 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_23(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[22].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[22].num)      # gets new room that player has selected
    rooms_arr[22].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 23 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 23")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_23 ends

# rm_24 Starts
# rm_24 - Room 24 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_24(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[23].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[23].num)      # gets new room that player has selected
    rooms_arr[23].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 24 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 24")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_24 ends

# rm_25 Starts
# rm_25 - Room 25 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_25(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[24].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[24].num)      # gets new room that player has selected
    rooms_arr[24].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 25 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 25")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_25 ends

# rm_26 Starts
# rm_26 - Room 26 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_26(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[25].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[25].num)      # gets new room that player has selected
    rooms_arr[25].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 26 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 26")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_26 ends

# rm_27 Starts
# rm_27 - Room 27 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_27(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[26].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[26].num)      # gets new room that player has selected
    rooms_arr[26].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 27 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 27")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_27 ends

# rm_28 Starts
# rm_28 - Room 28 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_28(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[27].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[27].num)      # gets new room that player has selected
    rooms_arr[27].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 28 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 28")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_28 ends

# rm_29 Starts
# rm_29 - Room 29 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_29(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[28].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[28].num)      # gets new room that player has selected
    rooms_arr[28].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 29 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 29")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_29 ends

# rm_30 Starts
# rm_30 - Room 30 with random encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_30(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[29].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[29].num)      # gets new room that player has selected
    rooms_arr[28].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that room 30 has been already entered and conquered
    print("THIS IS UR EXIT OF ROOM 30")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_30 ends

# rm_boss Starts
# rm_boss - Boss Room with boss encounter inside
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       new_room - int - Room that player will move into
#               rooms_arr - array - Returns modified room array
def rm_boss(desc, rooms_arr): 
    print(desc)
    #COMBAT GOES HERE
    next_direction = rm.Room.get_player_move(rooms_arr[31].pathing)              # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction.lower(), rooms_arr[31].num)      # gets new room that player has selected
    rooms_arr[31].re_entry = rm.Room.reentry_switch()         # changes rooms_arr to say that boss room has been already entered and conquered
    print("THIS IS UR EXIT OF BOSS ROOM")              # all rooms will need a unique exit statement

    return rooms_arr, new_room
# rm_boss ends

# rm_exit Starts
# rm_exit - Exit room with exit story
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       N/A
def rm_exit(desc, rooms_arr): 
    print(desc)
    print('Temp!Exit')

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
# Returns: returns the output of the corresponding function in the dictionary
def room_encounters(c_room, desc_arr, desc_arr_index, rms_arr):
    # special room descriptions (static encounters) are checked else normal room encounters play out
    if c_room == 0:     # entrance
        return encounter_dict[c_room](desc_arr[desc_arr_index], rms_arr)
    elif c_room == 31:      # exit
        return encounter_dict[c_room](desc_arr[desc_arr_index], rms_arr)
    elif c_room == 32:      # boss
        return encounter_dict[c_room](desc_arr[-1], rms_arr)
    else:
        return encounter_dict[c_room](desc_arr[desc_arr_index], rms_arr)
