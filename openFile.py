#Anh Vu
#This is the method to load files

import csv
import pandas as pd
import time
start_time = time.time()

#read file 
def loadFile(filename):
    with open(filename, 'r') as file:
        count = 0
        reader = csv.reader(file, delimiter = ',')
        cols = len(next(reader))
        for row in reader:
            count += 1
        print("--- %s seconds ---" % (time.time() - start_time), end =" ")
        print("Total columns read: ", cols) 
        print("--- %s seconds ---" % (time.time() - start_time), end =" ")
        print("Total rows read: ", count)


