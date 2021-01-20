from bathroom import Bathroom
from kitchen import Kitchen
from pantry import Pantry

class Manor(object):
    def __init__(self):
        bathroom = Bathroom()
        bedroom = Kitchen()
        pantry = Pantry()

        self.rooms = [bathroom, bedroom, pantry]

    def enter_room(self, num):
        return self.rooms[num-1]

    def lobby_rooms(self):
        print "\tUpon entering the lobby, you notice %d rooms around you. Which one do you enter?\n" % len(self.rooms)
        for index, room in enumerate(self.rooms):
            print "\t[%d] %s" % (index+1, room.name)

    def go_to_entrance(self):
        print "\n\tYou swallow your fear and slowly open the door in the manor."
