# Write a program to find the union, intersection and difference of two sets entered by the user.

Set_1 = set(map(int, input(" enter the set_1 elements :").split(",")))
Set_2 = set(map(int, input(" enter the set_2 elements :").split(",")))

New_set1 = Set_1 & Set_2
print(" The Common elements in both the sets are :", New_set1)

New_set2 = Set_1 | Set_2
print(" The Unique elements in both the sets are :", New_set2)

New_set3 = Set_1 - Set_2
print(" The difference between the set1 to set2 :", New_set3)

New_set4 = Set_2 - Set_1
print(" The difference between the set2 to set1 :", New_set4)