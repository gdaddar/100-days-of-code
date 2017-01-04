# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and # n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# from https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# !/usr/bin/python
def dict_gen(n):
  d = {k: k*k for k in range(1, n+1)}
  return d

print (dict_gen(8))
