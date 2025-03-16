from tkinter import messagebox, simpledialog, Tk

from numpy import empty
from sklearn.base import check_is_fitted 
"""
Ask how many people, rooms. amd nights.
Maybe different types of rooms.
Give a price for the stay.
Add and delete people. 
track room number(s)
"""


room_nums = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15.16,17,18,19,20)   
checked_rooms = list()
rooms = {}
def add_people():
    name_people = input("What's your name?")
    num_ppl = input("How many people are staying with us?")
    booked = ask_rooms(num_ppl)
    nights = input("How many nights are you staying with us?")
    price = int(len(booked)) * 200
    print("That will be $" + str(int(price)*int(nights)) + " for the whole stay.")
    checked_rooms.extend(booked)
    for room in booked:
        rooms[room] = name_people
    

def ask_rooms(num_ppl):
    room_got = input(f"Which rooms would you like? The rooms are{room_nums} and the checked out rooms are{checked_rooms}. Only 4 people are allowed in each room." )
    booked = room_got.split(",")
    booked = [int(room)for room in booked]
    taken_rooms = [room for room in booked if room in rooms.keys()]
    if int(num_ppl) > 4 * len(booked):
        print("Please book more roooms, only 4 people are allowed per room.")
        return ask_rooms(num_ppl)
    elif taken_rooms:      
        print("Sorry, the room that you booked is already taken by another customer, please book a different room.")
        return ask_rooms(num_ppl) 
    else:
        return booked     

    
def remove_people():
    name_people = input("What's your name?")
    booked = [] 
    for room, name in rooms.items():
        if name == name_people:
            booked.append(room)
    if booked is empty:
        print ("No rooms are currently booked")
        return
        
    for room in booked:        
        
        if name_people in rooms:
            print("Error: You were never checked in.")
            
        else:
            del rooms[room]
            checked_rooms.remove(room)
            print("Thank you for staying at Shanmith Inn")
    return name_people
   
def check_out(room_nums, rooms, add_people, remove_people):
    inout = (input("Are you checking in or checking out?"))
    if inout == "in":
        add_people()
        print(rooms)
        print(room_nums)
        print("Enjoy your stay.")
    elif inout == "out":
        print(rooms)
        if remove_people() not in rooms.values():
            print("you have been checked out already or you were never checked in.")
        

while room_nums:
    check_out(room_nums, rooms, add_people, remove_people)