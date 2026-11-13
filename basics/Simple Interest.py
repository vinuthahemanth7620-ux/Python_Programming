# Write a program to calculate the simple interest using principal, rate and time.
Principal = float(input("Enter the Principal amount :"))
Rate = float(input("Enter the Rate per annum for the Given amount :"))
Time = float(input("Enter the Time taken in years :"))

Simple_Interest = Principal * Rate * Time/100
print("The Simple Interest for the given Amount is :",Simple_Interest)
