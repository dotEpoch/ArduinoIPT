# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:53:32 2025

@author: dsedgh, vaucoi
"""

import serial
import time
import os
#import sys

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
    
if os.path.isfile("ButtonPress.txt"): 
    print("File already exists. Overwrite?")
    print("--> Yes haha")
    text_file = open("ButtonPress.txt", "w")
else:
    text_file = open("ButtonPress.txt", "a")

# ------------ Comms ------------#
while(True):
    time.sleep(1)
    print("Bytes in input buffer: ", ser.in_waiting)
    
    if (ser.in_waiting > 0):
        ser.flush()
        
        #packet = ser.read_until('><'.encode()).decode('utf-8')
        #print(packet)
        #time.sleep(3)
        
        count_raw = ser.read_until(','.encode()).decode('utf-8')
        print(count_raw)
        time.sleep(1)
        voltage_raw = ser.read_until(','.encode()).decode('utf-8')
        print(voltage_raw)
        time.sleep(1)
        elapsed_time_raw = ser.read_until().decode('utf-8')
        print(elapsed_time_raw)
        time.sleep(1)
        
        data_packet = count_raw + voltage_raw + elapsed_time_raw
        
        count = int(count_raw[:-1])
        voltage = float(voltage_raw[:-1])
        elapsed_time = float(elapsed_time_raw[:-1])
        
        print("_____________________Data point_______________________")
        print("\t Number of button presses:", count, "data points") if type(count) is int else print("[COUNT ERROR]")
        print("\t Measured Voltage:", voltage, "V" ) if type(voltage) is float else print("[VOLTAGE ERROR]") 
        print("\t Time of measurement:", elapsed_time, "s") if type(elapsed_time) is float else print("[TIMER ERROR]")
    
        
        # ------------ Write -------------#
        data_packet = data_packet[:-1]
        text_file.write("<"+ data_packet + ">\n")
        

# --------- Close ---------#
text_file.close()
ser.close()