# Write a program to check whether a number is positive, negative, or zero.

Number = int(input("Enter the Number :"))
print(Number)

for i in Number:
    if i % 2 ==0:
        print(" The Given Number is Positive ")
    else:
        print(" The Given Number is Negative ")
