#-ROUGH DRAFT------------------------------------------------------------------
# NAMES:
# Jarl Ramos
# Alonso Cardenas Sillas
# Anh Vu
# Shadi Abdul Razzak
# ASGT: Class Project: Basic Data Analysis Engine
# ORGN: CSUB - CMPS-3500
# FILE: ClassProjectGroup6_draft.py
# DATE: 27 November 2022
#-ROUGH DRAFT------------------------------------------------------------------

import csv
import pandas as pd
from decimal import Decimal # helps avoid floating point errors

read_info = { }
month_delay_list = []
day_delays = []
airline_delay_log = {}
airport_lists = {}
"""
fname = input("Enter file name: ")
method = input("Use pandas ? (yes/no) ")
"""
#read file without pandas
def loadFile(fname):
    count = 0
    with open(fname, 'r') as file:
        reader = csv.reader(file, delimiter = ',', skipinitialspace=True)
        cols = len(next(reader))
        for row in reader:
            yield row # yields a row each time the function is called as an iterator (in a for loop)
            #print(row)
            #count+=1
    #print ("Total columns:")
    #print (cols)
    #print ("Total rows:")
    #print (count)
    

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
'''
#fname = '/home/fac/walter/public_html/courses/cs3500/2022_fall/proj/data/2019_Airline_Delays_Dataset_train_Part2.csv' 
fname = input("Enter the file name: ")
def readByPandas(fname):
    try:
        df = pd.read_csv(fname)
    except FileNotFoundError:
        print("File was not found")
    return df
'''
'''
#read with pandas
def readByPandas(fname):
    #df = pd.read_csv(fname)
    # dummy code 
    # TODO: remove following line when fully optimized
    df = "hello\n"
    return df

    #colNum = input("Which column do you want to show? ")
    #print(mySwitch.colName(colNum))
    #print (df[['MONTH', 'DAY_OF_WEEK']])
'''
"""
if method == 'yes':
    readByPandas(fname)
else:
    loadFile(fname)
"""

# place holder sorting
def orderList(array):
    # TODO : implement sorting algo
    array = sorted(array)
    return array

#generator to prevent loading all of the object at once
def gen_objects(object):
    for item in object:
        yield item

def isOfNumber(numbers):
    if isinstance(numbers, (float, int)):
        array = [numbers]
        numbers = array

    for item in numbers:
        if not isinstance(item, (float, int)):
            raise Exception("A NaN was found. Please use numbers.")

def count(array):
    # enumerate(x) returns an index starting at 1 and the item in the list
    gen_array_item = gen_objects(array)
    for count, item in enumerate(gen_array_item, start=1):
        pass
    return count #all I need is the final count

# Return a list with only unique values. 
# Takes advantage of set's hashing functionality
def unique(array):
    
    # Create an empty set
    unique_array = set()
    #get iterable array generator object
    gen_array_item = gen_objects(array)
    for item in (gen_array_item):
        unique_array.add(item) # add item to set
    return list(unique_array) # return set as a list

def median(array):
    isOfNumber(array)
    length = len(array)
    isEven = not length %2
    middle_index = length //2 # floor division
    median = 0

    if (isEven):
        median = (array[middle_index] + array[middle_index-1]) /2
        return median
    else: #odd
        median = array[middle_index]
        return median

def mode(array):
    gen_array_item = gen_objects(array)

    # empty dictionary
    dictionary = {} # {value : occurence}
    for key_int in gen_array_item:
        isOfNumber(key_int) # check if dictionary keys are numbers
        if dictionary.get(key_int) is None: # if key does not exist yet
            # create dictionary key and set to one occurence
            dictionary[key_int] = 1 
        else:
            # increase the occurence if key exists
            dictionary[key_int] = dictionary.get(key_int)+1 
    dict_list = list(dictionary.values())
    dict_keys = list(dictionary.keys())

    mode_array = []
    for item in dict_keys:
        pass
    
    # code for one mode (the first one that appears)
    #occurences = maximum(dict_list)
    #modes = list(dictionary.keys())[dict_list.index(occurences)]
    return array

def minimum(array):
    gen_array_item = gen_objects(array)
    number = next(gen_array_item)
    isOfNumber(number) # check if the first array item is a number
    min_val = number
    for number in gen_array_item:
        isOfNumber(number)
        if min_val > number:
            min_val = number
    return min_val

def maximum(array):
    gen_array_item = gen_objects(array)
    number = next(gen_array_item)
    isOfNumber(number) # check if the first array item is a number
    max_val = number
    for number in gen_array_item:
        isOfNumber(number)
        if max_val < number:
            max_val = number
    return max_val

# finds the arithmetic mean of a list of numerical values
def mean(data_list):
    mean_sum = 0
    mean_num = len(data_list)
    for i in data_list:
        mean_sum += i
    return mean_sum / mean_num
 
# finds the variance of a list of values
def variance(data_list, mean):
    var_sum = 0
    for i in data_list:
        var_sum += (i - mean) ** 2
    return var_sum / (len(data_list) - 1)

# finds the variance of a list of values by taking in the variance
# returned by the above function
def std_dev(var):
    return var ** (1 / 2)

# finds the 20th percentile of a list
def per_20(data_list):
    return data_list[len(data_list) // 5 - 1]

# finds the 40th percentile of a list
def per_40(data_list):
    return data_list[len(data_list) // 2.5 - 1]

# finds the 50th percentile of a list
def per_50(data_list):
    return data_list[len(data_list) // 2 - 1]

# finds the 60th percentile of a list
def per_60(data_list):
    return data_list[len(data_list) // 1.66667 - 1]

# finds the 80th percentile of a list
def per_80(data_list):
    return data_list[len(data_list) // 1.25 - 1]

#-------------------

def find_month_delays(read_info, month_delays):
    if read_info[0] == "1":
        num = int(read_info[2])
        month_delays[0] += num
    elif read_info[0] == "2":
        num = int(read_info[2])
        month_delays[1] += num
    elif read_info[0] == "3":
        num = int(read_info[2])
        month_delays[2] += num
    elif read_info[0] == "4":
        num = int(read_info[2])
        month_delays[3] += num
    elif read_info[0] == "5":
        num = int(read_info[2])
        month_delays[4] += num
    elif read_info[0] == "6":
        num = int(read_info[2])
        month_delays[5] += num
    elif read_info[0] == "7":
        num = int(read_info[2])
        month_delays[6] += num
    elif read_info[0] == "8":
        num = int(read_info[2])
        month_delays[7] += num
    elif read_info[0] == "9":
        num = int(read_info[2])
        month_delays[8] += num
    elif read_info[0] == "10":
        num = int(read_info[2])
        month_delays[9] += num
    elif read_info[0] == "11":
        num = int(read_info[2])
        month_delays[10] += num
    elif read_info[0] == "12":
        num = int(read_info[2])
        month_delays[11] += num
def find_day_delays(read_info, day_delays):
    if read_info[1] == "1":
        num = int(read_info[2])
        day_delays[0] += num
    elif read_info[1] == "2":
        num = int(read_info[2])
        day_delays[1] += num
    elif read_info[1] == "3":
        num = int(read_info[2])
        day_delays[2] += num
    elif read_info[1] == "4":
        num = int(read_info[2])
        day_delays[3] += num
    elif read_info[1] == "5":
        num = int(read_info[2])
        day_delays[4] += num
    elif read_info[1] == "6":
        num = int(read_info[2])
        day_delays[5] += num
    elif read_info[1] == "7":
        num = int(read_info[2])
        day_delays[6] += num
def find_most_delayed_airline(read_info, month_index, d_log):
    if read_info[0] == month_index:
        if read_info[8] in d_log:
            d_log[read_info[8]] += 1
        else:
            dict_buf = {read_info[8] : 1}
            d_log.update(dict_buf)
    for i in d_log:
        hi_delays = i.key
        if (i.key > hi_delays):
            hi_delays = i.key
    return hi_delays

def find_avg_plane_age(carrier_name):
    avg_age = 0
    plane_count = 0
    if read_info[8] == carrier_name and read_info[2] == 1:
        avg_age += int(read_info[16])
        plane_count += 1

    return avg_age / plane_count

def snow_delay(read_info):
    count_of_planes = 0

    if int(read_info[22]) >= 15 and read_info[2] == 1:
        count_of_planes += 1
    
    return count_of_planes

def collect_airports(read_info, alist):
    if read_info[17] in alist:
        alist[read_info[17]] += 1
    else:
        dict_buf = {read_info[17] : 1}
        alist.update(dict_buf)

def top_5_airports(alist):
    new_dict = { }
    most_delays = 0
    most_delayed_airport = '0'
    for h in range(5):
        for i in alist:
            if alist[i] > most_delays:
                most_delays = alist[i]
                most_delayed_airport = alist
        dict_buf = {most_delayed_airport : most_delays}
        new_dict.update(dict_buf)
        del alist[most_delayed_airport]
    return new_dict

#Alonso #4
def top_5_airport_passengers(fname): #fname is file name string
    #Print the 5 airport that averaged the greatest number of passengers in 2019.
    # this function is confirmed to work
    five = [0, 0, 0, 0, 0]
    airports = {} # {airport_name:month_avg} dictionary
    months = [0] * 13 #index represent month number, value represents average passengers
    for row in loadFile(fname): #get necessary column values
        airport_name = row[17]
        month = int(row[0])
        month_avg = int(row[12])
        if airport_name in airports:
            months = airports[airport_name] 
        else:
            months = [0] * 13
        months[month] = month_avg
        airports[airport_name] = months #each airport holds each month and its avg


    airport_tot = {}
    for airport_name in list(airports.keys()):
        tot_pass = 0 #initialize total num of passengers for each airport
        print(months)
        print(airport_name)
        months = airports[airport_name]
        for avg in months:
            tot_pass += avg #sum up passengers for each of the 12 months
        airport_tot[airport_name] = tot_pass
    airtotval = list(airport_tot.values())
    five = []

    for i in range(0, 5):
        max1 = 0
		
        for j in range(len(airtotval)):	
            if (airtotval[j] > max1):
                max1 = airtotval[j]
				
        airtotval.remove(max1)
        five.append(max1)
    return five #list of 5 elements

# Alonso #5
def top_5_airline_employees(read_info):
    # This function needs 
    # GROUND_SERV_PER_PASS, FLT_ATTENDANTS_PER_PASS, passed as 2d array of strings
    # 
    # get the month and day, the airline carrier, number of seats
    #       sum all seats where (airline carrier, month, and day match) to get passenger number
    #       multiply passenger number with ground_serv_per_pass to get number of ground employees
    #       multiply passenger number with flt_attendants_per_pass to get number of flight attendants
    #           sum ground employees and flight attendants to get number of all employees
    # Print the 5 airlines that averaged the greatest number of employees in 2019
    pass