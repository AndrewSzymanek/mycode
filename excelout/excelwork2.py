#!/usr/bin/env python3

import pyexcel

def get_grocery_data():
    grocery_type = input("\nWhat is the grocery type? ")
    price = input("What is the price? ")
    color = input("What is the color? ")
    d = {"type": grocery_type, "price": price, "color": color}
    return d

mylistdict = []

print("Hello! This program makes a grocery list receipt in *.xls file")

while(True):
    mylistdict.append(get_grocery_data())
    keep_going = input("\nWould you like to add another value? Press enter for yes or 'q' to quit: ")
    if(keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the file?")

pyexcel.save_as(records=mylistdict, dest_file_name=f'{filename}.xls')

print("The file " + filename + " .xls should be in your local directory")
