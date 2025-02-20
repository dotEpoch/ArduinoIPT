# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:58:58 2025

@author: vaucoi
"""

import serial
import time
from datetime import datetime
from waiting import wait

def wait_until(condition):
    while True:
        if (condition): break
        
    

def main(ser):
    
    # ----------- INIT/Clear ------------ #
    wait(lambda: ser.in_waiting == 104, timeout_seconds=10)
    print("done Initalizing")
    
    ser.reset_input_buffer()
    ser.reset_output_buffer()
    time.sleep(1)
    
    # ------------ Comms ------------#
    
    repetitions = 200
    #voltage_array = np.array()
    full_voltage = []
    full_data_list = []
    for i in range(repetitions): #do 5 times
    
        step = 1 # int(input("Number of steps to send: "))
        
        # start_volt = ping_voltage(ser)
        # print("Starting Voltage:", start_volt)
        # ser.flush()
        # time.sleep(0.3)
        
        #send
        ser.write('{0}'.format(step).encode('utf-8'))
        #time.sleep(0.1)
        wait(lambda: ser.in_waiting > 0, sleep_seconds=0.5, timeout_seconds=5) # wait for command to reach arduino

        # Text file
        movement_raw = ser.readline().decode('utf-8')[:-3]
        #movement_raw = ser.read_until().decode('utf-8')[:-3]
        #wait(lambda: ser.in_waiting == 0, sleep_seconds=0.0001, timeout_seconds=5)
        #voltage_list = movement_raw
        #voltage_list = list(map(int(), movement_raw.split(',')))
        full_voltage.append(movement_raw)
        #print(len(voltage_list))
        
        # end_volt = ping_voltage(ser)
        # print("Ending Voltage:", end_volt)
        # voltage_bounds = f"({start_volt}, {end_volt})\n"
        # print(voltage_bounds)
        
        full_data_list.append(movement_raw + "\n")
        #print(full_data)
        
        
    
    #print(full_voltage) 
    text_file.write(''.join(full_data_list)) 
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
    text_file = open("P:\ArduinoIPT\Lab4\Data\Brewster\lab4_Q3_1stepsX200_startMin_sample2_{0}.txt".format(date_format), "w")
    
    try:
        #print("Starting Voltage:", ping_voltage(ser))
        main(ser)
    except Exception as e: 
        ser.close()
        print("ERROR", type(e).__name__, e)
    finally:
        text_file.close()
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        ser.close()
    


