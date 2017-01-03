# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Source: https://raw.githubusercontent.com/zhiwehu/Python-programming-exercises/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# ---------------------------------------------------------------------------------------------
# I will use list comprehension  
print([x for x in range(2000, 3201) if x%7==0 and x%5!=0])


