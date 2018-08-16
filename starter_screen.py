import turtle
"""
from pygame import mixer # Load the required library
import turtle

mixer.init()
mixer.music.load('song.mp3')
mixer.music.play()
"""
color_list = ['brown','green','blue','yellow','red']
colorNum = 0

def start_screen(color):

    turtle.hideturtle()
    screen = turtle.Screen()
    screen.setup(800,800)
    yuval=turtle.clone()
    yuval.pensize(7)
    yuval.color(color)
    yuval.shape("arrow")
    caleb=turtle.clone()
    caleb.hideturtle()
    caleb.shape("arrow")
    screen.bgcolor("light green") 
    yuval.penup()
    yuval.goto(150,-300)
    yuval.left(180)
    yuval.pendown()
    yuval.forward(300)
    yuval.right(90)
    yuval.forward(500)
    yuval.left(90)
    yuval.forward(20)
    yuval.left(90)
    yuval.forward(35)
    yuval.left(90)
    yuval.forward(20)
    yuval.left(90)
    yuval.forward(50)
    yuval.right(90)
    yuval.forward(300)
    yuval.right(90)
    yuval.forward(15)
    yuval.right(90)
    yuval.forward(300)
    yuval.backward(20)
    yuval.right(90)

    for i in range(7):
        yuval.forward(15)
        yuval.right(90)
        yuval.forward(20)
        yuval.right(90)
        yuval.forward(15)
        yuval.left(90)
        yuval.forward(20)
        yuval.left(90)
    yuval.right(180)
    yuval.forward(35)
    yuval.left(90)
    yuval.forward(20)
    yuval.left(90)
    yuval.forward(35)
    yuval.left(90)
    yuval.forward(20)
    yuval.left(90)
    yuval.forward(500)
    caleb.penup()
    caleb.color(color)
    caleb.goto(-136,-30)
    caleb.pendown()
    caleb.write('Junk\nJourney', font = ('Ariel', 48, 'bold'))


while True:
    for color in color_list:
        start_screen(color)

