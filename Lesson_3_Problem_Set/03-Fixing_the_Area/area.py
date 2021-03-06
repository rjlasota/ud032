#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
In this problem set you work with cities infobox data, audit it, come up with a cleaning idea and then clean it up.

Since in the previous quiz you made a decision on which value to keep for the "areaLand" field,
you now know what has to be done.

Finish the function fix_area(). It will receive a string as an input, and it has to return a float
representing the value of the area or None.
You have to change the function fix_area. You can use extra functions if you like, but changes to process_file
will not be taken into account.
The rest of the code is just an example on how this function can be used.
"""
import codecs
import csv
import json
import pprint

CITIES = 'cities.csv'


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


def fix_area(area):

    def none_type(area):
        return None

    def list_type(area):
        area_values = area[1:-1].split('|')
        area_lens = [len(item) for item in area_values]
        max_idx = area_lens.index(max(area_lens))
        return float(area_values[max_idx])

    def int_type(area):
        return float(area)

    def float_type(area):
        return float(area)

    def str_type(area):
        return None

    process_type = {type(None): none_type,
                    type(list()): list_type,
                    type(int()): int_type,
                    type(float()): float_type,
                    type(str()): str_type}

    return process_type[find_type(area)](area)


def process_file(filename):
    # CHANGES TO THIS FUNCTION WILL BE IGNORED WHEN YOU SUBMIT THE EXERCISE
    data = []

    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        # skipping the extra matadata
        for i in range(3):
            l = reader.next()

        # processing file
        for line in reader:
            # calling your function to fix the area value
            if "areaLand" in line:
                line["areaLand"] = fix_area(line["areaLand"])
            data.append(line)

    return data


def test():
    data = process_file(CITIES)

    print "Printing three example results:"
    for n in range(5, 8):
        pprint.pprint(data[n]["areaLand"])

    assert data[8]["areaLand"] == 55166700.0
    assert data[3]["areaLand"] == None


if __name__ == "__main__":
    test()
