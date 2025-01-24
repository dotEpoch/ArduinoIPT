# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 14:50:52 2025

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


pack_number = 6
data_packet = ""

for packet in range(pack_number):
    print("Bytes in input buffer: ", ser.in_waiting)
    time.sleep(1)
    if (ser.in_waiting == 0): break

    message = ser.read_until(','.encode()).decode('utf-8')
    time.sleep(1)
    print(message)
    data_packet = data_packet+message

# ------------ File -------------#
text_file = open("Packet.txt", "w")
data_packet = data_packet[:-1]
text_file.write("<"+ data_packet + ">")

# --------- Close ---------#
text_file.close()
ser.close()
