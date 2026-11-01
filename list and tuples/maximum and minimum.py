# Write a program to find the largest and smallest numbers in a list without using max() and min().

L = [20, 10, 30, 40, 50, 70, 5, 60]
largest = L[0]
smallest = L[0]

for i in L:
    if i > largest:
        largest = i

    if i < smallest:
        smallest = i

print(" The Largest number in the given list is :", largest)
print(" The Smallest number in the given list id :", smallest)
        