# Write a program to flatten a nested list (for example, [[1, 2], [3, 4], [5, 6]]).
L = [[1,2],[3,4],[5,6],[7,8]]

New_List = [ ]
for i in L:
    for j in i:
        New_List.append(j)

print("The Flatten nested List is :",New_List)

