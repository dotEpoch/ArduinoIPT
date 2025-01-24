# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:38:48 2025

@author: vaucoi
"""

import serial
import time

ser = serial.Serial(port = 'COM5', baudrate = 115200)
time.sleep(3)
print("port opened")

# ----------- Clear ------------ #
ser.reset_input_buffer()
ser.reset_output_buffer()

# ------------ File -------------#
text_file = open("Output.txt", "w")

# ------------ Comms ------------#
ser.write('t'.encode())
time.sleep(1)

print("Bytes in input buffer: ", ser.in_waiting)

while (ser.in_waiting > 0):
    message = ser.read_until(','.encode()).decode('utf-8')
    print(message)
    text_file.write(message)
    time.sleep(1)

# --------- Close ---------#
text_file.close()
ser.close()


