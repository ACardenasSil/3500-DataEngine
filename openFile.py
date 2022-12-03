#Anh Vu
#This is the method to load files

import csv
import pandas as pd
import time
start_time = time.time()

fname = input("Enter file name: ")
method = input("Use pandas ? (yes/no) ")
#read file without pandas
def loadFile(fname):
    with open(fname, 'r') as file:
        count = 0
        reader = csv.reader(file, delimiter = ',')
        cols = len(next(reader))
        for row in reader:
            count+=1
        print("--- %s seconds ---" % (time.time() - start_time), end =" ")
        print("Total columns read: ", cols) 
        print("--- %s seconds ---" % (time.time() - start_time), end =" ")
        print("Total rows read: ", count)
    

#read with pandas
def readByPandas(fname):
    df = pd.read_csv(fname)
    print(df)

    #colNum = input("Which column do you want to show? ")
    #print(mySwitch.colName(colNum))
    #print (df[['MONTH', 'DAY_OF_WEEK']])
