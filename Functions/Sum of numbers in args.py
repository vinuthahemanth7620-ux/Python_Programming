# Write a function that accepts any number of arguments using *args and returns their sum.
def Sum_Number(*Number):
   total = 0
   for i in Number:
      total += i

   return total
Numbers = Sum_Number(10,20,30,40,50,60)
print("The Sum of all the Numbers is :",Numbers)