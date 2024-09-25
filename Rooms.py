#######################################################################################################################################
# Title: Rooms
# Author: Tony Pescatore and Nick Pescatore
# Description: Pyramid layout
#######################################################################################################################################

# Imports
import sys

class Room():

    # Initializes parts of rooms
    def __init__(self, num, e_num, pathing, re_entry):
        self.num = num              # Room number - Integer
        self.e_num = e_num          # List of numbers used for encounter assignment - Integer List
        self.pathing = pathing      # Pathing that will be displayed when asked for direction to go after room is completed - String List
        self.re_entry = re_entry    # Determines if room has been entered or not - False means first entry and True means second or more entries - Boolean.  Default is false as it is the first entry

    # room_creation Starts
    # Creates all rooms with their unique randomized encounter number and all the possible directions as strings
    # Parameters:   e_list - List - Unique random numbers for encounter number
    # Returns:      room_array - Array - Array of rooms
    def room_creation(e_list):

        rE = Room(0, -3, ["North"], False)                                                          # Entrance room, can only go north from here into room 1
        r1 = Room(1, e_list[1], ["North", "East", "West"], False)                                   # Room 1, can go north to Room 3, east to Room 4, or west to Room 2 - Cannot go south as entrance will close
        r2 = Room(2, e_list[2], ["North", "East", "West"], False)                                   # Room 2, can go north to Room 6, east to Room 1, or west to Room 5
        r3 = Room(3, e_list[3], ["East", "West", "Northeast", "Northwest"], False)                  # Room 3, can go east to Room 7, west to Room 6, north east to Room 12, or north west to Room 11
        r4 = Room(4, e_list[4], ["East", "West"], False)                                            # Room 4, can go east to Room 31 or west to Room 1
        r5 = Room(5, e_list[5], ["East"], False)                                                    # Room 5, can go east to Room 2
        r6 = Room(6, e_list[6], ["East", "South", "West", "Northeast", "Northwest"], False)         # Room 6, can go east to Room 3, south to Room 2, west to Room 9, north east to Room 11, or north west to Room 10
        r7 = Room(7, e_list[7], ["East", "West", "Northeast", "Northwest"], False)                  # Room 7, can go east to Room 8, west to Room 3, north east to Room 13, or north west to Room 12
        r8 = Room(8, e_list[8], ["South", "West", "Northwest"], False)                              # Room 8, can go south to Room 31, west to Room 7, or north west to Room 13
        r9 = Room(9, e_list[9], ["East", "Northeast"], False)                                       # Room 9, can go east to Room 6 or north east to Room 10
        r10 = Room(10, e_list[10], ["East", "Southeast", "Southwest"], False)                       # Room 10, can go east to Room 14, south east to Room 6, or south west to Room 9
        r11 = Room(11, e_list[11], ["North", "East", "Southeast", "Southwest"], False)              # Room 11, can go north to Room 16, east to Room 12, south east to Room 3, or south west to Room 6
        r12 = Room(12, e_list[12], ["West", "Southeast", "Southwest"], False)                       # Room 12, can go west to Room 11, south east to Room 7, or south west to Room 3
        r13 = Room(13, e_list[13], ["East", "Southeast", "Southwest"], False)                       # Room 13, can go east to Room 18, south east to Room 8, or south west to Room 7
        r14 = Room(14, e_list[14], ["North", "East", "West"], False)                                # Room 14, can go north to Room 15, east to Room 11, or west to Room 10
        r15 = Room(15, e_list[15], ["East", "South", "West", "Northeast", "Northwest"], False)      # Room 15, can go east to Room 16, south to Room 14, west to Room 20, north east to Room 22, or north west to Room 21
        r16 = Room(16, e_list[16], ["East", "South", "West", "Northeast", "Northwest"], False)      # Room 16, can go east to Room 17, south to Room 11, west to Room 15, north east to Room 23, or north west to Room 22
        r17 = Room(17, e_list[17], ["East", "South", "West", "Northeast", "Northwest"], False)      # Room 17, can go east to Room 19, south to Room 12, west to Room 16, north east to Room 25, or north west to Room 23
        r18 = Room(18, e_list[18], ["North", "West"], False)                                        # Room 18, can go north to Room 19 or west to Room 13
        r19 = Room(19, e_list[19], ["South", "West", "Northwest"], False)                           # Room 19, can go south to Room 18, west to Room 17, or north west to Room 25
        r20 = Room(20, e_list[20], ["East", "Northeast"], False)                                    # Room 20, can go east to Room 15 or north east to Room 21
        r21 = Room(21, e_list[21], ["North", "West", "Southeast", "Southwest"], False)              # Room 21, can go north to Room 29, west to Room 26, south east to Room 15, or south west to Room 20
        r22 = Room(22, e_list[22], ["North", "Southeast", "Southwest"], False)                      # Room 22, can go north to Room 27, south east to Room 16, or south west to Room 15
        r23 = Room(23, e_list[23], ["North", "Southeast", "Southeast"], False)                      # Room 23, can go north to Room 28, south east to Room 17, or south west to Room 16
        r24 = Room(24, e_list[24], ["North", "South"], False)                                       # Room 24, can go north to Room 28 or south to Room 25
        r25 = Room(25, e_list[25], ["North", "Southeast", "Southwest"], False)                      # Room 25, can go north to Room 24, south east to Room 19, or south west to Room 17
        r26 = Room(26, e_list[26], ["North", "East"], False)                                        # Room 26, can go north to Room 30 or east to Room 21
        r27 = Room(27, e_list[27], ["East", "South", "West"], False)                                # Room 27, can go east to Room 28, south to Room 22, or west to Room 29
        r28 = Room(28, e_list[28], ["East", "South", "West"], False)                                # Room 28, can go east to Room 24, south to Room 23, or west to Room 27
        r29 = Room(29, e_list[29], ["East", "South", "West"], False)                                # Room 29, can go east to Room 27, south to room 22, or west to Room 30
        r30 = Room(30, e_list[30], ["North", "East", "South"], False)                               # Room 30, can go north to Room win, east to Room 29, or south to Room 26 - Boss battle room with fixed encounter and leads to the exit room
        r31 = Room(31, -1, ["North", "West"], False)                                                # Room 31, can go north to Room 8 or west to Room 4
        rW = Room(32, -2, ["North"], False)                                                         # Room win, can go north to exit (Exit room will be handled as more of an encounter thing as of right now)
        
        room_array = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19, r20, r21, r22, r23, r24, r25, r26, r27, r28, r29, r30, rE, r31, rW]
        return room_array
    # room_creation Ends

    # room_desc_read Starts
    # Reads all room descriptions from file and adds it to a list
    # Parameters:   None
    # Returns:      rm_desc_lst - List - Has all room descriptions
    def room_desc_read():

        rm_desc_f = open("Room Descriptions.txt", "r")              # Opens file with room descriptions
        rm_desc_lst = []                                            # Creates empty list
        for line in rm_desc_f:
            line = line.replace("\n", "")                           # Removes \n from every description
            rm_desc_lst.append(line)                                # Adds room description to the list
        return rm_desc_lst
    # room_desc_read Ends

    # Get Player Move Start
    # Get Player Move - Players decide which move they want to make
    # Parameters: options - list - Has all directions player can move in
    # Returns: player_direction - string - Has players chosen direction
    def get_player_move(options):
        
        if (len(options) == 5):
            # possible_rms = [6, 15, 16, 17]  with 5 options
            while True:
                player_direction = input('Enter the direction you wish to travel in: %s, %s, %s, %s, %s? ' %(options[0], options[1], options[2], options[3], options[4])).lower()
                # checks if player entered direction is valid and breaks while loop
                if player_direction == options[0].lower() or player_direction == options[1].lower() or player_direction == options[2].lower() or player_direction == options[3].lower() or player_direction == options[4].lower():
                    break
                else:
                    # continues while loop until player enters a valid direction
                    continue
            return player_direction
        
        elif (len(options) == 4):
            # possible_rms = [3, 7, 11, 21]  with 4 options
            while True:
                player_direction = input('Enter the direction you wish to travel in: %s, %s, %s, %s? ' %(options[0], options[1], options[2], options[3])).lower()
                # checks if player entered direction is valid and breaks while loop
                if player_direction == options[0].lower() or player_direction == options[1].lower() or player_direction == options[2].lower() or player_direction == options[3].lower():
                    break
                else:
                    # continues while loop until player enters a valid direction
                    continue
            return player_direction
        
        elif (len(options) == 3):
            # possible_rms = [1, 2, 8, 10, 12, 13, 19, 22, 23, 25, 27, 28, 29, 30]  with 3 options
            while True:
                player_direction = input('Enter the direction you wish to travel in: %s, %s, %s? ' %(options[0], options[1], options[2])).lower()
                # checks if player entered direction is valid and breaks while loop
                if player_direction == options[0].lower() or player_direction == options[1].lower() or player_direction == options[2].lower():
                    break
                else:
                    # continues while loop until player enters a valid direction
                    continue
            return player_direction
        
        elif (len(options) == 2):
            # possible_rms = [4, 9, 18, 20, 24, 26, 31]  with 2 options
            while True:
                player_direction = input('Enter the direction you wish to travel in: %s, %s? ' %(options[0], options[1])).lower()
                # checks if player entered direction is valid and breaks while loop
                if player_direction == options[0].lower() or player_direction == options[1].lower():
                    break
                else:
                    # continues while loop until player enters a valid direction
                    continue
            return player_direction
        
        else:
            # possible_rms = [0, 5, 32] with only 1 option
            while True:
                player_direction = input('Enter the direction you wish to travel in: %s? ' %(options[0])).lower()
                # checks if player entered direction is valid and breaks while loop
                if player_direction == options[0].lower():
                    break
                else:
                    # continues while loop until player enters a valid direction
                    continue
            return player_direction
        
    # Player Move End

# Cases for each room in game and what to do with dictionary lookup
# each function will return the new room number based on direction inputted
    def rm_0(dir):       # only 1 direction to go from here, takes you to room 1
        if dir == 'north':
            return 1
        else:
            print('Pathing Error!')
            sys.exit()

    def rm_1(dir): 
        if dir == 'north':      # north takes you to room 3
            return 3
        elif dir == 'east':     # east takes you to room 4
            return 4
        elif dir == 'west':     # west takes you to room 2
            return 2
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_2(dir): 
        if dir == 'north':      # north takes you to room 6
            return 6
        elif dir == 'east':     # east takes you to room 1
            return 1
        elif dir == 'west':     # west takes you to room 5
            return 5
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_3(dir): 
        if dir == 'northeast':      # northeast takes you to room 12
            return 12
        elif dir == 'northwest':      # northwest takes you to room 11
            return 11
        elif dir == 'east':     # east takes you to room 7
            return 7
        elif dir == 'west':     # west takes you to room 6
            return 6
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_4(dir):
        if dir == 'east':     # east takes you to room 31
            return 31
        elif dir == 'west':     # west takes you to room 1
            return 1
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_5(dir): 
        if dir == 'east':      # east takes you to room 2
            return 2
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_6(dir): 
        if dir == 'northeast':      # northeast takes you to room 11
            return 11
        elif dir == 'northwest':      # northwest takes you to room 10
            return 10
        elif dir == 'east':     # east takes you to room 3
            return 3
        elif dir == 'west':     # west takes you to room 9
            return 9
        elif dir == 'south':    # south takes you to room 2
            return 2
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_7(dir): 
        if dir == 'northeast':      # northeast takes you to room 13
            return 13
        elif dir == 'northwest':      # northwest takes you to room 12
            return 12
        elif dir == 'east':     # east takes you to room 8
            return 8
        elif dir == 'west':     # west takes you to room 3
            return 3
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_8(dir): 
        if dir == 'northwest':      # northwest takes you to room 13
            return 13
        elif dir == 'west':     # west takes you to room 7
            return 7
        elif dir == 'south':    # south takes you to room 31
            return 31
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_9(dir): 
        if dir == 'northeast':      # northeast takes you to room 10
            return 10
        elif dir == 'east':     # east takes you to room 6
            return 6
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_10(dir): 
        if dir == 'southeast':      # southeast takes you to room 6
            return 6
        elif dir == 'southwest':      # southwest takes you to room 9
            return 9
        elif dir == 'east':     # east takes you to room 14
            return 14
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_11(dir): 
        if dir == 'north':      # north takes you to room 16
            return 11
        elif dir == 'southwest':      # southwest takes you to room 6
            return 6
        elif dir == 'east':     # east takes you to room 12
            return 12
        elif dir == 'southeast':    # southeast takes you to room 26
            return 6
        else:
            print('Pathing Error!')
            sys.exit(1)
            
    def rm_12(dir): 
        if dir == 'southeast':      # southeast takes you to room 7
            return 7
        elif dir == 'southwest':      # southwest takes you to room 3
            return 3
        elif dir == 'west':     # west takes you to room 11
            return 11
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_13(dir): 
        if dir == 'southeast':      # southeast takes you to room 8
            return 8
        elif dir == 'east':     # east takes you to room 18
            return 18
        elif dir == 'southwest':    # southwest takes you to room 7
            return 7
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_14(dir): 
        if dir == 'north':      # north takes you to room 15
            return 15
        elif dir == 'east':     # east takes you to room 11
            return 11
        elif dir == 'west':     # west takes you to room 10
            return 10
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_15(dir): # START HERE TOMORROW
        if dir == 'northeast':      # northeast takes you to room 11
            return 11
        elif dir == 'northwest':      # northwest takes you to room 10
            return 10
        elif dir == 'east':     # east takes you to room 3
            return 3
        elif dir == 'west':     # west takes you to room 9
            return 9
        elif dir == 'south':    # south takes you to room 2
            return 2
        else:
            print('Pathing Error!')
            sys.exit(1)

    def rm_16(dir): 
        print('16!')
    def rm_17(dir): 
        print('17!')
    def rm_18(dir): 
        print('18!')
    def rm_19(dir): 
        print('19!')
    def rm_20(dir): 
        print('20!')
    def rm_21(dir): 
        print('21!')
    def rm_22(dir): 
        print('22!')
    def rm_23(dir): 
        print('23!')
    def rm_24(dir): 
        print('24!')
    def rm_25(dir): 
        print('25!')
    def rm_26(dir): 
        print('26!')
    def rm_27(dir): 
        print('27!')
    def rm_28(dir): 
        print('28!')
    def rm_29(dir): 
        print('29!')

    def rm_30(dir): 
        print('30!')

    def rm_boss(dir): 
        print('TEMP!BOSS')
    def rm_exit(dir): 
        print('Temp!Ex')

    # Dictionary to map rooms to proper room function
    room_dict = {
        0: rm_0, 1: rm_1, 2: rm_2, 3: rm_3, 4: rm_4, 5: rm_5, 6: rm_6, 7: rm_7, 8: rm_8, 9: rm_9, 10: rm_10, 
        11: rm_11, 12: rm_12, 13: rm_13, 14: rm_14, 15: rm_15, 16: rm_16, 17: rm_17, 18: rm_18, 19: rm_19, 20: rm_20, 
        21: rm_21, 22: rm_22, 23: rm_23, 24: rm_24, 25: rm_25, 26: rm_26, 27: rm_27, 28: rm_28, 29: rm_29, 30: rm_30, 
        31: rm_boss, 32: rm_exit
    }

    # room_move to lookup and execute the function based on players new room
    # room_move - Moves players into the next room
    # Parameters:   dict - dictionary - Has dictionary of all functions used to move to every room
    #               c_room - int - Current room the player is in
    #               dir - int - direction player is moving
    # Returns: returns the output of the corresponding function in the dictionary
    def room_move(dict, c_room, dir):
        return dict[c_room](dir)

    # next_room - Moves players into the next room
    # Parameters:   direction - string - Has players chosen direction
    #               curr_room - int - Current room the player is in
    # Returns: N/A
    def next_room(direction, curr_room):
        return Room.room_move(Room.room_dict, curr_room, direction)
    
    # reentry_switch - flips reentry bool on Room object to true once a room has been entered
    # Parameters:   N/A
    # Returns: N/A
    def reentry_switch():
        return True