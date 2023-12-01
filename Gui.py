#######################################################################################################################################
# Title: Gui
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
# Author: Tony Pescatore and Nick Pescatore
# Description: Simple Gui for the game
#######################################################################################################################################

# MAYBE ADD CONFIRMATION FUNCTION WINDOW WHEN X IS CLICKED | X |
# Gui layout needed for all room types with 1-8 choices    | o |
#       > Get info from Rooms.py
#           - List for all button names (North, East, West, etc)    List format
#           - Room Description and Encounter Description too
#           - Encounters should use same gui for every type (Combat, Riddle?, Status floor, Trap, Empty)

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
        event_Con = con_wind.read()
        if event_Con == sg.WIN_CLOSED:       # User did not confirm closure of program
            ex = False
            break
        if event_Con == "Yes":               # User selecter yes
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
        event_U, values_U = username_wind.read()
        if event_U == sg.WIN_CLOSED:                             # If user closes window
            if confirm_exit() == True:                          # User means to exit program if true
                sys.exit("Exited using the X button")
            else:                                               # User did not mean to exit program
                username_gui()                                  # Restarts the original function
                break
        if event_U == "Enter":                                   # User inputs name
            name = str(values_U[0])
            name = name[0].upper() + name[1:].lower()     # Gets name and makes it look nice
            break

    username_wind.close()     # Closes window
    return name
# intro_gui Ends

# intro_gui Starts
# Creates introduction encounters
# Parameters:   name - String - Users name
# Returns:      N/A 
def intro_gui(name):
    # intro gui layouts
    intro_lay_i = [     [sg.Text(name +", do you wish to enter Shanni's Sanctuary?")],
                        [sg.Button("Yes", bind_return_key = True), sg.Button("No")]
    ]
    intro_lay_no = [    [sg.Text("No?  Shanni is disappointed with your cowardice, but acknoledges your intellect.  She shall let you live and return to your life, as that is more hellish than what lies within.")],
                        [sg.Text("You turn away slowly as the invisble weight appears to be lifted from your shoulders.  As you begin away from the sanctuary you take one last look at its devilish stone before it is blown into dust by the wind.")],
                        [sg.Button("Exit", bind_return_key = True)]
    ]
    intro_lay_yes = [   [sg.Text("Yes?  Shanni is delighted with your stupidity, it's not everyday she gets a sacrifice so eager.  Please enter.")],
                        [sg.Text("The weight one your shoulders grows heavier as you walk into the black abyss beyond the door.")],
                        [sg.Text("Welcome to Shanni's Sanctuary " + name + ", good luck in there, you'll need it.")],
                        [sg.Button("Enter", bind_return_key = True)]
    ]
    
    # intro_gui_i Starts
    # Creates introduction encounters
    # Parameters:   N/A
    # Returns:      dec - Boolean - True means yes and False means no 
    def intro_gui_i():
        # intro start
        wind = sg.Window("Shanni's Sanctuary", intro_lay_i, use_custom_titlebar = True)   # Uses layout for the very start of the intro

        # User inputs
        while True:
            event_li = wind.read()
        
            if event_li == sg.WIN_CLOSED:                               # If user closes window
                if confirm_exit() == True:                              # User means to exit program if true
                    sys.exit("Exited using the X button")
                else:                                                   # User did not mean to exit program
                    intro_gui_i()                                       # Restarts the nested function from beginning
                    break
            if event_li == "Yes":                                       # User wishes to enter 
                    dec = True
                    break
            else:                                                       # User does not wish to enter 
                dec = False
                break
        wind.close()
        return dec
    # intro_gui_i Ends

    # intro_gui_dec Starts
    # Continues intro if user says yes
    # Parameters:   dec - Boolean - True means yes and False means no
    # Returns:      N/A
    def intro_gui_dec(dec):
        # Part 2 of intro

        # If user says yes to entering
        if dec == True:
            wind_t = sg.Window("Shanni's Sanctuary", intro_lay_yes, use_custom_titlebar = True)   # Uses layout for if the user said yes

            while True:
                event_t = wind_t.read()

                if event_t == sg.WIN_CLOSED:                                # If user closes window
                    if confirm_exit() == True:                              # User means to exit program if true
                        sys.exit("Exited using the X button")
                    else:                                                   # User did not mean to exit program
                        intro_gui_dec(dec)                                     # Restarts the nested function from beginning
                        break
                if event_t == "Enter":
                    print("YOU ENTERED THE SANCTUARY, GAME WILL START NOW")
                    wind_t.close()

        # If user said they wanted to leave and not enter
        if dec == False:
            wind_f = sg.Window("Shanni's Sanctuary", intro_lay_no, use_custom_titlebar = True)   # Uses layout for if the user said yes

            while True:
                event_f = wind_f.read()

                if event_f == sg.WIN_CLOSED:                                # If user closes window
                    if confirm_exit() == True:                              # User means to exit program if true
                        sys.exit("Exited using the X button")
                    else:                                                   # User did not mean to exit program
                        intro_gui_dec(dec)                                     # Restarts the nested function from beginning
                        break
                if event_f == "Exit":
                    sys.exit("Exited using the X button")
    # intro_gui_dec Ends

    # continue intro_gui function using local ones above
    dec = intro_gui_i()

    intro_gui_dec(dec)
# intro_gui Ends