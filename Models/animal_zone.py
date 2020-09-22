# coding: utf-8

import psycopg2

import Variables as Var

class Animal_zone():
    """
        Model for animal_zone table on database
    """

    def __init__(self, id_animal, id_zone):
        """
            Constructor
        """

        self.id_animal = id_animal
        self.id_zone = id_zone

# # ! code que j'ai rajouté. est-ce utile ? ######################
#         # calculated properties 
#         self.animal = [
#             my_animal.id   # ? remplacer id par name
#             for my_animal
#             in Var.animals
#             if my_animal.id == self.id_animal
#         ][0]
        
#         self.zone = [
#             my_zone.id   # ? remplacer id par name
#             for my_zone
#             in Var.zones
#             if my_zone.id == self.id_zone
#         ][0]
# # ! #########################################################