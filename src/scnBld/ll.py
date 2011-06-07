import csv

class readInCSV:
    def __init__(self, fileName):
        #instantiate the CSV file variable:
        self.fileName = fileName
        #read the CSV file and open it:
        self.fileReader = csv.reader(open(self.fileName, "rb"), delimiter = ',')
        #create a local array to hold the CSV data:
        self.fileReaderList = []
        #pop the file data into the local array:
        for data in self.fileReader:
            self.fileReaderList.append(data)