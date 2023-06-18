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
    state_cities = hbtn_0e_4_usa.cursor()
    injection = argv[4].find(';')
    if injection == -1:
        query = "SELECT cities.name " \
                "FROM `cities` " \
                "WHERE cities.state_id = (" \
                "   SELECT states.id " \
                "   FROM states " \
                "   WHERE states.name = '{}'" \
                ")" \
                "ORDER BY cities.id ASC".format(argv[4])
        state_cities.execute(query)
        stateCities = state_cities.fetchall()
        # print(stateCities)
        if stateCities is not None:
            print(", ".join([city[0] for city in stateCities]))
        # for row in stateCities:
        #     print(row)
    state_cities.close()
    # dataBase.close()
