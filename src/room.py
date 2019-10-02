class Room:

    def __init__(self, room_name, description):
        self.name = room_name
        self.description = description
        self.item_list = list

    def n_to(self):
        '''Links a room together South to North'''
        self.n_to = n_to
       

    def s_to(self):
        '''Links a room together North to South'''
        self.s_to = s_to
        

    def e_to(self):
        '''Links a room together West to East'''
        self.e_to = e_to
        

    def w_to(self):
        '''Links a room together East to West'''
        self.w_to = w_to

    def add_item_room(self, item):
        '''Adds item from room when dropped by player'''

        self.item_list.append(item)
    
    def rem_item_room(self, item):
        '''Removes item from room when picked up by player'''

        self.item_list.remove(item)

