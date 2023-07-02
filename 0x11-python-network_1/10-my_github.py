#!/usr/bin/python3
"""github authentication api"""
from sys import argv
import requests

if __name__ == '__main__':
    header = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer {}'.format(argv[2]),
        'X-GitHub-Api-Version': '2022-11-28'
    }
    req = requests.get('https://api.github.com/user', headers=header)
    # print(req)
    # print('{}'.format(req.text))
    print(req.json().get('id'))
