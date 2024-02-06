#!/usr/bin/python3
"""script that adds all arguments to a Python list"""
import json
import os.path
import sys
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
jsonlist = []

if os.path.exists(filename):
    jsonlist = load_from_json_file(filename)
for index in argv[1:]:
    jsonlist.append(index)

save_to_json_file(jsonlist, filename)
