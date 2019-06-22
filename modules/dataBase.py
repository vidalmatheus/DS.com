import os,psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

class dataAccess:
    def __init__(self):
        self.dataConnection = psycopg2.connect(DATABASE_URL, sslmode='require')

    def getConnector(self):
        return self.dataConnection