# Write a program to move all zeros in a list to the end while maintaining the order of other elements.
L = [10,0,20,30,40,0,60,0,70,0,80]

New_list = [ ]
Zeros = [ ]
for i in L:
    if i == 0:
        Zeros.append(i)
    else:
        New_list.append(i)

print(New_list)
print(Zeros)
New_list.extend(Zeros)
print("The list before moving the Zeros to the End :", L)
print("The List after moving all the zeros to the End :", New_list) 