from room import Room
from player import Player
from item import Item
from actions import search_room, get_item, drop_item
from setDungeon import room
from menu import view_controls

def current_room(user):
    '''Prints out the room and room description of a players current location'''
    print(room[user.current_room].name)
    print(room[user.current_room].description)

def move_room(user, room_method):
    '''Checks if a player can move in a user inputted direction'''
    test_set = {name for (name,obj) in room.items() if obj == room_method}
    if not test_set:
        print("There's nowhere to go! Try another direction.")
    else:
        user.current_room = list(test_set)[0]
        return (current_room(user))

def controls(user, user_input):
    '''Moves player north, south, east, or west into a different room'''
    if user_input == 'n':
        return move_room(user, room[user.current_room].n_to), print(room[user.current_room].viz)

    elif user_input == 's':
        return move_room(user, room[user.current_room].s_to), print(room[user.current_room].viz)
    
    elif user_input == 'w':
        return move_room(user, room[user.current_room].w_to), print(room[user.current_room].viz)
    
    elif user_input == 'e':
        return move_room(user, room[user.current_room].e_to), print(room[user.current_room].viz)
    
    elif user_input == 'l':
        return search_room(user)

    elif user_input == 'm':
        return view_controls()

    elif user_input == 'i':
        return user.check_inv()

    elif user_input.split()[0] == 'get':
        return get_item(user_input, user)

    elif user_input.split()[0] == 'drop':
        return drop_item(user_input, user)


if __name__=="__main__":
    user_id = input('Enter your character name:')
    user_name = Player(user_id)
    print('---------------- @@ -----------------')

    print(f'Welcome {user_id} to the scary dungeon!')
    print('\n')
    user_input = ''
    print("Enter 'm' to view controls")
    print('---------------- @@ -----------------')
    current_room(user_name)
    print(room[user_name.current_room].viz)
    while user_input != 'q':
        user_input = input()
        print('---------------- @@ -----------------')
        controls(user_name, user_input)

