# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:58:58 2025

@author: vaucoi
"""

import serial
import time
import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from waiting import wait

def main(ser):
    
    # ----------- INIT/Clear ------------ #
    wait(lambda: ser.in_waiting == 104, timeout_seconds=10)
    print("done Initalizing")
    
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(1)
    
    # ------------ File -------------#

    date_format = datetime.now().strftime("%Y-%m-%d-%Hh%Mm%Ss")
    text_file = open("P:\ArduinoIPT\Lab4\Limitations\lab4_testing_{0}.txt".format(date_format), "w")
    data_points = []
    
    
    # ------------ Comms ------------#
    repetitions = 5
    #voltage_array = np.array()
    full_voltage = []
    for i in range(repetitions): #do 5 times
        ser.flush()
        time.sleep(0.3)
        
        step = int(input("Number of steps to send: "))
        ser.write('{0}'.format(step).encode('utf-8'))
        wait(lambda: ser.in_waiting > 0, timeout_seconds=5) # wait for command to reach arduino

        while (ser.in_waiting > 0):
    
            # Text file
            movement_raw = ser.readline().decode('utf-8')[:-2]
            voltage_list = np.fromstring(movement_raw, dtype=int, sep=',')
            full_voltage.append(voltage_list)
            
            movement = movement_raw[:-1] + "\n"
            print(movement)
            text_file.write(movement)
            

    # --------- Close ---------#
    text_file.close()
    ser.close()
    
    print(full_voltage)
    return full_voltage


if __name__ == '__main__':
    ser = serial.Serial(port = 'COM5', baudrate = 115200, timeout=10.0)        
    print("port opened")
    
    try:
        main(ser)
    except Exception as e: 
        ser.close()
        print("ERROR", type(e).__name__, e)
    


