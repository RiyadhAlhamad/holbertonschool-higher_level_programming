#!/usr/bin/python3
"""Moudel load from json string"""
import json


def load_from_json_file(filename):
    """return json load"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return (json.load(f))
