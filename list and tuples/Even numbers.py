# Write a program to create a new list containing only even numbers from an existing list. 
# Solve it using both a regular loop and list comprehension.

values = [2,3,4,5,6,7,8,9,1,11,12,14,4,16]
New_list = [ ]

for i in values:
    if i % 2 == 0 and i not in New_list:
        New_list.append(i)
        
print(" The list contains only the Even number is :", New_list)

# approach - 2
values = [2,3,4,5,6,7,8,9,1,11,12,14,4,16]
New_list = [ i for i in values if i %2 == 0 ]
print(" The list contains only the Even number is :", New_list)
