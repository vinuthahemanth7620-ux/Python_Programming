# Write a program to find the missing number in a list containing numbers from 1 to N.

L = [ 1,2,3,4,5,6,7,8,10]
N = 10

Total = N*(N+1)//2
Missing = Total - sum(L)
print("The Missing number is",Missing)