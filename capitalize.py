# Write a program that accepts sequence of characters as input and prints 
# the characters after making all characters in the word capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Then, the output should be:
# HELLO WORLD

# from https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# !/usr/bin/python

def capitalize():
	st = input("Write your string : ")
	print ("".join([char.upper() for char in st]))
	return

capitalize()


