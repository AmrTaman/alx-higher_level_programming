#!/usr/bin/python3
"""
module for getting a request
"""

import requests

r = requests.get('https://alx-intranet.hbtn.io/status')

print("Body response:")
print("\t- type: {}".format(type(r.text)))
print("\t- content: {}".format(r.text))
