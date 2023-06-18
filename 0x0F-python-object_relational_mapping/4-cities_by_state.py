#!/usr/bin/python3
"""A Module that lists all cities from database hbtn_0e_4_usa"""

from sys import argv
import MySQLdb as dataBase

if __name__ == '__main__':
    # naming the database object after the name of the database expected
    hbtn_0e_4_usa = dataBase.connect(host="localhost", port=3306,
                                     user=argv[1], passwd=argv[2],
                                     db=argv[3], charset="utf8")
    # naming the cursor after the queries to be executed
    all_cities = hbtn_0e_4_usa.cursor()
    query = "SELECT cities.id, cities.name, states.name " \
            "FROM `cities` " \
            "JOIN `states` " \
            "ON cities.state_id = states.id " \
            "ORDER BY cities.id ASC"
    all_cities.execute(query)
    allCities = all_cities.fetchall()
    for row in allCities:
        print(row)
    all_cities.close()
    # dataBase.close()
