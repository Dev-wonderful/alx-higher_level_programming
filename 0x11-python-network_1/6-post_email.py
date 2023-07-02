#!/usr/bin/python3
"""post request email using requests module"""
import sys
import requests

if __name__ == '__main__':
    email = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=email)
    print('{}'.format(response.text))
