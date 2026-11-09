# Write a program to find elements that appear more than once in a list.

L = [10,20,30,20,10,40,50,60,50,70,80,60,90]
New_list = []
Another_List = []
for i in L:
    if i in New_list:
        if i not in Another_List:
            Another_List.append(i)
    else:
        New_list.append(i)
print("The elements which appear  more than one time are :",Another_List)
print("The elements which are appear on only one time :",New_list)

print("*" * 30)

# anothe method
L = [10,20,30,20,10,40,50,60,50,70,80,60,90]
Duplicates = []
for i in L:
    if L.count(i) > 1 and i not in Duplicates:
        Duplicates.append(i)
print("The Duplicate elements in the given list are :",Duplicates)
     
