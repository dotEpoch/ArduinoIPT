# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import serial

ser = serial.Serial(port = "COM5", baudrate = 115200)

rgb = ['g', 'b', 'b', 'b', 'b']
count = 0


while (count != 10000000):
    count = count + 1
    ser.write('r'.encode())
    ser.write('g'.encode())
    ser.write('b'.encode())
    #ser.write(rgb[count % 5].encode())
    #print(rgb[count % 5])
    
    
    ser.write('t'.encode())
    mess = ser.read(2)
    if (mess != None):
        mess.decode('utf-8')