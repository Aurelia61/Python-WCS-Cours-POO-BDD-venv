# coding: utf-8


import psycopg2

from Models.Animal import Animal
from Models.Type import Type
from Models.contact import Contact
from Models.country import Country



class Collection():
    """
        Model collection
    """

    def __init__(self, name):
        """
            Constructor
        """
        self.name = name
        self.collection = []


    def create_collection(self, MyResult, constructor, ResetCollection = True):
        """
            Create a collection from query result
            and return collection
        """
        if ResetCollection:
            self.collection.clear()

        # create collection
        for my_value in MyResult:
            if len(my_value) == 2 :
                self.collection.append(
                    constructor(      
                        my_value[0],
                        my_value[1]))
            elif len(my_value) == 3 :
                self.collection.append(
                    constructor(      
                        my_value[0],
                        my_value[1],
                        my_value[2]))



    def print_collection(self):
        """
            Print collection
        """
        # print collection

        print(f"\nLa liste de {self.name}  : \n")   # ? modifier nom de la table en fonction -------------------------------------------
        for my_value in self.collection:
            print(f"{my_value.id} {my_value.name}")    # ? modifier .id et .name si plus de champs ------------------------------
        print()