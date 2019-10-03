
class Player:
    
    def __init__(self, name, current_room='outside', has_light_item=False):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        self.has_light_item = has_light_item
        
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


