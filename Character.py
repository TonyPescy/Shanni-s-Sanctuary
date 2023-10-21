#######################################################################################################################################
# Title: Shanni's Sanctuary
# Date Started: 2/22/2022 dropped after 2/25/2022, picked again on 10/21/23
# Date Completed: TBD
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
  def _init_(self, hp, weapon, damage. armor_type, armor, shield_type, shield, buff_type, buff, debuff_type, debuff, inventory):
    self.hp = 100
    self.weapon = 'UNARMED'
    self.damage = 5
    self.armor_type = 'NONE'
    self.armor = 0
    self.shield_type = 'NONE'
    self.buff_type = 'NONE'
    self.buff = 0
    self.debuff_type = 'NONE'
    self.debuff = 0
    self.inventory = []

# Defines pickup weapon action and it's effect on damage
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

# Defines pickup armor action and it's effect on armor
def pickupArmor(armor_name):
  self.armor_type = armor_name
  # Switch statement to equip armor and update armor amount
  match self.armor_type:
    case 'NONE'
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
