# coding: utf-8

import psycopg2

import Variables as Var

class Animal_zone_contact():
    """
        Model for animal_zone table on database
    """

    def __init__(self, id_animal, id_zone, id_contact, date_obs, quantity_male, quantity_female):
        """
            Constructor
        """

        self.id_animal = id_animal
        self.id_zone = id_zone
        self.id_contact = id_contact
        self.date_obs = date_obs
        self.quantity_male = quantity_male
        self.quantity_female = quantity_female
