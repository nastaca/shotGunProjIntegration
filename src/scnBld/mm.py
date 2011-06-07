import csv

ifile  = open('Shot.csv', "rb")
reader = csv.reader(ifile)
ofile  = open('_Shot.csv', "wb")
writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

for row in reader:
    writer.writerow(row)

ifile.close()
ofile.close()