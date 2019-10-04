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
see a light eminating from the west end of the passageway. You hear strange noises coming from the north.""", dark_passage, dark_viz, is_light=False),

    'strange_room': Room("Strange Room", "You feel like you are being watched.", face_room, dark_viz),
    'regal_hallway': Room("Regal Hallway", "You hear monsters stirring about on the ground floor.", regal_hallway, dark_viz, is_locked=True),
    'kings_corner': Room("King's Corner", "You know what to do. Just do it.", kings_corner, dark_viz)
}

item = {
    'stick': Item("Stick", "It's brown and sticky!", is_key=False),
    'rock': Item("Rock", "You can throw this at people you don't like", is_key=False),
    'dusty_rod': Item("Dusty Rod", "This looks like it has seen some action", is_key=False),
    'broken_shield': Item("Broken Shield", "It's broken and can't be used!", is_key=False),
    'skeleton_bone': Item("Skeleton Bone", "It looks like it has been here for ages!", is_key=False),
    'old_journal': Item('Old Journal', 'The pages in this journal are frayed and the words are hardly legible. Looking closely you make out the name "Scary Terry"', is_key=False),
    'ol_rustys_hammer': Item("Ol' Rusty's Hammer", "You feel the power of Ol' Rusty eminating through you.", is_key=False),
    'lamp': LightSource("Lamp", "It lightens up the room!", is_key=False),
    'small_key': Key("Small Key", "Opens locked doors", is_key=True)
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
room['dark passageway'].n_to = room['strange_room']
room['dark passageway'].e_to = room['foyer']
room['dark passageway'].w_to = room['regal_hallway']

# Room 07 
room['strange_room'].s_to = room['dark passageway']

# Room 08 LOCKED
room['regal_hallway'].e_to = room['dark passageway']
room['regal_hallway'].n_to = room['kings_corner']

# Room 09
room['kings_corner'].s_to = room['regal_hallway']

# Create items in rooms
room['outside'].item_list = [item['stick'], item['rock']]
room['foyer'].item_list = [item['dusty_rod'], item['broken_shield']]
room['overlook'].item_list = [item['lamp'], item['ol_rustys_hammer']]
room['treasure'].item_list = [item['skeleton_bone'], item['old_journal']]
room['narrow'].item_list = [item['small_key']]







