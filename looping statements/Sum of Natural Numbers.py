# Find the sum of the first n natural numbers.
n = int(input("Enter the Natural Number to find Sum :"))

Total = 0
for i in range(1,n+1):
    Total += i
print("The sum of first",n,"Numbers is given by :", Total)