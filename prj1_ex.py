# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from pandas import DataFrame
import numpy as np
import sys

def XfromGPS(lat1_deg,long1_deg,lat2_deg,long2_deg):
    R=6.371*math.pow(10,6)          #earth radius
    lat1_ =lat1_deg*math.pi/180     #convert degrees into radians
    lat2_ =lat2_deg*math.pi/180
    long1_ =long1_deg*math.pi/180
    long2_ =long2_deg*math.pi/180
    x = numpy.array(R*(long2_-long1_)*numpy.cos(lat1_))
    return x

def YfromGPS(lat1_deg,long1_deg,lat2_deg,long2_deg):
    R=6.371*math.pow(10,6)           #earth radius
    lat1_ =lat1_deg*math.pi/180      #convert degrees into radians
    lat2_ =lat2_deg*math.pi/180
    long1_ =long1_deg*math.pi/180
    long2_ =long2_deg*math.pi/180
    y = numpy.array(R*(lat2_-lat1_))
    return y

#print

#1-hard coded way of reading a file (not what assignemt asks for)
#df = pd.read_csv('c:/Users/MSI_me/Dropbox/private/V2V-class/projects_wip/project1/input.csv')

#2-command line argument is file to read(this is what assignemt asks for)
file_name = str(sys.argv[1])
df = pd.read_csv(file_name)
print(df.iloc[0:1])