from room import Room
from item import Item, LightSource, Key
from setRoomGraphic import *

# Declare all the rooms

room = {
    'outside':  Room("Outside Dungeon Entrance",
                     "North of you, the Dungeon beckons", outside, dark_viz),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, west and east. A giant pillar is present at the center of the room.""", foyer, dark_viz),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", overlook, dark_viz),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", narrow, dark_viz, is_light=False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", treasure, dark_viz, is_locked=True),

    'dark passageway': Room("Dark Passageway", """It is pitch black in here! You can barely
see a light eminating from the west end of the passageway. You hear noises eminating from the ceiling.""", dark_passage, dark_viz, is_light=False),

    'r_o_b': Room("Room of Bones", "Bones surround the walls of this room.", r_o_b, dark_viz, is_locked=True)
}

item = {
    'stick': Item("Stick", "It's brown and sticky!"),
    'rock': Item("Rock", "You can throw this at people you don't like"),
    'dusty_rod': Item("Dusty Rod", "This looks like it has seen some action"),
    'broken_shield': Item("Broken Shield", "It's broken and can't be used!"),
    'skeleton_bone': Item("Skeleton Bone", "It looks like it has been here for ages!"),
    'old_journal': Item('Old Journal', "It's written in a language you don't understand."),
    'ol_rustys_hammer': Item("Ol' Rusty's Hammer", "You feel the power of Ol' Rusty eminating through you."),
    'lamp': LightSource("Lamp", "It lightens up the room!"),
    'small_key': Key("Small Key", "Opens locked doors")
}
# Link rooms together
# Room 01
room['outside'].n_to = room['foyer']

# Room 02
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['dark passageway']

# Room 03
room['overlook'].s_to = room['foyer']

# Room 04 (Dark)
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

# Room 05 LOCKED
room['treasure'].s_to = room['narrow']

# Room 06 
room['dark passageway'].n_to = room['r_o_b']
room['dark passageway'].e_to = room['foyer']

# Room 07 LOCKEd
room['r_o_b'].s_to = room['dark passageway']

# Create items in rooms
room['outside'].item_list = [item['stick'], item['rock']]
room['foyer'].item_list = [item['dusty_rod'], item['broken_shield']]
room['overlook'].item_list = [item['old_journal'], item['lamp'], item['ol_rustys_hammer']]
room['treasure'].item_list = [item['skeleton_bone']]
room['narrow'].item_list = [item['small_key']]






