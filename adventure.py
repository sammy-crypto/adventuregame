#--imports
import random
import time
#--function

def start_room():
    start_room_options = ["1","2","3"]
    choice =""
    while choice not in start_room_options:
        print("You enter a room and there is are three foods sitting on the table, an apple, another " +
          "apple, and a third apple, which apple you want? \nApple number 1 \nApple number 2\nApple number 3")
        choice = str(input("Pick: "))
    print("You picked " + choice)
    if choice == start_room_options[0]:
        room01()
    elif choice == start_room_options[1]:
        room02()
    elif choice == start_room_options[2]:
        room03()

def room01():
    print("\n\nYou shat in your pants from this apple")
    time.sleep(5)
def room02():
    print("\n\nYou enjoyed this apple")
    time.sleep(5)
def room03():
    print("\n\nYou died from the poison apple")
    time.sleep(5)


#--program run
start_room()
