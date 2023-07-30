#!/usr/bin/python

import psycopg2
import pandas as pd

def create_connection(databasename, password, hostname, port, username):
    """ "
    Description: This function create a postgresql connection object
    @ input params: database name,  password, and default values
    @ output params: create a connection
    """

    connection = None
    try:
        print("Connecting to the postgreSQL database ...")
        connection = psycopg2.connect(
            host=hostname,
            port=port,
            database=databasename,
            user=username,
            password=password,
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            # connection.close()
            print("Database connection created.")

    return connection


def load_data(connection, sql_query, values=None):
    """"
    Description: This function runs the data pull from postgresql and save it as a dataframe 
    @ input params: postgresql connection object, sql query to run 
    @ output params: return a dataframe
    """
    try:
        # create a cursor
        print(
            "Creating a pandas dataframe from the provided database connection and sql script started ..."
        )
        cursor = connection.cursor()
        cursor.execute(sql_query, values)  # None
        df = pd.DataFrame(cursor.fetchall())
        df.columns = [x[0] for x in cursor.description]
        cursor.close()
        print("Pandas dataframe creation complited successefuly!")
        return df
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.commit()
            connection.close()
            print("Database connection terminated.")

    # return df

