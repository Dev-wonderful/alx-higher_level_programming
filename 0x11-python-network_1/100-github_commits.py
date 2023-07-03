#!/usr/bin/python3
"""get 10 latest commits"""
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{1}/{0}/commits'.format(argv[1], argv[2])
    headers = {
        'Accept': 'application/vnd.github+json',
    }
    params = {'per_page': '10'}
    req = requests.get(url, headers=headers, params=params)
    print(req.text)
    for data in req.json():
        # print('{}'.format(data))
        print('{}: {}'.format(data.get('sha'), 
                                data.get('commit').get('author').get('name')))
