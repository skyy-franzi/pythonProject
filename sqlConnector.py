#!/usr/bin/python

import mysql.connector
import csv

class sql_Connector:

    def generate(self, outputFileName):
        if(outputFileName):
            return False

        myConnection = mysql.connector.connect( host="localhost", user="root", passwd="root_passwd", db="testdb2")
        cursor = myConnection.cursor()
        cursor.execute("Select * from MOCK_DATA")

        with open(outputFileName, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([i[0] for i in cursor.description])
            for row in cursor.fetchall():
                writer.writerow(row)
        myConnection.close()


