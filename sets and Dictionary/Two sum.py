# Find the two elements whose sum equals a target using a dictionary.

Numbers = [3,5,7,9,8,6,4,2,1]
Target = 10

Seen = { }
for i in Numbers:
    Difference = Target - i

    if Difference in Seen:
        break
    Seen[i] = True
            
print("The two numbers which equals to the target value are :",Difference , "and",i)

