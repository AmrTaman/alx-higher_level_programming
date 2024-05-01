#!/usr/bin/python3

"""
akkkk
"""

if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as res:
        head = res.headers.get('X-Request-Id')
        print(head)
