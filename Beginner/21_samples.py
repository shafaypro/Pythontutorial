name = "Person1"
name2 = "Person2"
name3 = "Person3"
in_input = input("Enter the person you want to see") # taking input
salary = int(input("Enter the salary here"))
if in_input == "Person1":
    print("This is person1 also a sportsman")
else:
    print("This is not person1")
if in_input == "Person2":
    print("This is person 2 right ????")
    print("I am here as i am a business man")
else:
    print("this is not person 2 ")
if in_input == "Person3":
    print("This is person aka , PYTHON PROGRAMMER")
else:
    print("There is no named person like this")
if salary == 20000:
    print("your salary is deducting")
    salary -= 10000 # this operation is important
    print(salary)
