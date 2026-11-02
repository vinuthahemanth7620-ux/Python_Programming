# Find the factorial of a number using a loop.
Number = int(input(" Enter the number to find factorial :"))

Factorial = 1
for i in range(1,Number+1):
    Factorial = Factorial * i
print("The Factorial of a given number",Number,"is",Factorial)

    
