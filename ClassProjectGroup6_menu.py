#------------------------------
# CMPS 3500 - Class Project: Basic Data Analysis Engine
# Anh Vu
#---------------------------

# Load file
from ExploringFile import readByPandas, distinctValue, dropColumn, searchColumn
from openFile import readFile

filename = '/home/fac/walter/public_html/courses/cs3500/2022_fall/proj/data/2019_Airline_Delays_Dataset_train_Part1.csv'

def main_menu():
    print("Main Menu:")
    print("**********")
    print("(1) Load Data")
    print("(2) Exploring Data")
    print("(3) Data Analysis")
    print("(4) Quit")

    ans1 = input()
    if ans1 == "1":
        print("Load data set: ")
        print("**********")
        readFile(filename)
    elif ans1 == "2":
        expData()
    elif ans1 == "3":
        #code
        exit()
    elif ans1 == "4":
        exit()
    else:
        print("Please Enter your option from 1 - 4")
        main_menu()

def expData():
    print("Exploring Data:")
    print("***************")
    print("(21) List all columns:")
    print("(22) Drop columns:")
    print("(23) Describe columns:")
    print("(24) Search Element in Column:")
    print("(25) Back to Main Menu:")
    ans2 = input()
    
    if ans2 == "21":
        readByPandas(filename)
        expData()
    elif ans2 == "22":
        dropColumn(filename)
        expData()
    elif ans2 == "23":
        exit()
    elif ans2 == "24":
        searchColumn(filename)
        expData()
    elif ans2 == "25":
        main_menu()

main_menu()
