#!/usr/bin/python3
"""Moudel to json string"""
import json


def save_to_json_file(my_obj, filename):
    """return save json file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
