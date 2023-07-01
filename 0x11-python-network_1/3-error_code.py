#!/usr/bin/python3
"""error codes with urllib"""
import sys
import urllib.request as request
from urllib.error import HTTPError

if __name__ == '__main__':
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            print('{}'.format(response.read().decode()))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
