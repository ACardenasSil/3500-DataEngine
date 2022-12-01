#Anh Vu
#This is the method to load files

import pandas as pd

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
        print("Columns to drop:")
        global dropInput 
        dropInput = input("")
        dropList.append(dropInput)
        drop = df.drop(columns=(dropList))
        print(drop)
    except KeyError:
        print("Columns were not found")


def searchColumn(fname):
    df = pd.read_csv(fname)
    try:
        #Search input values
        searchColInput = input("Columns to search for: ")
        searchCol = df[searchColInput]
        #if searchColInput != dropInput:
        if searchColInput in dropList:
            print("This column was dropped")
        elif searchColInput not in dropList:
            print(searchCol)
            searchInput = input("Value to search for:")
            counting = 0

            """
    for i in searchCol:
        if str(i) in searchInput:
            counting += 1
            print(df.loc[i])
    print(counting)
            """
            totalRow = 0
            for i in searchCol:
                totalRow+=1
                if str(i) in searchInput:
                    counting += 1
                    #print("Elements found in row: ", end= " ")
                    #print(totalRow)
            print("Elements were found in ", end= "" )
            print(counting, end =" ")
            print("rows")
        else:    
            print("Column was not found")
    except KeyError:
        print("Input does not exist")


def readByPandas(fname):
    #List all columns
    try:
        df = pd.read_csv(fname)
        for colName in range (26):
            if colName not in dropList:
                colName = df.iloc[0:0, colName].name
                print (colName)
    except FileNotFoundError:
        print("File was not found")

