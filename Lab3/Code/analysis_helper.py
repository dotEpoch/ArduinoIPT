# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 20:29:33 2025

@author: vince
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.special import factorial
from scipy.stats import poisson
from scipy import interpolate

### MATH ###

def expected_value(counts, bin_values):
    expected = 1/sum(counts)*sum(counts*bin_values)
    return expected

def variance(counts, bin_values):
    var = expected_value(counts, bin_values**2) - expected_value(counts, bin_values)**2
    return var
    

def get_countbins(data_set, dist, sample_num, sample_type, bin_size, edge):
    bin_values = np.arange(min(data_set), max(data_set)+1, bin_size)
    new_counts, bin_values, patches = plt.hist(data_set, bins=bin_values,
                                                        edgecolor=edge, alpha=0.7,
                                                        label='Massive data')
    width = int(bin_values[-1])
    plt.xlim(int(bin_values[0]), width)
    plt.ylim(0)
    plt.title(f'{sample_type} for {sample_num} datapoints @ {dist}mm')
    plt.xlabel('Clicks per Interval')
    plt.ylabel('Occurrences')
    plt.legend()
    
    print(new_counts, "\n", len(new_counts))
    print(bin_values, "\n", len(bin_values))
    bin_values = np.delete(bin_values, -1)
    return new_counts, bin_values
    
    

def full_poisson(data_set, dist, sample_type):
    bin_values = np.arange(min(data_set), max(data_set)+1, 1)
    sample_num = sum(data_set)

    new_counts, bin_values, patches = plt.hist(data_set, bins=bin_values,
                                                        edgecolor='black', alpha=0.7,
                                                        label='Massive data')

    print(new_counts, "\n", len(new_counts))
    print(bin_values, "\n", len(bin_values))
    bin_values = np.delete(bin_values, -1)
    


    #Poisson smooth
    poisson_fit = lambda k, lamb: sum(new_counts) * poisson.pmf(k, lamb)
    poisson_lambda = np.mean(data_set)
    print(sum(new_counts))
    print("poiss lambda", poisson_lambda)
    popt, pcov = curve_fit(poisson_fit, bin_values, new_counts, p0=[poisson_lambda])
    print('popt:', popt)
    print('pcov:', pcov)

    width = int(bin_values[-1])+1
    x_poisson = np.linspace(0, width, width*10)
    bspline = interpolate.make_interp_spline(bin_values, poisson_fit(bin_values, *popt))
    y_poisson = bspline(x_poisson)
    plt.plot(x_poisson, y_poisson, color='green')


    # Display Plot
    plt.xlim(0, width)
    plt.title(f'{sample_type} for {sample_num} datapoints @ {dist}mm')
    plt.xlabel('Clicks per Interval')
    plt.ylabel('Occurrences')
    plt.legend()
    plt.show()
    
def plot_poisson(counts, bin_values):

    #Poisson parameters
    poisson_fit = lambda k, lamb: sum(counts) * poisson.pmf(k, lamb)
    poisson_lambda = expected_value(counts, bin_values)
    print("poiss lambda", poisson_lambda)
    popt, pcov = curve_fit(poisson_fit, bin_values, counts, p0=[poisson_lambda])
    print('popt:', popt)
    print('pcov:', pcov)

    #plot poisson smooth
    width = int(bin_values[-1])+1
    x_poisson = np.linspace(0, width, width*10)
    bspline = interpolate.make_interp_spline(bin_values, poisson_fit(bin_values, *popt))
    y_poisson = bspline(x_poisson)
    plt.plot(x_poisson, y_poisson, color='green')
    
    
def full_gaussian(data_set, dist, get_num, sample_type):
    bin_values = np.arange(min(data_set), max(data_set)+1, 1)
    sample_num = get_num(data_set)

    new_counts, bin_values, patches = plt.hist(data_set, bins=bin_values,
                                                        edgecolor='black', alpha=0.7,
                                                        label='Massive data')

    print(new_counts, "\n", len(new_counts))
    print(bin_values, "\n", len(bin_values))
    bin_values = np.delete(bin_values, -1)
    


    #gaussian smooth
    gaussian_fit = lambda x, mu, sigma: sum(new_counts)*np.exp(-(x-mu)**2/2*sigma**2)
    gaussian_mean = np.mean(data_set)
    print(sum(new_counts))
    print("gauss mean", gaussian_mean)
    popt, pcov = curve_fit(gaussian_fit, bin_values, new_counts, p0=[gaussian_mean])
    print('popt:', popt)
    print('pcov:', pcov)

    width = int(bin_values[-1])+1
    x_gauss = np.linspace(0, width, width*10)
    bspline = interpolate.make_interp_spline(bin_values, gaussian_fit(bin_values, *popt))
    y_gauss = bspline(x_gauss)
    plt.plot(x_gauss, y_gauss, color='green')


    # Display Plot
    plt.xlim(0, width)
    plt.title(f'{sample_type} for {sample_num} datapoints @ {dist}mm')
    plt.xlabel('Clicks per Interval')
    plt.ylabel('Occurrences')
    plt.legend()
    plt.show()
    
def plot_gaussian(counts, bins):
    #gaussian smooth
    gaussian_fit = lambda x, mu, sigma: max(counts)*np.exp(-(x-mu)**2/(2*sigma))
    gaussian_mean = expected_value(counts, bins)
    gaussian_var = variance(counts, bins)
    print("gauss mean", gaussian_mean)
    print("gauss variance", gaussian_var)
    
    print(bins)
    print(counts)
    popt, pcov = curve_fit(gaussian_fit, bins, counts, p0=[gaussian_mean, gaussian_var])
    print('popt:', popt)
    print('pcov:', pcov)

    width = int(bins[-1])
    x_gauss = np.linspace(0, width, width*10)
    bspline = interpolate.make_interp_spline(bins, gaussian_fit(bins, gaussian_mean, gaussian_var), k=2)
    y_gauss = bspline(x_gauss)
    print(x_gauss)
    print(y_gauss)
    plt.plot(x_gauss, y_gauss, color='red')
    
def plot_exponential(counts, bins):    
    #exponential smooth
    exponential_fit = lambda x, A, b: A * np.exp(-b * x)
    
    exp_opt, exp_cov = curve_fit(exponential_fit, bins, counts)
    print('exp_opt:', exp_opt)
    print('exp_cov:', exp_cov)
    
    width = int(bins[-1])
    print(width)
    x_exp = np.linspace(0, width, width*10)
    bspline = interpolate.make_interp_spline(bins, exponential_fit(bins, *exp_opt))
    y_exp = bspline(x_exp)
    plt.plot(x_exp, y_exp, color='red')
    
    
    
### MAIN ###
if __name__ == '__main__':
    array = [1,2,4,7,2,4,3,6,2,0,0,6,2,3,2,5,2,4,2,3,5,4,5,3,2,0,3,6,8,4,3,7,6,4,5,2,3,2,4,6,4,3,3,3,6,5,2,3,4,2,3,1,2,4,1,5,1,7,4,3,2,3,1,5,4,7,1,6,0,2,4,6,3,6,6,7,5,2,5,3,2,2,4,3,4,2,3,3,2,3,5,10,3,4,1,1,4,4,3,0,2,5,1,2,3,2,0,1,3,0,3,4,5,6,4,2,5,3,4,4,6,4,7,3,3,3,3,2,5,2,5,4,4,1,1,4,3,3,3,0,3,5,3,2,6,4,3,5,2,3,2,2,7,6,3,6,2,1,5,7,3,3,2,1,3,1,3,3,6,1,4,3,2,0,5,3,1,1,2,3,4,4,5,3,2,2,7,3,0,6,2,2,3,4,2,3,0,4,3,2,4,]
    #array = [35,23,37,30,25,26,29,32,28,33,29,34,30,32,20,31,45,36,36,34,34,32,32,28,30,29,23,19,26,27,22,32,32,30,23,30,27,25,32,31,33,43,29,34,23,32,24,24,34,27,24,40,27,35,27,29,32,35,24,26,31,29,29,18,34,23,22,29,35,27,30,25,30,35,32,33,21,26,29,29,34,29,30,23,25,29,32,30,30,36,26,26,35,20,36,25,21,31,25,37,27,32,24,27,30,23,29,31,24,35,25,31,27,23,28,29,38,34,24,39,20,24,29,32,31,27,35,31,32,25,28,32,33,40,32,24,25,24,37,40,31,31,40,28,31,33,34,22,33,22,31,34,27,31,26,32,21,34,20,35,20,32,33,36,29,37,32,30,27,18,41,24,37,30,37,34,29,23,31,34,25,29,34,20,26,39,30,46,33,25,21,40,26,38,36,26,34,34,40,31,36,26,33,29,24,36,33,36,33,25,21,30,21,38,34,28,31,30,33,24,24,39,35,33,25,31,28,30,35,32,26,27,28,32,30,30,32,26,37,31,26,31,38,38,33,43,26,39,27,27,20,27,25,26,34,39,34,29,31,38,37,22,32,37,29,27,36,24,32,25,34,29,36,32,33,28,33,38,25,34,32,33,30,28,29,31,30,33,40,34,25,34,32,26,29,35,23,22,20,32,26,27,26,28,34,25,28,40,24,29,30,35,36,29,28,25,32,24,34,26,29,24,27,24,22,30,22,43,26,36,34,37,24,34,32,30,28,22,26,24,23,30,19,33,38,28,23,26,34,27,25,29,30,40,31,34,29,17,26,22,42,25,32,39,34,34,33,24,29,33,33,29,33,38,37,26,26,24,26,29,25,32,26,20,23,30,25,30,26,45,34,25,29,29,30,35,22,23,41,27,33,24,28,28,22,40,28,23,31,27,26,32,25,31,33,19,33,33,31,25,24,32,32,39,25,32,35,25,27,33,40,37,24,26,26,41,28,31,25,22,29,36,20,24,39,28,24,23,31,29,28,34,33,27,28,32,28,40,33,35,39,32,27,36,26,27,38,33,28,27,23,26,28,31,25,32,27,33,32,42,30,27,39,27,37,26,33,26,20,34,26,30,26,33,40,22,27,31,31,27,27,29,33,30,39,19,31,30,20,30,27,32,34,31,41,30,29,19,22,18,36,25,22,28,27,28,34,31,29,18,27,51,31,30,36,25,32,27,26,23,24,30,24,40,26,29,46,26,28,19,33,22,34,32,35,29,26,33,36,31,20,28,39,31,26,20,36,29,33,39,35,32,37,34,34,23,28,34,29,34,17,33,37,33,31,33,38,40,29,37,31,31,36,28,31,31,32,39,32,26,21,27,33,30,29,27,39,38,28,23,27,23,40,21,35,24,19,30,22,29,25,31,41,37,28,32,24,25,18,24,26,31,31,24,28,34,30,36,24,31,30,34,35,31,39,24,23,29,28,29,35,28,21,28,23,41,22,28,36,33,30,28,26,34,26,31,38,26,32,31,22,25,24,29,31,33,31,25,31,29,36,23,21,37,35,31,23,34,28,26,26,36,37,33,35,31,26,32,27,33,30,33,43,37,26,27,35,19,23,22,40,31,21,31,29,34,33,29,29,31,29,25,25,30,32,26,28,21,33,39,32,31,30,33,24,37,35,33,27,29,35,31,26,42,31,29,26,36,35,25,35,29,35,29,27,25,35,26,30,23,33,32,31,30,30,37,31,26,19,29,35,34,31,25,36,39,32,34,26,36,32,24,32,30,26,32,31,32,25,29,31,29,25,24,26,24,27,30,28,34,26,23,22,25,24,27,35,36,25,34,26,29,31,28,34,32,37,33,30,31,26,23,37,25,29,42,41,30,33,30,30,28,20,39,28,45,33,19,23,34,38,30,29,35,22,26,32,31,21,28,21,27,28,26,31,26,33,28,34,37,31,25,33,29,29,29,31,32,34,27,34,31,22,27,41,30,29,26,21,31,20,27,30,32,34,27,26,30,27,28,29,34,31,24,23,35,29,33,30,30,35]
    counts, bins = get_countbins(array, 178.5, sum(array), "Lower meaned Sample1")
    
    plot_gaussian(counts, bins) 
    plot_poisson(counts, bins)
  

    print(expected_value(counts, bins))
    print(variance(counts, bins))
