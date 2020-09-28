#!/usr/bin/python3

"""Lab 39 challenge 01"""
import pytest

def sayHello():
    return "hello!"
def returnTrue():
    return(2 == 2)

def test_sayHello():
    assert sayHello() == "hello!"
def test_returnTrue():
    assert returnTrue() == True
