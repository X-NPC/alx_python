#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if number > 5:
    print("Last digit of ", number, "is ",  ,", and is greater than 5.")
elif number == 0:
    print ("Last digit of ", number, "is ", ,", and is zero")
elif number < 6 and number != 0:
    print ("Last digit of ", number, "is ", , "and is less than 6 and not 0.")
else: 
    None