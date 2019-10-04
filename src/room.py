class Room:

    def __init__(self, room_name, description, light_viz, dark_viz, is_light=True, is_locked=False):
        self.name = room_name
        self.description = description
        self.light_viz = light_viz
        self.dark_viz = dark_viz
        self.viz = light_viz
        self.item_list = []
        self.is_light = is_light
        self.is_locked = is_locked



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

    def set_room_light(self):
        if self.is_light == True:
            self.viz = self.light_viz
        else:
            self.viz = self.dark_viz

    def lighten_room(self):
        self.viz = self.light_viz
        self.is_light = True

