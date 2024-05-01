#!/usr/bin/python3

"""
iam here
"""

if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    encoded = urllib.parse.urlencode({'email': sys.argv[2]})
    data = encoded.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
