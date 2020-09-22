#!/usr/bin/env python3

pecks = float(input("How many pecks of apples did you pick?"))
message = "You owe "
if pecks >= 5:
    message = message + '20 dollars.'
elif pecks < 5 and pecks > 1:
    message = message + '10 dollars.'
else:
    message = message + '5 dollars.'
print(message)
