#######################################################################################################################################
# Title: Items
# Author: Tony Pescatore
# Description: All functions related to items
#######################################################################################################################################

# imports


class Weapons:
    def __init__(self, name, description, damage, durability = 99, infusion = 'NONE'):
        self.name = name
        self.damage = damage
        self.description = description
        self.durability = durability
        self.infusion = infusion


# create_weapons Starts
# Creates all weapons that can be used in the game
# Parameters:   None
# Return:       w_list - List - Contains all weapons in the game
def create_weapons():
    # players have access to these weapons
    anc_swd = Weapons('Ancient Sword', 'TEMP DESC', 25, 10)
    shrt_swd = Weapons('Short Sword', 'TEMP', 10, 20)
    spear = Weapons('Spear', 'TEMP', 20, 30)
    rapier = Weapons('Rapier', 'TEMP', 15, 20)
    grt_swd = Weapons('Greatsword', 'TEMP', 30, 30)
    scrl_fb = Weapons('Scroll of Fireball', 'TEMP', 30, 10, 'burn')
    scrl_arc_msl = Weapons('Scroll of Arcane Missle', 'TEMP', 10, 40)
    # enemy only weapons below
    glm_fst = Weapons('Golem Fist', 'TEMP', 20, 99, 'crusher')
    undead_grb = Weapons('Grab', 'TEMP', 10)
    tongue = Weapons('Slimy Tongue', 'TEMP', 5, 99, 'slime')
    stn_plr = Weapons('Stone Pillar', 'TEMP', 35, 99, 'crusher')
    hrpy_claw = Weapons('Harpy Claws', 'TEMP', 10, 99, 'lacerate')
    bow = Weapons('Bow', 'TEMP', 15)
    mino_hrn = Weapons('Minotaur Horn', 'TEMP', 35, 99, 'gore')
    