#######################################################################################################################################
# Title: Character
# Author: Tony Pescatore and Nick Pescatore
# Description: Character Class to define the player character.
#######################################################################################################################################

################################################################################
# CHECKLIST
# 
# _X_ Initialize stats on creation of character
# ___ Create Weapon slot (awaiting final weapon/damage list)
# ___ Create Armor slot (awaiting final armor type/armor list)
# ___ Create Buff slot (awaiting final buff type/buff list)
# ___ Create Debuff slot (awaiting final debuff type/debuff list)
# ___ Create small Inventory list - approx. 5 items (awaiting final item list)
# ___ Create Attack action (awaiting battle system)
# ___ Create Receive Damage action (awaiting damage system)
################################################################################

class Character:
  # Initialize basic stats of the character
  def __init__(self, name, hp = 100, weapon = 'UNARMED', damage = 5, armor_type = 'WORK  CLOTHES', armor = 5, shield_type = 'NONE', shield_armor = 0, buff_type = 'NONE', buff = 0, debuff_type = 'NONE', debuff = 0, inventory = []):
    self.name = name
    self.hp = hp
    self.weapon = weapon
    self.damage = damage
    self.armor_type =armor_type
    self.armor = armor
    self.shield_type = shield_type
    self.shield_armor = shield_armor
    self.buff_type = buff_type
    self.buff = buff
    self.debuff_type = debuff_type
    self.debuff = debuff
    self.inventory = inventory

# Defines pickup weapon action and it's effect on damage
# Parameters:   weapon_name = 
# Return:       N/A
def pickupWeapon(weapon_name):
  self.weapon = weapon_name
  # Switch statement to equip weapon and update damage amount
  match self.weapon:
    case 'UNARMED':
      damage = 5

    case 'ANCIENT SWORD':
      damage = 20

    case 'SPEAR':
      damage = 10

'''
COMMENTED TO ALLOW FOR CHARACTER CREATION TESTING

# Defines pickup armor action and it's effect on armor
def pickupArmor(armor_name):
  self.armor_type = armor_name
  # Switch statement to equip armor and update armor amount
  match self.armor_type:
    case 'NONE':
      self.armor = 0

# Defines pickup shield action and it's effect on shield
def pickupShield(shield_name):
  self.shield_type = shield_name
  # Switch statement to equip shield and update shield amount
  match self.shield_type:
    case 'NONE'
      self.shield = 0

# Defines pickup buff action and it's effects
def pickupBuff(buff_name):
  self.buff_type = buff_name
  # TO DO 
  # Switch statement to activate buff and it's effects

# TO DO
# Item functions need working Items List to fully implement.
def pickupItem(item):
  self.inventory.append(item)

def dropItem(item):
'''