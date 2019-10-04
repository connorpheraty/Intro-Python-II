from setDungeon import room, item
from player import Player
from room import Room
from item import Item

def search_room(user):
    room_lst = room[user.current_room].item_list
    if room[user.current_room].is_light == True:
        if room_lst == []:
            print('You do not see any items in this room!')
        else:
            print('You search the room and discover:')
            for item in room_lst:       
                print(item.name)
    else:
        print("It's pitch black! I can't see anything")

def get_item(user_input, user):
    lst = user_input.split(' ', 1)
    item = lst[1]
    for i in room[user.current_room].item_list:
        if item == i.name:
            i.on_take()
            user.get_item_inv(i)
            room[user.current_room].rem_item_room(i)
            user.change_light_status()

def drop_item(user_input, user):
    lst = user_input.split(' ', 1)
    item_str = lst[1]
    for i in user.inventory:
        if item_str == i.name:
            i.on_drop()
            user.drop_item_inv(i)
            room[user.current_room].add_item_room(i)
            user.change_light_status()

def lighten_room(user, status, room):
    if status==False:
        if user.has_light_item ==True:
            room[user.current_room].lighten_room()
            print("The room illuminates around you")
            print(room[user.current_room].viz)
        else:
            print("You have nothing to lighten this room!")
    else:
        print("This room is already visible")





    
