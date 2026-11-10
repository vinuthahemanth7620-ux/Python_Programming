# Write a program to find all pairs of elements whose sum equals a given target
L = [10,20,4,5,6,30,12,3,13,14,15,0]
Target = 30

count = [ ]
for i in L:
    Difference = Target - i

    if Difference in L and L.index(i) < L.index(Difference):
        count.append((i,Difference))
        
print("The two Numbers are :",count)
