#######################################################################################################################################
# Title: Gui
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
# Author: Tony Pescatore and Nick Pescatore
# Description: Simple Gui for the game
#######################################################################################################################################

# MAYBE ADD CONFIRMATION FUNCTION WINDOW WHEN X IS CLICKED
# 

# Imports
import PySimpleGUI as sg
import sys

# Themes
sg.theme("SystemDefault1")

# confirm_exit Starts
# confirms if user wants to exit
# Parameters:   N/A
# Returns:      ex - Boolean - States if user wants to exit or not 
def confirm_exit():
    # confirm_exit layout
    confirm_layout = [  [sg.Text("Do you wish to exit?")],
                        [sg.Button("Yes", bind_return_key = True), sg.Button("No")]
    ]

    # Window for confirm_exit
    con_wind = sg.Window("Exit Confirmation", confirm_layout, use_custom_titlebar = True)

    # User input
    while True:
        eventCon, valuesU = con_wind.read()
        if eventCon == sg.WIN_CLOSED:       # User did not confirm closure of program
            ex = False
            break
        if eventCon == "Yes":               # User selecter yes
            ex = True
            break
        else:                               # User selected no
            ex = False      
            break

    con_wind.close()
    return ex 
# confirm_exit Ends

# username_gui Starts
# Creates layouts + gui for user name entering
# Parameters:   N/A
# Returns:      name - String - Users name
def username_gui():
    # Username gui layout
    username_layout = [ [sg.Text("The voice within asks:  What is your name? ")],
                        [sg.InputText()],
                        [sg.Button("Enter", bind_return_key = True)]
    ]

    # Window for username gui
    username_wind = sg.Window("Shanni's Sanctuary", username_layout, use_custom_titlebar = True)

    # Get user input
    while True:
        eventU, valuesU = username_wind.read()
        if eventU == sg.WIN_CLOSED:                             # If user closes window
            if confirm_exit() == True:                          # User means to exit program if true
                sys.exit("Exited using the X button")
            else:                                               # User did not mean to exit program
                username_gui()                                  # Restarts the original function
                break
        if eventU == "Enter":                                   # User inputs name
            name = str(valuesU[0])
            name = name[0].upper() + name[1:].lower()     # Gets name and makes it look nice
            break

    username_wind.close()     # Closes window
    return name
# intro_gui Ends

# intro_gui Starts
# Creates layouts + gui for intro
# Parameters:   N/A
# Returns:      