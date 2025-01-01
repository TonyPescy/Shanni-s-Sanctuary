# Shanni's Sanctuary
## Description
This is a simple and small text-based adventure game.  It has a labyrinth with rooms that are generated in the same path everytime, however every rooms encounter are randomized.  The starting room and ending rooms are not randomized.  The player has to manage their inventory with limited space and their health points as they navigate Shanni's Sanctuary.  The goal of the player is to escape the labryinth with their lives and get back to their regular lifestyle.
## Authors
Tony Pescatore (TonyPescy)

Nick Pescatore (NAP1313)
## Table of Contents
[Rooms](#Rooms)

[Known Issues](#known-issues)

[Fixed Issues](#fixed-issues)

## Rooms
[Table of Contents](#table-of-contents)
### Enemy Rooms
All enemy types and abilities (WAITING TO BE ADDED TO README)
### Item Rooms
All item types and abilities (WAITING TO BE ADDED TO README)
### Trap Rooms
All trap types and abilities (WAITING TO BE ADDED TO README)
### Other Rooms
All other types and abilities (WAITING TO BE ADDED TO README)

## Known Issues
[Table of Contents](#table-of-contents)
1. A big issue with this is that the maze layout is not randomized which lowers the replay value drastically.
    - The fix for this would result in a complete overhaul of pathing system for the labryinth, which would cause issues over the whole project.
    - Perhaps make several maps for the labryinth to take, as it will have more replayablility value along with the random room generator.
1. Repeated Code and Use of Inefficient Code Practices
    - The fix for this is optimizing and creating more functions to reduce code reuse, updating code practices etc...
    - The cause of this is learning more efficient ways to solve certain problems as I programmed leading to new practices being used as I wrote and older code still being outdated.
    - The solution will be implemented for this later after a working product has been produced as the possible performance issues of these bad practices should be negliable due to the smaller nature of the game. These issues are noted and currently being worked on.
1. Game Balance
    - Currently all game numbers have yet to be tested thoroughly enough so there may be issues of the game being too difficult and therefore not fun. The game is meant to be a bit challenging but should still be fair and enjoyable for the player.
    - The fix for this is more testing and most likely nerfing the enemy stats, giving the player starting potions, giving the player buffs in and out of combat, and changing some rooms to give player more chances to avoid damage or status effects
1. MAJOR ISSUE - Swap Mechanic/Consumable Use/Inventory Indexing Issue
    - Invetory had issues with addressing its index, especially when consumables are used and when weapons come after items that are more likely to be removed from the inventory (Example: armor, shields, and potions).
    - Cause: When swapping weapons multiple times, using consumables, breaking armor/weapons/shields, and all other times when the invetory is accessed and an item is removed from it the item will be popped which will reduce the inventory size and possibly shift the indexes of items around.
    - Fix: Complete overhaul of inventory system in multiple files including combat.py and Character.py. When any Character object is created the inventory will be filled as normal and then to max out the inventory at 5 items the remaining empty spaces will be filled with null values. All removals of items will instead replace the current item with a null value.
    - Potential issues with this fix: It will be more cumbersome to find the true size of ones inventory and may require any conditons that use the len() built-in function to use a custom len() function to only count the non-null values. This will also note the index of the non-null values within the inventory for accessing them within other functions.
    - Other: This will take a while to implement as inventory is used and accessed very often, especially within the combat.py functions. Most likely will require a rework of the logic of the combat_loop. Since combat_loop already needs to be slimmed down and split into smaller functions for different number of enemies, this change should be done in tandem with the 'Repeated Code and Use of Inefficient Code Practices' issue within the combat.py file. NOTE: combat_loop logic does not need significant changes for the necessary inventory changes to be made, so only a small amount of the 'Repeated Code and Use of Inefficient Code Practices' issue will be resolved within the combat loop.
1. 

## Fixed Issues
[Table of Contents](#table-of-contents)
This is to show the progress made to fix the known issues with the project and when they were fixed.
1. 