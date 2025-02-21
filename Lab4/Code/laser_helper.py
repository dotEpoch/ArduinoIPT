# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:05:06 2025

@author: vaucoi
"""

import matplotlib.pyplot as plt
import numpy as np
import step_control

def make_plot(angle, voltage):
    map(lambda: step_control.get_voltage, voltage)
    plt.scatter(x=np.arange(0, 99), y=voltage, )
    
    
    plt.ylim(0)
    plt.title('Descriptive Title')
    plt.xlabel('Steps taken (will become Angle)')
    plt.ylabel('Voltage')
    plt.legend()

    plt.show()
    
if __name__ == '__main__':
    
    #path = "../lab4_1stepX400_2025-02-17-16h03m01s.txt"
    #path = "../Data/Malus/lab4_Q2.2_1stepsX400_sample1_2025-02-18-16h29m54s.txt"
    # path = "../Data/Malus/lab4_Q2.2_1stepsX400_sample3_2025-02-18-17h07m03s.txt"
    #path = "../Data/Malus/lab4_Q2.2_SpeedTest_sample0_2025-02-20-14h57m44s.txt"
    # path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample4_2025-02-21-14h39m53s.txt"
    # path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample3_2025-02-21-14h37m30s.txt"
    path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample3_2025-02-21-14h37m30s.txt"
    #path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample6_2025-02-21-15h01m17s.txt"
    file = open(path, "r")
    current_data = np.fromstring(file.read(), dtype=int, sep='\n')
    print(current_data)
    max_val = max(current_data)
    print(max_val, np.where(current_data == max_val))
    
    try:
        make_plot([1,2,3,4,], current_data)
    except Exception as e: 
        print("ERROR", type(e).__name__, e)
    finally:
        file.close()
    
    
    