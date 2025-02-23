# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:05:06 2025

@author: vaucoi
"""

import matplotlib.pyplot as plt
import numpy as np
import step_control
from scipy.optimize import curve_fit
from scipy import interpolate

def make_plot(angle, voltage):
    map(lambda: step_control.get_voltage, voltage)
    plt.scatter(angle, y=voltage, )
    
    
    plt.ylim(0)
    plt.title('Descriptive Title')
    plt.xlabel('Steps taken (will become Angle)')
    plt.ylabel('Voltage')
    plt.legend()

    
    
def extract_data(*filename):
    full_data = []    
    # currline = ''
    
    # def get_line():
    #     currline = filename.readline()
        
    #     if (currline == ''): return False
    
    # while (get_line()):
    #     full_data.append(np.fromstring(currline, dtype=int, sep=','))
    
    for curr in filename:
        full_data.append(np.fromstring(curr, dtype=int, sep=','))
    
    return full_data

def expected_value(points):
    expected = 1/sum(points)*sum(points)
    return expected

def fit_fresnel(angles, sample):
    
    def fresnel_fit(angle, n1, n2, voltage_coefficient):
        #n1 = 1.00 #refrac_air
        #n2 = 1.5 #refrac_glass
        n = n2/n1
        
        transmit = np.arcsin(n1*np.sin(angle)/n2)
        
        numerator = 2.0*n*np.cos(angle)
        denominator = np.sqrt(n2**2.0-np.sin(angle)**2) + n**2.0*np.cos(angle)
        
        result = n*abs(numerator / denominator)**2.0 * np.cos(transmit)/np.cos(angle) * voltage_coefficient
        # plt.plot(angle, result)
        # plt.show()
        return result

    
    #calculate curve
    popt, pcov = curve_fit(fresnel_fit, angles, sample, bounds=([0.8, 1, 800], [1.2, 1.7, 1000]), p0=[0.9, 1.6, 4.7/5.0*1024])
    print('popt:', popt)
    print('pcov:', pcov)

    # Draw Interpolated new points
    #width = int(bins[-1])
    x_fresnel = np.linspace(0, angles[-1], 90)
    bspline = interpolate.make_interp_spline(angles, fresnel_fit(angles, *popt), k=2)
    y_fresnel = bspline(x_fresnel)
    plt.plot(x_fresnel, y_fresnel, color='red')
    
    max_val = max(sample)
    max_pos=[]
    for val in np.where(np.array(sample) == max_val)[0]:
        max_pos.append(np.radians(val*0.9))
    
    print(max_val, "@", max_pos)
    
    return (max_val, max_pos)


if __name__ == '__main__':
    
    #path = "../lab4_1stepX400_2025-02-17-16h03m01s.txt"
    #path = "../Data/Malus/lab4_Q2.2_1stepsX400_sample1_2025-02-18-16h29m54s.txt"
    # path = "../Data/Malus/lab4_Q2.2_1stepsX400_sample3_2025-02-18-17h07m03s.txt"
    #path = "../Data/Malus/lab4_Q2.2_SpeedTest_sample0_2025-02-20-14h57m44s.txt"
    # path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample4_2025-02-21-14h39m53s.txt"
    #path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample3_2025-02-21-14h37m30s.txt"
    #path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample3_2025-02-21-14h37m30s.txt"
    #path = "../Data/Brewster/lab4_Q3_1stepsX100_newPolar_sample6_2025-02-21-15h01m17s.txt"
    
    path = "../Data/Brewster/lab4_Q3_1stepsX100_quickSpin_sample1_2025-02-21-16h01m02s.txt"

    
    file = open(path, "r")
    data = extract_data(*file)
    
    try:
        for sample in data:
            
            angles = list(map( lambda x: np.radians(x*0.9) , np.arange(0, len(sample), 1) ))
            
            make_plot(angles, sample)
            max_val, max_pos = fit_fresnel(angles, sample)
            avg_brew = round(np.mean(max_pos), 3)
            
            plt.annotate(r'$\theta_p = {0}$'.format(avg_brew), xy=(avg_brew, 100), va='bottom')
            plt.axvline(x=avg_brew, color='green', linestyle='--')
            plt.show()
    # except Exception as e: 
    #     print("ERROR", type(e).__name__, e)
    finally:
        file.close()
    
    
    