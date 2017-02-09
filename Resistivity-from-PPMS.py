"""
Created on Mon Oct 31 09:27:27 2016

@author: feliciaullstad

This script will take a dat PPMS resistance file and output another file with
the temperature and resistance data plus the resistivity
"""

import matplotlib.pyplot as plt
import pandas as pd
plt.close("all")


Sample_name='F15'
file_location='/home/feliciaullstad/Desktop/Google_Drive/PhD/SmN data/PPMS/F15 SmN 20160504'
file_name='F15-SmN-Hall-RvsT-heatup'
Channel=3   #2 or 3, which channel that holds the resistance data
Sample_thickness=144.5    #In nanometers

Sample_width=1.5        #In millimeter (1.5 for Hall bar)
Sample_length=2.5       #In millimeter (2.5 for Hall bar)

Resistivity_coefficient=Sample_width*Sample_thickness/Sample_length*10**-7

#def Resistivity(myfile,Resistivity_coefficient):
myfile=file_location+'/'+file_name
data=pd.read_csv(myfile+'.dat', header=0, sep=',',skiprows=31)

if Channel==2:
    R_channel="Bridge 2 Resistance (Ohms)"
    Ch='Ch2'
else:
    R_channel="Bridge 3 Resistance (Ohms)"
    Ch='Ch3'
Resistivity=data[R_channel]*Resistivity_coefficient
data['Resistivity (Ohm cm)']=pd.Series(Resistivity)
headers=list(data.columns.values)
data.to_csv(file_location+'-python/'+Sample_name+'_'+str(Sample_thickness)+'nm_resistivity.txt', header=headers, index=None, sep=' ', mode='w')

fig1=plt.figure()
plot1 = fig1.add_subplot(111)
plot1=plt.plot(data["Temperature (K)"],data['Resistivity (Ohm cm)'])
ax = plt.gca()
ax.ticklabel_format(useOffset=False)
plt.subplots_adjust(bottom=.1, left=.2)
plt.xlabel('Temperature (K)')
plt.ylabel('Resistivity (Ohm cm)')
plt.title('Resistance vs Temperature '+Ch+Sample_name)

plot1=plt.savefig(file_location+'-python/'+Sample_name+'_'+str(Sample_thickness)+'nm_resistivity.pdf', format='pdf', dpi=1200)
plt.close()

print data
