# Question:
# Write a program that accepts a comma separated sequence of words as 
# input and prints the words in a comma-separated sequence after 
# sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# from https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# !/usr/bin/python
def reverse_string(st):
	sorted_list = sorted(st.split(','))
	print( ','.join(sorted_list))
	return

reverse_string("without,hello,bag,world")
