#!/usr/bin/python3
"""request header using requests module"""
import sys
import requests

if __name__ == '__main__':
    try:
        req = requests.get(sys.argv[1])
        # print('{}'.format(req.headers.get('X-Request-Id')))
        # using get would prevent using try except
        print('{}'.format(req.headers['X-Request-Id']))
    except KeyError:
        pass
