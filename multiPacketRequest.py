# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 15:12:47 2025

@author: vaucoi
"""

import serial
import time

#pack_number = readline()

ser = serial.Serial(port = 'COM5', baudrate = 115200)
time.sleep(3)
print("port opened")

# ----------- Clear ------------ #
ser.reset_input_buffer()
ser.reset_output_buffer()
time.sleep(1)

# ------------ Comms ------------#
ser.write('t'.encode())
time.sleep(1)


print("Bytes in input buffer: ", ser.in_waiting)
    
string_message = ser.read_until(','.encode()).decode('utf-8')
print(string_message)
time.sleep(1)
int_message = ser.read_until(','.encode()).decode('utf-8')
print(int_message)
time.sleep(1)
float_message = ser.read_until(','.encode()).decode('utf-8')
print(float_message)
time.sleep(1)

data_packet = string_message + int_message + float_message

int_data = int(int_message[:-1])
float_data = float(float_message[:-1])

if type(string_message) is str: print("First field is a string")
if type(int_data) is int: print("Second field is an int")
if type(float_data) is float: print("Third field is a float")

    
# ------------ File -------------#
text_file = open("MultiPacket.txt", "w")
data_packet = data_packet[:-1]
text_file.write("<"+ data_packet + ">")

# --------- Close ---------#
text_file.close()
ser.close()
