# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:04:45 2025

@author: vaucoi
"""

import serial
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from waiting import wait

import step_control


# ----------- INIT/Clear ------------ #

ser = serial.Serial(port = 'COM5', baudrate = 115200, timeout=10.0)        
print("port opened")

try:
    print(step_control.ping_voltage(ser))
    
    
    
    
    
except Exception as e:
    print("ERROR", type(e).__name__, e)
finally:
    ser.close()
    

""" !!!!! IMPORTANT !!!!!
    Ambient light is 80mV (30mV with laser off, -50mV with blocked photodiode)
"""
