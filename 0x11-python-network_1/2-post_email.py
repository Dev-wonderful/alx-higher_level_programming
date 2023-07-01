#!/usr/bin/python3
"""post request"""
import sys
import urllib.request as request

if __name__ == '__main__':
    req = request.Request(sys.argv[1])
    email = sys.argv[2]
    email = email.encode()
    with request.urlopen(req, email) as response:
        print('{}'.format(response.read().decode()))
