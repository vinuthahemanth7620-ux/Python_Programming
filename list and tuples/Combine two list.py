# Write a program to combine two lists, 
# sort the result in ascending order, and then display it in descending order.

List_1 = [2,4,6,8,10]
List_2 = [1,3,5,7,9]

List_1.extend(List_2)
print(" the combined list is :", List_1)

List_1.sort( )
print(" The Ascending order of the given list elements are :", List_1)

List_1.sort(reverse = True)
print("The Ascending order of the given list elements are :", List_1)
      