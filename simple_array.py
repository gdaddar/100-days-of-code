# Write a program which takes 2 digits, X,Y as input and generates a 2-# dimensional array. The element value in the i-th row and j-th column # of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,..Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
# from https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# !/usr/bin/python
def arr(x,y):
	flattened = [i*j for i in range(x) for j in range(y)]
	return ([flattened[i*y:i*y+y] for i in range(x)])

print(arr(3,5))
