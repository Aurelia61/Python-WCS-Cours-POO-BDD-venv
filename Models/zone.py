# coding: utf-8

import psycopg2
class Zone():
    """
        Model for zone table on database
    """

    def __init__(self, properties):
        """
            Constructor
        """

        # native properties
        self.id = properties[0]
        self.name = properties[1]
    

