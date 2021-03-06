#!/usr/bin/python3

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  use [item]
''')
"""This was modified by Andrew Szymanek
    I added two rooms: the library and the porch.
    Then, I made it so you needed the sunglasses to continue to the porch.
    After that, I made it so that you can't win the game without wearing the sunglasses outside
    Otherwise, it's game over because you lose your sight!
    Also added use [item] to the commands menu
        and the used variable initialized to false
    That's how the game knows whether or not you used the sunglasses"""
def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

used = False

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key',
                  'north' : 'Library'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Library' : {
                    'south' : 'Hall',
                    'east' : 'Porch',
                    'item' : 'sunglasses'
                },
            'Porch' : {
                    'east' : 'Dining Room'
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion',
                  'north' : 'Pantry',
               },
            'Garden' : {
                  'north' : 'Dining Room'
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)
  
  #if they type 'use' first
  if move[0] == 'use':
      if move[1] in inventory:
        used = True
        inventory.remove(move[1])
      else:
        print('Whatever it was, ya can\'t use it! Sorry...')

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
        if currentRoom == 'Library' and 'sunglasses' in inventory:
          #move from library to porch successfully WITH sunglasses
            currentRoom = rooms[currentRoom][move[1]]
            #can't move on from library to porch WITHOUT sunglasses
        elif currentRoom == 'Library' and 'sunglasses' not in inventory:
            print("You need the sunglasses first")
        if currentRoom == 'Dining Room':
            if used == True:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                print("Oops, you needed to use the sunglasses! Now you've lost your sight. GAME OVER")
                break
            #not in the library, condition just sets currentRoom to next room
        else:
            currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion, plus you protected your eye health... YOU WIN!')
    break
  
  ## If a player enters a room with a monster BUT HAS A COOKIE
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'cookie' in inventory:
    print('The monster takes your cookie and runs away! Whew!')
    del rooms[currentRoom]['item']
    inventory.remove('cookie')

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
