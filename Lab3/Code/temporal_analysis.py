# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 17:21:39 2025

@author: vince
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
from scipy import interpolate
import os
from itertools import zip_longest

import analysis_helper


"""
Part I: Logistics and data extraction.
"""
# Declare path of all the data files.
cwd = os.getcwd()

paths1 = [
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample1__2025-02-06-13h16m35s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample2__2025-02-06-13h18m35s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample3__2025-02-06-13h19m56s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample4__2025-02-06-13h22m40s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample5__2025-02-06-13h24m15s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample6__2025-02-06-13h28m28s.txt"
    ]

paths = [
       r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_10000clicks_(30mm)_sampleBIG__2025-02-07-14h26m34s.txt"
       #r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_10000clicks_(130mm)_sampleBIG__2025-02-07-13h03m52s.txt"
       ]


# Read the content of the data files and put in string_data dictionary.
string_data = {}
for i in range(len(paths)):
    with open(paths[i], "r") as doc:
        content = doc.read()
        string_data[i] = content.split(',')
        print(f"String data {i+1}: ", string_data[i])
# All the data is now put in a dictionary as lists with string values.


# We would like to now turn the string values inside the lists as integer values.
data = {}
for index in range(len(string_data)):
    if string_data[index][-1] == '':
        string_data[index].pop() # Deletes that pesky ''.
        
    for j in range(len(string_data[index])):
        string_data[index][j] = int(string_data[index][j])
    data[index] = string_data[index]

print("Data dictionnary: ", data)
for i in range(len(data)):
    print("Data ", i + 1, data[i])
    
"""
Part II: Split list 
# """

# Define a list of integers from 1 to 15


# Define the chunk size for splitting the list
chunk_amount = 100 #20

# Create a list of empty lists, one for each chunk
sample_list = [[] for _ in range(chunk_amount)]

# Iterate over the elements and their indices in my_list
for index, value in enumerate(data[0]):
    # Calculate the index of the sublist where the current value should go using modulo operation
    sublist_index = index % chunk_amount
    
    # Append the current value to the corresponding sublist in split_list
    sample_list[sublist_index].append(value)

"""
Part III: Plot the total collapsed 
# """

# bin_size = 10
# for i in range(len(data)):
    
#     counts, bins = analysis_helper.get_countbins(data[i], 178.5, 200, f"LOWER meaned Sample{i+1}", bin_size,edge=None)
    
#     analysis_helper.plot_exponential(counts, bins) 
#     plt.show()
    
#     print(analysis_helper.expected_value(counts, bins))
#     print(analysis_helper.variance(counts, bins))
    
bin_size = 10 #10
replica_bins = []
for sample_data in sample_list:
    
    counts, bins = analysis_helper.get_countbins(sample_data, 178.5, 10000/chunk_amount, f"LOWER meaned Sample{i+1}", bin_size,edge=None)
    
    replica_bins.append(counts)
    analysis_helper.plot_exponential(counts, bins) 
    plt.show()
    
    print(analysis_helper.expected_value(counts, bins))
    print(analysis_helper.variance(counts, bins))
    

#print("replica", replica_bins)
count_bins = list(zip_longest(*replica_bins, fillvalue=0))
#print("count_bins", count_bins)

bin_average = lambda x: sum(x)/len(x)
average_bins = list(map(bin_average, count_bins))
#print(average_bins)


bin_variance = lambda x: sum(list(map(lambda y: y**2, x)))/len(x) - (sum(x)/len(x))**2
variance_bins = list(map(bin_variance, count_bins))
#print(variance_bins)



"""
Part IV: Plot the total collapsed 
"""

#create collapsed histogram
data_set = np.concatenate(list(data.values()))
print(len(data_set), data_set)

collapsed_counts, collapsed_bins = analysis_helper.get_countbins(data_set, 178.5, 10000, "LOWER meaned Temporal distribution", bin_size,edge=None)

analysis_helper.plot_exponential(collapsed_counts, collapsed_bins)
plt.errorbar(
    collapsed_bins,  # Use left bin edges directly
    collapsed_counts,
    yerr=variance_bins,
    fmt='o',
    color='black',
    capsize=4,                   # Length of caps (horizontal lines)
    capthick=1,                  # Thickness of cap lines
    elinewidth=1,
    markersize=4,
    label='Error bars'
)
plt.show()

plt.bar(collapsed_bins, average_bins, width=10)
width = int(bins[-1])+1
plt.xlim(int(bins[0]), width)
plt.ylim(0)
plt.title('{Average  temporal histogram for {collapsed datapoints @ 130mm')
plt.xlabel('Clicks per Interval')
plt.ylabel('Occurrences')
plt.legend()

plt.errorbar(
    collapsed_bins,  # Use left bin edges directly
    average_bins,
    yerr=variance_bins,
    fmt='o',
    color='black',
    capsize=4,                   # Length of caps (horizontal lines)
    capthick=1,                  # Thickness of cap lines
    elinewidth=1,
    markersize=4,
    label='Error bars'
)
plt.show()




























