flag = False # its a boolean experission --> 0 --> false

counter = 1
while not flag:
    print("The value of counter is : ",counter)
    counter += 1 # Adds the counter value with one .
    if counter > 10:
        flag = True # This will break after 10 numbers
    
# while CONDITION:
# ____:statments here
# keep in mind to have NON - infinite loops (finite loop)
# 
