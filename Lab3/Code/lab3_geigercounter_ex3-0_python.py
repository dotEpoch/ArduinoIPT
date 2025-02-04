# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:53:32 2025

@author: dsedgh, vaucoi
"""

import serial
import time
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# ----------- Init ------------- #
try:
    ser = serial.Serial(port = 'COM5', baudrate = 115200)
    time.sleep(3)
except: 
    os.system("ser.close()")
    ser = serial.Serial(port = 'COM5', baudrate = 115200)
    time.sleep(3)

print("port opened")

# ----------- Clear ------------ #
ser.reset_input_buffer()
ser.reset_output_buffer()
time.sleep(1)

# ------------ File -------------#

    # Add a check if file exists
    
#if os.path.isfile("ButtonPress.txt"): 
 #   print("File already exists. Overwrite?")
  #  print("--> Yes haha")
   # text_file = open("ButtonPressreal.txt", "w")
#else:
    
date_format = datetime.now().strftime("%Y-%m-%d-%Hh%Mm%Ss")

text_file = open("P:\ArduinoIPT\Lab3\Data\lab3_data_CPI(30mm)_{0}.txt".format(date_format), "w")
data_points = []
end_time = time.time() + 900 # Record data for 10 minutes

# ------------ Comms ------------#
while(time.time() < end_time):
    ser.flush()
    time.sleep(0.3)

    
    if (ser.in_waiting > 0):

        # Text file
        count_raw = ser.read_until(','.encode()).decode('utf-8')
        print(count_raw)
        text_file.write(count_raw)

    
        # Histogram
        count = int(count_raw[:-1])
        data_points.append(count)
        
        #stdout
        print("_____________________Data point_______________________")
        print("\t Number of geiger clicks in 1.00s:", count, "data points") if type(count) is int else print("[COUNT ERROR]")


# Plotting
counts, bins = np.histogram(data_points)
plt.stairs(counts, bins, fill=True)
plt.savefig("P:\ArduinoIPT\Lab3\Hist\lab3_hist_CPI(30mm)_{0}.png".format(date_format)) # plus or minus 5mm
plt.show()  


print("Number of data points:", len(data_points))
        

# --------- Close ---------#
text_file.close()
ser.close()
