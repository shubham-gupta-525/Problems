#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    s = sorted(s)
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    frquency_sorted = sorted(frequency.items(), key = lambda x: (-x[1], x[0]))   
    
    for k,v in frquency_sorted[:3]:
        print(k,v) 
        