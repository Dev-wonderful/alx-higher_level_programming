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
    try:
        result = response.json()
        if bool(result):
            print('[{}] {}'.format(result['id'], result['name']))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
