#!/usr/bin/python3

"""
iam here
"""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) == 1:
        val = ""
    else:
        val = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': val})
    try:
        if len(r.json()) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r.json()['id'], r.json()['name']))
    except ValueError:
        print("Not a valid JSON")
