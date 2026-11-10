# Write a program to find elements that exist in the first list but not in the second list.

Set_1 = set(map(int,input("Enter the values :").split()))
Set_2 = set(map(int,input("Enter the Values :").split()))

Set_3 = Set_1 - Set_2
print("The elements exist in first set and not in second one are :",Set_3)
