#! /usr/bin/python
# -*- coding: utf-8 -*-
import csv

"""
    Parse Shotgun csv file
    get columns data and write 'temp.csv' with extracted values
"""
#ifile  = open('Shot.csv', "rb")
#reader = csv.reader(ifile)
ofile  = open('temp.csv', "wb")
writer = csv.writer(ofile)

with open('Shot.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        shotCode = row[1]
        cutIn = row[22]
        cutOut = row[23]
        
        outparsed = str(shotCode), str(cutIn), str(cutOut)
                
        if not row[1].startswith('Shot Code') and outparsed[0] != "":
            print outparsed
            writer.writerow(outparsed)        

#ifile.close()
ofile.close()
