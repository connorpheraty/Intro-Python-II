from setDungeon import room, item
from player import Player
from room import Room


def search_room(user): 
    lst = room[user.current_room].item_list
    print('You search the room and discover:')
    for item in lst:       
        print(item.name)

def get_item(user_input, user):
    lst = user_input.split()
    item = lst[1]
    for i in room[user.current_room].item_list:
        if item == i.name:
            user.get_item_inv(i)
            room[user.current_room].rem_item_room(i)

def drop_item(user_input, user):
    lst = user_input.split()
    item_str = lst[1]
    for i in user.inventory:
        if item_str == i.name:
            user.drop_item_inv(i)
            room[user.current_room].add_item_room(i)



    
