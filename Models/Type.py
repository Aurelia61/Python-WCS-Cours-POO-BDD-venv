# coding: utf-8

import psycopg2

import Variables as Var
class Type():
    """
        Model for Type table in database
    """

    def __init__(self,
        properties):
        """
            Constructor
        """

        # native properties
        self.id = properties[0]
        self.name = properties[1]
        self.id_parent = properties[2]
        
        # calculated properties
