# Implement a class to hold room information. This should have name and
# description attributes.

"""
class named Room

attributes (name, description)

Need 5 rooms ('outside', 'foyer', 'Grand Overlook', 'Narrow Passage', 'Treasure CHamber')


Each room has its own description

"""

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.all_items = []
       

"""
 set deafult values to directional arguments so you dont have to declare
 them every time a new Room class is instantiated


"""