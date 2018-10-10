#Day0
#Objective 
#In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an instructional video!
#Task 
$Given an array,X, of N integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))
