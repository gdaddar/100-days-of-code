# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a # comma-separated sequence.
# Example
# Let us assume the following input list is given to the program:
# [100,150,180]
# The output of the program should be:
# [18,22,24]
# from https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# !/usr/bin/python
import math
def q(d):
	c = 50.0
	h = 30.0
	return([int(round(math.sqrt((2*c*x)/h))) for x in d])

print(q([100,150,180]))
	
