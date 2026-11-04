# Write a function using **kwargs to accept and display a person's details.
def Person_details(**Details):
    for key,value in Details.items( ):
        print(key,":",value)
Person_details(Name= "Vinutha",age= 20, Course ="BE", Marks= 500)
