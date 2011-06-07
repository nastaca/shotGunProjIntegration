import csv

portfolio = csv.reader(open("Shot.csv", "rb"))
names = []
for row in portfolio:
    names.append(row[1])
print names