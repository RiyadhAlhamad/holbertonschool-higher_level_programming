#!/usr/bin/python3
"""Moudel  json string to object"""
import json


def from_json_string(my_str):
    """return json to object"""
    return json.loads(my_str)
