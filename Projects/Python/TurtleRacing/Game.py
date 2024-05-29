import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "green", "orange", "yellow", "black", "pink", "brown", "cyan", "blue", "purple"]


def get_number__of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2 - 10. Try again!")
            continue

def create_turtles(colors):
    turtles = []
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()

        turtles.append(racer)


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


racers = get_number__of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]  #to get the first number of colors as much as we have racers
create_turtles(colors)

