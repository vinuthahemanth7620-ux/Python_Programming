# Write a program to find the GCD of two numbers.

Num_1 = int(input("Enter the Number_1 :"))
Num_2 = int(input("Enter the Number_2 :"))

GCD = 1

for i in range(1, min(Num_1,Num_2)+1):
    if Num_1 % i ==0 and Num_2 % i == 0:
        GCD = i
print("The GCD of two numbers is :", GCD)