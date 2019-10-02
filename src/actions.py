from setDungeon import room, item
from player import Player
from room import Room
from item import Item


def search_room(user): 
    lst = room[user.current_room].item_list
    if lst == []:
        print('You do not see any items in this room!')
    else:
        print('You search the room and discover:')
        for item in lst:       
            print(item.name)

def get_item(user_input, user):
    lst = user_input.split(' ', 1)
    item = lst[1]
    for i in room[user.current_room].item_list:
        if item == i.name:
            i.on_take()
            user.get_item_inv(i)
            room[user.current_room].rem_item_room(i)

def drop_item(user_input, user):
    lst = user_input.split(' ', 1)
    item_str = lst[1]
    for i in user.inventory:
        if item_str == i.name:
            i.on_drop()
            user.drop_item_inv(i)
            room[user.current_room].add_item_room(i)



    
