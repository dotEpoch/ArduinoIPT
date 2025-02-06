# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:19:07 2025

@author: vaucoi
"""
import serial
import time
import IPC_geiger_helper
import CPI_geiger_helper


# # ----------- Init ------------- #
ser = serial.Serial(port = 'COM5', baudrate = 115200)
time.sleep(3)
print("port open")

# # ----------- Clear ------------ #
ser.reset_input_buffer()
ser.reset_output_buffer()
time.sleep(1)


### Functions ###

#Get user input -> IPC or CPI
def start_collection(points, dist, mean):
    try: 
        mode = input("Input data collection mode (CPI or IPC): ")
        
        if (mode == "CPI"):
            #ser.write('c'.encode())
            time.sleep(1)
            #return CPI_geiger_helper
        elif (mode == "IPC"):
            #ser.write('t'.encode())
            time.sleep(1)
            #return IPC_geiger_helper
        else:
            raise Exception("Not a valid data collection mode.")
    except:
        start_collection()

def make_hist():
    return 0


def get_data():
    #-------- User Parameters ------------#
    num_points = input("Number of data points: ")
    distance = input("Distance of radioactive source: ") #for naming purposes
    mean = input("Mean category (HIGH, MID, LOWER): ") #for naming purposes
    data_array = start_collection(num_points, distance, mean)
    
    # --------- Plot ---------#
    
    #save histogram
    make_hist()
    
    return data_array
    

### Script ###

sample_number = input("Number of samples to collect: ")

for i in range(sample_number):
    data_array = get_data()



# --------- Analysis ---------#


# --------- Close ---------#
ser.close()
print("done")


