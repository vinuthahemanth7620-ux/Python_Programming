# Write a program to check whether a number is a perfect number.
Number = int(input("Enter the Number :"))

sum = 0
for i in range(1,Number):
    if Number % i == 0:
        sum += i

if sum == Number and Number > 0:
    print("The given Number",Number,"is a Perfect Number")
else:
    print("The given Number",Number,"is not a Perfect Number")

