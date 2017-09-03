# Range  in the previous lecture
# lists
'''
itemlist = ["Vegetables ", "Fruits", "JUices ", "pizzas"]
# Going through each item in the list like this
for item in itemlist:
    print(item)

# looping through the range function 
for number in range(0,1000):
    print(number)
'''
#for   [ANYVARIABLEWHICH DOENST EXISTS BEFORE ] in [list here]]]]]
counter = 1 # A variable to count ! 
for _ in range(0,3):
    in_text = input("Enter you message here")
    print(in_text) # printings the texts
    print(counter)  # printing the counter
    counter += 1 # incrementing the counter
