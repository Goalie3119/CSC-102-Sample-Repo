from Room import Room

######################################################
# creates the rooms
print("YOU ARE IN THE BACKROOMS...WELCOME, and GOOD LUCK LEAVING!")
def createRooms():
# r1 through r4 are the four rooms in the mansion
# currentRoom is the room the player is currently in (which
# can be one of r1 through r4)
# since it needs to be changed in the main part of the
# program, it must be global
    global currentRoom
    global hiddenRoom
    # create the rooms and give them meaningful names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    r5 = Room("Cave")
    r6 = Room("Win")
    # add exits to rooms
    r1.addExit("east", r2)
    r2.addExit("west", r1)
    r2.addExit("south", r3)
    r3.addExit("west", r4)
    r3.addExit("north", r2)
    r4.addExit("east", r3)
    #r4.addExit("cave", r5)
    r4.addExit("up", r1)
    r5.addExit("exit", None)
    # add grabbables to room 1
    # add items to room 1
    r1.addItem("clock", "There is a tall coocoo-clock in the corner of the room. It stands there with no hands on the face. Maybe we need to find them?")
    r1.addItem("table", "It is made of oak. Nothing fucking important.")
    # add items to room 2
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes.")
    r3.addItem("desk", "It is too dark to see anything on the desk...look for some light")
    r3.addItem("lamp", "There is a lamp in the corner of the room that produces a dim light, so dim that when it is on, it feels like someone is watching you")
    r4.addItem("wallpaper", "There is a tear in the wallpaper on the wall...something seems to be behind it.")
    r4.addItem("ladder", "There is a weird, crooked ladder in here...I wonder where it goes..")
    r5.addItem("sign", "You are now trapped here. Try to leave and you shall DIE!")
    # set room 1 as the current room at the beginning
    # of the game
    currentRoom = r1
    hiddenRoom = r5

        
######################################################
# START THE GAME!!!
inventory = [] # nothing in inventory...yet
createRooms() # add the rooms to the game


def death():
    print(" " * 17 + "u" * 7)
    print(" " * 13 + "u" * 2 + "$" * 11 + "u" * 2)
    print(" " * 10 + "u" * 2 + "$" * 17 + "u" * 2)
    print(" " * 9 + "u" + "$" * 21 + "u")
    print(" " * 8 + "u" + "$" * 23 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 25 + "u")
    print(" " * 7 + "u" + "$" * 6 + "\"" + " " * 3 + "\"" + "$"* 3 + "\"" + " " * 3 + "\"" + "$" * 6 + "u")
    print(" " * 7 + "\"" + "$" * 4 + "\"" + " " * 6 + "u$u" + " " * 7 + "$" * 4 + "\"")
    print(" " * 8 + "$" * 3 + "u" + " " * 7 + "u$u" + " " * 7 +"u" + "$" * 3)
    print(" " * 8 + "$" * 3 + "u" + " " * 6 + "u" + "$" * 3 +"u" + " " * 6 + "u" + "$" * 3)
    print(" " * 9 + "\"" + "$" * 4 + "u" * 2 + "$" * 3 + " " * 3+ "$" * 3 + "u" * 2 + "$" * 4 + "\"")
    print(" " * 10 + "\"" + "$" * 7 + "\"" + " " * 3 + "\"" +"$" * 7 + "\"")
    print(" " * 12 + "u" + "$" * 7 + "u" + "$" * 7 + "u")
    print(" " * 13 + "u$\"$\"$\"$\"$\"$\"$u")
    print(" " * 2 + "u" * 3 + " " * 8 + "$" * 2 + "u$ $ $ $ $u"+ "$" * 2 + " " * 7 + "u" * 3)
    print(" u" + "$" * 4 + " " * 8 + "$" * 5 + "u$u$u" + "$" * 3+ " " * 7 + "u" + "$" * 4)
    print(" " * 2 + "$" * 5 + "u" * 2 + " " * 6 + "\"" + "$" * 9+ "\"" + " " * 5 + "u" * 2 + "$" * 6)
    print("u" + "$" * 11 + "u" * 2 + " " * 4 + "\"" * 5 + " " *4 + "u" * 4 + "$" * 10)
    print("$" * 4 + "\"" * 3 + "$" * 10 + "u" * 3 + " " * 3 +"u" * 2 + "$" * 9 + "\"" * 3 + "$" * 3 + "\"")
    print(" " + "\"" * 3 + " " * 6 + "\"" * 2 + "$" * 11 + "u" *2 + " " + "\"" * 2 + "$" + "\"" * 3)
    print(" " * 11 + "u" * 4 + " \"\"" + "$" * 10 + "u" * 3)
    print(" " * 2 + "u" + "$" * 3 + "u" * 3 + "$" * 9 + "u" * 2+ " \"\"" + "$" * 11 + "u" * 3 + "$" * 3)
    print(" " * 2 + "$" * 10 + "\"" * 4 + " " * 11 + "\"\"" +"$" * 11 + "\"")
    print(" " * 3 + "\"" + "$" * 5 + "\"" + " " * 22 + "\"\"" +"$" * 4 + "\"\"")
    print(" " * 5 + "$" * 3 + "\"" + " " * 25 + "$" * 4 + "\"")
    
def win():
    if (action == "go win-or-trick?"):     
        print(" .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .-----------------.")
        print("| .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. |")
        print("| |  ____  ____  | || |     ____     | || | _____  _____ | | | | _____  _____ | || |     _____    | || | ____  _____  | |")
        print("| | |_  _||_  _| | || |   .-    -.   | || ||_   _||_   _|| | | ||_   _||_   _|| || |    |_   _|   | || ||_   \|_   _| | |")
        print("| |   \ \  / /   | || |  /  .--.  \  | || |  | |    | |  | | | |  | | /\ | |  | || |      | |     | || |  |   \ | |   | |")
        print("| |    \ \/ /    | || |  | |    | |  | || |  | |    | |  | | | |  | |/  \| |  | || |      | |     | || |  | |\ \| |   | |")
        print("| |    _|  |_    | || |  \  `---  /  | || |   \ `--- /   | | | |  |   /\   |  | || |     _| |_    | || | _| |_\   |_  | |")
        print("| |   |______|   | || |   `.____.-   | || |    `.__.-    | | | |  |__/  \__|  | || |    |_____|   | || ||_____|\____| | |")
        print("| |              | || |              | || |              | | | |              | || |              | || |              | |")
        print("| ---------------- || ---------------- || ---------------- | | ---------------- || ---------------- || ---------------- |")
        print("------------------  ------------------  ------------------   ------------------  ------------------  ------------------ ")
    


# play forever (well, at least until the player dies or asks to
#  quit)
while (True):
    # set the status so the player has situational awareness
    # the status has room and inventory from playsound import playsound
    if (currentRoom == None):
        response = "YOU ARE SO DEAD!"
        status = "LITERALLY DEAD."
        print(response)
        print(status)
        death()
        break
    
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    # display the status
    print("=========================================")
    print(status)
 
    # if the current room is None (and the player is dead),
    #  exit the game
    
    
    # prompt for player input
    # the game supports a simple language of <verb> <noun>
    # valid verbs are go, look, and take
    # valid nouns depend on the verb
    action = input("What to do? ")

    # set the user's input to lowercase to make it easier to
    #  compare the verb and noun to known values
    action = action.lower()

    if (action == "go win-or-trick?"):
        win()
        break
    # exit the game if the player wants to leave (supports
    #  quit, exit, and bye)
    if (action == "quit" or action == "exit" or action == "bye"):
        break

    # set a default response
    response = "Make sure you are trying a verb/noun. Valid verbs are go, look, take, and use"
    # split the user input into words (words are separated by
    #  spaces)
    words = action.split()
     
    if currentRoom.name == "Room 4" and action == "look wallpaper":
        currentRoom.addItem("cave", "There was a cave behind the wallpaper! Shall we explore? IT MIGHT BE A LIE...Be Careful.")
        currentRoom.addExit("cave", hiddenRoom)
    if currentRoom.name == "Room 3" and action == "use lamp":
        response = "You used the lamp and found something hiding in the dark on the desk. Try to look at it"
        currentRoom.addItem("paper", "There is a pair of clockhands underneath the paper, they seemed to have been misplaced.")
        currentRoom.addGrabbable("clockhands")
    
    # the game only understands two word inputs
    if (len(words) == 2):
        # isolate the verb and noun
        verb = words[0]
        noun = words[1]

        # the verb is: go
        if (verb == "go"):
            # set a default response
            response = "Invalid exit."

            # check for valid exits in the current room
            for i in range(len(currentRoom.exits)):
                # a valid exit is found
                if (noun == currentRoom.exits[i]):
                    # change the current room to the one
                    #  that is associated with the specified
                    #  exit
                    response = "You went " + noun
                    if currentRoom.name == "Room 4" and noun == "up":
                        response = "YOU ARE BACK WHERE YOU STARTED! ROOM 1!!!"
       
                    currentRoom =  currentRoom.exitLocations[i]

                    # set the response (success
                    #no need to check any more exits
                    break
        # the verb is: look
        elif (verb == "look"):
            # set a default response
            response = "I don't see that item."

            # check for valid items in the current room
            for i in range(len(currentRoom.items)):
                # a valid item is found
                if (noun == currentRoom.items[i]):
                    # set the response to the item's
                    #  description
                    
                    if "clockhands" in inventory and noun == "paper":
                        currentRoom.itemDescriptions[i] = "It is a piece of paper, it USED to have the clockhands underneath it."
                    response = currentRoom.itemDescriptions[i]
                    # no need to check any more items
                    break
        # the verb is: take
        elif (verb == "take"):
            # set a default response
            response = "I don't see that item."

            # check for valid grabbable items in the current
            #  room
            for grabbable in currentRoom.grabbables:
                # a valid grabbable item is found
                if (noun == grabbable):
                    # add the grabbable item to the player's
                    #  inventory
                    inventory.append(grabbable)

                    # remove the grabbable item from the
                    #  room
                    currentRoom.delGrabbable(grabbable)
                    # set the response (success)
                    response = "Item grabbed."

                    # no need to check any more grabbable
                    break
        elif (verb == "use"):
            for n in inventory:
                if (noun == n and currentRoom.name == "Room 1"):
                    response = "You used the " + grabbable + " and opened another exit."
                    inventory.remove(n)
                    currentRoom.addExit("win-or-trick?", win())
                else:
                    print("\nTHIS IS NOT THE RIGHT PLACE TO USE THAT ITEM.")
                break
                
    # display the response
    print("{}".format(response))