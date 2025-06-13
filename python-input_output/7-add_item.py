#!/usr/bin/python3
"""script that adds all arguments to a Python list, and then save them to a file"""
import sys


save_to_jason_file = __import__('5-save_to_json_file').save_to_jason_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
file_name = "add_item.json"

"""Try to load existing data from file and save file to json file"""
item_list = load_from_json_file(file_name)
item_list.extend(sys.argv[1:])
save_to_jason_file(item_list, file_name)
