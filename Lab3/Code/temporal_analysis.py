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

import analysis_helper


"""
Part I: Logistics and data extraction.
"""
# Declare path of all the data files.
cwd = os.getcwd()

paths = [
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample1__2025-02-06-13h16m35s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample2__2025-02-06-13h18m35s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample3__2025-02-06-13h19m56s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample4__2025-02-06-13h22m40s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample5__2025-02-06-13h24m15s.txt",
    r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_200clicks_(178_5mm)_sample6__2025-02-06-13h28m28s.txt"
    ]

paths1 = [
       r"C:\Users\vince\zZ.Lab\ArduinoIPT\Lab3\Data\lab3_data_IPC_10000clicks_(30mm)_sampleBIG__2025-02-07-14h26m34s.txt"
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
# """
for i in range(len(data)):
    
    counts, bins = analysis_helper.get_countbins(data[i], 178.5, 200, f"LOWER meaned Sample{i+1}", 10,edge=None)
    
    analysis_helper.plot_exponential(counts, bins) 
    plt.show()
    
    print(analysis_helper.expected_value(counts, bins))
    print(analysis_helper.variance(counts, bins))
    
    
"""
Part IV: Plot the total collapsed 
"""

#create collapsed histogram
data_set = np.concatenate(list(data.values()))
print(len(data_set), data_set)

counts, bins = analysis_helper.get_countbins(data_set, 178.5, 1000, "LOWER meaned Temporal distribution", 10,edge=None)


analysis_helper.plot_exponential(counts, bins)




























