# Write a program to find the LCM of two numbers.


Num_1 = int(input("Enter the Number_1 :"))
Num_2 = int(input("Enter the Number_2 :"))

LCM = 1
for i in range(max(Num_1,Num_2),(Num_1* Num_2)+1):
    if i % Num_1 == 0 and i % Num_2 == 0:
        LCM = i
        break
print("The LCM of given Numbers is :",LCM)