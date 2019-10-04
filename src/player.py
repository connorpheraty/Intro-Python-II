
class Player:
    
    def __init__(self, name, current_room='outside', has_light_item=False, has_key=False):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.has_light_item = has_light_item
        self.has_key = has_key
        
    def get_item_inv(self, item):
        self.inventory.append(item)

    def drop_item_inv(self, item):
        self.inventory.remove(item)

    def check_inv(self):
        lst = self.inventory
        print("INVENTORY:")
        for i in lst:
            print(i.name," - ", i.description)

    def change_light_status(self):
        for item in self.inventory:
            if item.is_light == True:
                self.has_light_item = True
            else:
                self.has_light_item = False

    def check_for_key(self):
        for item in self.inventory:
            if item.is_key == True:
                self.has_key = True
            else:
                self.has_key =  False


