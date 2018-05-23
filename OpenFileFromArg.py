# -*- coding: utf-8 -*-
"""
Created on Mon May 21 19:23:52 2018

@author: MSI_me
"""

import sys

#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
print("sys.argv[0]:",sys.argv[0])
print("sys.argv[1]:",sys.argv[1])

with open(sys.argv[1],'r') as f:
    lines = f.readlines()
    
for ix in range(len(lines)):
    print(lines[ix])
