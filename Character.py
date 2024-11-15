#######################################################################################################################################
# Title: Character
# Author: Tony Pescatore and Nick Pescatore
# Description: Character Class to define the player character.
#######################################################################################################################################

# imports
import sys
import Items as it
import random as rand

# ALL STATS SUBJECT TO CHANGE
# MORE WEAPONS/ITEMS TO BE ADDED
# BREAK WEAPONS, ARMOR, AND SHIELDS INTO THEIR OWN CLASS
# EACH WILL HOLD THEIR OWN STATS FOR EXAMPLE WEAPON WILL HAVE THE NAME AND DAMAGE

class Character:
  # Initialize basic stats of the character
  def __init__(self, name, hp = 200, weapon = 'NONE', armor = 'NONE', shield = 'NONE', inventory = [], buff = 'NONE', debuff = 'NONE', num_of_atks = 1, handicap = 0, buff_stack = 0, debuff_stack = 0, warded = False):
    self.name = name
    self.hp = hp
    self.weapon = weapon
    self.armor = armor
    self.shield = shield
    self.inventory = inventory
    self.buff = buff
    self.debuff = debuff
    self.num_of_atk = num_of_atks
    self.handicap = handicap
    self.buff_stack = buff_stack
    self.debuff_stack = debuff_stack
    self.warded = warded


  # creates the player character
  def create_player(name, w_list, a_list):
    player = Character(name, 200, w_list[0], a_list[0], 'NONE', [w_list[0], a_list[0]])
    return player


# all enemies created

  # honorable duelist
  def create_duelist(w_list, a_list, s_list):
    duelist = Character('Honorable Duelist', 100, w_list[4], a_list[1], s_list[0], [w_list[4], a_list[1], s_list[0]])
    return duelist

  # skeletons of various types
  def create_skeleton(variant, w_list, a_list, s_list, num):
    if variant == 'bow':  # skeletons using bow and arrows
      match num:
        # case for 1 skeletons appearing
        case 1:   
          skeleton = Character('Bow Skeleton', 40, w_list[13], a_list[1], 'NONE', [w_list[13], a_list[1]])
          return skeleton

        # case for 2 skeleton appearing
        case 2:
          skeleton1 = Character('Bow Skeleton 1', 30, w_list[13], a_list[1], 'NONE', [w_list[13], a_list[1]])
          skeleton2 = Character('Bow Skeleton 2', 30, w_list[13], a_list[1], 'NONE', [w_list[13], a_list[1]])
          return skeleton1, skeleton2
        
    elif variant == 'sword':
      match num:
        # case for 1 skeleton appearing
        case 1:   
          skeleton = Character('Sword Skeleton', 50, w_list[13], 'NONE', s_list[0], [w_list[13], s_list[0]])
          return skeleton

        # case for 2 skeletons appearing
        case 2:
          skeleton1 = Character('Sword Skeleton 1', 40, w_list[13], 'NONE', s_list[0], [w_list[13], s_list[0]])
          skeleton2 = Character('Sword Skeleton 2', 40, w_list[13], 'NONE', s_list[0], [w_list[13], s_list[0]])
          return skeleton1, skeleton2
        
        # case for 3 skeletons appearing
        case 3:
          skeleton1 = Character('Sword Skeleton 1', 40, w_list[13], 'NONE', s_list[0], [w_list[13], s_list[0]])
          skeleton2 = Character('Sword Skeleton 2', 40, w_list[13], 'NONE', s_list[0], [w_list[13], s_list[0]])
          skeleton3 = Character('Sword Skeleton 2', 40, w_list[13], 'NONE', s_list[0], [w_list[13], s_list[0]])
          return skeleton1, skeleton2, skeleton3
    else:
      print('Enemy Creation Error!')
      sys.exit(1) 

  # decaying ancient captain
  def create_decay_capt(w_list, s_list):
    capt = Character('Decayed Ancient Captain', 100, w_list[3], 'NONE', s_list[2], [w_list[3], s_list[2]])
    return capt
  
  # golem
  def create_golem(w_list):
    golem = Character('Stone Golem', 110, w_list[8], 'NONE', 'NONE', [w_list[8]], 'warded', 'NONE', 1, 0, 2, 0, True)
    return golem
  
  def create_mummy(w_list):
    mummy = Character('Mummy', 100, w_list[9], 'NONE', 'NONE', [w_list[9]])
    return mummy
  
  def create_cyclops(w_list, a_list):
    cyclops = Character('Cyclops', 125, w_list[11], a_list[0], 'NONE', [w_list[11], a_list[0]])
    return cyclops
  
  def create_harpies(num, w_list):
    match num:
      # 1 harpy
      case 1:
        harpy = Character('Harpy', 75, w_list[12], 'NONE', 'NONE', [w_list[12]], 'NONE', 'NONE', 2)
        return harpy
      
      # 2 harpies
      case 2:
        harpy1 = Character('Harpy 1', 55, w_list[12], 'NONE', 'NONE', [w_list[12]], 'NONE', 'NONE', 2)
        harpy2 = Character('Harpy 2', 60, w_list[12], 'NONE', 'NONE', [w_list[12]], 'NONE', 'NONE', 2)
        return harpy1, harpy2
      
      # 3 harpies
      case 3:
        harpy1 = Character('Harpy 1', 45, w_list[12], 'NONE', 'NONE', [w_list[12]], 'NONE', 'NONE', 2)
        harpy2 = Character('Harpy 2', 50, w_list[12], 'NONE', 'NONE', [w_list[12]], 'NONE', 'NONE', 2)
        harpy3 = Character('Harpy 3', 40, w_list[12], 'NONE', 'NONE', [w_list[12]], 'NONE', 'NONE', 2)
        return harpy1, harpy2, harpy3

  def create_mino(w_list):
    mino = Character('Minotaur', 130, w_list[14], 'NONE', 'NONE', [w_list[14]])
    return mino
  
  def create_siren(w_list):
    siren = Character('Siren', 150, w_list[15], 'NONE', 'NONE', [w_list[15]])
    return siren
  
  def create_vmt(w_list):
    vmt = Character('Venus Mantrap', 115, w_list[16], 'NONE', 'NONE', [w_list[14]])
    return vmt
  
  def create_pristine_capt(w_list, a_list, s_list):
    infused_anc_sword = w_list[1]
    infused_anc_sword.infusion = 'magic'
    capt = Character('Pristine Ancient Captain', 100, infused_anc_sword, a_list[2], s_list[2], [infused_anc_sword, a_list[2], s_list[2]])
    return capt
  
  def create_spellspear(w_list, a_list, s_list):
    infused_spear = w_list[3]
    infused_spear.infusion = 'magic'
    splspear = Character('Ancient Spell Spear', 100, infused_spear, a_list[1], s_list[1], [infused_spear, a_list[1], s_list[1]])
    return splspear
  
  def create_hellknight(w_list, a_list, s_list):
    hellknight = Character('Hellknight', 125, w_list[5], a_list[2], s_list[2], [w_list[5], a_list[2], s_list[2]])
    return hellknight
  
  def create_travelers(w_list, a_list):
    traveler1 = Character('Lost Traveler 1', 100, w_list[9], a_list[1], 'NONE', [w_list[9], a_list[1]])
    traveler2 = Character('Lost Traveler 2', 100, w_list[9], a_list[1], 'NONE', [w_list[9], a_list[1]])
    return traveler1, traveler2
  
  def create_mage(w_list, a_list):
    mage = Character('Forsaken Mage', 100, w_list[7], a_list[1], 'NONE', [], 'NONE', 'NONE', 2)
    return mage
  
  def create_shadow(player):
    shad_name = 'Shadow' + player.name
    shadow = Character(shad_name, 100, player.weapon, player.armor, player.shield, player.inventory, player.buff, player.debuff)
    return shadow
  
  def create_toad(w_list):
    toad = Character('Overgrown Toad', 80, w_list[10])
    return toad
  
  def create_hounds(w_list, num):
    match num:
      case 1:
        hound = Character('Hell Hound', 70, w_list[17])
        return hound
      case 2:
        hound1 = Character('Hell Hound 1', 60, w_list[17])
        hound2 = Character('Hell Hound 2', 65, w_list[17])
        return hound1, hound2
      
  def create_brd(w_list, a_list):
    brd = Character('Baby Red Dragon', 125, w_list[18], a_list[3])
    return brd
  
  def create_ard(w_list, a_list):
    ard = Character('Adult Red Dragon', 250, w_list[20], a_list[4], 'NONE', [w_list[20], w_list[19]])
    return ard