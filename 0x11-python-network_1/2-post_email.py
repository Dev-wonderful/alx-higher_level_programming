#!/usr/bin/python3
"""post request"""
import sys
import urllib.request as request
import urllib.parse as parse

if __name__ == '__main__':
    req = request.Request(sys.argv[1])
    email = {'email': sys.argv[2]}
    data = parse.urlencode(email)
    data = data.encode()
    with request.urlopen(req, data) as response:
        print('{}'.format(response.read().decode()))
