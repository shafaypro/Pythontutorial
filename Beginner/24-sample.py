# NEsted if conditions ,
# Nested if else conditions
name = input("Enter the name here")
brothername = input("Enter the brother name here")
number = int(input("Enter the number here"))
# take all the inputs
# The more you do, the more it get complex
if name == "Shafay":
    print("Name is Shafay")
    if brothername == "Rafay":
        print("Brother name is Rafay")
        if number == 1000:
            print("The number is 1000")
        else:
            print("The number is not 1000") 
    else:
        print("Brother name is not Rafay")
else:
    print("Name is not Shafay")
    if brothername == "Rafay":
        print("Brother name is Rafay")
    else:
        print("Brother name is not Rafay")
