# coding: utf-8

import psycopg2
class Country():
    """
        Model for country table on database
    """

    def __init__(self, properties):
        """
            Constructor
        """

        # native properties
        self.id = properties[0]
        self.name = properties[1]

        def __str__(self):
            """
                Overloads the print method
            """
            return f"{self.id} {self.name}"