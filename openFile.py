#Anh Vu
#This is the method to load files

import csv
import pandas as pd

fname = input("Enter file name: ")
method = input("Use pandas ? (yes/no) ")
#read file without pandas
def loadFile(fname):
    count = 0
    with open(fname, 'r') as file:
        reader = csv.reader(file, delimiter = ',')
        cols = len(next(reader))
        for row in reader:
            count+=1
    print ("Total columns:")
    print (cols)
    print ("Total rows:")
    print (count)
    
"""
class nameSwitch:
    def colName(self, colNum):
        default = "Done"
        return getattr(self, 'case_' + str(colNum), lambda:default)()
    def case_1(self):
        return "MONTH"
    def case_2(self):
        return "DAY_OF_WEEK"
    def case_3(self):
        return "DEP_DEL15"
mySwitch = nameSwitch()
"""

#read with pandas
def readByPandas(fname):
    df = pd.read_csv(fname)
    print(df)

    #colNum = input("Which column do you want to show? ")
    #print(mySwitch.colName(colNum))
    #print (df[['MONTH', 'DAY_OF_WEEK']])

if method == 'yes':
    readByPandas(fname)
else:
    loadFile(fname)
