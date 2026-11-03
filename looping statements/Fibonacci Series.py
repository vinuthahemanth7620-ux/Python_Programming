# Print the Fibonacci sequence up to n terms.
Number = int(input("Enter the Number :"))

First = 0
Second = 1

if Number >= 1:
    print(First,end=",")

if Number >= 2:
    print(Second,end=",")
    
for i in range(2, Number):
    Next = First + Second 
    print(Next,end= ",")

    First = Second
    Second = Next