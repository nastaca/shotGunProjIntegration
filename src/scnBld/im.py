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
        
#        print shotCode, cutIn, cutOut

        outparsed = str(shotCode), str(cutIn), str(cutOut)
        print outparsed
        for row in outparsed:
#            print row
            try:
                t=int(row[i])
                row[i]=t 
            except ValueError:
                t=float(row[i])
                row[i]=t
                row=tuple(row)

 
#        names = []
#        for i in range(len(row)):
#            try:
#                t=int(row[i])
#                row[i]=t 
#            except ValueError:
#                t=float(row[i])
#                row[i]=t
#                row=tuple(row)
#                names.append(row)
#                print names
                

#        for row in outparsed:
#            names.append(row[10])
#        print names


            