"""Ex03 Turtle Scene."""

__author__ = "730481331"

from turtle import Turtle, colormode, done


def pen(house: Turtle, x: float, y: float) -> None:
    """Sets the speed, and color or the pen."""
    house.speed(75)
    house.hideturtle()
    house.penup()
    house.goto(x, y)
    house.pendown()
    return None


def color_type(house: Turtle, x: float, y: float, z: float) -> None:
    """Sets the type of color used."""
    colormode(255)
    house.color(x, y, z)
    return None


def draw_rectangle(house: Turtle, x: float, y: float) -> None:
    """Draws a rectangle for the ground."""
    pen(house, x, y)
    color_type(house, 0, 128, 0)
    house.begin_fill()
    i: int = 0
    while (i < 2):
        house.forward(600)
        house.right(90)
        house.forward(250)
        house.right(90)
        i = i + 1
    house.end_fill()
    return None


def draw_triangle(house: Turtle, x: float, y: float) -> None:
    """Draws a triangle for a house."""
    pen(house, x, y)
    color_type(house, 255, 0, 0)
    house.begin_fill()
    i: int = 0
    while (i < 3):
        house.forward(150)
        house.left(120)
        i = i + 1
    house.end_fill()
    return None


def big_square(house: Turtle, x: float, y: float) -> None:
    """Draws a big square for a house."""
    pen(house, x, y)
    color_type(house, 165, 42, 42)
    house.begin_fill()
    i: int = 0  
    while (i < 4):
        house.forward(150)
        house.right(90)
        i = i + 1
    house.end_fill()
    return None


def small_square(house: Turtle, x: float, y: float) -> None:
    """Draws a small square for a window."""
    pen(house, x, y)
    color_type(house, 0, 0, 0)
    house.begin_fill()
    i: int = 0
    while (i < 4):
        house.forward(50)
        house.right(90)
        i = i + 1
    house.end_fill()
    return None


def main() -> None:
    """Function to draw entire scene."""
    pen_setup: Turtle = Turtle()            
    draw_rectangle(pen_setup, -300, 25) 

    i: int = 0
    x_cordinate: int = -300

    while(i < 3): 
        draw_triangle(pen_setup, x_cordinate, 175)
        big_square(pen_setup, x_cordinate, 175)
        small_square(pen_setup, x_cordinate + 50, 130)
        i = i + 1
        x_cordinate = x_cordinate + 200
    done()
    return None
