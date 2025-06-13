#!/usr/bin/env python3
"""XML serialization and deserialization module"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to XML format and save to file

    Args:
        dictionary (dict): Python dictionary to serialize
        filename (str): name of the XML file to save to
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ", level=0)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize XML data from file and return as Python dictionary

    Args:
        filename (str): name of the XML file to read from

    Returns:
        dict: Python dictionary with deserialized data
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result_dict = {}

        for child in root:
            result_dict[child.tag] = child.text

        return result_dict

    except (ET.ParseError, FileNotFoundError):
        return {}
