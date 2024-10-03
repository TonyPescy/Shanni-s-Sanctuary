#######################################################################################################################################
# Title: Items
# Author: Tony Pescatore
# Description: All functions related to items
#######################################################################################################################################

# imports


class Weapons:
    def __init__(self, name, desc, damage, durability = 99, infusion = 'NONE'):
        self.name = name
        self.damage = damage
        self.desc = desc
        self.durability = durability
        self.infusion = infusion


    # create_weapons Starts
    # Creates all weapons that are in the game
    # Parameters:   None
    # Return:       w_list - List - Contains all weapons in the game
    def create_weapons():
        # players have access to these weapons
        anc_swd = Weapons('Ancient Sword', 'All over the sword\'s  cracked blade intricate engravings glow faintly, whirring with power', 25, 10)
        shrt_swd = Weapons('Short Sword', 'A simple straight sword, a sidearm for hundreds of years', 10, 20)
        spear = Weapons('Spear', 'A pointy stick that has proven itself on the battlefield time and time again', 20, 30)
        rapier = Weapons('Rapier', 'A gentleman\'s sword, sharp and light in the hands', 15, 20)
        grt_swd = Weapons('Greatsword', 'This heavy sword can cleave through flesh and bone like butter, though it\'s more like a hunk of iron than a sword', 30, 30)
        scrl_fb = Weapons('Scroll of Fireball', 'A lost language of strange symbols is scribbled hastily along with a simple image of a ball of fire', 30, 10, 'burn')
        scrl_arc_msl = Weapons('Scroll of Arcane Missle', 'A lost language of strange symbols is scribbled hastily along with a simple image of a small dregs of energy', 10, 40)
        # enemy only weapons below
        glm_fst = Weapons('Iron Fist', 'NONE', 20, 99, 'crusher')
        undead_grb = Weapons('Hands', 'NONE', 10)
        tongue = Weapons('Slimy Tongue', 'NONE', 5, 99, 'slime')
        stn_plr = Weapons('Stone Pillar', 'NONE', 35, 99, 'crusher')
        hrpy_claw = Weapons('Long Claws', 'NONE', 10, 99, 'serrated')
        bow = Weapons('Bow', 'NONE', 15)
        mino_hrn = Weapons('Minotaur Horn', 'NONE', 35, 99, 'gore')
        srn_claw = Weapons('Claws', 'NONE', 5)
        vmt_teeth = Weapons('Maneater Teeth', 'NONE', 15, 99, 'acid')
        hh_bite = Weapons('Jaws', 'NONE', 20, 99, 'fiery')
        brd_maw = Weapons('Maw', 'NONE', 15)
        ard_maw = Weapons('Large Maw', 'NONE', 25)
        ard_brth = Weapons('Fire Breath', 'NONE', 40, 99, 'fiery')

        w_list = [anc_swd, shrt_swd, spear, rapier, grt_swd, scrl_fb, scrl_arc_msl, glm_fst, undead_grb, tongue, stn_plr, hrpy_claw, bow, mino_hrn, srn_claw, vmt_teeth, hh_bite, brd_maw, ard_maw, ard_brth]

        return w_list
    # create_weapons Ends

class Shields:
    def __init__(self, name, desc, defence):
        self.name = name
        self.desc = desc
        self.defence = defence

    # create_shields Starts
    # Creates all shields that are in the game
    # Parameters:   None
    # Return:       s_list - List - Contains all shields in the game
    def create_shields():
        buckler = Shields('Buckler', 'A small round shield made for parrying and deflecting blows', 15)
        mag_shi = Shields('Magic Shield', 'A medium square shield made of pure energy', 30)
        sturdy_shi = Shields('Study Shield', 'A large kite shield that can cover most of your body with ease', 40)

        s_list = [buckler, mag_shi, sturdy_shi]

        return s_list
    # create_shields ends

class Armors:
    def __init__(self, name, desc, defence):
        self.name = name
        self.desc = desc
        self.defence = defence

    # create_armors Starts
    # Creates all armors that are in the game
    # Parameters:   None
    # Return:       a_list - List - Contains all armors in the game
    def create_armors():
        lght_arm = Armors('Light Armor', 'Lightweight and flexible armor made of boiled leather', 20)
        hvy_arm = Armors('Heavy Armor', 'Plates of metal to cover the whole body from head to toe, it is suprisingly lightweight and easy to move in', 40)

        a_list = [lght_arm, hvy_arm]

        return a_list
    # create_armors ends
