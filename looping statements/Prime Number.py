# Check whether a number is prime.
Number = int(input("Enter the Number :"))

if Number < 0:
    print("The given Number",Number,"is Not Primr.")
else:
    for i in range(2,Number):
        if Number % i == 0:
            print("The given Number",Number,"is Not Primr.")
            break
    else:
        print("The given Number",Number,"is Prime")
            
