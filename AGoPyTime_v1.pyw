# -*- coding: utf-8 -*-
# Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("GoPyTime v1 analogique")
print("----------------------------------------------------------------------")

# Initialisation des variables communes et importation des modules.
import time
import turtle
import random
from tkinter import *
from tkinter.messagebox import *

v_tk_textaf_2_1 = 30		# Permet de verifier si il y a un message.
mesaffoui = 0 			# Permet de savoir si le message a déjà été affiché.
egea_1 = 0				# 
colorachif = 0			# Compte le nombre de couleur choisi par l'utilisateur.
stop = 0				# Permet d'arrêter la boucle une fois le temps écoulé.
stop_min = 0			# Contient les minutes de l'heure d'arrêt de la boucle.

# Initialisation des variables "analogique".
mm = 1		# Savoir si l'heure a changée après la boucle.
hh = 1		# Savoir si les minutes ont changées après la boucle.
unefois = 0		# Permet de faire la parie aléatoire et le cadre une seule fois.

lire = open("ana_pytime_v1.save", "r")
liste = []
for ligne in lire:
	liste.append(ligne)
version = liste[7]
liste = liste[6]
liste = liste.split(";")
v_tk_alea_h1_1 = int(liste[0])
v_tk_alea_h1_2 = int(liste[1])
v_tk_alea_h1_3 = int(liste[2])
v_tk_alea_h1_4 = int(liste[3])
v_tk_alea_h1_5 = int(liste[4])
v_tk_alea_h1_6 = int(liste[5])
v_tk_alea_h1_7 = int(liste[6])
v_tk_alea_h1_8 = int(liste[7])
v_tk_alea_h1_9 = int(liste[8])
v_tk_alea_h1_10 = int(liste[9])
v_tk_alea_h1_11 = int(liste[10])
v_tk_alea_h1_12 = int(liste[11])
v_tk_nuit_1 = int(liste[12])
v_tk_nuit_2 = int(liste[13])
v_tk_nuit_3 = int(liste[14])
v_tk_tour_3 = int(liste[15])
v_tk_speed_1 = int(liste[16])
v_tk_speed_2 = int(liste[17])
v_tk_speed_3 = int(liste[18])
v_tk_tyai_1 = int(liste[19])
v_tk_tyai_2 = int(liste[20])
v_tk_tyai_3 = int(liste[21])
v_tk_chco_1 = int(liste[22])
v_tk_chco_2 = int(liste[23])
v_tk_textaf_1_1 = str(liste[24])
v_tk_textaf_2_1 = int(liste[25])
v_tk_textaf_2_3 = int(liste[26])

#Confgure la vitesse.
if v_tk_speed_1 == 1:
	v_tk_speed = "slow"
if v_tk_speed_2 == 1:
	v_tk_speed = "normal"
if v_tk_speed_3 == 1:
	v_tk_speed = "fastest"
	
# 
if v_tk_nuit_1 == 1 and v_tk_nuit_2 == 1 and v_tk_nuit_3 == 1:
	egea_1 = 1
	v_tk_alea_h1_4 = 0
	v_tk_alea_h2_4 = 0
	v_tk_alea_m1_4 = 0
	v_tk_alea_m2_4 = 0

# Fin : Fenètre de commande.



def acontour(a, b, t):
	x_d = 0
	y_d = 400
	t.speed(v_tk_speed)
	if a == 1:
		t.speed(10)
	# Pour changer aléatoirement la marque qui dessine, à chaque tour.
	alea = random.randint(0, 5)
	forme = ['arrow', 'turtle', 'circle', 'square', 'triangle',\
	'classic']
	logo = forme[alea]
	t.shape(logo)
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	if a == 1 and v_tk_chco_2 == 1:
		t.penup()
	t.width(3)
	t.pencolor(b)
	t.circle(-400)
	t.hideturtle()
	if a == 1:
		t.reset()
		t.hideturtle()
		
def heurmin(b, t):
	x_d = 0
	y_d = 300
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.pencolor(b)
	t.down()
	t.width(2)
	t.speed(v_tk_speed)
	t.speed(20)
	for i in range(12):
		t.circle(-300, extent=30)
		t.left(-90)
		t.forward(12)
		t.right(-180)
		t.forward(12)
		t.left(-90)
	for i in range(60):
		t.penup()
		t.circle(-300, extent=6)
		t.down()
		t.left(-90)
		t.forward(5)
		t.right(-180)
		t.forward(5)
		t.left(-90)
	t.hideturtle()
	
def petitmil(a, b, t):
	x_d = 25
	y_d = 0
	if a == 1:
		t.speed(100)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.circle(25)
	t.hideturtle()
	t.end_fill()
	
def postrois(b, t):
	x_d = 370
	y_d = -40
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.forward(70)
	t.left(90)
	t.forward(40)
	t.left(90)
	t.forward(5)
	t.left(90)
	t.forward(35)
	t.right(90)
	t.forward(25)
	t.right(90)
	t.forward(20)
	t.left(90)
	t.forward(5)
	t.left(90)
	t.forward(20)
	t.right(90)
	t.forward(30)
	t.right(90)
	t.forward(35)
	t.left(90)
	t.forward(5)
	t.left(90)
	t.forward(40)
	t.end_fill()
	t.hideturtle()
	
def posdouze(b, t):
	x_d = -10
	y_d = 310
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.forward(70)
	t.left(130)
	t.forward(50)
	t.left(90)
	t.forward(5)
	t.left(90)
	t.forward(40)
	t.left(-130)
	t.forward(60)
	t.left(90)
	t.forward(4.5)
	t.end_fill()
	t.penup()
	t.forward(55)
	t.down()
	t.begin_fill()
	t.left(90)
	t.forward(5)
	t.left(90)
	t.forward(35)
	t.right(90)
	t.forward(25)
	t.right(90)
	t.forward(35)
	t.left(90)
	t.forward(40)
	t.left(90)
	t.forward(40)
	t.left(90)
	t.forward(5)
	t.left(90)
	t.forward(35)
	t.right(90)
	t.forward(30)
	t.right(90)
	t.forward(35)
	t.left(90)
	t.forward(35)
	t.left(90)
	t.forward(40)
	t.end_fill()
	t.hideturtle()
	
def possix(b, t):
	x_d = -15
	y_d = -350
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.right(0)
	t.forward(35)
	t.right(90)
	t.forward(35)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(70)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(5)
	t.right(90)
	t.forward(35)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(30)
	t.left(90)
	t.forward(25)
	t.left(90)
	t.forward(30)
	t.end_fill()
	t.hideturtle()

def posneuf(b, t):
	x_d = -330
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(180)
	t.pencolor(b)
	t.down()
	t.speed(v_tk_speed)
	t.color(b)
	t.begin_fill()
	t.right(0)
	t.forward(35)
	t.right(90)
	t.forward(35)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(70)
	t.right(90)
	t.forward(40)
	t.right(90)
	t.forward(5)
	t.right(90)
	t.forward(35)
	t.left(90)
	t.forward(60)
	t.left(90)
	t.forward(30)
	t.left(90)
	t.forward(25)
	t.left(90)
	t.forward(30)
	t.end_fill()
	t.hideturtle()
		
def aiguillem(a, b, t):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*6)
	t.color(b)
	t.begin_fill()
	t.forward(5)
	t.left(90)
	t.forward(250)
	t.right(90)
	t.forward(25)
	t.left(135)
	t.forward(42)
	t.left(90)
	t.forward(42)
	t.left(135)
	t.forward(25)
	t.right(90)
	t.forward(250)
	t.left(90)
	t.forward(15)
	t.end_fill()
	t.hideturtle()
	
def aiguillem1(a, b, t):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*6)
	t.color(b)
	t.begin_fill()
	t.forward(5)
	t.left(90)
	t.forward(250)
	t.left(10)
	t.forward(30)
	t.left(160)
	t.forward(30)
	t.left(10)
	t.forward(250)
	t.left(90)
	t.forward(5)
	t.end_fill()
	t.hideturtle()
	
def aiguillem2(a, b, t):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*6)
	t.color(b)
	t.begin_fill()
	t.forward(5)
	t.left(91)
	t.forward(280)
	t.left(178)
	t.forward(280)
	t.left(91)
	t.forward(5)
	t.end_fill()
	t.hideturtle()
	
def aiguilleh(a, b, t):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*30)
	t.color(b)
	t.begin_fill()
	t.forward(10)
	t.left(90)
	t.forward(200)
	t.right(90)
	t.forward(20)
	t.left(135)
	t.forward(42)
	t.left(90)
	t.forward(42)
	t.left(135)
	t.forward(20)
	t.right(90)
	t.forward(200)
	t.left(90)
	t.forward(10)	
	t.end_fill()
	t.hideturtle()
	
def aiguilleh1(a, b, t):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*30)
	t.color(b)
	t.begin_fill()
	t.forward(10)
	t.left(90)
	t.forward(180)
	t.left(20)
	t.forward(30)
	t.left(140)
	t.forward(30)
	t.left(20)
	t.forward(180)
	t.left(90)
	t.forward(10)
	t.end_fill()
	t.hideturtle()
	
def aiguilleh2(a, b, t):
	x_d = 0
	y_d = 0
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.speed(v_tk_speed)
	t.pencolor(b)
	t.right(a*30)
	t.color(b)
	t.begin_fill()
	t.forward(10)
	t.left(93)
	t.forward(180)
	t.left(174)
	t.forward(180)
	t.left(93)
	t.forward(10)
	t.end_fill()
	t.hideturtle()
	
turtle.setup(width=850,height=850)
turtle.title(version)
while stop == 0:
	heure = time.strftime("%H")	# heure prend les heures de l'heure qu'il est.
	minu = time.strftime("%M")	# minu prend les minutes de l'heure qu'il est.
	h1 = int(heure)			# Prend l'heure et la convertit en entier.
	m1 = int(minu)			# Prend les minutes et les convertient en entier.
	
	# Lit les options de la fenètre de commande et en fonction, met le mode
	# nuit ou le mode jour ou automatiquement.
	# Si il fait jour ou nuit (nuit entre 18h et 08h), et en
	# fonction, détermine la couleur de l'effacement des chiffres et la
	# couleur du cadre et de la date.
	if v_tk_nuit_2 == 1 and unefois == 0:
		fondcolor = 'white'
		ifondcolor = 'black'
		alea = 98
		turtle.bgcolor('black')
	elif v_tk_nuit_3 == 1 and unefois == 0:
		fondcolor = 'black'
		ifondcolor = 'white'
		alea = 99
		turtle.bgcolor('white')
	elif v_tk_nuit_1 == 1 and unefois == 0:
		if (h1 >= 18) or (h1 <= 8):
			fondcolor = 'white'
			ifondcolor = 'black'
			alea = 98
			turtle.bgcolor('black')
		else:
			fondcolor = 'black'
			ifondcolor = 'white'
			alea = 99
			turtle.bgcolor('white')
	if egea_1 == 1 and unefois == 0:
		fondcolor = 'black'
		ifondcolor = 'green'
		alea = 99
		turtle.bgcolor('green')
		
	# Choisi la couleur choisi par l'utilisateur. Si il en a choisi plusieurs
	# afficher une couleur aléatoire parmi celles choisi. Si aléatoire a été
	# cocher, choisir une couleur aléatoire.
	if v_tk_alea_h1_1 == 1 and unefois == 0:
		if v_tk_alea_h1_2 == 1:
			colora.append('blue')
			colorachif += 1
		if v_tk_alea_h1_3 == 1:
			colora.append('red')
			colorachif += 1
		if v_tk_alea_h1_4 == 1:
			colora.append('green')
			colorachif += 1
		if v_tk_alea_h1_5 == 1:
			colora.append('violet')
			colorachif += 1
		if v_tk_alea_h1_6 == 1:
			colora.append('yellow')
			colorachif += 1
		if v_tk_alea_h1_7 == 1:
			colora.append('brown')
			colorachif += 1
		if v_tk_alea_h1_8 == 1:
			colora.append('pink')
			colorachif += 1
		if v_tk_alea_h1_9 == 1:
			colora.append('purple')
			colorachif += 1
		if v_tk_alea_h1_10 == 1:
			colora.append('grey')
			colorachif += 1
		if v_tk_alea_h1_11 == 1:
			colora.append('orange')
			colorachif += 1
		if colorachif > 0:
			colorachif -= 1
			alea = random.randint(0, colorachif)
			fondcolor = colora[alea]
		else:
			alea = random.randint(0, 9)
			colr = ['blue', 'red', 'green', 'violet', 'yellow', 'brown',\
			'pink', 'purple', 'grey', 'orange']
			fondcolor = colr[alea]
			
	elif v_tk_alea_h1_12 == 1:
		if alea == 98:
			fondcolor = 'white'
		elif alea == 99:
			fondcolor = 'black'
			
	elif v_tk_alea_h1_2 == 1:
		fondcolor = 'blue'
	elif v_tk_alea_h1_3 == 1:
		fondcolor = 'red'
	elif v_tk_alea_h1_4 == 1:
		fondcolor = 'green'
	elif v_tk_alea_h1_5 == 1:
		fondcolor = 'violet'
	elif v_tk_alea_h1_6 == 1:
		fondcolor = 'yellow'
	elif v_tk_alea_h1_7 == 1:
		fondcolor = 'brown'
	elif v_tk_alea_h1_8 == 1:
		fondcolor = 'pink'
	elif v_tk_alea_h1_9 == 1:
		fondcolor = 'purple'
	elif v_tk_alea_h1_10 == 1:
		fondcolor = 'grey'
	elif v_tk_alea_h1_11 == 1:
		fondcolor = 'orange'
		
	# Permet de réinitialiser les variables.
	colora = []
	colorachif = 0
		
	# Créé l'horloge selon les options voulu.
	if mm == 1:
		petitmil(0, fondcolor, turtle.Turtle())
		if v_tk_tyai_1 == 1:
			aiguillem(m1, fondcolor, turtle.Turtle())
		elif v_tk_tyai_2 == 1:
			aiguillem1(m1, fondcolor, turtle.Turtle())
		else:
			aiguillem2(m1, fondcolor, turtle.Turtle())
	if hh == 1:
		petitmil(0, fondcolor, turtle.Turtle())
		if v_tk_tyai_1 == 1:
			aiguilleh(h1, fondcolor, turtle.Turtle())
		elif v_tk_tyai_2 == 1:
			aiguilleh1(h1, fondcolor, turtle.Turtle())
		else:
			aiguilleh2(h1, fondcolor, turtle.Turtle())
	if unefois == 0:
		acontour(0, fondcolor, turtle.Turtle())
		heurmin(fondcolor, turtle.Turtle())
		posdouze(fondcolor, turtle.Turtle())
		postrois(fondcolor, turtle.Turtle())
		possix(fondcolor, turtle.Turtle())
		posneuf(fondcolor, turtle.Turtle())
	unefois = 1
	
	# Permet de reconstruire l'aiguille des heures si l'aiguille 
	# des minute passe dessus.
	if h1 >= 12:
		reheure = 5 * (h1 - 12)
	else:
		reheure = 5 * h1
	if (reheure == m1 or reheure == m1-1 or reheure == m1-2\
	or reheure == m1-3 or reheure == m1-4 or reheure == m1-5\
	or reheure == m1-6 or reheure == m1+1 or reheure == m1+2\
	or reheure == m1+3 or reheure == m1+4 or reheure == m1+5\
	or reheure == m1+6) and mm == 1:
		if v_tk_tyai_1 == 1:
			aiguilleh(h1, fondcolor, turtle.Turtle())
		elif v_tk_tyai_2 == 1:
			aiguilleh1(h1, fondcolor, turtle.Turtle())
		else:
			aiguilleh2(h1, fondcolor, turtle.Turtle())
	
	# Fait tourner le grand cercle à chaque boucle. La boucle est
	# nécessaire si on change time.sleep et le nombre de tour (change le
	# temps d'actualisation sans toucher au grand cercle qui bouge).
	for i in range(1):
		alea = random.randint(0, 9)
		colr = ['blue', 'red', 'green', 'violet', 'yellow', 'brown',\
		'pink', 'purple', 'grey', 'orange']
		mfondcolor = colr[alea]
			
		acontour(1, mfondcolor, turtle.Turtle())
		time.sleep(0)
	
	heure1 = time.strftime("%H")	# heure prend les heures de l'heure qu'il est.
	minu1 = time.strftime("%M")	# minu prend les minutes de l'heure qu'il est.
	h11 = int(heure1)
	m11 = int(minu1)
	mm = 0
	hh = 0
	if m11 != m1:
		mm = 1
		if v_tk_tyai_1 == 1:
			aiguillem(m1, ifondcolor, turtle.Turtle())
		elif v_tk_tyai_2 == 1:
			aiguillem1(m1, ifondcolor, turtle.Turtle())
		else:
			aiguillem2(m1, ifondcolor, turtle.Turtle())
	if h11 != h1:
		hh = 1
		if v_tk_tyai_1 == 1:
			aiguilleh(h1, ifondcolor, turtle.Turtle())
		elif v_tk_tyai_2 == 1:
			aiguilleh1(h1, ifondcolor, turtle.Turtle())
		else:
			aiguilleh2(h1, ifondcolor, turtle.Turtle())
	# Pour que l'horloge se ferme automatiquement après l'heure indiqué passé.
	minuav = int(minu)
	minuap = int(minu1)
	if minuav != minuap:
		stop_min += 1
	if stop_min >= v_tk_tour_3:
		stop = 1
	
	# Pour afficher le message à l'heure indiqué.
	if v_tk_textaf_2_1 != 30 and mesaffoui == 0:
		heuremess = int(heure)
		if v_tk_textaf_2_1 == heuremess:
			if v_tk_textaf_2_3 == minuav:
				showinfo("Votre message", v_tk_textaf_1_1)
				mesaffoui = 1
"""
GoPyTime v1 :
Code de PyTime v13.0
Compatible à partir des sauvegardes pytime_v1.save
"""