# coding: utf-8

import psycopg2

import bdd

import Variables as Var
from collection import Collection



# def DBConnect():
#     """
#         Connect to Database
#     """
#     MyConnection = None

#     try:
#         MyConnection = psycopg2.connect(
#             host="localhost",
#             database="dojo_animal",
#             user="postgres",
#             password="Formation2020-at"
#         )
#     except(Exception, psycopg2.DatabaseError) as Error:
#         # error
#         print(f"\nCannot connect to specified DB :\n{Error}")

#     return MyConnection

# def ExecuteQuery(
#     MyConnection,
#     MyQuery):
#     """
#         Execute Specified SQL query
#         return query result
#     """
#     MyResult = None

#     if MyConnection is not None:
#         # create DB cursor
#         MyCursor = MyConnection.cursor()
#         # execute query
#         MyCursor.execute(MyQuery)
#         # get result
#         MyResult = MyCursor.fetchall()
#         # close cursor
#         MyCursor.close()

#     return MyResult

# def CreateAnimalCollection(
#     MyResult,
#     ResetCollection = True):
#     """
#         Create Animals collection from query result
#     """
#     if ResetCollection:
#         Var.Animals = []
    
#     # create Animals collection
#     for MyAnimal in MyResult:
#         # print(f"({Animal[0]}) {Animal[1]} - {Animal[2]}")
#         # add an new instance of animal to Animals (collection of animals)
#         # this means each line in animal table (DB)
#         #    equals one instance of animal class 
#         Var.Animals.append(
#             Animal(
#                 MyAnimal[0], 
#                 MyAnimal[1], 
#                 MyAnimal[2]))
    
# def CreateTypeCollection(
    # MyResult,
    # ResetCollection = True):
    # """
    #     Create Types collection from query result
    #     and return collection
    # """
    # if ResetCollection:
    #     Var.Types = []
    
    # # create Animals collection
    # for MyType in MyResult:
    #     Var.Types.append(
    #         Type(
    #             MyType[0], 
    #             MyType[1], 
    #             MyType[2]))






# def PrintAnimalCollection():
#     """ 
#         print Animals
#     """    
#     # print collection
#     print(f"\n Liste des animaux :")
#     for MyAnimal in Var.Animals:
#         print(f"({MyAnimal.id}) {MyAnimal.name} - {MyAnimal.type} ({MyAnimal.id_type})")

# def PrintTypeCollection():
#     """
#         Print Types
#     """
#     # print collection
#     print(f"\n Liste des types d'animaux :")
#     for MyType in Var.Types:
#         print(f"({MyType.id}) {MyType.name} - {MyType.id_parent}")



def Main():
    """
        Program entry
    """

    # connect to DB
    MyConnection = bdd.DBConnect()
    collection_choosen = input("\n Quelle table voulez-vous ? \n- Animal \n- contact \n- country \n- Type \n- zone\n")
    print(f'main :: {collection_choosen}')
    MyQuery = f"SELECT * FROM {collection_choosen}" 
    print(f'my query :: {MyQuery}')   # ! à suppr #####################""
    MyResult = bdd.ExecuteQuery(MyConnection, MyQuery)
    print(f'my result dans le main :: {MyResult}')   # ! à suppr #####################
    bdd.make_collection(f"{collection_choosen}", MyConnection, MyResult, f"{collection_choosen}.TableName" )

    # # try DB
    # MyQuery = "SELECT version()"
    # MyResult = ExecuteQuery(MyConnection, MyQuery)
    # # print query result
    # print(f"\n Résultat du test initial : {MyResult[0]}")

# * à decommenter #########################
    # # execute query
    # MyQuery = (
    #     "SELECT * " +
    #     "FROM type")
    # MyResult = ExecuteQuery(MyConnection, MyQuery)
    # # create Types collection
    # CreateTypeCollection(MyResult)
    # # print collection
    # PrintTypeCollection()

    # # execute query
    # MyQuery = (
    #     "SELECT * " +
    #     "FROM animal " +
    #     "ORDER BY animal.name")
    # MyResult = ExecuteQuery(MyConnection, MyQuery)
    # # print query result
    # # print(f"\n Résultat de la requête : {MyResult}")
    # # create Animals collection
    # CreateAnimalCollection(MyResult)
    # # print collection
    # PrintAnimalCollection()
    # * à decommenter ############################################
    # country_collection = Collection("Country")

    # # ? execute create and print collection
    # MyQuery = ( "SELECT * FROM country" ) # ? ------------ country à modifier ---------------------------------------
    # MyResult = ExecuteQuery(MyConnection, MyQuery)
    # # create collection
    # country_collection.create_collection(MyResult, Country) # ? ------------ Var.countries à modifier -----------------------
    # # print collection
    # country_collection.print_collection()
    # # ?

    # close resources
    MyConnection.close()


# code entry point
if __name__ == "__main__":
    Main()