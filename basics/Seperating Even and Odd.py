# Write a program to separate positive and negative numbers into two different lists.
L = [2,3,4,5,6,7,8,9,10]
Even = [ ]
Odd = [ ]

for i in L:
    if i%2 == 0:
        Even.append(i)
    else:
        Odd.append(i)

print("The list contains only Even values :",Even)
print("The list contains only Odd values :",Odd)