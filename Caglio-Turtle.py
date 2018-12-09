#!/usr/bin/python2
# -*- coding: utf8 
# auteur:<atfield2501@gmail.com>
# Fleur de Vie... Ou autre chose. 

import turtle
import random


turtle.getcanvas().postscript(file="Caglio-Fleur-d-Vie.eps") # Enregistrement de la figure final dans un fichier.
unique=turtle.Turtle()                                       # Deffinition d'un tortue au nom unique.
clone_unique =turtle.Turtle()
espace = turtle.Screen()                                     # Deffinition de l'aire de jeu pour tortues 
                                                             #
espace.setup(width=0.5, height=1.0, startx=-1, starty=0)     #
espace.bgcolor("black")                                      #


########### DATAs
a = 15
b = 20
phi = 1.64
angle = 5
distance = 10


def rosace(d):
    """
     Fonction prenant en charge le dessin d'une rosace

    """
    while d<=20:
        unique.color(random.choice(['red', 'green', 'pink' , 'blue', 'orange', 'purple']) )
        unique.circle(180, 360)
        unique.up()
#        unique.goto(a, b)
        unique.down()
        unique.left(15)
#        unique.speed(random.choice(['slowest', 'slow', 'normal' , 'fast', 'fastest']))
        unique.speed('fastest')

        d += 1


def spirale(d,angle):
    """
     Fonction prenant en charge le dessin d'une spirale

    """
    while d <= 30:
        unique.forward(distance)
        unique.right(angle)
        unique.forward(distance+d)
        d += 1
        angle += 2

def transpose():
    """
     Fonction prenant en charge la transposition de l'ensemble du dessin

    """
    unique.up()
    unique.goto(a, b) 
    unique.down()

def bubble(d):
    nbBlue = 0
    nbBubble= random.choice([1, 2, 5 , 8, 10 ,15])  
    while nbBlue != nbBubble:
        unique.down()
        unique.circle(180, 360)  
        unique.up() 
        unique.goto(a + nbBlue, b)  
        nbBlue += 1

def remplissage():
    unique.fill(1)

def carre(d):
    while d <= 10:
        clone_unique.color('red')
        clone_unique.width(2)
        clone_unique.forward(random.choice([50,120]))
        clone_unique.left(90)
        clone_unique.forward(random.choice([50,120,30]))
        clone_unique.left(90)
        clone_unique.forward(95)
        clone_unique.right(30)
        d +=1

############################ BOUCLE DU PROGRAMME

while 1:
    d=0
    unique.speed('fastest')
    unique.width(random.choice(['1', '1.5', '2' , '2.5', '5' ,'8']))
    unique.write('^[;,,;]^')
#    aAa += 0.5
    xxx=random.choice(['1','2','3','4','5','6','7'])
    if xxx == '1':
        bubble(d)
    if xxx == '2':
        rosace(d)
    if xxx == '3':
        spirale(d,angle)
    if xxx == '4':
        clone_unique.reset()
    if xxx == '5':
        remplissage()
    if xxx == '6':
        carre(d)
    if xxx == '7':
        unique.reset()
        
