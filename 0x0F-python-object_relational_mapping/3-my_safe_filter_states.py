#!/usr/bin/python3
"""Module to take filter input and process against SQL injection"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    injection = sys.argv[4].find(';')
    if injection == -1:
        cur = conn.cursor()
        query = "SELECT * FROM states WHERE `name` = '{}'".format(sys.argv[4])
        cur.execute(query)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
    conn.close()
