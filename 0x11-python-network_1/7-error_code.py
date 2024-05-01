#!/usr/bin/python3

"""
iam here
"""

if __name__ == '__main__':
    import sys
    import requests

    r = requests.get(sys.argv[1])
    st = r.status_code
    if (st >= 400):
        print('Error code: {}'.format(st))
    else:
        print(r.text)
