# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:04:45 2025

@author: vaucoi
"""

import serial
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from waiting import wait

import step_control

from laser_helper import *






print("replica", replica_bins)
count_bins = list(zip_longest(*replica_bins, fillvalue=0))
print("count_bins", count_bins)

bin_average = lambda x: sum(x)/len(x)
average_bins = list(map(bin_average, count_bins))
print(average_bins)

bin_variance = lambda x: sum(list(map(lambda y: y**2, x)))/len(x) - (sum(x)/len(x))**2
variance_bins = list(map(bin_variance, count_bins))
print(variance_bins)
    

if __name__ == '__main__':
    
    #path = "../lab4_1stepX400_2025-02-17-16h03m01s.txt"
    #path = "../Data/Malus/lab4_Q2.2_1stepsX400_sample1_2025-02-18-16h29m54s.txt"
    # path = "../Data/Malus/lab4_Q2.2_1stepsX400_sample3_2025-02-18-17h07m03s.txt"
    #path = "../Data/Malus/lab4_Q2.2_SpeedTest_sample0_2025-02-20-14h57m44s.txt"
    # path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample4_2025-02-21-14h39m53s.txt"
    # path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample3_2025-02-21-14h37m30s.txt"
    #path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample3_2025-02-21-14h37m30s.txt"
    #path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample6_2025-02-21-15h01m17s.txt"
    
    path = "../Data/Brewster/lab4_Q3_1stepsX100_quickSpin_sample1_2025-02-21-16h01m02s.txt"
    
    
    file = open(path, "r")
    data = extract_data(*file)
    

    # max_val = map(max, data)
    # print(max_val, np.where(data == max_val))
    
    try:
        for sample in data:
            make_plot(len(sample), sample)
    except Exception as e: 
        print("ERROR", type(e).__name__, e)
    finally:
        file.close()
        


""" !!!!! IMPORTANT !!!!!
    Ambient light is 80mV (30mV with laser off, -50mV with blocked photodiode)
"""
