class Item:

    def __init__(self, name, description, is_light=True):
        self.name = name
        self.description = description
        self.is_light = is_light
        
    def on_take(self):
        item = self.name
        print(f'You have picked up {item}!')

    def on_drop(self):
        item = self.name
        print(f'You have dropped {item}!')

class Treasures(Item):

    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

class LightSource(Item):

    def __init__(self, name, description, is_light=True):
        super().__init__(name, description)
        self.is_light = is_light

    def on_drop(self):
        light_source = self.name
        print(f"You shouldn't drop {light_source}, you will need this later!")
        
    



    

    