# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# from https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# !/usr/bin/python
class SimpleClass:
	def __init__(self):
		self.st = ""
	def getString(self):
		nb = input('Write your string here: ')
		self.st = nb
	def printString(self):
		print(self.st.upper())

x = SimpleClass()
x.getString()
x.printString()
