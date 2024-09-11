#######################################################################################################################################
# Title: Library
# Author: Tony Pescatore
# Description: Holds functions to be used in other classes
#######################################################################################################################################

# imports
import sys

# Uses binary search to search through an ordered array
# Parameters:   arr = ordered array
#               tar = target in array
# Return:       N/A
def bin_search(arr, tar):

    low = 0
    high = (len(arr) - 1)
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # ignore left half if target is greater
        if arr[mid] < tar:
            low = mid + 1

        # ignore right half if target is smaller
        if arr[mid] < tar:
            high = mid - 1

        # when target is found at mid
        else:
            return mid
        
    # target was not found, fatal error for game
    print('Error finding room')
    sys.exit(1)