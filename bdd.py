# coding: utf-8

import psycopg2

from collection import Collection
from Models.Animal import Animal
from Models.Type import Type
from Models.contact import Contact
from Models.country import Country
from Models.zone import Zone
from Models.animal_zone import Animal_zone
from Models.animal_zone_contact import Animal_zone_contact


def DBConnect():
    """
        Connect to Database
    """
    MyConnection = None

    try:
        MyConnection = psycopg2.connect(
            host="localhost",
            database="dojo_animal",
            user="postgres",
            password="Formation2020-at"
        )
    except(Exception, psycopg2.DatabaseError) as Error:
        # error
        print(f"\nCannot connect to specified DB :\n{Error}")

    return MyConnection


def ExecuteQuery(
    MyConnection,
    MyQuery):
    """
        Execute Specified SQL query
        return query result
    """
    MyResult = None

    if MyConnection is not None:
        # create DB cursor
        MyCursor = MyConnection.cursor()
        # execute query
        MyCursor.execute(MyQuery)
        # get result
        MyResult = MyCursor.fetchall()
        print(f' My result dans bdd executeQuery {MyResult}')    # ! à suppr #####################
        # close cursor
        MyCursor.close()

    return MyResult


def make_collection(collection_choosen, MyConnection, MyResult, MyModel):
    """
        makes collection
    """

    # create an object collection (empty ?)
    current_collection = Collection(collection_choosen)
    print(f'current collection créée à linstant :: {current_collection}' )    # ! à suppr #####################
    
    # create collection
    # ! name = Animal_zone_contact
    current_collection.create_collection(MyResult, MyModel) # ? ------------ nom de la classe à modifier -----------------------
    print(f'current collection apres creat_collection :: {current_collection}')    # ! à suppr #####################
    # print collection
    current_collection.print_collection()
