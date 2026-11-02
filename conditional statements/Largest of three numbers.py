# Write a program to find the largest of three numbers using conditional statements.

Numbers = [50,10,30]
if Numbers[0] > Numbers[1] and Numbers[0] > Numbers[2]:
    print("The First Number is the largest Number in the given list")
elif Numbers[1] > Numbers[2] and Numbers[1] > Numbers[0]:
    print("The Second Number is the Largest Number in the given list")
else:
    print("The Last Number is the Largest Number in the given list ")