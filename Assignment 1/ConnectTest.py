"""
-------------------------------------------------------
ConnectTest.py
Fall 2020
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2020-10-07"
-------------------------------------------------------
"""
# Imports
from Connect import Connect

def test_connect():
    print("Standard Connection")

    try:
        # Connect to the DCRIS database with an option file
        conn = Connect("dcris.txt")
        # Get the connection cursor object
        cursor = conn.cursor
        # Define a SQL query
        sql = "SELECT * FROM keyword"
        # Execute the query from the connection cursor
        cursor.execute(sql)
        # Print the column names from the query result
        print("Columns:")
        print(cursor.column_names)
        # Get and print the contents of the query results (raw results)
        rows = cursor.fetchall()
        print("Row count: {}".format(cursor.rowcount))

        print("Data:")
        for row in rows:
            print(row)
        # Close the Connect object
        conn.close()
    except Exception as e:
        print(str(e))


# Test connection
test_connect()