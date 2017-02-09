# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 11:31:29 2016

@author: feliciaullstad

This script takes a sample name and a file directory of PPMS data files as input.
It takes all the .dat files in the file directory and plots them appropriately,
saves them with proper title and file name. The file name is different for magnetoresistance,
hall effect and RvsT.


For each run you need to change:
file_location - your file directory path
Sample_name - your sample (needed for plot titles and file names)
Ch_2 - "Hall" or "Magneto" or ""
Ch_3 - "Hall" or "Magneto" or ""
trimstart/trimend - How many characters are stripped from the start/end of .dat file name to make title/graph file name.

If you have several different datasets in the same .dat file you have to filter the dataframe like this:
Fit_value=170
PPMS_data_filtered=PPMS_data_raw[PPMS_data_raw["Sample Position (deg)"] >Fit_value]
# Filters away data with values under Fit_value

"""
#######################################################
#Settings for the PPMS data
file_location='/home/feliciaullstad/Desktop/Google Drive Synced files/PhD/SmN data/PPMS/F19 SmN 20160720'
Sample_name='F19'
Ch_3="Hall"
Ch_2="Magneto"
trimstart=9
trimend=-4

#######################################################
import matplotlib.pyplot as plt
import pandas as pd
import os

plt.close("all")    #Closes plots from previous run

######################################################
if not os.path.exists(file_location+'-python'):     #Checks if the python folder exists
    os.makedirs(file_location+'-python')            #If not, it makes it
#######################################################
#Importing and plotting the PPMS data

"""
Scan through datafolder. Find all .dat files. List them.
"""
datfiles_list=[]
for file in os.listdir(file_location):
    if file.endswith(".dat"):
        datfiles_list.append(file)


"""
Interesting things to plot:
Temperature (K)
Magnetic Field (Oe)
Bridge 2 Resistance (Ohms)
Bridge 3 Resistance (Ohms)
"""


print "Datfiles being processed:"
for datafile in datfiles_list:
    print datafile
    Scan_program=datafile[trimstart:trimend]
    PPMS_data_raw=pd.read_csv(file_location+'/'+datafile, header=0, sep=',',skiprows=31)
    if not 'RvsT' in datafile:
        if PPMS_data_raw.empty:
             print'Empty file: '+datafile
        else:
            fig1=plt.figure()
            plot1 = fig1.add_subplot(111)
            plot1=plt.plot(PPMS_data_raw["Magnetic Field (Oe)"],PPMS_data_raw["Bridge 2 Resistance (Ohms)"],'.')
            ax = plt.gca()
            ax.ticklabel_format(useOffset=False)
            plt.subplots_adjust(bottom=.1, left=.2)
            plt.xlabel('Field (Oe)')
            plt.ylabel('Resistance (Ohm)')
            plt.title(Ch_2+'resistance '+Scan_program+' Ch 2 '+Sample_name)
            plot1=plt.savefig(file_location+'-python/'+Sample_name+'_Ch2_plot_'+Ch_2+'resistance_'+Scan_program+'.pdf', format='pdf', dpi=1200)
            plt.close()

            fig1=plt.figure()
            plot1 = fig1.add_subplot(111)
            plot1=plt.plot(PPMS_data_raw["Magnetic Field (Oe)"],PPMS_data_raw["Bridge 3 Resistance (Ohms)"],'.')
            ax = plt.gca()
            ax.ticklabel_format(useOffset=False)
            plt.subplots_adjust(bottom=.1, left=.2)
            plt.xlabel('Field (Oe)')
            plt.ylabel('Resistance (Ohm)')
            plt.title(Ch_3+'resistance '+Scan_program+' Ch 3 '+Sample_name)
            plot1=plt.savefig(file_location+'-python/'+Sample_name+'_Ch3_plot_'+Ch_3+'resistance_'+Scan_program+'.pdf', format='pdf', dpi=1200)
            plt.close()
    if "RvsT" in datafile:
         if PPMS_data_raw.empty:
             print'Empty file '+datafile
         else:
             if Ch_2=="Magneto":
                 R_channel="Bridge 2 Resistance (Ohms)"
                 Ch='Ch2'
             else:
                 R_channel="Bridge 3 Resistance (Ohms)"
                 Ch='Ch3'
             fig1=plt.figure()
             plot1 = fig1.add_subplot(111)
             plot1=plt.plot(PPMS_data_raw["Temperature (K)"],PPMS_data_raw[R_channel])
             ax = plt.gca()
             ax.ticklabel_format(useOffset=False)
             plt.subplots_adjust(bottom=.1, left=.2)
             plt.xlabel('Temperature (K)')
             plt.ylabel('Resistance (Ohm)')
             plt.title('Resistance vs Temperature '+Ch+Sample_name)
             plot1=plt.savefig(file_location+'-python/'+Sample_name+'_'+'Ch'+'_plot_'+Scan_program+'.pdf', format='pdf', dpi=1200)
             plt.close()
print
print 'All data plotted successfully'
