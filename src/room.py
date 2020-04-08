# Implement a class to hold room information. This should have name and
# description attributes.

"""
class named Room

attributes (name, description)

Need 5 rooms ('outside', 'foyer', 'Grand Overlook', 'Narrow Passage', 'Treasure CHamber')


Each room has its own description

"""
# WHY DOES ROOM NEED THE DIRECTION IN THE ARGUEMNTS?
class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to ):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

# Do i want to set deafult values to directional arguments
# so i dont have to declare them every time a new Room class is instantiated