#######################################################################################################################################
# Title: Encounter
# Author: Tony Pescatore and Nick Pescatore
# Description: All encounter descriptions and encounter interactions
#######################################################################################################################################

# imports
import sys
import Rooms as rm

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
    answer = str(input(name + ", do you wish to enter Shanni's Sanctuary?  Yes or no? "))
    answer = answer.lower()
    if (answer != 'yes' or answer != 'no'):
        input
    return name, answer
# Username Ends

# Entrance Starts
# Entrance encounter - For going into the sanctuary
# Parameters:   name = players name
# Return:       N/A
def entrance(name, answer):         # Entrance to the sanctuary, this decides if user wishes to play the game or not
    if answer == "no":      # If user says no
        print("No?  Shanni is disappointed with your cowardice, but acknowledges your intellect.  She shall let you live and return to your life, as that is more hellish than what lies within.")
        print("You turn away slowly as the invisble weight appears to be lifted from your shoulders.  As you begin away from the sanctuary you take one last look at its devilish stone before it is blown into dust by the wind.")
        sys.exit(1)
    elif answer == "yes":   # If user says yes
        print("Yes?  Shanni is delighted with your stupidity, it's not everyday she gets a sacrifice so eager.  Please enter.")
        print("The weight one your shoulders grows heavier as you walk into the black abyss beyond the door.")
        print("Welcome to Shanni's Sanctuary " + name + ", good luck in there, you'll need it.")
    else:                   # If no proper answer is given, program tries again
        answer = input("Enter yes or no ")
        entrance(name, answer)
# Entrance Ends

# Introduction Starts
# Introduction encounter - For finding the sanctuary
# Parameters:   None
# Return:       N/A
def intro():            # Intro to the game 
    temp = 0        # temp for while loop to ensure yes or no is provided
    print("You are walking down the side walk of the city you've spent your entire life in, during that time nothing much has changed.  It was always a small city, but now that you've grown up it seems to have gotten smaller and much duller.  You know every inch of this city like the back of your hand, you could walk the streets blindfolded and make it to work on time.  However today was odd, a peculiar weight was on you shoulders, maybe work was getting to you?  But that can't be making you feel this way can it?.")
    answer = str(input("That's when something catches your eye, something you never saw before.  A large overgrown pyramid in the center of the street, how have you never noticed this before?  A voice speaks to you, it comes from within your own mind, it's beckoning you forth.  Come closer it says, egging you on and on.  Do you listen to what the voice says?  Yes or no? ").lower())
    while temp == 0:
        if answer.lower() == "no":
            print("Your body does not listen to you, instead it does the opposite and begins towards the massive black pyramid.")
            temp = 1
        elif answer.lower() == "yes":
            print("Your begin towards the massive black pyramid, unaware of the implications it will have for your future... or if there will be one to come back to. ")
            temp = 1
        else:               # If no proper answer is given, program tries again
            answer = input("Enter yes or no ")
            
# Introduction Ends

# random encounters start
# Cases for each room in game and what to do with dictionary lookup
# each function will return the new room number based on direction inputted

# rm_entrance Starts
# rm_entrance - First encounter within the actual pyramid
# Parameters:   desc - string - description of the room
#               rooms_arr - array - array of all rooms
# Return:       N/A
def rm_entrance(desc, rooms_arr):
    print(desc)
    next_direction = rm.Room.get_player_move(rooms_arr[-3].pathing)     # gets player input on what direction they would like to go
    new_room = rm.Room.next_room(next_direction, rooms_arr[-3].num)     # gets new room that player has selected
    print('As you you make your way north, those heavy wooden doors slam shut. Another barrier to ensure you do not escape Shanni\'s Sanctuary.')
    
    return rooms_arr, new_room
# room_entrance ends

def rm_1(desc, rooms_arr): 
    print('Temp!')
def rm_2(desc, rooms_arr): 
    print('Temp!')
def rm_3(desc, rooms_arr): 
    print('Temp!')
def rm_4(desc, rooms_arr): 
    print('Temp!')
def rm_5(desc, rooms_arr): 
    print('Temp!')
def rm_6(desc, rooms_arr): 
    print('Temp!')
def rm_7(desc, rooms_arr): 
    print('Temp!')
def rm_8(desc, rooms_arr): 
    print('Temp!')
def rm_9(desc, rooms_arr): 
    print('Temp!')
def rm_10(desc, rooms_arr): 
    print('Temp!')
def rm_11(desc, rooms_arr): 
    print('Temp!')
def rm_12(desc, rooms_arr): 
    print('Temp!')
def rm_13(desc, rooms_arr): 
    print('Temp!')
def rm_14(desc, rooms_arr): 
    print('Temp!')
def rm_15(desc, rooms_arr): 
    print('Temp!')
def rm_16(desc, rooms_arr): 
    print('Temp!')
def rm_17(desc, rooms_arr): 
    print('Temp!')
def rm_18(desc, rooms_arr): 
    print('Temp!')
def rm_19(desc, rooms_arr): 
    print('Temp!')
def rm_20(desc, rooms_arr): 
    print('Temp!')
def rm_21(desc, rooms_arr): 
    print('Temp!')
def rm_22(desc, rooms_arr): 
    print('Temp!')
def rm_23(desc, rooms_arr): 
    print('Temp!')
def rm_24(desc, rooms_arr): 
    print('Temp!')
def rm_25(desc, rooms_arr): 
    print('Temp!')
def rm_26(desc, rooms_arr): 
    print('Temp!')
def rm_27(desc, rooms_arr): 
    print('Temp!')
def rm_28(desc, rooms_arr): 
    print('Temp!')
def rm_29(desc, rooms_arr): 
    print('Temp!')
def rm_30(desc, rooms_arr): 
    print('Temp!')
def rm_boss(desc, rooms_arr): 
    print('TEMP!BOSS')
def rm_exit(desc, rooms_arr): 
    print('Temp!Ex')

encounter_dict = {
    0: rm_entrance, 1: rm_1, 2: rm_2, 3: rm_3, 4: rm_4, 5: rm_5, 6: rm_6, 7: rm_7, 8: rm_8, 9: rm_9, 10: rm_10, 
    11: rm_11, 12: rm_12, 13: rm_13, 14: rm_14, 15: rm_15, 16: rm_16, 17: rm_17, 18: rm_18, 19: rm_19, 20: rm_20, 
    21: rm_21, 22: rm_22, 23: rm_23, 24: rm_24, 25: rm_25, 26: rm_26, 27: rm_27, 28: rm_28, 29: rm_29, 30: rm_30, 
    31: rm_boss, 32: rm_exit
}

# room_encounters to lookup and execute the function based on players room
# room_encounters - selects room encounter to play out according to the player current room
# Parameters:   dict - dictionary - Has dictionary of all functions used to run encounter of every room
#               c_room - int - Current room the player is in
#               desc_arr - array - Array of all room descriptions
#               desc_arr_index - int - Index for current room 
#               rmms_arr - array - Array of all room objects
# Returns: returns the output of the corresponding function in the dictionary
def room_encounters(c_room, desc_arr, rms_arr):
    # special room descriptions (static encounters) are checked else normal room encounters play out
    if c_room == 0:
        return encounter_dict[c_room](desc_arr[-3], rms_arr)
    elif c_room == 31:
        return encounter_dict[c_room](desc_arr[-2], rms_arr)
    elif c_room == 32:
        return encounter_dict[c_room](desc_arr[-1], rms_arr)
    else:
        return encounter_dict[c_room](desc_arr[c_room], rms_arr)
