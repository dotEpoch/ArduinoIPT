# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 13:19:07 2025

@author: vaucoi
"""
import serial
import time
import IPC_geiger_helper
import CPI_geiger_helper
import test_helper


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
def start_collection(points, dist, mean, curr_sample):
    try: 

        
        if (mode == "CPI"):
            #ser.write('c'.encode())
            time.sleep(1)
            #return CPI_geiger_helper.main(ser, points, dist, mean)
        elif (mode == "IPC"):
            #ser.write('t'.encode())
            time.sleep(1)
            return IPC_geiger_helper.main(ser, points, dist, mean, curr_sample)
        else:
            raise Exception("Not a valid data collection mode.")
    except:
        start_collection()
        
#Make a histogram with data
def make_hist(data_points):
    print("lacking make histogram function")
    return 0

### Depreciated
def get_data(num_points, distance, mean):
    ## More stuff here?
    return start_collection(num_points, distance, mean)
    

                                ### Script ###

#------------- Intro --------------#
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("||           GeigerCounterV1.0         ||")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("--> How to Use: Input the following desired parameters for data collection.")
print("--> Output: The program saves the raw data as .txt (or .csv) files and produces respective histograms for each requested dataset")
print("\t ... (make sure the Arduino is plugged in and the geiger counter is ON)\n")

#-------- User Parameters ------------#
num_points = int(input("Number of data points (int): "))
distance = input("Distance of radioactive source (mm): ") #for naming purposes
mean = input("Mean category (HIGH, MID, LOWER): ") #for naming purposes
sample_number = int(input("Number of datasets to collect (int): "))
mode = input("Input data collection mode (CPI or IPC): ")

for i in range(sample_number):
    data_array = start_collection(num_points, distance, mean, i+1)
    print("Data Collected for sample{0}\n".format(i+1))
    
    # --------- Plot ---------#
    
    #save histogram
    make_hist(data_array)


# --------- Analysis ---------#


# --------- Close ---------#
ser.close()
print("done")


