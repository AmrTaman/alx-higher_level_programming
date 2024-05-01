#!/usr/bin/python3
"""module for getting a request
dddddd
"""

import requests
import sys

r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
