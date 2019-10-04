class Item:

    def __init__(self, name, description, is_key, is_light=True):
        self.name = name
        self.description = description
        self.is_key = is_key
        self.is_light = is_light
        
        
    def on_take(self):
        item = self.name
        print(f'You have picked up {item}!')

    def on_drop(self):
        item = self.name
        print(f'You have dropped {item}!')

class Key(Item):

    def __init__(self, name, description, is_key):
        super().__init__(name, description, is_key)


class LightSource(Item):

    def __init__(self, name, description, is_key, is_light=True):
        super().__init__(name, description, is_key)
        self.is_light = is_light

    def on_drop(self):
        light_source = self.name
        print(f"You shouldn't drop {light_source}, you will need this later!")
        
    



    

    