# coding: utf-8

import psycopg2

import Variables as Var

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



# ! code que j'ai rajouté. est-ce utile ? ######################
        # calculated properties
        self.zone = [
            my_zone.id   # ? remplacer id par name
            for my_zone
            in Var.zones
            if my_zone.id == self.id_zone
        ][0]

                # calculated properties
        self.country = [
            my_country.id   # ? remplacer id par name
            for my_country
            in Var.countries
            if my_country.id == self.id_country
        ][0]
# ! #########################################################
