#!/usr/bin/python3
"""Module 9-add_item.
Adds all arguments to a Python list,
and then save them to a file.
"""

import sys
import json
import os.path

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_file = 'add_item.json'
my_list = []
for word in sys.argv:
    my_list.append(word)
save_to_json_file(my_list, add_item.json)

