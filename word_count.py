# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 21:46:20 2018

@author: shalini
"""

import os
import sys
import time
import random
import subprocess
import threading

string1 = "if shalini gupta is a mad girl and shalini gupta is also a good girl"
list1 = string1.split(" ")

already_counted_word=[]
for item in list1:
    if item in already_counted_word:
        continue
    count = 0
    for word in list1:
        if item == word:
            count += 1
    print ("frequency of %s : %s"%(item,count))
    already_counted_word.append(item)
    





dict1={}
already_counted_word=[]
for item in list1:
    dict1[item] = 1
    if item in already_counted_word:
        dict1[item] += 1   
    already_counted_word.append(item)

print (dict1)
