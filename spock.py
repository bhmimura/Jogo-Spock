# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 03:21:11 2015

@author: marcelotanak
"""

from random import randint
x = input("Estou pronto para jogar, escolha (pedra papel tesoura lagarto ou spock):")
y = randint (1,5)

if x == "tesoura":
    x = 1
if x == "papel":
    x = 2
if x == "pedra":
    x = 3
if x == "lagarto":
    x = 4
if x == "spock":
    x = 5

if y == 1:
    w = "tesoura"
if y == 2:
    w = "papel"
if y == 3:
    w = "pedra"
if y == 4:
    w = "lagarto"
if y == 5:
    w = "spock"
    
print (w)

if x == 1:
    if y == 2 or y == 4:
        print ("Ganhou")
if x == 1:
    if y == 3 or y == 5:
        print ("Perdeu")
if x == 1:
    if y == 1:
        print ("Empate")
        

if x == 2:
    if y == 3 or y == 5:
        print ("Ganhou")
if x == 2:
    if y == 1 or y == 4:
        print ("Perdeu")
if x == 2:
    if y == 2:
        print ("Empate")
        
    
if x == 3:
    if y == 4 or y == 1:
        print ("Ganhou")
    
if x == 3:
    if y == 2 or y == 5:
        print ("Perdeu")
    
if x == 3:
    if y == 3:
        print ("Empate")
        
    
    
if x == 4:
    if y == 5 or y == 2:
        print ("Ganhou")
    
if x == 4:
    if y == 1 or y == 3:
        print ("Perdeu")
    
if x == 4:
    if y == 4:
        print ("Empate")
        
    
    
if x == 5:
    if y == 1 or y == 3:
        print ("Ganhou")
    
if x == 5:
    if y == 2 or y == 4:
        print ("Perdeu")
    
if x == 5:
    if y == 5:
        print ("Empate")
    
    
