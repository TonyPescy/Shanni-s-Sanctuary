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

# ALL STATS SUBJECT TO CHANGE
# MORE WEAPONS/ITEMS TO BE ADDED
# BREAK WEAPONS, ARMOR, AND SHIELDS INTO THEIR OWN CLASS
# EACH WILL HOLD THEIR OWN STATS FOR EXAMPLE WEAPON WILL HAVE THE NAME AND DAMAGE

class Character:
  # Initialize basic stats of the character
  def __init__(self, name, hp = 100, weapon = 'UNARMED', damage = 5, armor_type = 'CLOTHES', armor = 5, shield_type = 'NONE', shield_armor = 0, buff_type = 'NONE', buff = 0, debuff_type = 'NONE', debuff = 0, num_of_atks = 1, inventory = []):
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
    self.num_of_atk = num_of_atks
    self.inventory = inventory

    # Defines pickup weapon action and it's effect on damage
    # Parameters:   new_weapon = string
    # Return:       N/A
    def pickup_weapon(self, new_weapon):
      
      # Switch statement to equip weapon and update damage amount
      match new_weapon:
        case 'UNARMED':
          self.damage = 5

        case 'ANCIENT SWORD':
          self.damage = 30

        case 'SPEAR':
          self.damage = 10


    # Defines pickup armor action and it's effect on armor
    # Parameters:   new_armor = string
    # Return:       N/A
    def pickup_armor(self, new_armor):
      # Switch statement to equip armor and update armor amount
      match new_armor:
        case 'NONE':
          self.armor = 0

    # Defines pickup shield action and it's effect on shield
    # Parameters:   new_shield = string
    # Return:       N/A
    def pickup_shield(self, new_shield):
      # Switch statement to equip shield and update shield amount
      match new_shield:
        case 'NONE':
          self.shield = 0

    # Defines pickup buff action and it's effects
    # Parameters:   new_buff = string
    # Return:       N/A
    def pickup_buff(self, new_buff):
      # Switch statement to activate buff and it's effects
      match new_buff:
          case 'NONE':
            self.buff = 0

    # Defines pickup buff action and it's effects
    # Parameters:   new_debuff = string
    # Return:       N/A
    def pickup_debuff(self, new_debuff):
      # Switch statement to activate buff and it's effects
      match new_debuff:
          case 'NONE':
            self.buff = 0

  '''
    # Item functions need working Items List to fully implement.
    def pickupItem(item):
      self.inventory.append(item)

    def dropItem(item):
  '''