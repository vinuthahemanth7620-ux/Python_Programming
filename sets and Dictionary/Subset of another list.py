# Write a program to check whether one set is a subset of another set.

Set_1 = set(map(int,input("Enter the values :").split()))
Set_2 = set(map(int,input("Enter the Values :").split()))

Set_3 = Set_1.issubset(Set_2)
print(Set_3)