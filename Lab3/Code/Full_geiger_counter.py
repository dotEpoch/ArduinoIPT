# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:19:07 2025

@author: vaucoi
"""
import serial
import time
import IPC_geiger_helper
import CPI_geiger_helper


# ----------- Init ------------- #
ser = serial.Serial(port = 'COM5', baudrate = 115200)
time.sleep(3)

# ----------- Clear ------------ #
ser.reset_input_buffer()
ser.reset_output_buffer()
time.sleep(1)

#Get user input -> IPC or CPI
mode = input("Input data collection mode (CPI or IPC): ")


#run respective helper script with input: (number of data points, distance, number of repititions)

#Plot immediately from here

#Call analysis

