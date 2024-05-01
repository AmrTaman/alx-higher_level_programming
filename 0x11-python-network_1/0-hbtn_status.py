#!/usr/bin/python3

"""
iam here
"""

import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    amr = resp.read()
    print("\t- type: {}".format(type(resp.read())))
    print("\t- content: {}".format(amr))
    utf8 = amr.decode('utf-8')
    print("\t- utf8 content: {}".format(utf8))
