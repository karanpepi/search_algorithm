#Given an integer array A of N elements. You need to find the sum of
#two elements such that sum is closest to zero.

list = [1,2,-3,5,23,-67]

a = [(x+y) for x in list for y in list]

value = [(i) for i in a if i <= 0]

value.sort()

print(value[-1])

