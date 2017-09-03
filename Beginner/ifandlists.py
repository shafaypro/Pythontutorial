shoppingList = [ "potatos", "tomatos", "a book"] # this is a list

item = input("Enter the item you just bought")

if item in shoppingList:  # true or false 
    print(item)
    print("was found in the shopping list")
else:
    print(" you just wasted your money because you didn't read the list")


# 0    ----> [ 0 , 1 ,2 , 3 ]
# 0 in [ 0 ,1 ,2 ,3 ] ---> yes ---> True !!!
number = int(input("Enter the number here"))
number2 = int(input("Enter the number here"))

number_list = [number , number2] # We create a number list from variable.

print(number_list) # printing out the number list
print(type(number_list))
print("The first number is : \t",number_list[0]," The last number is \t ",number_list[-1])
