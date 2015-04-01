# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:04:57 2015

@author: marcelotanak
"""


import turtle

j = turtle.Screen ()
j.bgcolor("DarkGreen")
j.title("Jogo da Forca")

erros = 0 


def forca ():
    v = turtle.Turtle()
    v.penup()
    v.setpos(-300,-100)
    v.pendown()
    v.left(90)
    v.forward(350)
    v.speed(5000)
    v.hideturtle()

    z = turtle.Turtle()
    z.penup()
    z.setpos(-300,250)
    z.pendown()
    z.forward(100)
    z.speed(5000)
    z.hideturtle()

    k = turtle.Turtle()
    k.penup()
    k.setpos(-200,250)
    k.pendown()
    k.left(270)
    k.forward(60)
    k.speed(5000)
    k.hideturtle()

def boneco ():
    if erros == 1:
        d = turtle.Turtle ()
        d.penup()
        d.setpos (-200, 150)
        d.pendown()
        d.circle(20)
        d.speed(5000)
        d.hideturtle()

    if erros == 2:
        x = turtle.Turtle ()    
        x.penup()    
        x.setpos(-200,150)
        x.pendown ()
        x.left (270)
        x.forward (200)
        x.speed(5000)
        x.hideturtle()

    if erros == 3:
        y = turtle.Turtle ()
        y.penup()
        y.setpos(-200,120)
        y.pendown()
        y.left(200)
        y.forward(50)
        y.speed(5000)
        y.hideturtle()

    if erros == 4:
        w = turtle.Turtle()
        w.penup()   
        w.setpos(-200,120)
        w.pendown()
        w.left(340)
        w.forward(50)
        w.speed(5000)
        w.hideturtle()

    if erros == 5:
        p = turtle.Turtle()
        p.penup()
        p.setpos(-200,-50)
        p.pendown()
        p.left(200)
        p.forward(50)
        p.speed(5000)
        p.hideturtle()

    if erros == 6:
        q = turtle.Turtle()
        q.penup()
        q.setpos(-200,-50)
        q.pendown()
        q.left(340)
        q.forward(50)
        q.speed(5000)
        q.hideturtle()




from random import randint

text = open ("entrada.txt", encoding = "utf-8")

r = randint (1,11)

t = text.readlines ()

palavra = t[r].strip().upper ()

n = turtle.Turtle ()
n.penup ()
n.penup ()
n.setpos (-200, -200)
n.pendown ()

for i in palavra:
    n.forward (20)
    n.penup ()
    n.forward (4)
    n.pendown ()

letra = turtle.textinput ("Jogo da Forca" , "Digite uma Letra" )





j.exitonclick()




    

  
