# Write a program to remove duplicate elements from a list while preserving the original order.
Original_list = [10, 20, 30, 40, 50, 30, 60, 40, 20, 10, 80]
New_list = [ ]

for i in Original_list:
    if i not in New_list:
        New_list.append(i)

print(" the original list is :", Original_list)
print(" the List after removing the duplicates :", New_list)

