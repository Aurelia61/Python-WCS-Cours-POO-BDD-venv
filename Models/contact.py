# coding: utf-8

import psycopg2
class Contact():
    """
        Model for contact table on database
    """

    def __init__(self, properties):
        """
            constructor
        """

        # native properties
        self.id = properties[0]
        self.name = properties[1]