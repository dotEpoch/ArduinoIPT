# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 12:51:37 2025

@author: vaucoi
"""

import serial
import time
import os
from datetime import datetime

### Functions ###

def main(ser, points, dist, mean, curr):

    # ----------- Clear ------------ #
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(1)
    
    # ------------ File -------------#
    
    date_format = datetime.now().strftime("%Y-%m-%d-%Hh%Mm%Ss")
    text_file = open("P:\ArduinoIPT\Lab3\Data\lab3_data_IPC_{4}_{2}clicks_({1}mm)_sample{3}__{0}.txt"\
                     .format(date_format, dist, points, curr, mean), "w")
    data_points = []
    
    # ------------ Comms ------------#
    while(len(data_points) < points):
        ser.flush()
        
        if (ser.in_waiting > 0):
    
            # Text file
            time_interval_raw = ser.read_until(','.encode()).decode('utf-8')
            print(time_interval_raw)
            #text_file.write(time_interval_raw)
    
        
            # Histogram
            time_interval = int(time_interval_raw[:-1])
            data_points.append(time_interval)
            
            #stdout
            print("_____________________Data point_______________________")
            print("\t Number of time elapsed since last click:", time_interval, "ms") if type(time_interval) is int else print("[COUNT ERROR]")
            

    print("Number of data points:", len(data_points))
    print(data_points)
    
    # --------- Close ---------#
    text_file.close()
    return data_points


### Script ###

if __name__ == '__main__':
    try:
        main()
    except: 
        os.system("ser.close()")
        main()
    print("port opened")