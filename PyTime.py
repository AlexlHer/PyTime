# -*- coding: utf-8 -*-
# Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("Horloge")
print("----------------------------------------------------------------------")
print("")
print("Ne pas fermer la fenetre.")

import time
from turtle import Turtle
import turtle
import random
hh1 = 1
hh2 = 1
mm1 = 1
mm2 = 1

choix = str(input("Avec des couleurs aléatoire ? "))

def zero(t, c, f):
	x_d = c[0] - int(-80)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
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

def un(t, c, f):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
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
	
def deux(t, c, f):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
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
		
def trois(t, c, f):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
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
	
def quatre(t, c, f):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
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
	
def cinq(t, c, f):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
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

def six(t, c, f):
	x_d = c[0] - int(-70)
	y_d = c[1] - int(-70)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
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
	
def sept(t, c, f):
	x_d = c[0] - int(0)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(50)
	t.down()
	t.pencolor(f)
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
	
def huit(t, c, f):
	x_d = c[0] - int(-80)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
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
	
def neuf(t, c, f):
	x_d = c[0] - int(0)
	y_d = c[1] - int(-70)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(180)
	t.down()
	t.pencolor(f)
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
	
def milieu(t, c, f):
	x_d = c[0] - int(-80)
	y_d = c[1] - int(0)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.forward(50)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(100)
	t.left(90)
	t.forward(20)
	t.left(90)
	t.forward(50)
	
def main0(a, b, f):
	t = Turtle()
	c = (a +(-130), b + (-50))
	zero(t, c, f)

def main1(a, b, f):
	t = Turtle()
	c = (a +(-60), b + (-50))
	un(t, c, f)
	
def main2(a, b, f):
	t = Turtle()
	c = (a +(-60), b + (-50))
	deux(t, c, f)

def main3(a, b, f):
	t = Turtle()
	c = (a +(-60), b + (-50))
	trois(t, c, f)
	
def main4(a, b, f):
	t = Turtle()
	c = (a +(-60), b + (-50))
	quatre(t, c, f)
	
def main5(a, b, f):
	t = Turtle()
	c = (a +(-140), b + (-50))
	cinq(t, c, f)
	
def main6(a, b, f):
	t = Turtle()
	c = (a +(-200), b + (-50))
	six(t, c, f)
	
def main7(a, b, f):
	t = Turtle()
	c = (a +(-140), b + (-50))
	sept(t, c, f)
	
def main8(a, b, f):
	t = Turtle()
	c = (a +(-140), b + (-50))
	huit(t, c, f)
	
def main9(a, b, f):
	t = Turtle()
	c = (a +(-70), b + (-50))
	neuf(t, c, f)
	
def mainm(a, b, f):
	t = Turtle()
	c = (a +(-70), b + 0)
	milieu(t, c, f)
	
for i in range(1000):
	heure = time.strftime("%H")
	minu = time.strftime("%M")
	h1 = int(heure[0])
	h2 = int(heure[1])
	m1 = int(minu[0])
	m2 = int(minu[1])
	
	if (h1 == 1 and h2 >= 8) or (h1 == 2) or (h1 == 0 and h2 <= 8):
		ifondcolor = 'black'
		alea = 98
		turtle.bgcolor('black')
	else:
		ifondcolor = 'white'
		alea = 99
		turtle.bgcolor('white')
		
	if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
		alea = random.randint(1,10)
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
		
	if hh1 == 1:
		if h1 == 0:
			main0(-100, 0, fondcolor)
		elif h1 == 1:
			main1(-100, 0, fondcolor)
		elif h1 == 2:
			main2(-100, 0, fondcolor)
			
	if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
		alea = random.randint(1,10)
  
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
		
	if hh2 == 1:
		if h2 == 0:
			main0(-10, 0, fondcolor)
		elif h2 == 1:
			main1(-10, 0, fondcolor)
		elif h2 == 2:
			main2(-10, 0, fondcolor)
		elif h2 == 3:
			main3(-10, 0, fondcolor)
		elif h2 == 4:
			main4(-10, 0, fondcolor)
		elif h2 == 5:
			main5(-10, 0, fondcolor)
		elif h2 == 6:
			main6(-10, 0, fondcolor)
		elif h2 == 7:
			main7(-10, 0, fondcolor)
		elif h2 == 8:
			main8(-10, 0, fondcolor)
		elif h2 == 9:
			main9(-10, 0, fondcolor)
		
	if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
		alea = random.randint(1,10)
  
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
		
	if mm1 == 1:
		if m1 == 0:
			main0(190, 0, fondcolor)
		elif m1 == 1:
			main1(190, 0, fondcolor)
		elif m1 == 2:
			main2(190, 0, fondcolor)
		elif m1 == 3:
			main3(190, 0, fondcolor)
		elif m1 == 4:
			main4(190, 0, fondcolor)
		elif m1 == 5:
			main5(190, 0, fondcolor)
		
	if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
		alea = random.randint(1,10)
  
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
		
	if mm2 == 1:
		if m2 == 0:
			main0(290, 0, fondcolor)
		elif m2 == 1:
			main1(290, 0, fondcolor)
		elif m2 == 2:
			main2(290, 0, fondcolor)
		elif m2 == 3:
			main3(290, 0, fondcolor)
		elif m2 == 4:
			main4(290, 0, fondcolor)
		elif m2 == 5:
			main5(290, 0, fondcolor)
		elif m2 == 6:
			main6(290, 0, fondcolor)
		elif m2 == 7:
			main7(290, 0, fondcolor)
		elif m2 == 8:
			main8(290, 0, fondcolor)
		elif m2 == 9:
			main9(290, 0, fondcolor)
	
	for i in range(1):
		if choix == "oui" or choix == "o" or choix == "Oui" or choix == "O":
			alea = random.randint(1,10)
   
		if alea == 98:
			mfondcolor = 'white'
		elif alea == 99:
			mfondcolor = 'black'
		elif alea == 1:
			mfondcolor = 'blue'
		elif alea == 2:
			mfondcolor = 'red'
		elif alea == 3:
			mfondcolor = 'green'
		elif alea == 4:
			mfondcolor = 'violet'
		elif alea == 5:
			mfondcolor = 'yellow'
		elif alea == 6:
			mfondcolor = 'brown'
		elif alea == 7:
			mfondcolor = 'pink'
		elif alea == 8:
			mfondcolor = 'purple'
		elif alea == 9:
			mfondcolor = 'grey'
		else:
			mfondcolor = 'orange'
   
		mainm(-10, 15, mfondcolor)
		time.sleep(1)
		
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
			main0(-100, 0, ifondcolor)
		elif h1 == 1:
			main1(-100, 0, ifondcolor)
		elif h1 == 2:
			main2(-100, 0, ifondcolor)
   
	if h21 != h2:
		hh2 = 1
		if h2 == 0:
			main0(-10, 0, ifondcolor)
		elif h2 == 1:
			main1(-10, 0, ifondcolor)
		elif h2 == 2:
			main2(-10, 0, ifondcolor)
		elif h2 == 3:
			main3(-10, 0, ifondcolor)
		elif h2 == 4:
			main4(-10, 0, ifondcolor)
		elif h2 == 5:
			main5(-10, 0, ifondcolor)
		elif h2 == 6:
			main6(-10, 0, ifondcolor)
		elif h2 == 7:
			main7(-10, 0, ifondcolor)
		elif h2 == 8:
			main8(-10, 0, ifondcolor)
		elif h2 == 9:
			main9(-10, 0, ifondcolor)
   
	if m11 != m1:
		mm1 = 1
		if m1 == 0:
			main0(190, 0, ifondcolor)
		elif m1 == 1:
			main1(190, 0, ifondcolor)
		elif m1 == 2:
			main2(190, 0, ifondcolor)
		elif m1 == 3:
			main3(190, 0, ifondcolor)
		elif m1 == 4:
			main4(190, 0, ifondcolor)
		elif m1 == 5:
			main5(190, 0, ifondcolor)
   
	if m21 != m2:
		mm2 = 1
		if m2 == 0:
			main0(290, 0, ifondcolor)
		elif m2 == 1:
			main1(290, 0, ifondcolor)
		elif m2 == 2:
			main2(290, 0, ifondcolor)
		elif m2 == 3:
			main3(290, 0, ifondcolor)
		elif m2 == 4:
			main4(290, 0, ifondcolor)
		elif m2 == 5:
			main5(290, 0, ifondcolor)
		elif m2 == 6:
			main6(290, 0, ifondcolor)
		elif m2 == 7:
			main7(290, 0, ifondcolor)
		elif m2 == 8:
			main8(290, 0, ifondcolor)
		elif m2 == 9:
			main9(290, 0, ifondcolor)

# Pour éviter que la fenètre de commande se ferme.
print("")
print("==========================")
print("")
input("Appuyer sur Entrer pour fermer le programme.")