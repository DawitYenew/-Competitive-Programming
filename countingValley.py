#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    vally = 0
    curr_level = 0
    if steps % 2 != 0:
        return vally
    for step in path:
        if step == 'U':
            curr_level += 1
            if curr_level == 0:
                vally += 1
        elif step == 'D':
                curr_level -= 1
    return vally

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
