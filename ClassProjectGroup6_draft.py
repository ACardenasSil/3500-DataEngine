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
            print(row)
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
    return merge_sort(array)
#used for orderList()
def merge_sort(list):
    list_length = len(list)
    if list_length <= 1:
        return list

    half = list_length // 2
    left = merge_sort(list[:half])
    right = merge_sort(list[half:])

    return merge(left, right)

#used for orderList()
def merge(left, right):
    merged = []
    i = 0
    j = 0

    while ((i < len(left)) and (j < len(right))):
        if left[i] > right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

#generator to prevent loading all of the object at once
def gen_objects(object):
    for item in object:
        yield item

def isOfNumber(numbers):
    if isinstance(numbers, (float, int)):
        array = [numbers]

    for item in array:
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
    max_val = 0
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

#6
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
#7
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
#8
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
#9
def find_avg_plane_age(carrier_name):
    avg_age = 0
    plane_count = 0
    if read_info[8] == carrier_name and read_info[2] == 1:
        avg_age += int(read_info[16])
        plane_count += 1

    return avg_age / plane_count
#10
def snow_delay(read_info):
    count_of_planes = 0

    if int(read_info[22]) >= 15 and read_info[2] == 1:
        count_of_planes += 1
    
    return count_of_planes
    
#2
def collect_airports(read_info, alist):
    if read_info[17] in alist:
        alist[read_info[17]] += 1
    else:
        dict_buf = {read_info[17] : 1}
        alist.update(dict_buf)
#11
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
def top_5_airport_passengers(dep_airports_list, avg_month_pass_airport): #fname is file name string
    #Print the 5 airport that averaged the greatest number of passengers in 2019.
    # this function is confirmed to work

    airports = {} # {airport_name:month_avg} dictionary
    for index, airport in enumerate(dep_airports_list): #get necessary column values
        if airport not in airports:
            avg_month_pass = avg_month_pass_airport[index]
            airports[airport] = avg_month_pass
    #^^^loop takes the largest amount of time

    airport_tot = {}
    airkeys = list(airports.keys())
    for airport_name in airkeys:
        tot_pass = 0 # total num of passengers for each airport
        month_avg = airports[airport_name]
        tot_pass = month_avg*12
        airport_tot[airport_name] = tot_pass
    airtotval = list(airport_tot.values())
    airtotval = orderList(airtotval)
    airtotval = airtotval[:5] #cut the largest 5 values

    # for loop to convert values to their keys
    top_air_names = []
    for value in airtotval:
        top_air_names.extend(i for i in airport_tot if airport_tot[i]==value)

    return top_air_names #list of 5 elements

# Alonso #5
def top_5_airline_employees(airline_names, avg_monthly_pass_airline, flt_attendants_per_pass, ground_serv_per_pass):
    # Print the 5 airlines that averaged the greatest number of employees in 2019
    # This function works 
    # GROUND_SERV_PER_PASS, FLT_ATTENDANTS_PER_PASS, passed as 2d array of strings
    # 
    # get the month and day, the airline carrier, number of seats
    #       sum all seats where (airline carrier, month, and day match) to get passenger number
    #       multiply passenger number with ground_serv_per_pass to get number of ground employees
    #       multiply passenger number with flt_attendants_per_pass to get number of flight attendants
    #           sum ground employees and flight attendants to get number of all employees
    airlines_dict = {} # {airline_name:month_avg} dictionary
    for index, airline in enumerate(airline_names): #get necessary column values

        if ((airline) not in airlines_dict): #skip line if airline already has been analyzed
            month_avg_pass = avg_monthly_pass_airline[index]
            emp_per_pass = flt_attendants_per_pass[index] + ground_serv_per_pass[index] 
            tot_emp = month_avg_pass * emp_per_pass
            airlines_dict[airline] = [tot_emp] # each airline key values a monthly avg
    #^^^loop takes the largest amount of time

    airline_tot = {}
    airkeys = list(airlines_dict.keys())
    for airline in airkeys:
        tot_emp = airlines_dict[airline]
        airline_tot[airline] = tot_emp
    airtotval = list(airline_tot.values())
    airtotval = orderList(airtotval)
    airtotval = airtotval[:5] #cut the largest 5 values

    # for loop to convert values to their keys
    top_air_names = []
    for value in airtotval:
        top_air_names.extend(i for i in airline_tot if airline_tot[i]==value)

    return top_air_names #list of 5 elements
'''
dep_airports = []
avg_monthly_pass_airport = []
avg_monthly_pass_airline = []
airline_names = []
flt_attendants_per_pass = []
ground_serv_per_pass = []

for row in loadFile("2019_Airline_Delays_Dataset_train_Part1.csv"): #get necessary column values
    try:
        dep_airports.append(row[17])

        temp = int(row[12])
        isOfNumber(temp)
        avg_monthly_pass_airport.append(temp)
        # 8 13 14 15
        airline_names.append(row[8])
        
        temp = int(row[13])
        isOfNumber(temp)
        avg_monthly_pass_airline.append(temp)

        temp = float(row[14])
        isOfNumber(temp)
        flt_attendants_per_pass.append(temp)

        temp = float(row[15])
        isOfNumber(temp)
        ground_serv_per_pass.append(temp)
    except Exception:
        print("Line read error, skipping line.")

input("Hit enter for Question 4:")
print(top_5_airport_passengers(dep_airports, avg_monthly_pass_airport))
input("Hit Enter for Question 5:")
print(top_5_airline_employees(airline_names, avg_monthly_pass_airline, flt_attendants_per_pass, ground_serv_per_pass))
'''