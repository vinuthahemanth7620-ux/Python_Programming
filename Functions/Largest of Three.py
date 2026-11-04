# Write a function that returns the largest of three numbers.

def Largest(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= c and b >= a:
        return b
    else:
        return c
Numbers =Largest(30,30,20)
print("The Largest Number in the given series is :", Numbers)