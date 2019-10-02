# Implement a class to hold room information. This should have name and
# description attributes.

class Room:

    def __init__(self, room_name, description):
        self.name = room_name
        self.description = description

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
