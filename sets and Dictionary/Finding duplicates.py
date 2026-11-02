# Write a program to find the common elements between two lists using sets.
List_1 = [10,20,30,20,40,50,60]
List_2 = [70,60,50,80,30,80,20,100,20]

Set_1 = set(List_1)
Set_2 = set( List_2)
Common_elements = Set_1 & Set_2

print(" The Common elements in both sets are : ", Common_elements)

