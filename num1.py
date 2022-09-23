#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'closestNumbers' function below.
#
# The function accepts INTEGER_ARRAY numbers as parameter.
#

def closestNumbers(numbers):
    # Write your code here
    
    numbers.sort()
    
    if len(numbers) > 1:
        pairs = []
        min_diff = numbers[1] - numbers[0]

        for l in range(len(numbers)):
            for i in range(l + 1, len(numbers)):
                if abs(numbers[i] - numbers[l]) < min_diff:
                    min_diff = numbers[i] - numbers[l]
                if abs(numbers[i] - numbers[l]) == min_diff:
                    pairs.append((numbers[i], numbers[l]))
                    
        for (p1, p2) in pairs:
            if abs(p1 - p2) == min_diff:
                print(str(p2) + " " + str(p1))
    else:
        print("")

closestNumbers([4, 2, 1, 3])