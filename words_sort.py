# Write a program that accepts a sequence of whitespace separated 
# words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
# from https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# !/usr/bin/python

def sort_words():
	st = input("Write your string : ")
	print (" ".join(sorted(set(st.split(' ')))))
	# print ("".join([char.upper() for char in st]))
	return

sort_words()

