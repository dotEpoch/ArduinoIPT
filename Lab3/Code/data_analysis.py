# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 22:27:32 2025

@author: vince
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
from scipy import interpolate
from itertools import zip_longest

import analysis_helper

"""
Part I: Logistics and data extraction.
"""
# Declare path of all the data files.
paths = [
    #     r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_LOWER_200s_(178_5mm)_sample2_interval1s_2025-02-05-14h31m32s.txt",
    # r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_LOWER_200s_(178_5mm)_sample3_interval1s_2025-02-05-15h19m22s.txt",
    # r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_LOWER_200s_(178_5mm)_sample4_interval1s_2025-02-05-14h48m55s.txt",
    # r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_LOWER_200s_(178_5mm)_sample5_interval1s_2025-02-05-14h58m45s.txt",
    # r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_LOWER_200s_(178_5mm)_sample1_interval1s_2025-02-05-15h09m32s.txt"
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_HIGH_200s_(30mm)_sample3_interval1s_2025-02-05-12h49m17s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_HIGH_200s_(30mm)_sample4_interval1s_2025-02-05-12h53m31s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_HIGH_200s_(30mm)_sample5_interval1s_2025-02-05-12h58m05s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_HIGH_200s_(30mm)_sample6_interval1s_2025-02-05-13h02m42s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_HIGH_200s_(30mm)_sample1_interval1s_2025-02-05-12h39m11s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_CPI_HIGH_200s_(30mm)_sample2_interval1s_2025-02-05-12h44m10s.txt"
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
Part III: Plot the total collapsed 
"""
replica_bins = []

#plot histograms and bins
for i in range(len(data)):
    
    counts, bins = analysis_helper.get_countbins(data[i], 178.5, sum(data[i]), f"Lower meaned Sample{i+1}", 1, edge='black')
    print(f"counts{i}: ", counts)
    print(f"bins{i}: ", bins)
    
    replica_bins.append(counts)
    
    analysis_helper.plot_gaussian(counts, bins) 
    analysis_helper.plot_poisson(counts, bins)
    plt.show()
    
    
    print(analysis_helper.expected_value(counts, bins))
    print(analysis_helper.variance(counts, bins))


## get expected value and variance
print("replica", replica_bins)
count_bins = list(zip_longest(*replica_bins, fillvalue=0))
print("count_bins", count_bins)

bin_average = lambda x: sum(x)/len(x)
average_bins = list(map(bin_average, count_bins))
print(average_bins)

bin_variance = lambda x: sum(list(map(lambda y: y**2, x)))/len(x) - (sum(x)/len(x))**2
variance_bins = list(map(bin_variance, count_bins))
print(variance_bins)



"""
Part IV: Plot the total collapsed 
"""

data_set = np.concatenate(list(data.values()))
print("WE ARE IN FINAL COLLAPSED GRAPH:", len(data_set), data_set)

collapsed_count, collapsed_bins = analysis_helper.get_countbins(data_set, 178.5, sum(data_set), "LOWER mean collapsed samples", 1, edge='black')

analysis_helper.plot_gaussian(collapsed_count, collapsed_bins) 
analysis_helper.plot_poisson(collapsed_count, collapsed_bins)

plt.errorbar(
    collapsed_bins[:-1],  # Use left bin edges directly
    collapsed_count[:-1],
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

print(analysis_helper.expected_value(counts, bins))
print(analysis_helper.variance(counts, bins))




























