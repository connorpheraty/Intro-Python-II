
class Player:
    
    def __init__(self, name, current_room='outside'):
        self.name = name
        self.current_room = current_room
        self.inventory = []
        
    def get_item_inv(self, item):
        self.inventory.append(item)

    def drop_item_inv(self, item):
        self.inventory.remove(item)

    def check_inv(self):
        lst = self.inventory
        print("INVENTORY:")
        for i in lst:
            print(i.name)


