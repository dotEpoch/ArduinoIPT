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
from itertools import zip_longest
import scienceplots

def make_plot(angle, voltage):
    map(lambda: step_control.get_voltage, voltage)
    plt.scatter(np.degrees(angle), y=voltage, label='Data')
    
    
    plt.ylim(0)
    plt.title("Transmitted Energy from Oblique Incident Beam on Glass Interface")
    plt.xlabel(r'Angle $\theta$ (degrees °)')
    plt.ylabel('Voltage (mV)')
    plt.grid()
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


def fresnel_fit(angle, n1, n2, voltage_coefficient):
    #n1 = 1.00 #refrac_air
    #n2 = 1.5 #refrac_glass
    n=n2/n1
    transmit = np.arcsin(n1*np.sin(angle)/n2)
    normal = 2*n1/(n2+n1) * voltage_coefficient
    print(normal)
    
    # numerator = n1*np.sqrt(1 - (1/n*np.sin(angle))**2) - n2*np.cos(angle)
    # denominator = n1*np.sqrt(1 - (1/n*np.sin(angle))**2) + n2*np.cos(angle)
    # result = 1-(numerator/denominator)**2
    
    numerator = n2*np.cos(angle) - n1*np.cos(transmit)
    denominator = n2*np.cos(angle) + n1*np.cos(transmit)
    result = 1-abs(numerator/denominator)**2
    
    
    
    # n = n2/n1
    # transmit = np.arcsin(n1*np.sin(angle)/n2)
    
    # numerator = 2.0*n*np.cos(angle)
    # denominator = np.sqrt(n2**2.0-np.sin(angle)**2.0) + n**2.0*np.cos(angle)
    # result = n*abs(numerator / denominator)**2.0 * np.cos(transmit)/np.cos(angle)
    
    # plt.plot(angle, result)
    # plt.show()
    return result * voltage_coefficient

def fit_fresnel(angles, sample):
    
    #find parameters
    max_val = max(sample)
    max_pos=[]
    for val in np.where(np.array(sample) == max_val)[0]:
        max_pos.append(np.radians(val*0.9))
    print(max_val, "@", max_pos)  
    avg_brew = round(np.mean(max_pos), 3)
    ratio = np.tan(avg_brew)

    #calculate curve
    popt, pcov = curve_fit(fresnel_fit, angles, sample, bounds=([0.9, 1.4, 2000], [1.1, 1.8, 5000]), p0=[1.0, 1.5, max_val])
    print('popt:', popt)
    print('pcov:', pcov)

    # Draw Interpolated new points
    #width = int(bins[-1])
    x_fresnel = np.linspace(0, angles[-1], 90)
    bspline = interpolate.make_interp_spline(angles, fresnel_fit(angles, *popt), k=2)
    y_fresnel = bspline(x_fresnel)
    plt.plot(np.degrees(x_fresnel), y_fresnel, color='red', label='Fresnel')
    plt.legend()
    
    return (max_val, round(np.degrees(avg_brew), 2), popt)


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
    
    count = 0
    try:
        
        replica_samples = []
        for sample_raw in data:
            if(count % 2 ==0):
                
                angles = list(map( lambda x: np.radians(x*0.9) , np.arange(0, len(sample_raw), 1) ))
                sample = list(map(lambda x: step_control.get_voltage(x), sample_raw))
                replica_samples.append(sample)
                
                make_plot(angles, sample)
                max_val, avg_brew, popt = fit_fresnel(angles, sample)
                
                plt.annotate(r'$\theta_p = {0}°$'.format(avg_brew), xy=(avg_brew+3, 100), va='bottom')
                plt.axvline(x=avg_brew, color='green', linestyle='--')
                #plt.style.use(['science', 'grid'])
                plt.show()
            count += 1
    
    
        ## get expected value and variance
        print("replica", replica_samples)
        sample_set = list(zip_longest(*replica_samples, fillvalue=0))
        print("sample_set", sample_set)

        sample_average = lambda x: sum(x)/len(x)
        average_sample = list(map(np.mean, sample_set))
        print(average_sample)

        #sample_variance = lambda x: (sum(list(map(lambda y: y**2, x)))/len(x) - (sum(x)/len(x))**2)
        variance_sample = list(map(np.var, sample_set))
        print(variance_sample)
        
        make_plot(angles, average_sample)
        
        plt.title('Averaged Sample for Parallel Polarization')
        plt.ylabel('Voltage (mV)')
        plt.xlabel(r'Angle $\theta$ (degrees °)')
        #plt.style.use(['science', 'grid'])
        plt.legend()

        # plt.errorbar(
        #     angles,  # Use left bin edges directly
        #     average_sample,
        #     yerr=variance_sample,
        #     fmt='o',
        #     color='black',
        #     capsize=0,                   # Length of caps (horizontal lines)
        #     capthick=1,                  # Thickness of cap lines
        #     elinewidth=0.5,
        #     markersize=4,
        #     label='Error bars'
        # )
        
        full_max_val, full_avg_brew, chi_popt = fit_fresnel(angles, average_sample)
        
        plt.annotate(r'$\theta_p \approx {0}°$'.format(full_avg_brew), xy=(avg_brew+3, 100), va='bottom')
        plt.axvline(x=round(full_avg_brew, 2), color='green', linestyle='--')
        
        chi_volt = list(fresnel_fit(angles, *popt))
        chi_list = round(step_control.Chi2(average_sample, chi_volt, variance_sample), 2)
        
        plt.legend([r'$\chi^2 = {0}$'.format(chi_list)]) 
        
        
        plt.show()



        
    # except Exception as e: 
    #     print("ERROR", type(e).__name__, e)
    finally:
        file.close()
    
    
    