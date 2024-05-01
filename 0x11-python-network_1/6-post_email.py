#!/usr/bin/python3

"""
iam here
"""

if __name__ == '__main__':

    import sys
    import requests

    email = dict(email=sys.argv[2])
    r = requests.post(sys.argv[1], data=email)
    print(r.text)
