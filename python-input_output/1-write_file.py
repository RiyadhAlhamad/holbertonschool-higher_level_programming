#!/usr/bin/python3
"""Moudel read_file to read files"""


def write_file(filename="", text=""):
    """This function to recive filename to read it to files"""
    with open(filename, 'w') as f:
        print(f.write(text), end="")
