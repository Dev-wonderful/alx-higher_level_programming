#!/usr/bin/python3
"""http request using urllib"""
import sys
import urllib.request as request

if __name__ == '__main__':
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as response:
        value = response.headers
        print(value['X-Request-Id'])
