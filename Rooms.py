#######################################################################################################################################
# Title: Rooms
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
# Author: Tony Pescatore and Nick Pescatore
# Description: Pyramid layout
#######################################################################################################################################

class Room():

    # Initializes parts of rooms
    def __init__(self, num, eNum, exit1, exit2, exit3, exit4, exit5, exit6, exit7, exit8):
        self.num = num          # Room number
        self.eNum = eNum        # List of numbers used for encounter assignment
        self.n = exit1          # North
        self.e = exit2          # East 
        self.s = exit3          # South
        self.w = exit4          # West
        self.ne = exit5         # North East
        self.se = exit6         # South East
        self.sw = exit7         # South West
        self.nw = exit8         # North West

    # Room Creation Starts
    # Creates all rooms with their unique randomized encounter number and all the possible directions as booleans
    # Parameters:   eList = list of unique random numbers for encounter number
    # Returns:      N/A
    def roomCreation(eList):
        rE = Room(0, -1, True, False, False, False, False, False, False, False)              # Entrance room, can only go north from here into room 1
        r1 = Room(1, eList[1], True, True, False, True, False, False, False, False)         # Room 1, can go north to Room 3, east to Room 4, or west to Room 2 - Cannot go south as entrance will close
        r2 = Room(2, eList[2], True, True, False, True, False, False, False, False)         # Room 2, can go north to Room 6, east to Room 1, or west to Room 5
        r3 = Room(3, eList[3], False, True, True, True, True, False, False, True)           # Room 3, can go east to Room 7, west to Room 6, north east to Room 12, or north west to Room 11
        r4 = Room(4, eList[4], False, True, False, True, False, False, False, False)        # Room 4, can go east to Room 31 or west to Room 1
        r5 = Room(5, eList[5], False, True, False, False, False, False, False, False)       # Room 5, can go east to Room 2
        r6 = Room(6, eList[6], False, True, True, True, True, False, False, True)           # Room 6, can go east to Room 3, south to Room 2, west to Room 9, north east to Room 11, or north west to Room 10
        r7 = Room(7, eList[7], False, True, False, True, True, False, False, True)          # Room 7, can go east to Room 8, west to Room 3, north east to Room 13, or north west to Room 12
        r8 = Room(8, eList[8], False, False, True, True, False, False, False, True)         # Room 8, can go south to Room 31, west to Room 7, or north west to Room 13
        r9 = Room(9, eList[9], False, True, False, False, True, False, False, False)        # Room 9, can go east to Room 6 or north east to Room 10
        r10 = Room(10, eList[10], False, True, False, False, False, True, True, False)      # Room 10, can go east to Room 14, south east to Room 6, or south west to Room 9
        r11 = Room(11, eList[11], True, True, False, True, False, True, True, False)        # Room 11, can go north to Room 16, east to Room 12, wouth east to Room 3, or south west to Room 6
        r12 = Room(12, eList[12], True, False, False, True, False, True, True, False)       # Room 12, can go west to Room 11, south east to Room 7, or south west to Room 3
        r13 = Room(13, eList[13], True, False, False, False, False, False, False, False)
        r14 = Room(14, eList[14], True, False, False, False, False, False, False, False)
        r15 = Room(15, eList[15], True, False, False, False, False, False, False, False)
        r16 = Room(16, eList[16], True, False, False, False, False, False, False, False)
        r17 = Room(17, eList[17], True, False, False, False, False, False, False, False)
        r18 = Room(18, eList[18], True, False, False, False, False, False, False, False)
        r19 = Room(19, eList[19], True, False, False, False, False, False, False, False)
        r20 = Room(20, eList[20], True, False, False, False, False, False, False, False)
        r21 = Room(21, eList[21], True, False, False, False, False, False, False, False)
        r22 = Room(22, eList[22], True, False, False, False, False, False, False, False)
        r23 = Room(23, eList[23], True, False, False, False, False, False, False, False)
        r24 = Room(24, eList[24], True, False, False, False, False, False, False, False)
        r25 = Room(25, eList[25], True, False, False, False, False, False, False, False)
        r26 = Room(26, eList[26], True, False, False, False, False, False, False, False)
        r27 = Room(27, eList[27], True, False, False, False, False, False, False, False)
        r28 = Room(28, eList[28], True, False, False, False, False, False, False, False)
        r29 = Room(29, eList[29], True, False, False, False, False, False, False, False)
        r30 = Room(30, eList[30], True, False, False, False, False, False, False, False)
        r31 = Room(31, eList[31], True, False, False, False, False, False, False, False)
        rW = Room(-1, -2, True, False, False, False, False, False, False, False)
        # Room Creation Ends