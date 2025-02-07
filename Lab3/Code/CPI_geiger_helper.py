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

def main(ser, points, dist, mean, curr):

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
    
    text_file = open("P:\ArduinoIPT\Data\Misc\lab3_data_CPI_{4}_{2}s_({1}mm)_sample{3}_interval1s_{0}.txt"\
                     .format(date_format, dist, points, curr, mean), "w")
    data_points = []
    end_time = time.time() + points # Record data for 10 minutes
    
    # ------------ Comms ------------#
    while(time.time() < end_time):
        ser.flush()
        time.sleep(0.3)
    
        
        if (ser.in_waiting > 0):
    
            # Text file
            count_raw = ser.read_until(','.encode()).decode('utf-8')
            print(count_raw)
            text_file.write(count_raw)
    
            # data_array
            count = int(count_raw[:-1])
            data_points.append(count)
            
            #stdout
            print("_____________________Data point_______________________")
            print("\t Number of geiger clicks in 1.00s:", count, "data points") \
                if type(count) is int else print("[COUNT ERROR]")
    
    print("Number of data points:", len(data_points))
    
    # --------- Close ---------#
    text_file.close()
    return data_points



if __name__ == '__main__':
    try:
        main()
    except: 
        os.system("ser.close()")
        main()
    print("port opened")


