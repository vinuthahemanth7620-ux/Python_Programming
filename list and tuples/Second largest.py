# Write a program to find the second-largest distinct number in a list.
L = [10, 20, 60, 40, 30, 20, 80, 70, 80, 70, 80, 40, 90]
Largest = L[0]
Second_largest = L[0]

for i in L:
    if i > Largest:
        Second_largest = Largest
        Largest = i


    elif i > Second_largest and i < Largest :
        Second_largest = i

print(" The largest number in the given list is :", Largest)
print(" The Second largest number in the given list is :", Second_largest)



