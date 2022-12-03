#------------------------------
# CMPS 3500 - Class Project: Basic Data Analysis Engine
# Anh Vu
#---------------------------

# Load file
from ExploringFile import readByPandas, distinctValue, dropColumn, searchColumn, describe_data
from openFile import loadFile
from ClassProjectGroup6_draft import analyze, solve_reqs
        
print("Please type the name of the file to load:")
filename = input("")
#filename = '/home/fac/walter/public_html/courses/cs3500/2022_fall/proj/data/2019_Airline_Delays_Dataset_train_Part1.csv'
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
        loadFile(filename)
        print("File loaded succesfully!")
        main_menu()
    elif ans1 == "2":
        expData()
    elif ans1 == "3":
        df = readByPandas(filename)
        solve_reqs(filename)
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
        print("List all columns:")
        print("**********************")
        readByPandas(filename)
        expData()
    elif ans2 == "22":
        print("Drop Columns:")
        print("******************")
        dropColumn(filename)
        expData()
    elif ans2 == "23":
        col = describe_data(filename)
        print("Column stats: ")
        print("*************")
        try:
            answers = analyze(col)
        except TypeError:
            print("Error 102: Incorrect datatype")
        print(f"Count: {answers[0]}")
        print(f"Unique: {answers[1]}")
        print(f"Mean: {answers[2]}")
        print(f"Median: {answers[3]}")
        print(f"Mode: {answers[4]}")
        print(f"Variance: {answers[5]}")
        print(f"Standard deviation: {answers[6]}")
        print(f"20th percentile: {answers[7]}")
        print(f"40th percentile: {answers[8]}")
        print(f"50th percentile: {answers[9]}")
        print(f"60th percentile: {answers[10]}")
        print(f"80th percentile: {answers[11]}")
        expData()
    elif ans2 == "24":
        print("Search Element in Column:")
        print("************************")
        searchColumn(filename)
        expData()
    elif ans2 == "25":
        main_menu()
    elif ans2 == "26":
        addColumn(filename)
        expData()
    else:
        print("Please choose again")
        expData()

#Calling function
main_menu()
