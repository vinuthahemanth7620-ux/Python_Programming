# Write a program to rotate a list to the right by one position.
L= [10,20,30,40,50]

count =L[-1 :] + L[:-1]
print(count)
