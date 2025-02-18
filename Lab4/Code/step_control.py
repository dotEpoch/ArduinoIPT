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
from statistics import mean

def main(ser):
    
    # ----------- INIT/Clear ------------ #
    wait(lambda: ser.in_waiting == 104, timeout_seconds=10)
    print("done Initalizing")
    
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(1)
    
    # ------------ Comms ------------#
    
    
    
    repetitions = 400
    #voltage_array = np.array()
    full_voltage = []
    for i in range(repetitions): #do 5 times
    
        step = 1 # int(input("Number of steps to send: "))
        
        # start_volt = ping_voltage(ser)
        # print("Starting Voltage:", start_volt)
        ser.flush()
        time.sleep(0.3)
        
        ser.write('{0}'.format(step).encode('utf-8'))
        wait(lambda: ser.in_waiting > 0, timeout_seconds=5) # wait for command to reach arduino


        # Text file
        movement_raw = ser.readline().decode('utf-8')[:-2]
        wait(lambda: ser.in_waiting == 0, timeout_seconds=5)
        voltage_list = np.fromstring(movement_raw, dtype=int, sep=',')
        full_voltage.append(voltage_list)
        #print(len(voltage_list))
        
        # end_volt = ping_voltage(ser)
        # print("Ending Voltage:", end_volt)
        # voltage_bounds = f"({start_volt}, {end_volt})\n"
        # print(voltage_bounds)
        
        full_data = movement_raw[:-1] + "\n"
        print(full_data)
        
        text_file.write(full_data)
            
        
            
    
    print(full_voltage)
    return full_voltage


"""
        @ Functions @
"""

def ping_voltage(ser, ):
    
    # ----------- INIT/Clear ------------ #
    # wait(lambda: ser.in_waiting == 104, timeout_seconds=10)
    # print("done Initalizing")
    
    # ser.reset_input_buffer()
    # ser.reset_output_buffer()
    # time.sleep(0.5)
    
    # --- Ping --- #
    ser.write(b'1')
    wait(lambda: ser.in_waiting > 0, timeout_seconds=5)
    ser.write(b'-1')
    now = ser.readline().decode('utf-8')[:-3]
    #print("bump:", now, "=", get_voltage(now))
    
    wait(lambda: ser.in_waiting > 0, timeout_seconds=5)
    volt_ping = ser.readline().decode('utf-8')[:-3]
    print(volt_ping)
    
    return ( get_voltage(volt_ping) + get_voltage(now) )/ 2.0


def get_voltage(analog_read):
    ### Base voltage is 4.70 approx +- 2
    return float(analog_read)/1024 * 5.00 - 0.008
    

def find_zero():
    # binary search
    
    return 0




if __name__ == '__main__':
    ser = serial.Serial(port = 'COM5', baudrate = 115200, timeout=10.0)        
    print("port opened")
    
    # ------------ File -------------#
    date_format = datetime.now().strftime("%Y-%m-%d-%Hh%Mm%Ss")
    text_file = open("P:\ArduinoIPT\Lab4\Data\Malus\lab4_Q2.2_1stepsX400_sample2_{0}.txt".format(date_format), "w")
    
    try:
        #print("Starting Voltage:", ping_voltage(ser))
        main(ser)
    except Exception as e: 
        ser.close()
        print("ERROR", type(e).__name__, e)
    finally:
        text_file.close()
        ser.close()
    


