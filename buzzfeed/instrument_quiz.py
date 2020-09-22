#!/usr/bin/env python3


def whatInstrument():
    stillPlaying = True
    score = 0

    while stillPlaying:
        subject = input("What's your favorite subject? Type Math, History, Music, or Lunch. ")
        if subject.lower() == 'math':
            score+=1
        elif subject.lower() == 'history':
            score +=2
        elif subject.lower() == 'music':
            score +=3
        elif subject.lower() == 'lunch':
            score +=0
        else:
            print("start over")
            stillPlaying = False
        food = input("What's your favorite food? Type Pizza, Burgers, Anything sweet, or Tacos. ")
        if food.lower() == 'pizza':
            score+=1
        elif food.lower() == 'burgers':
            score +=2
        elif food.lower() == 'anything sweet':
            score +=3
        elif food.lower() == 'tacos':
            score +=0
        else:
            print("start over")
            stillPlaying = False
        hobby = input("What do you do in your free time? Type Hang with friends, play sports, read, or watch TV.    ")
        if hobby.lower() == 'hang with friends':
            score +=1
            stillPlaying = False
        elif hobby.lower() == 'play sports':
            score +=2
            stillPlaying = False
        elif hobby.lower() == 'read':
            score +=3
            stillPlaying = False
        elif hobby.lower() == 'watch tv':
            score +=0
            stillPlaying = False
        else:
            print("start over")
            stillPlaying = False

        if score == 0:
            print("You are a bass")
        if score == 1: 
            print("You are a euphonium")
        if score == 2:
            print("You are a french horn") 
        if score == 3:
            print("You are a guitar")
        if score == 4:
            print("You are a drum")
        if score == 5: 
            print("You are a trumpet")
        if score == 6:
            print("You are a singer")
        if score == 7:
            print("You are an oboe")
        if score == 8:
            print("You are a didgeridoo")
        if score == 9:
            print("You are a flute")

whatInstrument()
