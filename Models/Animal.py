# coding: utf-8

import psycopg2

import Variables as Var

class Animal():
    """
        Model for Animal table in database
    """

    # class properties
    ListName = "animaux"
    TableName = "animal"

    def __init__(self,
        properties):
        """
            Constructor
        """

        # native properties
        self.id = properties[0]
        self.name = properties[1]
        self.id_type = properties[2]
        
        # calculated properties
        # MyQuery = (
        #     "SELECT type.name " +
        #     "FROM type " + 
        #     f"WHERE type.id = {self.id_type}")
        # MyResult = ExecuteQuery(MyConnection, MyQuery)
        # self.type = ""
        # for MyType in Var.Types:
        #     if MyType.id == self.id_type:
        #         self.type = MyType.name 
        
        self.type = [
            MyType.name
            for MyType
            in Var.Types
            if MyType.id == self.id_type][0]

        def __str__(self):
            """
                Overloads the print method
            """
            return f"{self.id} {self.name} {self.id_type}"