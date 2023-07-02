#!/usr/bin/python3
"""error codes with urllib"""
import sys
import requests

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    if response.ok:
        print('{}'.format(response.text))
    else:
        print('Error code: {}'.format(response.status_code))
