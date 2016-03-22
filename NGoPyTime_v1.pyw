# -*- coding: utf-8 -*-
# Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("GoPyTime v1.1 numérique")
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

# Initialisation des variables "numerique".
hh1 = 1		# Savoir si l'heure a changée après la boucle.
hh2 = 1		# Savoir si l'heure a changée après la boucle.
mm1 = 1		# Savoir si les minutes ont changées après la boucle.
mm2 = 1		# Savoir si les minutes ont changées après la boucle.
cadredate = 0	# Permet de faire le cadre et la date une seule fois.
colora = []		# Permet de sauvegarder les couleurs choisi.

lire = open("num_pytime_v1.save", "r")
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
v_tk_alea_h2_1 = int(liste[12])
v_tk_alea_h2_2 = int(liste[13])
v_tk_alea_h2_3 = int(liste[14])
v_tk_alea_h2_4 = int(liste[15])
v_tk_alea_h2_5 = int(liste[16])
v_tk_alea_h2_6 = int(liste[17])
v_tk_alea_h2_7 = int(liste[18])
v_tk_alea_h2_8 = int(liste[19])
v_tk_alea_h2_9 = int(liste[20])
v_tk_alea_h2_10 = int(liste[21])
v_tk_alea_h2_11 = int(liste[22])
v_tk_alea_h2_12 = int(liste[23])
v_tk_alea_m1_1 = int(liste[24])
v_tk_alea_m1_2 = int(liste[25])
v_tk_alea_m1_3 = int(liste[26])
v_tk_alea_m1_4 = int(liste[27])
v_tk_alea_m1_5 = int(liste[28])
v_tk_alea_m1_6 = int(liste[29])
v_tk_alea_m1_7 = int(liste[30])
v_tk_alea_m1_8 = int(liste[31])
v_tk_alea_m1_9 = int(liste[32])
v_tk_alea_m1_10 = int(liste[33])
v_tk_alea_m1_11 = int(liste[34])
v_tk_alea_m1_12 = int(liste[35])
v_tk_alea_m2_1 = int(liste[36])
v_tk_alea_m2_2 = int(liste[37])
v_tk_alea_m2_3 = int(liste[38])
v_tk_alea_m2_4 = int(liste[39])
v_tk_alea_m2_5 = int(liste[40])
v_tk_alea_m2_6 = int(liste[41])
v_tk_alea_m2_7 = int(liste[42])
v_tk_alea_m2_8 = int(liste[43])
v_tk_alea_m2_9 = int(liste[44])
v_tk_alea_m2_10 = int(liste[45])
v_tk_alea_m2_11 = int(liste[46])
v_tk_alea_m2_12 = int(liste[47])
v_tk_nuit_1 = int(liste[48])
v_tk_nuit_2 = int(liste[49])
v_tk_nuit_3 = int(liste[50])
v_tk_tour_3 = int(liste[51])
v_tk_speed_1 = int(liste[52])
v_tk_speed_2 = int(liste[53])
v_tk_speed_3 = int(liste[54])
v_tk_epais_1 = int(liste[55])
v_tk_epais_2 = int(liste[56])
v_tk_epais_3 = int(liste[57])
v_tk_textaf_1_1 = str(liste[58])
v_tk_textaf_2_1 = int(liste[59])
v_tk_textaf_2_3 = int(liste[60])

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
	
# Configure l'épaisseur des chiffres.
if v_tk_epais_1 == 1:
	v_tk_epais = 1
elif v_tk_epais_2 == 1:
	v_tk_epais = 3
elif v_tk_epais_3 == 1:
	v_tk_epais = 5

# Construction des chiffres par Turtle : a désigne le positionnement gauche/
# droite, b désigne le positionnement haut/bas, f désigne la couleur du crayon,
# g désigne l'épaisseur du crayon et t désigne la class Turtle().
def zero(a, b, f, g, t):
	x_d = a + (-50)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.left(90)
	t.forward(140)
	t.left(90)
	t.forward(80)
	t.left(180)
	t.penup()
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

def un(a, b, f, g, t):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def deux(a, b, f, g, t):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
		
def trois(a, b, f, g, t):
	x_d = a +(-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def quatre(a, b, f, g, t):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def cinq(a, b, f, g, t):
	x_d = a + (-140)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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

def six(a, b, f, g, t):
	x_d = a + (-130)
	y_d = b + 20
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def sept(a, b, f, g, t):
	x_d = a + (-140)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(50)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def huit(a, b, f, g, t):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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

def neuf(a, b, f, g, t):
	x_d = a + (-70)
	y_d = b + (20)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(180)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def pzero(a, b, f, g, t):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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

def pun(a, b, f, g, t):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def pdeux(a, b, f, g, t):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
		
def ptrois(a, b, f, g, t):
	x_d = a + (-65)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def pquatre(a, b, f, g, t):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def pcinq(a, b, f, g, t):
	x_d = a + (-90)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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

def psix(a, b, f, g, t):
	x_d = a + (-85)
	y_d = b + (-27)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(0)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def psept(a, b, f, g, t):
	x_d = a + (-85)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(50)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def phuit(a, b, f, g, t):
	x_d = a + (-60)
	y_d = b + (-50)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def pneuf(a, b, f, g, t):
	x_d = a + (-58)
	y_d = b + (-27)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(180)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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
	
def milieu(a, b, f, g, t):
	x_d = a + 20
	y_d = b
	
	# Pour changer aléatoirement la marque qui dessine, à chaque tour.
	alea = random.randint(0, 5)
	forme = ['arrow', 'turtle', 'circle', 'square', 'triangle',\
	'classic']
	logo = forme[alea]
	t.shape(logo)
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
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

def contour(a, b, f, g, t):
	x_d = a + 280
	y_d = b + (-90)
	t.shape('turtle')
	t.penup()
	t.setposition(x_d, y_d)
	t.setheading(90)
	t.down()
	t.pencolor(f)
	t.width(g)
	t.speed(v_tk_speed)
	t.forward(190)
	t.left(90)
	t.forward(540)
	t.left(90)
	t.forward(190)
	t.left(90)
	t.forward(540)
	t.hideturtle()
	
# Permet de faire appel au chiffre appelé.
def main(d, a, b, f, g):
	if d == "p0":
		chif = pzero
	if d == "p1":
		chif = pun
	if d == "p2":
		chif = pdeux
	if d == "p3":
		chif = ptrois
	if d == "p4":
		chif = pquatre
	if d == "p5":
		chif = pcinq
	if d == "p6":
		chif = psix
	if d == "p7":
		chif = psept
	if d == "p8":
		chif = phuit
	if d == "p9":
		chif = pneuf
	if d == "0":
		chif = zero
	if d == "1":
		chif = un
	if d == "2":
		chif = deux
	if d == "3":
		chif = trois
	if d == "4":
		chif = quatre
	if d == "5":
		chif = cinq
	if d == "6":
		chif = six
	if d == "7":
		chif = sept
	if d == "8":
		chif = huit
	if d == "9":
		chif = neuf
	if d == "c":
		chif = contour
	if d == "m":
		chif = milieu
	t = turtle.Turtle()
	chif(a, b, f, g, t)
	
# Configure la fenètre.
turtle.setup(width=850,height=450)
turtle.title(version)

# Boucle qui permet de faire tourner le rectangle du milieu et d'actualiser
# l'heure. La boucle fait le nombre de tour indiqué par la fenètre de commande.
while stop == 0:
	heure = time.strftime("%H")	# heure prend les heures de l'heure qu'il est.
	minu = time.strftime("%M")	# minu prend les minutes de l'heure qu'il est.
	day = time.strftime("%d")	# day prend le jour où l'on est.
	mois = time.strftime("%m")	# mois prend le mois où l'on est.
	ans = time.strftime("%y")	# ans prend l'année où l'on est.
	h1 = int(heure[0])	# |
	h2 = int(heure[1])	# |
	m1 = int(minu[0])	 	# |
	m2 = int(minu[1]) 	# |
	d1 = int(day[0]) 	 	# Prend le premier caractère, le converti en
	d2 = int(day[1]) 	 	# entier et le met dans la variable.
	mo1 = int(mois[0]) 	# |
	mo2 = int(mois[1]) 	# |
	a1 = int(ans[0]) 	 	# |
	a2 = int(ans[1]) 	 	# |
		
	
	# Lit les options de la fenètre de commande et en fonction, met le mode
	# nuit ou le mode jour ou automatiquement.
	# Si il fait jour ou nuit (nuit entre 18h et 08h), et en
	# fonction, détermine la couleur de l'effacement des chiffres et la
	# couleur du cadre et de la date.
	if v_tk_nuit_2 == 1:
		fondcolor = 'white'
		ifondcolor = 'black'
		alea = 98
		turtle.bgcolor('black')
	elif v_tk_nuit_3 == 1:
		fondcolor = 'black'
		ifondcolor = 'white'
		alea = 99
		turtle.bgcolor('white')
	elif v_tk_nuit_1 == 1:
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
	if egea_1 == 1:
		fondcolor = 'black'
		ifondcolor = 'green'
		alea = 99
		turtle.bgcolor('green')

	# Dessine le cadre et la date une seul fois (tant que cadredate = 0).
	if cadredate == 0:
		main("c", -10, 15, fondcolor, 1)
		if d1 == 0:
			main("p0", -50, -100, fondcolor, 1)
		elif d1 == 1:
			main("p1", -50, -100, fondcolor, 1)
		elif d1 == 2:
			main("p2", -50, -100, fondcolor, 1)
		elif d1 == 3:
			main("p3", -50, -100, fondcolor, 1)
		if d2 == 0:
			main("p0", -10, -100, fondcolor, 1)
		elif d2 == 1:
			main("p1", -10, -100, fondcolor, 1)
		elif d2 == 2:
			main("p2", -10, -100, fondcolor, 1)
		elif d2 == 3:
			main("p3", -10, -100, fondcolor, 1)
		elif d2 == 4:
			main("p4", -10, -100, fondcolor, 1)
		elif d2 == 5:
			main("p5", -10, -100, fondcolor, 1)
		elif d2 == 6:
			main("p6", -10, -100, fondcolor, 1)
		elif d2 == 7:
			main("p7", -10, -100, fondcolor, 1)
		elif d2 == 8:
			main("p8", -10, -100, fondcolor, 1)
		elif d2 == 9:
			main("p9", -10, -100, fondcolor, 1)
		if mo1 == 0:
			main("p0", 50, -100, fondcolor, 1)
		elif mo1 == 1:
			main("p1", 50, -100, fondcolor, 1)
		if mo2 == 0:
			main("p0", 90, -100, fondcolor, 1)
		elif mo2 == 1:
			main("p1", 90, -100, fondcolor, 1)
		elif mo2 == 2:
			main("p2", 90, -100, fondcolor, 1)
		elif mo2 == 3:
			main("p3", 90, -100, fondcolor, 1)
		elif mo2 == 4:
			main("p4", 90, -100, fondcolor, 1)
		elif mo2 == 5:
			main("p5", 90, -100, fondcolor, 1)
		elif mo2 == 6:
			main("p6", 90, -100, fondcolor, 1)
		elif mo2 == 7:
			main("p7", 90, -100, fondcolor, 1)
		elif mo2 == 8:
			main("p8", 90, -100, fondcolor, 1)
		elif mo2 == 9:
			main("p9", 90, -100, fondcolor, 1)
		if a1 == 1:
			main("p1", 150, -100, fondcolor, 1)
		elif a1 == 2:
			main("p2", 150, -100, fondcolor, 1)
		elif a1 == 3:
			main("p3", 150, -100, fondcolor, 1)
		if a2 == 0:
			main("p0", 190, -100, fondcolor, 1)
		elif a2 == 1:
			main("p1", 190, -100, fondcolor, 1)
		elif a2 == 2:
			main("p2", 190, -100, fondcolor, 1)
		elif a2 == 3:
			main("p3", 190, -100, fondcolor, 1)
		elif a2 == 4:
			main("p4", 190, -100, fondcolor, 1)
		elif a2 == 5:
			main("p5", 190, -100, fondcolor, 1)
		elif a2 == 6:
			main("p6", 190, -100, fondcolor, 1)
		elif a2 == 7:
			main("p7", 190, -100, fondcolor, 1)
		elif a2 == 8:
			main("p8", 190, -100, fondcolor, 1)
		elif a2 == 9:
			main("p9", 190, -100, fondcolor, 1)
			
	# Pour que le cadre et la date apparaissent une seul fois.
	cadredate = 1
	
	# Choisi la couleur choisi par l'utilisateur. Si il en a choisi plusieurs
	# afficher une couleur aléatoire parmi celles choisi. Si aléatoire a été
	# cocher, choisir une couleur aléatoire.
	if v_tk_alea_h1_1 == 1:
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
		
	# Choisi un chiffre selon l'heure.
	if hh1 == 1:
		if h1 == 0:
			main("0", -100, 0, fondcolor, v_tk_epais)
		elif h1 == 1:
			main("1", -100, 0, fondcolor, v_tk_epais)
		elif h1 == 2:
			main("2", -100, 0, fondcolor, v_tk_epais)
			
	if v_tk_alea_h2_1 == 1:
		if v_tk_alea_h2_2 == 1:
			colora.append('blue')
			colorachif += 1
		if v_tk_alea_h2_3 == 1:
			colora.append('red')
			colorachif += 1
		if v_tk_alea_h2_4 == 1:
			colora.append('green')
			colorachif += 1
		if v_tk_alea_h2_5 == 1:
			colora.append('violet')
			colorachif += 1
		if v_tk_alea_h2_6 == 1:
			colora.append('yellow')
			colorachif += 1
		if v_tk_alea_h2_7 == 1:
			colora.append('brown')
			colorachif += 1
		if v_tk_alea_h2_8 == 1:
			colora.append('pink')
			colorachif += 1
		if v_tk_alea_h2_9 == 1:
			colora.append('purple')
			colorachif += 1
		if v_tk_alea_h2_10 == 1:
			colora.append('grey')
			colorachif += 1
		if v_tk_alea_h2_11 == 1:
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
			
	elif v_tk_alea_h2_12 == 1:
		if alea == 98:
			fondcolor = 'white'
		elif alea == 99:
			fondcolor = 'black'
			
	elif v_tk_alea_h2_2 == 1:
		fondcolor = 'blue'
	elif v_tk_alea_h2_3 == 1:
		fondcolor = 'red'
	elif v_tk_alea_h2_4 == 1:
		fondcolor = 'green'
	elif v_tk_alea_h2_5 == 1:
		fondcolor = 'violet'
	elif v_tk_alea_h2_6 == 1:
		fondcolor = 'yellow'
	elif v_tk_alea_h2_7 == 1:
		fondcolor = 'brown'
	elif v_tk_alea_h2_8 == 1:
		fondcolor = 'pink'
	elif v_tk_alea_h2_9 == 1:
		fondcolor = 'purple'
	elif v_tk_alea_h2_10 == 1:
		fondcolor = 'grey'
	elif v_tk_alea_h2_11 == 1:
		fondcolor = 'orange'
		
	colora = []
	colorachif = 0		
		
	if hh2 == 1:
		if h2 == 0:
			main("0", 0, 0, fondcolor, v_tk_epais)
		elif h2 == 1:
			main("1", 0, 0, fondcolor, v_tk_epais)
		elif h2 == 2:
			main("2", 0, 0, fondcolor, v_tk_epais)
		elif h2 == 3:
			main("3", 0, 0, fondcolor, v_tk_epais)
		elif h2 == 4:
			main("4", 0, 0, fondcolor, v_tk_epais)
		elif h2 == 5:
			main("5", 0, 0, fondcolor, v_tk_epais)
		elif h2 == 6:
			main("6", 0, 0, fondcolor, v_tk_epais)
		elif h2 == 7:
			main("7", 0, 0, fondcolor, v_tk_epais)
		elif h2 == 8:
			main("8", 0, 0, fondcolor, v_tk_epais)
		elif h2 == 9:
			main("9", 0, 0, fondcolor, v_tk_epais)
		
	if v_tk_alea_m1_1 == 1:
		if v_tk_alea_m1_2 == 1:
			colora.append('blue')
			colorachif += 1
		if v_tk_alea_m1_3 == 1:
			colora.append('red')
			colorachif += 1
		if v_tk_alea_m1_4 == 1:
			colora.append('green')
			colorachif += 1
		if v_tk_alea_m1_5 == 1:
			colora.append('violet')
			colorachif += 1
		if v_tk_alea_m1_6 == 1:
			colora.append('yellow')
			colorachif += 1
		if v_tk_alea_m1_7 == 1:
			colora.append('brown')
			colorachif += 1
		if v_tk_alea_m1_8 == 1:
			colora.append('pink')
			colorachif += 1
		if v_tk_alea_m1_9 == 1:
			colora.append('purple')
			colorachif += 1
		if v_tk_alea_m1_10 == 1:
			colora.append('grey')
			colorachif += 1
		if v_tk_alea_m1_11 == 1:
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
			
	elif v_tk_alea_m1_12 == 1:
		if alea == 98:
			fondcolor = 'white'
		elif alea == 99:
			fondcolor = 'black'
			
	elif v_tk_alea_m1_2 == 1:
		fondcolor = 'blue'
	elif v_tk_alea_m1_3 == 1:
		fondcolor = 'red'
	elif v_tk_alea_m1_4 == 1:
		fondcolor = 'green'
	elif v_tk_alea_m1_5 == 1:
		fondcolor = 'violet'
	elif v_tk_alea_m1_6 == 1:
		fondcolor = 'yellow'
	elif v_tk_alea_m1_7 == 1:
		fondcolor = 'brown'
	elif v_tk_alea_m1_8 == 1:
		fondcolor = 'pink'
	elif v_tk_alea_m1_9 == 1:
		fondcolor = 'purple'
	elif v_tk_alea_m1_10 == 1:
		fondcolor = 'grey'
	elif v_tk_alea_m1_11 == 1:
		fondcolor = 'orange'
		
	colora = []
	colorachif = 0		
		
	if mm1 == 1:
		if m1 == 0:
			main("0", 190, 0, fondcolor, v_tk_epais)
		elif m1 == 1:
			main("1", 190, 0, fondcolor, v_tk_epais)
		elif m1 == 2:
			main("2", 190, 0, fondcolor, v_tk_epais)
		elif m1 == 3:
			main("3", 190, 0, fondcolor, v_tk_epais)
		elif m1 == 4:
			main("4", 190, 0, fondcolor, v_tk_epais)
		elif m1 == 5:
			main("5", 190, 0, fondcolor, v_tk_epais)
		
	if v_tk_alea_m2_1 == 1:
		if v_tk_alea_m2_2 == 1:
			colora.append('blue')
			colorachif += 1
		if v_tk_alea_m2_3 == 1:
			colora.append('red')
			colorachif += 1
		if v_tk_alea_m2_4 == 1:
			colora.append('green')
			colorachif += 1
		if v_tk_alea_m2_5 == 1:
			colora.append('violet')
			colorachif += 1
		if v_tk_alea_m2_6 == 1:
			colora.append('yellow')
			colorachif += 1
		if v_tk_alea_m2_7 == 1:
			colora.append('brown')
			colorachif += 1
		if v_tk_alea_m2_8 == 1:
			colora.append('pink')
			colorachif += 1
		if v_tk_alea_m2_9 == 1:
			colora.append('purple')
			colorachif += 1
		if v_tk_alea_m2_10 == 1:
			colora.append('grey')
			colorachif += 1
		if v_tk_alea_m2_11 == 1:
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
			
	elif v_tk_alea_m2_12 == 1:
		if alea == 98:
			fondcolor = 'white'
		elif alea == 99:
			fondcolor = 'black'
			
	elif v_tk_alea_m2_2 == 1:
		fondcolor = 'blue'
	elif v_tk_alea_m2_3 == 1:
		fondcolor = 'red'
	elif v_tk_alea_m2_4 == 1:
		fondcolor = 'green'
	elif v_tk_alea_m2_5 == 1:
		fondcolor = 'violet'
	elif v_tk_alea_m2_6 == 1:
		fondcolor = 'yellow'
	elif v_tk_alea_m2_7 == 1:
		fondcolor = 'brown'
	elif v_tk_alea_m2_8 == 1:
		fondcolor = 'pink'
	elif v_tk_alea_m2_9 == 1:
		fondcolor = 'purple'
	elif v_tk_alea_m2_10 == 1:
		fondcolor = 'grey'
	elif v_tk_alea_m2_11 == 1:
		fondcolor = 'orange'
		
	colora = []
	colorachif = 0
		
	if mm2 == 1:
		if m2 == 0:
			main("0", 295, 0, fondcolor, v_tk_epais)
		elif m2 == 1:
			main("1", 295, 0, fondcolor, v_tk_epais)
		elif m2 == 2:
			main("2", 295, 0, fondcolor, v_tk_epais)
		elif m2 == 3:
			main("3", 295, 0, fondcolor, v_tk_epais)
		elif m2 == 4:
			main("4", 295, 0, fondcolor, v_tk_epais)
		elif m2 == 5:
			main("5", 295, 0, fondcolor, v_tk_epais)
		elif m2 == 6:
			main("6", 295, 0, fondcolor, v_tk_epais)
		elif m2 == 7:
			main("7", 295, 0, fondcolor, v_tk_epais)
		elif m2 == 8:
			main("8", 295, 0, fondcolor, v_tk_epais)
		elif m2 == 9:
			main("9", 295, 0, fondcolor, v_tk_epais)
	
	# Fait tourner le rectangle du milieu à chaque boucle. La boucle est
	# nécessaire si on change time.sleep et le nombre de tour (change le
	# temps d'actualisation sans toucher au rectangle qui bouge).
	for i in range(1):
		if v_tk_alea_h1_12 == 1 and v_tk_alea_h2_12 == 1 and \
		v_tk_alea_m1_12 == 1 and v_tk_alea_m2_12 == 1:
			if alea == 98:
				mfondcolor = 'white'
			elif alea == 99:
				mfondcolor = 'black'
		else:
			alea = random.randint(0, 9)
			colr = ['blue', 'red', 'green', 'violet', 'yellow', 'brown',\
			'pink', 'purple', 'grey', 'orange']
			mfondcolor = colr[alea]
			
		main("m", -10, 15, mfondcolor, 1)
		time.sleep(0)
		
	# Si un chiffre change, "l'effacer" (colore le chiffre de la couleur 
	# du fond) et met la valeur 1 à xx1 pour changer le chiffre en 
	# recommencent la boucle.
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
			main("0", -100, 0, ifondcolor, v_tk_epais)
		elif h1 == 1:
			main("1", -100, 0, ifondcolor, v_tk_epais)
		elif h1 == 2:
			main("2", -100, 0, ifondcolor, v_tk_epais)
   
	if h21 != h2:
		hh2 = 1
		if h2 == 0:
			main("0", 0, 0, ifondcolor, v_tk_epais)
		elif h2 == 1:
			main("1", 0, 0, ifondcolor, v_tk_epais)
		elif h2 == 2:
			main("2", 0, 0, ifondcolor, v_tk_epais)
		elif h2 == 3:
			main("3", 0, 0, ifondcolor, v_tk_epais)
		elif h2 == 4:
			main("4", 0, 0, ifondcolor, v_tk_epais)
		elif h2 == 5:
			main("5", 0, 0, ifondcolor, v_tk_epais)
		elif h2 == 6:
			main("6", 0, 0, ifondcolor, v_tk_epais)
		elif h2 == 7:
			main("7", 0, 0, ifondcolor, v_tk_epais)
		elif h2 == 8:
			main("8", 0, 0, ifondcolor, v_tk_epais)
		elif h2 == 9:
			main("9", 0, 0, ifondcolor, v_tk_epais)
   
	if m11 != m1:
		mm1 = 1
		if m1 == 0:
			main("0", 190, 0, ifondcolor, v_tk_epais)
		elif m1 == 1:
			main("1", 190, 0, ifondcolor, v_tk_epais)
		elif m1 == 2:
			main("2", 190, 0, ifondcolor, v_tk_epais)
		elif m1 == 3:
			main("3", 190, 0, ifondcolor, v_tk_epais)
		elif m1 == 4:
			main("4", 190, 0, ifondcolor, v_tk_epais)
		elif m1 == 5:
			main("5", 190, 0, ifondcolor, v_tk_epais)
   
	if m21 != m2:
		mm2 = 1
		if m2 == 0:
			main("0", 295, 0, ifondcolor, v_tk_epais)
		elif m2 == 1:
			main("1", 295, 0, ifondcolor, v_tk_epais)
		elif m2 == 2:
			main("2", 295, 0, ifondcolor, v_tk_epais)
		elif m2 == 3:
			main("3", 295, 0, ifondcolor, v_tk_epais)
		elif m2 == 4:
			main("4", 295, 0, ifondcolor, v_tk_epais)
		elif m2 == 5:
			main("5", 295, 0, ifondcolor, v_tk_epais)
		elif m2 == 6:
			main("6", 295, 0, ifondcolor, v_tk_epais)
		elif m2 == 7:
			main("7", 295, 0, ifondcolor, v_tk_epais)
		elif m2 == 8:
			main("8", 295, 0, ifondcolor, v_tk_epais)
		elif m2 == 9:
			main("9", 295, 0, ifondcolor, v_tk_epais)
	
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
GoPyTime v1.1 :
Code de PyTime v14.0

GoPyTime v1 :
Code de PyTime v13.0
Compatible à partir des sauvegardes pytime_v1.save
"""
