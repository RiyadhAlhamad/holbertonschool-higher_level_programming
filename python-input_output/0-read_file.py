#!/usr/bin/python3
"""Moudel read_file to read files"""

def read_file(filename=""):
    """This function to recive filename to read it to files"""
    with open as filename:
        files = open(filename, 'r', encoding="UTF-8")