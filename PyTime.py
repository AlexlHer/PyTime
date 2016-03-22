# -*- coding: utf-8 -*-
# Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("Horloge v3.2")
print("----------------------------------------------------------------------")
print("Ne pas fermer la fenètre sauf pour fermer l'horloge.")

import time
from turtle import Turtle
import turtle
import random
hh1 = 1
hh2 = 1
mm1 = 1
mm2 = 1
cadre = 0

print("")
choix = str(input("Avec des couleurs aléatoire ? "))

def zero(t, c, f, g):
	x_d = c[0] - int(-80)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.penup()
	t.left(180)
	t.forward(10)
	t.right(90)
	t.forward(10)
	t.down()
	t.forward(120)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(60)
	t.hideturtle()

def un(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140)
	t.left(130)
	t.forward(100)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(80)
	t.left(-130)
	t.forward(120)
	t.left(90)
	t.forward(9)
	t.hideturtle()
	
def deux(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(10)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(60)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(70)
	t.left(90)
	t.forward(80)
	t.hideturtle()
		
def trois(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(40)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(40)
	t.right(90)
	t.forward(60)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(80)
	t.hideturtle()
	
def quatre(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140)
	t.left(140)
	t.forward(120)
	t.left(130)
	t.forward(90)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(70)
	t.right(130)
	t.forward(75)
	t.right(140)
	t.forward(116)
	t.left(90)
	t.forward(9)
	t.hideturtle()
	
def cinq(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(80)
	t.left(90)
	t.forward(70)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(60)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(70)
	t.right(90)
	t.forward(50)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(10)
	t.hideturtle()

def six(t, c, f, g):
	x_d = c[0] - int(-70)
	y_d = c[1] - int(-70)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.right(0)
	t.forward(70)
	t.right(90)
	t.forward(70)
	t.right(90)
	t.forward(80)
	t.right(90)
	t.forward(140)
	t.right(90)
	t.forward(80)
	t.right(90)
	t.forward(10)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.hideturtle()
	
def sept(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(50)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.right(-10)
	t.forward(70)
	t.right(60)
	t.forward(20)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(15)
	t.right(120)
	t.forward(80)
	t.left(120)
	t.forward(80)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(65)
	t.right(120)
	t.forward(68)
	t.right(60)
	t.forward(20)
	t.left(90)
	t.forward(10)
	t.left(90)
	t.forward(15)
	t.right(120)
	t.forward(70)
	t.left(120)
	t.forward(10)
	t.hideturtle()
	
def huit(t, c, f, g):
	x_d = c[0] - int(-80)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.penup()
	t.left(180)
	t.forward(10)
	t.right(90)
	t.forward(10)
	t.down()
	t.forward(60)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(60)
	t.penup()
	t.left(90)
	t.forward(70)
	t.down()
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.hideturtle()
	
def neuf(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(-70)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(180)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.right(0)
	t.forward(70)
	t.right(90)
	t.forward(70)
	t.right(90)
	t.forward(80)
	t.right(90)
	t.forward(140)
	t.right(90)
	t.forward(80)
	t.right(90)
	t.forward(10)
	t.right(90)
	t.forward(70)
	t.left(90)
	t.forward(120)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(50)
	t.left(90)
	t.forward(60)
	t.hideturtle()
	
def pzero(t, c, f, g):
	x_d = c[0] - int(-80)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.penup()
	t.left(180)
	t.forward(10/3)
	t.right(90)
	t.forward(10/3)
	t.down()
	t.forward(120/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(120/3)
	t.left(90)
	t.forward(60/3)
	t.hideturtle()

def pun(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140/3)
	t.left(130)
	t.forward(100/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(80/3)
	t.left(-130)
	t.forward(120/3)
	t.left(90)
	t.forward(9/3)
	t.hideturtle()
	
def pdeux(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(10/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(50/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(60/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(70/3)
	t.left(90)
	t.forward(80/3)
	t.hideturtle()
		
def ptrois(t, c, f, g):
	x_d = c[0] - int(-10)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(50/3)
	t.right(90)
	t.forward(40/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(40/3)
	t.right(90)
	t.forward(60/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(80/3)
	t.hideturtle()
	
def pquatre(t, c, f, g):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140/3)
	t.left(140)
	t.forward(120/3)
	t.left(130)
	t.forward(90/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(70/3)
	t.right(130)
	t.forward(75/3)
	t.right(140)
	t.forward(116/3)
	t.left(90)
	t.forward(9/3)
	t.hideturtle()
	
def pcinq(t, c, f, g):
	x_d = c[0] - int(-60)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(80/3)
	t.left(90)
	t.forward(70/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(60/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(70/3)
	t.right(90)
	t.forward(50/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(10/3)
	t.hideturtle()

def psix(t, c, f, g):
	x_d = c[0] - int(-115)
	y_d = c[1] - int(-23)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.right(0)
	t.forward(70/3)
	t.right(90)
	t.forward(70/3)
	t.right(90)
	t.forward(80/3)
	t.right(90)
	t.forward(140/3)
	t.right(90)
	t.forward(80/3)
	t.right(90)
	t.forward(10/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(120/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(50/3)
	t.left(90)
	t.forward(60/3)
	t.hideturtle()
	
def psept(t, c, f, g):
	x_d = c[0] - int(-55)
	y_d = c[1] - int(-0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(50)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.right(-10)
	t.forward(70/3)
	t.right(60)
	t.forward(20/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(15/3)
	t.right(120)
	t.forward(80/3)
	t.left(120)
	t.forward(80/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(65/3)
	t.right(120)
	t.forward(68/3)
	t.right(60)
	t.forward(20/3)
	t.left(90)
	t.forward(10/3)
	t.left(90)
	t.forward(15/3)
	t.right(120)
	t.forward(70/3)
	t.left(120)
	t.forward(10/3)
	t.hideturtle()
	
def phuit(t, c, f, g):
	x_d = c[0] - int(-80)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.left(90)
	t.forward(140/3)
	t.left(90)
	t.forward(80/3)
	t.penup()
	t.left(180)
	t.forward(10/3)
	t.right(90)
	t.forward(10/3)
	t.down()
	t.forward(60/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(60/3)
	t.penup()
	t.left(90)
	t.forward(70/3)
	t.down()
	t.forward(50/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(50/3)
	t.left(90)
	t.forward(60/3)
	t.hideturtle()
	
def pneuf(t, c, f, g):
	x_d = c[0] - int(-12)
	y_d = c[1] - int(-23)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(180)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.right(0)
	t.forward(70/3)
	t.right(90)
	t.forward(70/3)
	t.right(90)
	t.forward(80/3)
	t.right(90)
	t.forward(140/3)
	t.right(90)
	t.forward(80/3)
	t.right(90)
	t.forward(10/3)
	t.right(90)
	t.forward(70/3)
	t.left(90)
	t.forward(120/3)
	t.left(90)
	t.forward(60/3)
	t.left(90)
	t.forward(50/3)
	t.left(90)
	t.forward(60/3)
	t.hideturtle()
	
def milieu(t, c, f, g):
	x_d = c[0] - int(-90)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(50)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(50)
	t.hideturtle()
	t.reset()
	t.hideturtle()

def contour(t, c, f, g):
	x_d = c[0] - int(-350)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.forward(190)
	t.left(90)
	t.forward(540)
	t.left(90)
	t.forward(190)
	t.left(90)
	t.forward(540)
	t.hideturtle()
	
def color(alea):
	if alea == 98:
		fondcolor = 'white'
	elif alea == 99:
		fondcolor = 'black'
	elif alea == 1:
		fondcolor = 'blue'
	elif alea == 2:
		fondcolor = 'red'
	elif alea == 3:
		fondcolor = 'green'
	elif alea == 4:
		fondcolor = 'violet'
	elif alea == 5:
		fondcolor = 'yellow'
	elif alea == 6:
		fondcolor = 'brown'
	elif alea == 7:
		fondcolor = 'pink'
	elif alea == 8:
		fondcolor = 'purple'
	elif alea == 9:
		fondcolor = 'grey'
	else:
		fondcolor = 'orange'
	return fondcolor
	
def main0(a, b, f, g):
	t = Turtle()
	c = (a +(-130), b + (-50))
	zero(t, c, f, g)

def main1(a, b, f, g):
	t = Turtle()
	c = (a +(-60), b + (-50))
	un(t, c, f, g)
	
def main2(a, b, f, g):
	t = Turtle()
	c = (a +(-60), b + (-50))
	deux(t, c, f, g)

def main3(a, b, f, g):
	t = Turtle()
	c = (a +(-60), b + (-50))
	trois(t, c, f, g)
	
def main4(a, b, f, g):
	t = Turtle()
	c = (a +(-60), b + (-50))
	quatre(t, c, f, g)
	
def main5(a, b, f, g):
	t = Turtle()
	c = (a +(-140), b + (-50))
	cinq(t, c, f, g)
	
def main6(a, b, f, g):
	t = Turtle()
	c = (a +(-200), b + (-50))
	six(t, c, f, g)
	
def main7(a, b, f, g):
	t = Turtle()
	c = (a +(-140), b + (-50))
	sept(t, c, f, g)
	
def main8(a, b, f, g):
	t = Turtle()
	c = (a +(-140), b + (-50))
	huit(t, c, f, g)
	
def main9(a, b, f, g):
	t = Turtle()
	c = (a +(-70), b + (-50))
	neuf(t, c, f, g)
	
def mainp0(a, b, f, g):
	t = Turtle()
	c = (a +(-130), b + (-50))
	pzero(t, c, f, g)

def mainp1(a, b, f, g):
	t = Turtle()
	c = (a +(-60), b + (-50))
	pun(t, c, f, g)
	
def mainp2(a, b, f, g):
	t = Turtle()
	c = (a +(-60), b + (-50))
	pdeux(t, c, f, g)

def mainp3(a, b, f, g):
	t = Turtle()
	c = (a +(-60), b + (-50))
	ptrois(t, c, f, g)
	
def mainp4(a, b, f, g):
	t = Turtle()
	c = (a +(-60), b + (-50))
	pquatre(t, c, f, g)
	
def mainp5(a, b, f, g):
	t = Turtle()
	c = (a +(-140), b + (-50))
	pcinq(t, c, f, g)
	
def mainp6(a, b, f, g):
	t = Turtle()
	c = (a +(-200), b + (-50))
	psix(t, c, f, g)
	
def mainp7(a, b, f, g):
	t = Turtle()
	c = (a +(-140), b + (-50))
	psept(t, c, f, g)
	
def mainp8(a, b, f, g):
	t = Turtle()
	c = (a +(-140), b + (-50))
	phuit(t, c, f, g)
	
def mainp9(a, b, f, g):
	t = Turtle()
	c = (a +(-70), b + (-50))
	pneuf(t, c, f, g)
	
def mainm(a, b, f, g):
	t = Turtle()
	c = (a +(-70), b + 0)
	milieu(t, c, f, g)
	
def mainc(a, b, f, g):
	t = Turtle()
	c = (a +(-70), b + (-90))
	contour(t, c, f, g)

turtle.setup(width=850,height=450)
turtle.title("Horloge v3.2")

for i in range(1000):
	heure = time.strftime("%H")
	minu = time.strftime("%M")
	day = time.strftime("%d")
	mois = time.strftime("%m")
	ans = time.strftime("%y")
	h1 = int(heure[0])
	h2 = int(heure[1])
	m1 = int(minu[0])
	m2 = int(minu[1])
	d1 = int(day[0])
	d2 = int(day[1])
	mo1 = int(mois[0])
	mo2 = int(mois[1])
	a1 = int(ans[0])
	a2 = int(ans[1])
	
	
	if (h1 == 1 and h2 >= 8) or (h1 == 2) or (h1 == 0 and h2 <= 8):
		fondcolor = 'white'
		ifondcolor = 'black'
		alea = 98
		turtle.bgcolor('black')
	else:
		fondcolor = 'black'
		ifondcolor = 'white'
		alea = 99
		turtle.bgcolor('white')
		
	if cadre == 0:
		mainc(-10, 15, fondcolor, 1)
		if d1 == 0:
			mainp0(-50, -100, fondcolor, 1)
		elif d1 == 1:
			mainp1(-50, -100, fondcolor, 1)
		elif d1 == 2:
			mainp2(-50, -100, fondcolor, 1)
		elif d1 == 3:
			mainp3(-50, -100, fondcolor, 1)
		if d2 == 0:
			mainp0(-10, -100, fondcolor, 1)
		elif d2 == 1:
			mainp1(-10, -100, fondcolor, 1)
		elif d2 == 2:
			mainp2(-10, -100, fondcolor, 1)
		elif d2 == 3:
			mainp3(-10, -100, fondcolor, 1)
		elif d2 == 4:
			mainp4(-10, -100, fondcolor, 1)
		elif d2 == 5:
			mainp5(-10, -100, fondcolor, 1)
		elif d2 == 6:
			mainp6(-10, -100, fondcolor, 1)
		elif d2 == 7:
			mainp7(-10, -100, fondcolor, 1)
		elif d2 == 8:
			mainp8(-10, -100, fondcolor, 1)
		elif d2 == 9:
			mainp9(-10, -100, fondcolor, 1)
		if mo1 == 0:
			mainp0(50, -100, fondcolor, 1)
		elif mo1 == 1:
			mainp1(50, -100, fondcolor, 1)
		if mo2 == 0:
			mainp0(90, -100, fondcolor, 1)
		elif mo2 == 1:
			mainp1(90, -100, fondcolor, 1)
		elif mo2 == 2:
			mainp2(90, -100, fondcolor, 1)
		elif mo2 == 3:
			mainp3(90, -100, fondcolor, 1)
		elif mo2 == 4:
			mainp4(90, -100, fondcolor, 1)
		elif mo2 == 5:
			mainp5(90, -100, fondcolor, 1)
		elif mo2 == 6:
			mainp6(90, -100, fondcolor, 1)
		elif mo2 == 7:
			mainp7(90, -100, fondcolor, 1)
		elif mo2 == 8:
			mainp8(90, -100, fondcolor, 1)
		elif mo2 == 9:
			mainp9(90, -100, fondcolor, 1)
		if a1 == 1:
			mainp1(150, -100, fondcolor, 1)
		elif a1 == 2:
			mainp2(150, -100, fondcolor, 1)
		elif a1 == 3:
			mainp3(150, -100, fondcolor, 1)
		if a2 == 0:
			mainp0(190, -100, fondcolor, 1)
		elif a2 == 1:
			mainp1(190, -100, fondcolor, 1)
		elif a2 == 2:
			mainp2(190, -100, fondcolor, 1)
		elif a2 == 3:
			mainp3(190, -100, fondcolor, 1)
		elif a2 == 4:
			mainp4(190, -100, fondcolor, 1)
		elif a2 == 5:
			mainp5(190, -100, fondcolor, 1)
		elif a2 == 6:
			mainp6(190, -100, fondcolor, 1)
		elif a2 == 7:
			mainp7(190, -100, fondcolor, 1)
		elif a2 == 8:
			mainp8(190, -100, fondcolor, 1)
		elif a2 == 9:
			mainp9(190, -100, fondcolor, 1)
	cadre = 1
	
	if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
		alea = random.randint(0, 9)
		colr = ['blue', 'red', 'green', 'violet', 'yellow', 'brown',\
		'pink', 'purple', 'grey', 'orange']
		fondcolor = colr[alea]
	elif alea == 98:
		fondcolor = 'white'
	elif alea == 99:
		fondcolor = 'black'
		
	if hh1 == 1:
		if h1 == 0:
			main0(-100, 0, fondcolor, 3)
		elif h1 == 1:
			main1(-100, 0, fondcolor, 3)
		elif h1 == 2:
			main2(-100, 0, fondcolor, 3)
			
	if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
		alea = random.randint(0, 9)
		colr = ['blue', 'red', 'green', 'violet', 'yellow', 'brown',\
		'pink', 'purple', 'grey', 'orange']
		fondcolor = colr[alea]
	elif alea == 98:
		fondcolor = 'white'
	elif alea == 99:
		fondcolor = 'black'
		
	if hh2 == 1:
		if h2 == 0:
			main0(0, 0, fondcolor, 3)
		elif h2 == 1:
			main1(0, 0, fondcolor, 3)
		elif h2 == 2:
			main2(0, 0, fondcolor, 3)
		elif h2 == 3:
			main3(0, 0, fondcolor, 3)
		elif h2 == 4:
			main4(0, 0, fondcolor, 3)
		elif h2 == 5:
			main5(0, 0, fondcolor, 3)
		elif h2 == 6:
			main6(0, 0, fondcolor, 3)
		elif h2 == 7:
			main7(0, 0, fondcolor, 3)
		elif h2 == 8:
			main8(0, 0, fondcolor, 3)
		elif h2 == 9:
			main9(0, 0, fondcolor, 3)
		
	if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
		alea = random.randint(0, 9)
		colr = ['blue', 'red', 'green', 'violet', 'yellow', 'brown',\
		'pink', 'purple', 'grey', 'orange']
		fondcolor = colr[alea]
	elif alea == 98:
		fondcolor = 'white'
	elif alea == 99:
		fondcolor = 'black'
		
	if mm1 == 1:
		if m1 == 0:
			main0(190, 0, fondcolor, 3)
		elif m1 == 1:
			main1(190, 0, fondcolor, 3)
		elif m1 == 2:
			main2(190, 0, fondcolor, 3)
		elif m1 == 3:
			main3(190, 0, fondcolor, 3)
		elif m1 == 4:
			main4(190, 0, fondcolor, 3)
		elif m1 == 5:
			main5(190, 0, fondcolor, 3)
		
	if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
		alea = random.randint(0, 9)
		colr = ['blue', 'red', 'green', 'violet', 'yellow', 'brown',\
		'pink', 'purple', 'grey', 'orange']
		fondcolor = colr[alea]
	elif alea == 98:
		fondcolor = 'white'
	elif alea == 99:
		fondcolor = 'black'
		
	if mm2 == 1:
		if m2 == 0:
			main0(290, 0, fondcolor, 3)
		elif m2 == 1:
			main1(290, 0, fondcolor, 3)
		elif m2 == 2:
			main2(290, 0, fondcolor, 3)
		elif m2 == 3:
			main3(290, 0, fondcolor, 3)
		elif m2 == 4:
			main4(290, 0, fondcolor, 3)
		elif m2 == 5:
			main5(290, 0, fondcolor, 3)
		elif m2 == 6:
			main6(290, 0, fondcolor, 3)
		elif m2 == 7:
			main7(290, 0, fondcolor, 3)
		elif m2 == 8:
			main8(290, 0, fondcolor, 3)
		elif m2 == 9:
			main9(290, 0, fondcolor, 3)
	
	for i in range(1):
		if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
			alea = random.randint(0, 9)
			colr = ['blue', 'red', 'green', 'violet', 'yellow', 'brown',\
			'pink', 'purple', 'grey', 'orange']
			mfondcolor = colr[alea]
		elif alea == 98:
			mfondcolor = 'white'
		elif alea == 99:
			mfondcolor = 'black'
   
		mainm(-10, 15, mfondcolor, 1)
		time.sleep(0)
		
	heure1 = time.strftime("%H")
	minu1 = time.strftime("%M")
	h11 = int(heure1[0])
	h21 = int(heure1[1])
	m11 = int(minu1[0])
	m21 = int(minu1[1])
	hh1 = 0
	hh2 = 0
	mm1 = 0
	mm2 = 0
	if h11 != h1:
		hh1 = 1
		if h1 == 0:
			main0(-100, 0, ifondcolor, 3)
		elif h1 == 1:
			main1(-100, 0, ifondcolor, 3)
		elif h1 == 2:
			main2(-100, 0, ifondcolor, 3)
   
	if h21 != h2:
		hh2 = 1
		if h2 == 0:
			main0(0, 0, ifondcolor, 3)
		elif h2 == 1:
			main1(0, 0, ifondcolor, 3)
		elif h2 == 2:
			main2(0, 0, ifondcolor, 3)
		elif h2 == 3:
			main3(0, 0, ifondcolor, 3)
		elif h2 == 4:
			main4(0, 0, ifondcolor, 3)
		elif h2 == 5:
			main5(0, 0, ifondcolor, 3)
		elif h2 == 6:
			main6(0, 0, ifondcolor, 3)
		elif h2 == 7:
			main7(0, 0, ifondcolor, 3)
		elif h2 == 8:
			main8(0, 0, ifondcolor, 3)
		elif h2 == 9:
			main9(0, 0, ifondcolor, 3)
   
	if m11 != m1:
		mm1 = 1
		if m1 == 0:
			main0(190, 0, ifondcolor, 3)
		elif m1 == 1:
			main1(190, 0, ifondcolor, 3)
		elif m1 == 2:
			main2(190, 0, ifondcolor, 3)
		elif m1 == 3:
			main3(190, 0, ifondcolor, 3)
		elif m1 == 4:
			main4(190, 0, ifondcolor, 3)
		elif m1 == 5:
			main5(190, 0, ifondcolor, 3)
   
	if m21 != m2:
		mm2 = 1
		if m2 == 0:
			main0(290, 0, ifondcolor, 3)
		elif m2 == 1:
			main1(290, 0, ifondcolor, 3)
		elif m2 == 2:
			main2(290, 0, ifondcolor, 3)
		elif m2 == 3:
			main3(290, 0, ifondcolor, 3)
		elif m2 == 4:
			main4(290, 0, ifondcolor, 3)
		elif m2 == 5:
			main5(290, 0, ifondcolor, 3)
		elif m2 == 6:
			main6(290, 0, ifondcolor, 3)
		elif m2 == 7:
			main7(290, 0, ifondcolor, 3)
		elif m2 == 8:
			main8(290, 0, ifondcolor, 3)
		elif m2 == 9:
			main9(290, 0, ifondcolor, 3)

"""
Changelog :
v3.2
Réglage de la taille de la fenètre.
Améliorations de l'affichage de la date.
Ajout d'un titre pour la fenètre.
Optimisation du code.

v3.1
Correction de quelques bugs.

v3.0
Ajout d'un cadre.
Ajout de la date.

v2.2
Correction d'un problème de ralentissement.

v2.1
Ajout de quelques couleurs.

v2.0
Ajout des couleurs aléatoire.
Ajout du mode nuit.

v1.0
Version final de Projet Pytime, renommée Horloge.
"""
