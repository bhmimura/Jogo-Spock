# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:04:57 2015

@author: marcelotanak
"""

import turtle

j = turtle.Screen ()
j.bgcolor("lightblue")
j.title("Ismalove")


d = turtle.Turtle ()
d.penup()
d.setpos (-250, 150)
d.pendown()
d.circle(20)
d.speed(5000)

x = turtle.Turtle ()    
x.penup()    
x.setpos(-250,150)
x.pendown ()
x.left (270)
x.forward (200)
x.speed(5000)

y = turtle.Turtle ()
y.penup()
y.setpos(-250,120)
y.pendown()
y.left(180)
y.forward(50)
y.speed(5000)

w = turtle.Turtle()
w.penup()
w.setpos(-250,120)
w.pendown()
w.forward(50)
w.speed(5000)



    
j.exitonclick()