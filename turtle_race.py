# this is a python program that utilizes turtle.
# a number of turtles will be selected to go on a race and the winner will be outputted as such
import turtle
import time

WIDTH, HEIGHT=500,500
def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Ninja Turtle Racing")

def get_input():
    user_input = 0
    while True:
        user_input = input("How many turtle do you want in the race:  ")
        if user_input.isdigit():
                user_input=int(user_input)
        else:
            print("You need to enter a numeric value")
            continue
        if 2 <= user_input <= 10:
            return user_input
        else:
             print("You need to select between the range of 2-10")

get_input()
init_turtle()
time.sleep(100)