# coding: utf-8


import psycopg2

import Variables as Var

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



    def create_collection(self, MyResult, constructor, ResetCollection = True):
        """
            Create a collection from query result
            and return collection
        """
        if ResetCollection:
            Var.collection_list.clear()

        # create collection
        for my_value in MyResult:
            Var.collection_list.append(
                constructor(my_value))
        return Var.collection_list
            # elif len(my_value) == 3 :
            #     self.collection.append(
            #         constructor(      
            #             my_value[0],
            #             my_value[1],
            #             my_value[2]))
            # elif len(my_value) == 6:
            #     self.collection.append(
            #         constructor(      
            #             my_value[0],
            #             my_value[1],
            #             my_value[2],
            #             my_value[3],
            #             my_value[4],
            #             my_value[5]))




    def print_collection(self):
        """
            Print collection
        """
        # print collection

        print(f"\nLa liste de {self.name}  : \n")   # ? modifier nom de la table en fonction -------------------------------------------
        for my_value in Var.collection_list:
            print (my_value)   # ? modifier .id et .name si plus de champs ------------------------------
        print()