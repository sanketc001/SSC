import mysql.connector
from mysql.connector.cursor import MySQLCursorPrepared
#from mysql.connector import connect, Error
import json
import os
from sscpackage import parsessc as sscp
import pandas as pd


class StoreSSC:
    """
    Class for checking, storing and fetching data from a local, predefined DB
    """
    def __init__(self, host="localhost", user="DB_USER", password="DB_PASS", *args, **kwargs):
        self.host = host
        self.user = user
        self.password = password

    """Need to finish"""
    def create_table(self, tablename="test", *args, **kwargs):

        ctable_assemblyvar = """
                        USE sscdb;
                        CREATE TABLE {tname} (
                        {tablevarbody}
                        );
                        """.format(tname=tablename, tablevarbody=args)
        dbtbl_create = """
                        USE sscdb;
                        CREATE TABLE {0} (
                            id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                            ticker VARCHAR(5),
                            logTime DATETIME DEFAULT CURRENT_TIMESTAMP,
                            fetchdata LONGBLOB,
                            idict JSON,
                            bdict JSON,
                            grade VARCHAR(2),
                            elist JSON,
                            arlist JSON
                        );"""


    def db_chksetup(self):
        """
        Checks to ensure that the 'sscdb' exists on server 'localhost', if it doesn't, it creates the database and
        table 'logentry'
        Requires - local environment variables for username and password

        *Note: Fails if no server 'localhost' exists.
        :return:
        """
        try:
            with mysql.connector.connect(
                    host=self.host,
                    user=str(os.getenv(self.user)),
                    password=str(os.getenv(self.password)),
            ) as connection:

                db_check = """
                SELECT COUNT(*)
                FROM INFORMATION_SCHEMA.SCHEMATA
                WHERE SCHEMA_NAME = 'sscdb'
                """

                table_check="""
                SELECT COUNT(*)
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_NAME = {tablename}"""

                dbtbl_create = """
                CREATE DATABASE IF NOT EXISTS sscdb;
                USE sscdb;
                CREATE TABLE IF NOT EXISTS logentry (
                    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    ticker VARCHAR(5),
                    logTime DATETIME DEFAULT CURRENT_TIMESTAMP,
                    grade VARCHAR(2),
                    parsecombo JSON
                );"""

                with connection.cursor(buffered=True) as cursor:
                    cursor.execute(dbtbl_create)

        except mysql.connector.Error as e:
            print("Error in ssc_st - TRY1: " + str(e))

# TODO: fix store process, GradeSSC is no longer the default location for stored info.  Use gradecollectionssc.
    def log_entry(self, parsecombo, grade_ssc, ticker_entry="MSFT"):
        self.insert_db_table = "INSERT INTO logentry (ticker, grade, parsecombo) VALUES (%s, %s, %s)"

        """
        This function is taking the ticker symbol, fetch data from API, parse data
        and the rest of the information and storing it in a local mysql db with the
        following information.
        DB Name = sscdb
        Table Name = logentry
        :param ticker_entry:
        :param res_json:
        :return: None
        """

        log_insertion = {
            "ticker": ticker_entry,
            "grade": grade_ssc,
            "parsecombo": parsecombo
        }
        # The following sql.connector object adds information from '..._parsetool.py' function attributes to 'logentry'

        try:
            with mysql.connector.connect(
                    host="localhost",
                    user=str(os.getenv("DB_USER")),
                    password=str(os.getenv("DB_PASS")),
                    database="sscdb",
            ) as connection:

                # The following code is mySQL

                show_db_ticker = "SELECT * FROM logentry"

                with connection.cursor(buffered=True, cursor_class=MySQLCursorPrepared) as cursor:
                    cursor.execute(self.insert_db_table, (ticker_entry, grade_ssc, parsecombo,))
                    connection.commit()
                    connection.close()

        except mysql.connector.Error as e:
            print("Error in ssc_st - TRY2: " + str(e))

        finally:
            connection.close()

        return None

    def show_db(self):
        """
        Pulls data on sscdb.
        bound to 'show db' tk.button on user GUI
        :return: results (response string from API - JSON)
        """

        try:
            with mysql.connector.connect(
                    host="localhost",
                    user=str(os.getenv("DB_USER")),
                    password=str(os.getenv("DB_PASS")),
                    database="sscdb",
            ) as connection:
                show_db_ticker = "SELECT * FROM logentry"
                with connection.cursor(cursor_class=MySQLCursorPrepared) as cursor:
                    cursor.execute(show_db_ticker)
                    results = cursor.fetchall()
                    connection.commit()

        except mysql.connector.Error as e:
            print(e)

        finally:
            connection.close()

        return results


if __name__ == '__main__':
    S_SSC = StoreSSC()
    S_SSC.db_chksetup()
