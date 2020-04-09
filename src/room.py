# Implement a class to hold room information. This should have name and
# description attributes.

"""
class named Room

attributes (name, description)

Need 5 rooms ('outside', 'foyer', 'Grand Overlook', 'Narrow Passage', 'Treasure CHamber')


Each room has its own description

"""

class Room:
    def __init__(self, name, description, n_to = None, s_to = None, e_to = None, w_to = None ):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
       

"""
 set deafult values to directional arguments so you dont have to declare
 them every time a new Room class is instantiated


"""