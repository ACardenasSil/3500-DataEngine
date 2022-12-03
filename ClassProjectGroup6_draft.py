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
    try:
        answer = mean_sum / mean_num
    except ZeroDivisionError:
        print("Error 103: Division by zero error")
    return answer
 
# finds the variance of a list of values
def variance(data_list, mean):
    var_sum = 0
    for i in data_list:
        var_sum += (i - mean) ** 2
    try:
        answer = var_sum / (len(data_list) - 1)
    except ZeroDivisionError:
        print("Error 103: Division by zero error")
    return answer

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
def find_month_delays(fname):
    month_delays = 12 * [0]
    months = []
    delays = []
    for row in loadFile(fname):
        months.append(row[0])
        delays.append(row[2])
    delay_c = 0
    for m in months:
        if m == "1":
            num = int(delays[delay_c])
            month_delays[0] += num
        elif m == "2":
            num = int(delays[delay_c])
            month_delays[1] += num
        elif m == "3":
            num = int(delays[delay_c])
            month_delays[2] += num
        elif m == "4":
            num = int(delays[delay_c])
            month_delays[3] += num
        elif m == "5":
            num = int(delays[delay_c])
            month_delays[4] += num
        elif m == "6":
            num = int(delays[delay_c])
            month_delays[5] += num
        elif m == "7":
            num = int(delays[delay_c])
            month_delays[6] += num
        elif m == "8":
            num = int(delays[delay_c])
            month_delays[7] += num
        elif m == "9":
            num = int(delays[delay_c])
            month_delays[8] += num
        elif m == "10":
            num = int(delays[delay_c])
            month_delays[9] += num
        elif m == "11":
            num = int(delays[delay_c])
            month_delays[10] += num
        elif m == "12":
            num = int(delays[delay_c])
            month_delays[11] += num
        delay_c += 1
    
    return month_delays

def most_delayed_month(month_list):
    index = 0
    most_delayed = 0
    most_index = 0

    for m in month_list:
        if m > most_delayed:
            most_delayed = m
            most_index = index
        index += 1

    dict_buf = { most_index + 1 : most_delayed }
    return dict_buf

#7
def find_day_delays(fname):
    day_delays = 7 * [0]
    days = []
    delays = []
    for row in loadFile(fname):
        days.append(row[1])
        delays.append(row[2])
    delay_c = 0
    for d in days:
        if d == "1":
            num = int(delays[delay_c])
            day_delays[0] += num
        elif d == "2":
            num = int(delays[delay_c])
            day_delays[1] += num
        elif d == "3":
            num = int(delays[delay_c])
            day_delays[2] += num
        elif d == "4":
            num = int(delays[delay_c])
            day_delays[3] += num
        elif d == "5":
            num = int(delays[delay_c])
            day_delays[4] += num
        elif d == "6":
            num = int(delays[delay_c])
            day_delays[5] += num
        elif d == "7":
            num = int(delays[delay_c])
            day_delays[6] += num
            delay_c += 1
    return day_delays
def most_delayed_day(day_list):
    index = 0
    most_delayed = 0
    most_index = 0

    for d in day_list:
        if d > most_delayed:
            most_delayed = d
            most_index = index
        index += 1

    dict_buf = { most_index + 1 : most_delayed }
    return dict_buf

#8
def organize_monthly_delays(fname, month1, month2, month3):
    d_log = {}
    # read_info[i][0] = month
    # read_info[i][1] = carrier name
    months = []
    carr_names = []
    delays = []
    delay_c = 0
    for row in loadFile(fname):
        months.append(row[0])
        carr_names.append(row[8])
        delays.append(row[2])
    for m in months:
        if m == month1 or m == month2 or m == month3:
            if delays[delay_c] == "1":
                if carr_names[delay_c] in d_log:
                    d_log[carr_names[delay_c]] += 1
                else:
                    dict_buf = {carr_names[delay_c] : 1}
                    d_log.update(dict_buf)
        delay_c += 1
    return d_log

def find_most_delayed_airline(d_log):
    most_delayed = ""
    hi_delays = 0
    for i in d_log:
        if (d_log[i] > hi_delays):
            hi_delays = d_log[i]
            most_delayed = i
    return most_delayed

#9
def find_avg_plane_age(fname, carrier_name):
    delays = []
    carr_names = []
    plane_ages = []

    avg_age = 0
    plane_count = 0
    age_c = 0

    for row in loadFile(fname):
        delays.append(row[2])
        carr_names.append(row[8])
        plane_ages.append(row[16])

    for d in delays:
        if carr_names[age_c] == carrier_name and d == "1":
            avg_age += int(plane_ages[age_c])
            plane_count += 1
        age_c += 1
    try:
        answer = avg_age / plane_count
    except ZeroDivisionError:
        print("Error 103: Division by zero error")

    return answer
#10
def snow_delay(fname):
    delays = []
    snow_inches = []
    snow_c = 0
    # read_info[i][0] = delay
    # read_info[i][1] = inches of snow
    count_of_planes = 0
    for row in loadFile(fname):
        delays.append(row[2])
        snow_inches.append(row[22])
    for d in delays:
        if float(snow_inches[snow_c]) >= 15.0:
            if d == "1":
                count_of_planes += 1
        snow_c += 1
    return count_of_planes
#2
def collect_airports(fname):
    alist = {}
    airports = []
    delays = []
    airport_c = 0

    for row in loadFile(fname):
        airports.append(row[17])
        delays.append(row[2])
    for a in airports:
        if delays[airport_c] == "1":
            if a in alist:
                alist[a] += 1
            else:
                dict_buf = {a : 1}
                alist.update(dict_buf)
        airport_c += 1
    return alist
#11
def top_5_airports(alist):
    new_dict = { }
    for h in range(5):
        most_delays = 0
        most_delayed_airport = '0'
        for i in alist:
            if alist[i] > most_delays:
                most_delays = alist[i]
                most_delayed_airport = i
        dict_buf = {most_delayed_airport : most_delays}
        new_dict.update(dict_buf)
        del alist[most_delayed_airport]
    return new_dict

def count_airlines(fname):
    airlines = []
    air_count = 0
    air_list = []
    for row in loadFile(fname):
        airlines.append(row[8])
    for a in airlines:
        if a not in air_list:
            air_count += 1
            air_list.append(a)
    return air_count

def sort_airlines(fname):
    sorted_list = []
    airlines = []
    for row in loadFile(fname):
        airlines.append(row[8])
    for i in range(5):
        sorted_list.append(airlines[i])
    sorted_list.sort()
    return sorted_list 

def count_airports(fname):
    airports = []
    air_count = 0
    air_list = []
    for row in loadFile(fname):
        airports.append(row[17])
    for a in airports:
        if a not in air_list:
            air_count += 1
            air_list.append(a)
    return air_count

def sort_airports_bottom(fname):
    sorted_list = []
    airports = []
    for row in loadFile(fname):
        airports.append(row[17])
    list_len = len(airports)
    for i in range(list_len - 1, list_len - 6, -1):
        sorted_list.append(airports[i])
    sorted_list.sort()

    return sorted_list

def airline_age_dict(fname):
    #read_info[i][0] = carrier name
    #read_info[i][1] = plane age
    airlines = []
    plane_age = []
    airline_dict = {}
    age_c = 0

    for row in loadFile(fname):
        airlines.append(row[8])
        plane_age.append(row[16])
    for a in airlines:
        dict_buf = {a : plane_age[age_c]}
        airline_dict.update(dict_buf)
        age_c += 1
    return airline_dict

def list_of_oldest_planes(airline_dict):
    sorted_dict = { }
    for h in range(5):
        oldest_airline = ""
        oldest = 0
        for i in airline_dict:
            if int(airline_dict[i]) > oldest:
                oldest = int(airline_dict[i])
                oldest_airline = i
        dict_buf = {oldest_airline : oldest}
        sorted_dict.update(dict_buf)
        del airline_dict[oldest_airline]
    return sorted_dict

def get_oldest_airline(sorted_dict):
    for key in sorted_dict:
        return key

def analyze(column):
    
    for number in column:
        isOfNumber(number)

    a = count(column)
    b = unique(column)
    c = mean(column)
    d = median(column)
    e = mode(column)
    f = variance(column, c)
    g = std_dev(f)
    h = per_20(column)
    i = per_40(column)
    j = per_50(column)
    k = per_60(column)
    l = per_80(column)
    list_of_answers = [a, b, c, d, e, f, g, h, i, j, k, l]
    
    return list_of_answers
    

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

def file_solver(fname):
    a_names = []
    a_mon_p = []
    flight_a = []
    g_serv = []
    dep_airports = []
    amp_airport = []

    for row in loadFile(fname):
        a_names.append(row[8])
        a_mon_p.append(row[13])
        flight_a.append(row[14])
        g_serv.append(row[15])
        dep_airports(row[17])
        amp_airport(row[12])
    
    top_5_airport_passengers(dep_airports, amp_airport)
    top_5_airline_employees(a_names, a_mon_p, flight_a, g_serv)

def solve_reqs(fname):
    month_delay_list = find_month_delays(fname)
    day_delay_list = find_day_delays(fname)
    delayed_airlines = organize_monthly_delays(fname, "1","7", "12")
    most_delayed_airline = find_most_delayed_airline(delayed_airlines)
    average_delay_age = find_avg_plane_age(fname, "American Airlines Inc.")
    num_of_snow_planes = snow_delay(fname)
    list_of_airports = collect_airports(fname)
    top_5 = top_5_airports(list_of_airports)
    num_of_airlines = count_airlines(fname)
    t5_airlines = sort_airlines(fname)
    num_of_airports = count_airports(fname)
    b5_airports = sort_airports_bottom(fname)
    airline_ages = airline_age_dict(fname)
    sorted_airlines_by_age = list_of_oldest_planes(airline_ages)
    old_airline = get_oldest_airline(sorted_airlines_by_age)
    mdm = most_delayed_month(month_delay_list)
    mdd = most_delayed_day(day_delay_list)
    top_5_pass = top_5_airport_passengers(fname)
    top_employees = top_5_airline_employees(fname)

    print("Data Analysis:")
    print("**************")

    print("How many airlines are included in the data set? Print the first 5 in alphabetical order.")
    print(num_of_airlines)
    print(t5_airlines)

    print("How many departing airports are included in the data set? Print the last 5 in alphabetical order.")
    print(num_of_airports)
    print(b5_airports)

    print("What airline has the oldest plane? Print the 5 airlines that have the 5 oldest planes recorded.")
    print(old_airline)
    print(sorted_airlines_by_age)

    # TODO: 4 and 5

    print("What was the month of the year in 2019 with most delays overall? And how many delays were recorded in that month?")
    print(mdm)

    print("What was the day of the year in 2019 with most delays overall? And how many delays were recorded in that day?")
    print(mdd)

    print("What airline carrier experience the most delays in January, July and December?")
    print(most_delayed_airline)

    print("What was the average plane age of all planes with delays operated by American Airlines inc.")
    print(average_delay_age)

    print("How many planes were delayed for more than 15 minutes during days with \"heavy snow\" (Days when the inches of snow on ground were 15 or more)?")
    print(num_of_snow_planes)

    print("What are the 5 airports (Departing Airports) that had the most delays in 2019? Print the airports and the number of delays")
    print(top_5)

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