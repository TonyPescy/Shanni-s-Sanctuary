#######################################################################################################################################
# Title: Rooms
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
# Author: Tony Pescatore and Nick Pescatore
# Description: Pyramid layout
#######################################################################################################################################

# Constants
TOTRMS = 32                     # Total number or rooms including entrance and exit
# ROOMARR = [0] * TOTRMS          # List of all the rooms 0 - 31 for room pathing (0 is entrance, 31 is exit)
# for i in range(1, TOTRMS):      # Sets all room number into a list for pathing
#     ROOMARR[i] = i

class Room():

    # Initializes parts of rooms
    def __init__(self, num, eNum, exit1, exit2, exit3, exit4, exit5, exit6, exit7, exit8):
        self.num = num
        self.eNum = eNum
        self.n = exit1
        self.e = exit2
        self.s = exit3
        self.w = exit4
        self.ne = exit5
        self.se = exit6
        self.sw = exit7
        self.nw = exit8

r0 = Room(0, 0, True, False, False, False, False, False, False, False)          # Entrance room, can only go north from here into room 1