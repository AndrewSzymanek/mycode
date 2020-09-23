#!/usr/bin/env python3

def whichFunction():
    answer = input("Do you want to add, subtract, multiply, or divide?")
    return answer

def router():
    answer = whichFunction()
    answers = ["add", "subtract", "multiply", "divide"]
    if answer not in answers:
        print("select add, subtract, multiply, or divide")
        router()
    else:
        x = float(input("Give me your first number: "))
        y = float(input("Give me your second number: "))
        if answer.lower() == "add":
            add(x,y)
        elif answer.lower() == "subtract":
            subtract(x,y)
        elif answer.lower() == "multiply":
            multiply(x,y)
        elif answer.lower() == "divide":
            divide(x,y)

def add(x,y):
    sum = x+y
    print(sum)
def subtract(x,y):
    remainder = x-y
    print(remainder)
def multiply(x,y):
    quotient = x*y
    print(quotient)
def divide(x,y):
    dividend = x/y
    print(dividend)

router()
