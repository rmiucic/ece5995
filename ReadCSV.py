# -*- coding: utf-8 -*-
"""
Created on Wed May 23 18:43:07 2018

@author: MSI_me
"""

#Research and post online

import sys
import csv
import numpy as np

#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
print("sys.argv[0]:",sys.argv[0])
print("sys.argv[1]:",sys.argv[1])

with open(sys.argv[1],mode='rb') as f:
    spamreader = csv.reader(f)
    
    #next(spamreader, None)  # skip the headers
    for row in spamreader:
        print(row)
    #    print(row)
        #times.append(row[0])
        #longitudes.append(row[1])
        #latitudes.append(row[2])

