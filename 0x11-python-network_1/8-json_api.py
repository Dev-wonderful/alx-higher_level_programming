#!/usr/bin/python3
"""post request email using requests module"""
import sys
import requests

if __name__ == '__main__':
    value = ''
    if len(sys.argv) > 1:
        value = sys.argv[1]
    q = {'q': value}
    response = requests.post('http://0.0.0.0:5000/search_user', data=q)
    print('{}'.format(response.json))
