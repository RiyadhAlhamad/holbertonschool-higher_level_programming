#!/usr/bin/python3
"""Moudel read_file to read files"""


def append_write(filename="", text=""):
    """This function to recive filename to read it to files"""
    with open(filename, 'a') as f:
        f.write(text)
    return len(text)
