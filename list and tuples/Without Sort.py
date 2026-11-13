# Write a program to merge two sorted lists into a single sorted list without using sort()
L1 = [10,20,30,50,60]
L2 = [15,20,25,40,55,65]

i = 0
j = 0
New_list = [ ]

while i<len(L1) and j<len(L2):
    if L1[i] < L2[j]:
         New_list.append(L1[i])
         i+=1
    else:
         New_list.append(L2[j])
         j+=1
New_list.extend(L1[i :])
New_list.extend(L2[j :])

print("The Merged List is :",New_list)
