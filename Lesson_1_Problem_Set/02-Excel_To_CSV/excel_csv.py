# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def get_col_max(sheet, column):
    """
    returns ['AREA_NAME', year, month, day, hour, max load]
    for column of sheet
    """
    col_data = sheet.col_values(column,start_rowx=1)    
    
    max_value = max(col_data)
    max_index = col_data.index(max_value) 
    max_time = xlrd.xldate_as_tuple(sheet.cell_value(max_index + 1, 0),0)   

    col_name = [sheet.cell_value(0,column)]  # get column name (region)
    col_max = col_name + list(max_time)[:4] + [max_value]  # concatenate data into one list
    return col_max

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    header = [u'Station',u'Year',u'Month',u'Day',u'Hour',u'Max Load']
    data = [header] + [get_col_max(sheet, i) for i in range(1,9)]
    return data

def save_file(data, filename):
    with open(filename, 'wb') as f:
        w = csv.writer(f, delimiter = '|')
        w.writerows(data)
    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert ans[s][field] == line[field]

        
test()
