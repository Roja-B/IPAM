#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Date: 01/02/2013 
# Author: Roja Bandari
''' This program creates a list of upper cased names of long programs (called INCLUDEList). '''
from string import upper

f = open("AllLongProgramList.txt","r")
t = open("INCLUDElist","w")
f.readline()

for line in f:
     program = line.split('\t')[1]
     t.write(
     upper(program)+'\n')

f.close()
t.close()


     
