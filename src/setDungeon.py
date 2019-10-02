from room import Room
from item import Item

# Room visualizations

outside="""
|--------------\     /--------------|
|               \( )/               |
|                        I          |  
|          o     | |                |
|               /  /      o         |
|              |  |                 |
|   o          |  |                 |
|              |  |    o            |
|              /  /                 |
|-------------/  /------------------|
"""

foyer="""
|--------------/   \----------------|
|                                   |
|                                   |  
|-              ____          I     |
               /    \               |
|-             \____/              -|
|                                   
|     @                    B       -|
|                                   |
|-------------\     /---------------|
"""

overlook="""
|-----------------------------------|
|   M                        M      |
|                                   |  
|                                   |
|  M      ___________________    M  |
|       /                   \       |
|      /                     \      |
|     /    B           TT     \     |
|    |                         |    |
|--------------/    \---------------|
"""

narrow="""
|---------------------  ------------|
|                     | |           |
|                     / /           |  
|       _____        / /            |
|      / ___ \      / /             |
|~~~~~/ /   \ \____/ /              |
       /     \______/               |
|~~~~~/                             |
|                                   | 
|-----------------------------------|
"""

treasure="""
|-----------------------------------|
|$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$|
|$           ___^___               $|
|$          |_______|       &      $|
|$          S       S              $|
|$                                 $|
|$                          &      $|
|$                            &    $|
|$$$$$$$$$$$$$$$$$$   $$$$$$$$$$$$$$|                         
|-------------------  --------------|
"""

dark_passage="""
|--------------\     /--------------|
|              |     |              |
|              |     |         /----|  
|              |     |        /   
|______________\      \      / /----|
|                      \----/ /     |
|----------------------------/      |
|                                   |
|                                   |
|-----------------------------------|
"""




# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", outside),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, west and east.""", foyer),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", overlook),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", narrow),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", treasure),

    'dark passageway': Room("Dark Passageway", """It is pitch black in here! You can barely
see a light eminating from the west end of the passageway. You hear noises eminating from the ceiling.""", dark_passage)
}

item = {
    'stick': Item("Stick", "It's brown and sticky!"),
    'rock': Item("Rock", "You can throw this at people you don't like"),
    'dusty_rod': Item("Dusty Rod", "This looks like it has seen some action"),
    'broken_shield': Item("Broken Shield", "It's broken and can't be used!"),
    'skeleton_bone': Item("Skeleton Bone", "It looks like it has been here for ages!"),
    'old_journal': Item('Old Journal', "It's written in a language you don't understand."),
    'ol_rustys_hammer': Item("Ol' Rusty's Hammer", "You feel the power of Ol' Rusty eminating through you.")
}
# Link rooms together

room['outside'].n_to = room['foyer']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['dark passageway']

room['overlook'].s_to = room['foyer']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

room['treasure'].s_to = room['narrow']

room['dark passageway'].e_to = room['foyer']


# Create items in rooms
room['outside'].item_list = [item['stick'], item['rock']]
room['foyer'].item_list = [item['dusty_rod'], item['broken_shield']]
room['overlook'].item_list = [item['old_journal']]
room['treasure'].item_list = [item['skeleton_bone']]
room['overlook'].item_list = [item['ol_rustys_hammer']]



