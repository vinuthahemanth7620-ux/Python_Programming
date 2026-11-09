# Write a program to check whether two sets are disjoint.

Set_1 = set(map(int,input("Enter the values :").split()))
Set_2 = set(map(int,input("Enter the Values :").split()))

Set_3 = Set_1.isdisjoint(Set_2)
print("The given Sets are Disjoint : ",Set_3)