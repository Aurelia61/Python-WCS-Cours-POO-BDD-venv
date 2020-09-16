# coding: utf-8

import Variables

class Zone_country():
    """
        Model for zone_country table on database
    """

    def __init__(self, id_zone, id_country):
        """
            Constructor
        """

        self.id_zone = id_zone
        self.id_country = id_country

        # calculated properties
        self.zone = [
            my_zone.name
            for my_zone
            in Variables.zones
            if my_zone.id == self.id_zone
        ][0]
        print(self.zone)


