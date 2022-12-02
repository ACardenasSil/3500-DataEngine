#Anh Vu
#This is the method to load files

import pandas as pd
import time 
start_time = time.time()

fname = '/home/fac/walter/public_html/courses/cs3500/2022_fall/proj/data/2019_Airline_Delays_Dataset_train_Part2.csv' 
#fname = input("Enter the file name: ")

dropList = []

def distinctValue(fname):
    df = pd.read_csv(fname)
    try:    
        #print unique values 
        colUnique = input("Columns needs to find distinct values :")
        uniqueVal = df[colUnique].unique()
        print ("Unique values of chosen values are:", end = " ")
        print (uniqueVal)
        #Counting unique values
        count = 0
        for i in uniqueVal:
            if i != (i+1):
                count += 1
        print("Unique values of this columns:", end = " ")
        print(count)
    except KeyError:
        print("Columns were not found")

def dropColumn(fname):
    df = pd.read_csv(fname)
    try: 
       #Drop a column
        print("Name Column to Drop:")
        print("--- %s seconds ---" % (time.time() - start_time), end = " ")
        global dropInput 
        dropInput = input("")
        dropList.append(dropInput)
        drop = df.drop(columns=(dropList))
        #print(drop)   #uncomment to see list after dropping
        print("--- %s seconds ---" % (time.time() - start_time), end = " ")
        print("Column dropped!")
    except KeyError:
        print("Columns were not found")

def addColumn(fname):
    df = pd.read_csv(fname)
    try:
        #Add a column
        print("Name Column to Add:")
        global addInput
        addInput = input("")
        dropList.remove(addInput)
        add = df.drop(columns=(dropList))
        print("Columns were added!")
    except KeyError:
        print("Columns were not found")

def searchColumn(fname):
    df = pd.read_csv(fname)
    try:
        #Search input values
        print("--- %s seconds ---" % (time.time() - start_time), end = "")
        searchColInput = input("Enter Column Name: ")
        searchCol = df[searchColInput]
        #if searchColInput != dropInput:
        if searchColInput in dropList:
            print("This column was dropped")
        elif searchColInput not in dropList:
            #print("--- %s seconds ---" % (time.time() - start_time), end = "")
            print(searchCol)
            print("--- %s seconds ---" % (time.time() - start_time), end = "")
            searchInput = input("Enter Element to Search: ")
            counting = 0

            """
            for i in searchCol:            # uncomment to print
                if str(i) in searchInput:  # all columns of the 
                    counting += 1          # searched values
                    print(df.loc[i])      
            print(counting)
            """
            totalRow = 0
            for i in searchCol:
                totalRow+=1
                if str(i) in searchInput:
                    counting += 1
                    #print("Elements found in row: ", end= " ") # uncomment to see which rows have
                    #print(totalRow)                            # the searched values
            print("--- %s seconds ---" % (time.time() - start_time), end = "")
            print("Elements found in ", end= "" )
            print(counting, end =" ")
            print("rows")
        else:    
            print("Column was not found")
    except KeyError:
        print("Column does not exist")
    
def get_column(fname, col_name):
    df = pd.read_csv(fname)
    column = df[col_name]
    return column
    
def describe_data(fname):
    user_col = input("Name column to describe: ")
    print(user_col)
    out_col = get_column(fname, user_col)
    return out_col

def readByPandas(fname):
    #List all columns
    try:
        count = 0
        i = 1
        df = pd.read_csv(fname)
        for colName in range (26):
            colName = df.iloc[0:0, colName].name
            if colName not in dropList: 
                print ("Column", i, ":", colName)
                i+=1
    except FileNotFoundError:
        print("File was not found")

