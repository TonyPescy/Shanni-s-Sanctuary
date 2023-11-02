#######################################################################################################################################
# Title: Rooms
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
# Author: Tony Pescatore and Nick Pescatore
# Description: Pyramid layout
#######################################################################################################################################

# Imports
# import random

# Constants
ENTRANCE_D_NUM = 0


class Room():

    # Initializes parts of rooms
    def __init__(self, num, e_num, pathing, desc_num, re_entry):
        self.num = num              # Room number - Integer
        self.e_num = e_num          # List of numbers used for encounter assignment - Integer
        self.pathing = pathing      # Pathing that will be displayed when asked for direction to go after room is completed - String
        self.desc_num = desc_num    # Number that determines what the room will be described as - Integer
        self.re_entry = False       # Determines if room has been entered or not - False means first entry and True means second or more entries - Boolean

    # room_creation Starts
    # Creates all rooms with their unique randomized encounter number and all the possible directions as strings
    # Parameters:   e_list = List of unique random numbers for encounter number
    #               d_list = List of all room descriptions
    # Returns:      N/A
    def room_creation(e_list, d_list):
        # random.seed(420)        # Hahaha funni number, for testing
        # rm_desc_lst_nums = list(random.sample(range(50), 31))                             # Generates random room descriptions for all rooms, excludes special rooms with constant room descriptions

        rE = Room(0, -1, "North", )                                                 # Entrance room, can only go north from here into room 1
        r1 = Room(1, e_list[1], "North, East, or West")                              # Room 1, can go north to Room 3, east to Room 4, or west to Room 2 - Cannot go south as entrance will close
        r2 = Room(2, e_list[2], "North, East, or West")                              # Room 2, can go north to Room 6, east to Room 1, or west to Room 5
        r3 = Room(3, e_list[3], "East, West, Northeast, or Northwest")               # Room 3, can go east to Room 7, west to Room 6, north east to Room 12, or north west to Room 11
        r4 = Room(4, e_list[4], "East or West")                                      # Room 4, can go east to Room 31 or west to Room 1
        r5 = Room(5, e_list[5], "East")                                              # Room 5, can go east to Room 2
        r6 = Room(6, e_list[6], "East, South, West, Northeast, or Northwest")        # Room 6, can go east to Room 3, south to Room 2, west to Room 9, north east to Room 11, or north west to Room 10
        r7 = Room(7, e_list[7], "East, West, Northeast, or Northwest")               # Room 7, can go east to Room 8, west to Room 3, north east to Room 13, or north west to Room 12
        r8 = Room(8, e_list[8], "South, West, or Northwest")                         # Room 8, can go south to Room 31, west to Room 7, or north west to Room 13
        r9 = Room(9, e_list[9], "East or Northeast")                                 # Room 9, can go east to Room 6 or north east to Room 10
        r10 = Room(10, e_list[10], "East, Southeast, or Southwest")                  # Room 10, can go east to Room 14, south east to Room 6, or south west to Room 9
        r11 = Room(11, e_list[11], "North, East, Southeast, or Southwest")           # Room 11, can go north to Room 16, east to Room 12, south east to Room 3, or south west to Room 6
        r12 = Room(12, e_list[12], "West, Southeast, or Southwest")                  # Room 12, can go west to Room 11, south east to Room 7, or south west to Room 3
        r13 = Room(13, e_list[13], "East, Southeast, or Southwest")                  # Room 13, can go east to Room 18, south east to Room 8, or south west to Room 7
        r14 = Room(14, e_list[14], "North, East, or West")                           # Room 14, can go north to Room 15, east to Room 11, or west to Room 10
        r15 = Room(15, e_list[15], "East, South, West, Northeast, or Northwest")     # Room 15, can go east to Room 16, south to Room 14, west to Room 20, north east to Room 22, or north west to Room 21
        r16 = Room(16, e_list[16], "East, South, West, Northeast, or Northwest")     # Room 16, can go east to Room 17, south to Room 11, west to Room 15, north east to Room 23, or north west to Room 22
        r17 = Room(17, e_list[17], "East, South, West, Northeast, or Northwest")     # Room 17, can go east to Room 19, south to Room 12, west to Room 16, north east to Room 25, or north west to Room 23
        r18 = Room(18, e_list[18], "North or West")                                  # Room 18, can go north to Room 19 or west to Room 13
        r19 = Room(19, e_list[19], "South, West, or Northwest")                      # Room 19, can go south to Room 18, west to Room 17, or north west to Room 25
        r20 = Room(20, e_list[20], "East or Northeast")                              # Room 20, can go east to Room 15 or north east to Room 21
        r21 = Room(21, e_list[21], "North, West, Southeast, or Southwest")           # Room 21, can go north to Room 29, west to Room 26, south east to Room 15, or south west to Room 20
        r22 = Room(22, e_list[22], "North, Southeast, or Southwest")                 # Room 22, can go north to Room 27, south east to Room 16, or south west to Room 15
        r23 = Room(23, e_list[23], "North, Southeast, or Southeast")                 # Room 23, can go north to Room 28, south east to Room 17, or south west to Room 16
        r24 = Room(24, e_list[24], "North or South")                                 # Room 24, can go north to Room 28 or south to Room 25
        r25 = Room(25, e_list[25], "North, Southeast, or Southwest")                 # Room 25, can go north to Room 24, south east to Room 19, or south west to Room 17
        r26 = Room(26, e_list[26], "North or East")                                  # Room 26, can go north to Room 30 or east to Room 21
        r27 = Room(27, e_list[27], "East, South, or West")                           # Room 27, can go east to Room 28, south to Room 22, or west to Room 29
        r28 = Room(28, e_list[28], "East, South, or West")                           # Room 28, can go east to Room 24, south to Room 23, or west to Room 27
        r29 = Room(29, e_list[29], "East, South, or West")                           # Room 29, can go east to Room 27, south to room 22, or west to Room 30
        r30 = Room(30, e_list[30], "North, East, or South")                          # Room 30, can go north to Room win, east to Room 29, or south to Room 26 - Boss battle room with fixed encounter and leads to the exit room
        r31 = Room(31, e_list[31], "North or West")                                  # Room 31, can go north to Room 8 or west to Room 4
        rW = Room(-1, -2, "North")                                                   # Room win, can go north to exit (Exit room will be handled as more of an encounter thing as of right now)
    # room_creation Ends

    # room_desc_read Starts
    # Reads all room descriptions from file and adds it to a list
    # Parameters:   None
    # Returns:      rm_desc_lst - List - Has all room descriptions
    def room_desc_read():
        rm_desc_f = open("Room Descriptions.txt", "r")  # Opens file with room descriptions
        rm_desc_lst = []                                # Creates empty list
        for line in rm_desc_f:
            line = line.replace("\n", "")               # Removes \n from every description
            rm_desc_lst.append(line)
        return rm_desc_lst
    # room_desc_read Ends