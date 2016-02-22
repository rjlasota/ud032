#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.
In the first exercise we want you to audit the datatypes that can be found in some particular fields in the dataset.
The possible types of values can be:
- 'NoneType' if the value is a string "NULL" or an empty string ""
- 'list', if the value starts with "{"
- 'int', if the value can be cast to int
- 'float', if the value can be cast to float, but is not an int
- 'str', for all other values

The audit_file function should return a dictionary containing fieldnames and the datatypes that can be found in the field.
All the data initially is a string, so you have to do some checks on the values first.

"""
import codecs
import csv
import json
import pprint
from collections import defaultdict

CITIES = 'cities.csv'

FIELDS = [
    "name", "timeZone_label", "utcOffset", "homepage", "governmentType_label", "isPartOf_label", "areaCode", "populationTotal",
    "elevation", "maximumElevation", "minimumElevation", "populationDensity", "wgs84_pos#lat", "wgs84_pos#long",
    "areaLand", "areaMetro", "areaUrban"]


def find_type(string):
    if not string or string == 'NULL':
        return type(None)
    elif string[0] == '{':
        return type(list())
    try:
        int(string)
        return type(int())
    except:
        pass
    try:
        float(string)
        return type(float())
    except:
        return type(str())


def audit_file(filename, fields):
    fieldtypes = defaultdict(set)
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if 'dbpedia.org' in row['URI']:
                for fn in fields:
                    fieldtypes[fn].add(find_type(row[fn]))
    return fieldtypes


def test():
    fieldtypes = audit_file(CITIES, FIELDS)

    pprint.pprint(fieldtypes)

    assert fieldtypes["areaLand"] == set([type(1.1), type([]), type(None)])
    assert fieldtypes['areaMetro'] == set([type(1.1), type(None)])

if __name__ == "__main__":
    test()
