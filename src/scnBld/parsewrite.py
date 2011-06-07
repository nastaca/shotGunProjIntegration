#! /usr/bin/python
# -*- coding: utf-8 -*-
import csv

"""
    Parse Shotgun csv file
    get columns data 
"""

with open('Shot.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        shotCode = row[1]
        cutIn = row[22]
        cutOut = row[23]
        
        outparsed = str(shotCode), str(cutIn), str(cutOut)

        f = outparsed        
        data = [item for item in csv.reader(f)]
#        f.close()
 
        new_column = [shotCode, cutIn, cutOut]
 
        new_data = []
 
        for i, item in enumerate(data):
            try:
                item.append(new_column[i])
            except IndexError, e:
                item.append("placeholder")
            new_data.append(item)
            print new_data
#            f = open('csv2B.txt', 'w')
#            csv.writer(f).writerows(new_data)
#            f.close()         