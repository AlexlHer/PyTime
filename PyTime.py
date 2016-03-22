# -*- coding: utf-8 -*-
# Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("Horloge v5.0")
print("----------------------------------------------------------------------")
print("Ne pas fermer la fenètre sauf pour fermer l'horloge.")

# Initialisation des variables et importation des modules.
import time
import turtle
import random
from tkinter import *
hh1 = 1		# Savoir si l'heure a changée après la boucle.
hh2 = 1		# Savoir si l'heure a changée après la boucle.
mm1 = 1		# Savoir si les minutes ont changées après la boucle.
mm2 = 1		# Savoir si les minutes ont changées après la boucle.
cadredate = 0	# Permet de faire le cadre et la date une seule fois.
test = 0
colora = []
colorachif = 0
boutononf = 0

# Début : Fenètre de commande.
fenetre = Tk()
fenetre.title("Horloge v5.0")

# Initialisation des variables de la fenètre de commande.
v_tk_alea_h1_1 = IntVar()
v_tk_alea_h1_2 = IntVar()
v_tk_alea_h1_3 = IntVar()
v_tk_alea_h1_4 = IntVar()
v_tk_alea_h1_5 = IntVar()
v_tk_alea_h1_6 = IntVar()
v_tk_alea_h1_7 = IntVar()
v_tk_alea_h1_8 = IntVar()
v_tk_alea_h1_9 = IntVar()
v_tk_alea_h1_10 = IntVar()
v_tk_alea_h1_11 = IntVar()
v_tk_alea_h1_12 = IntVar()

v_tk_alea_h2_1 = IntVar()
v_tk_alea_h2_2 = IntVar()
v_tk_alea_h2_3 = IntVar()
v_tk_alea_h2_4 = IntVar()
v_tk_alea_h2_5 = IntVar()
v_tk_alea_h2_6 = IntVar()
v_tk_alea_h2_7 = IntVar()
v_tk_alea_h2_8 = IntVar()
v_tk_alea_h2_9 = IntVar()
v_tk_alea_h2_10 = IntVar()
v_tk_alea_h2_11 = IntVar()
v_tk_alea_h2_12 = IntVar()

v_tk_alea_m1_1 = IntVar()
v_tk_alea_m1_2 = IntVar()
v_tk_alea_m1_3 = IntVar()
v_tk_alea_m1_4 = IntVar()
v_tk_alea_m1_5 = IntVar()
v_tk_alea_m1_6 = IntVar()
v_tk_alea_m1_7 = IntVar()
v_tk_alea_m1_8 = IntVar()
v_tk_alea_m1_9 = IntVar()
v_tk_alea_m1_10 = IntVar()
v_tk_alea_m1_11 = IntVar()
v_tk_alea_m1_12 = IntVar()

v_tk_alea_m2_1 = IntVar()
v_tk_alea_m2_2 = IntVar()
v_tk_alea_m2_3 = IntVar()
v_tk_alea_m2_4 = IntVar()
v_tk_alea_m2_5 = IntVar()
v_tk_alea_m2_6 = IntVar()
v_tk_alea_m2_7 = IntVar()
v_tk_alea_m2_8 = IntVar()
v_tk_alea_m2_9 = IntVar()
v_tk_alea_m2_10 = IntVar()
v_tk_alea_m2_11 = IntVar()
v_tk_alea_m2_12 = IntVar()

v_tk_nuit_1 = IntVar()
v_tk_nuit_2 = IntVar()
v_tk_nuit_3 = IntVar()

v_tk_tour_3 = IntVar()

v_tk_ok_1 = IntVar()

titre = Label(fenetre, text="Horloge")

tk_alea = LabelFrame(fenetre, text="Couleur des chiffres", padx=2, pady=2)
tk_alea_h1 = LabelFrame(tk_alea, text="1er chiffre des heures", padx=2, pady=2)
tk_alea_h1_1 = Checkbutton(tk_alea_h1, text="Aleatoire", variable = v_tk_alea_h1_1)
tk_alea_h1_2 = Checkbutton(tk_alea_h1, text="Bleu", variable = v_tk_alea_h1_2)
tk_alea_h1_3 = Checkbutton(tk_alea_h1, text="Rouge", variable = v_tk_alea_h1_3)
tk_alea_h1_4 = Checkbutton(tk_alea_h1, text="Vert", variable = v_tk_alea_h1_4)
tk_alea_h1_5 = Checkbutton(tk_alea_h1, text="Violet", variable = v_tk_alea_h1_5)
tk_alea_h1_6 = Checkbutton(tk_alea_h1, text="Jaune", variable = v_tk_alea_h1_6)
tk_alea_h1_7 = Checkbutton(tk_alea_h1, text="Marron", variable = v_tk_alea_h1_7)
tk_alea_h1_8 = Checkbutton(tk_alea_h1, text="Rose", variable = v_tk_alea_h1_8)
tk_alea_h1_9 = Checkbutton(tk_alea_h1, text="Violet foncé", variable = v_tk_alea_h1_9)
tk_alea_h1_10 = Checkbutton(tk_alea_h1, text="Gris", variable = v_tk_alea_h1_10)
tk_alea_h1_11 = Checkbutton(tk_alea_h1, text="Orange", variable = v_tk_alea_h1_11)
tk_alea_h1_12 = Checkbutton(tk_alea_h1, text="Noir/Blanc", variable = v_tk_alea_h1_12)

tk_alea_h2 = LabelFrame(tk_alea, text="2eme chiffre des heures", padx=2, pady=2)
tk_alea_h2_1 = Checkbutton(tk_alea_h2, text="Aleatoire", variable = v_tk_alea_h2_1)
tk_alea_h2_2 = Checkbutton(tk_alea_h2, text="Bleu", variable = v_tk_alea_h2_2)
tk_alea_h2_3 = Checkbutton(tk_alea_h2, text="Rouge", variable = v_tk_alea_h2_3)
tk_alea_h2_4 = Checkbutton(tk_alea_h2, text="Vert", variable = v_tk_alea_h2_4)
tk_alea_h2_5 = Checkbutton(tk_alea_h2, text="Violet", variable = v_tk_alea_h2_5)
tk_alea_h2_6 = Checkbutton(tk_alea_h2, text="Jaune", variable = v_tk_alea_h2_6)
tk_alea_h2_7 = Checkbutton(tk_alea_h2, text="Marron", variable = v_tk_alea_h2_7)
tk_alea_h2_8 = Checkbutton(tk_alea_h2, text="Rose", variable = v_tk_alea_h2_8)
tk_alea_h2_9 = Checkbutton(tk_alea_h2, text="Violet foncé", variable = v_tk_alea_h2_9)
tk_alea_h2_10 = Checkbutton(tk_alea_h2, text="Gris", variable = v_tk_alea_h2_10)
tk_alea_h2_11 = Checkbutton(tk_alea_h2, text="Orange", variable = v_tk_alea_h2_11)
tk_alea_h2_12 = Checkbutton(tk_alea_h2, text="Noir/Blanc", variable = v_tk_alea_h2_12)

tk_alea_m1 = LabelFrame(tk_alea, text="1er chiffre des minutes", padx=2, pady=2)
tk_alea_m1_1 = Checkbutton(tk_alea_m1, text="Aleatoire", variable = v_tk_alea_m1_1)
tk_alea_m1_2 = Checkbutton(tk_alea_m1, text="Bleu", variable = v_tk_alea_m1_2)
tk_alea_m1_3 = Checkbutton(tk_alea_m1, text="Rouge", variable = v_tk_alea_m1_3)
tk_alea_m1_4 = Checkbutton(tk_alea_m1, text="Vert", variable = v_tk_alea_m1_4)
tk_alea_m1_5 = Checkbutton(tk_alea_m1, text="Violet", variable = v_tk_alea_m1_5)
tk_alea_m1_6 = Checkbutton(tk_alea_m1, text="Jaune", variable = v_tk_alea_m1_6)
tk_alea_m1_7 = Checkbutton(tk_alea_m1, text="Marron", variable = v_tk_alea_m1_7)
tk_alea_m1_8 = Checkbutton(tk_alea_m1, text="Rose", variable = v_tk_alea_m1_8)
tk_alea_m1_9 = Checkbutton(tk_alea_m1, text="Violet foncé", variable = v_tk_alea_m1_9)
tk_alea_m1_10 = Checkbutton(tk_alea_m1, text="Gris", variable = v_tk_alea_m1_10)
tk_alea_m1_11 = Checkbutton(tk_alea_m1, text="Orange", variable = v_tk_alea_m1_11)
tk_alea_m1_12 = Checkbutton(tk_alea_m1, text="Noir/Blanc", variable = v_tk_alea_m1_12)

tk_alea_m2 = LabelFrame(tk_alea, text="2eme chiffre des minutes", padx=2, pady=2)
tk_alea_m2_1 = Checkbutton(tk_alea_m2, text="Aleatoire", variable = v_tk_alea_m2_1)
tk_alea_m2_2 = Checkbutton(tk_alea_m2, text="Bleu", variable = v_tk_alea_m2_2)
tk_alea_m2_3 = Checkbutton(tk_alea_m2, text="Rouge", variable = v_tk_alea_m2_3)
tk_alea_m2_4 = Checkbutton(tk_alea_m2, text="Vert", variable = v_tk_alea_m2_4)
tk_alea_m2_5 = Checkbutton(tk_alea_m2, text="Violet", variable = v_tk_alea_m2_5)
tk_alea_m2_6 = Checkbutton(tk_alea_m2, text="Jaune", variable = v_tk_alea_m2_6)
tk_alea_m2_7 = Checkbutton(tk_alea_m2, text="Marron", variable = v_tk_alea_m2_7)
tk_alea_m2_8 = Checkbutton(tk_alea_m2, text="Rose", variable = v_tk_alea_m2_8)
tk_alea_m2_9 = Checkbutton(tk_alea_m2, text="Violet foncé", variable = v_tk_alea_m2_9)
tk_alea_m2_10 = Checkbutton(tk_alea_m2, text="Gris", variable = v_tk_alea_m2_10)
tk_alea_m2_11 = Checkbutton(tk_alea_m2, text="Orange", variable = v_tk_alea_m2_11)
tk_alea_m2_12 = Checkbutton(tk_alea_m2, text="Noir/Blanc", variable = v_tk_alea_m2_12)

tk_nuit = LabelFrame(fenetre, text="Mode nuit", padx=2, pady=2)
tk_nuit_1 = Checkbutton(tk_nuit, text="Auto", variable = v_tk_nuit_1)
tk_nuit_2 = Checkbutton(tk_nuit, text="Oui", variable = v_tk_nuit_2)
tk_nuit_3 = Checkbutton(tk_nuit, text="Non", variable = v_tk_nuit_3)

tk_tour = LabelFrame(fenetre, text="Tour", padx=2, pady=2)
tk_tour_1 = Label(tk_tour, text="Choisissez le nombre de tour que l'horloge")
tk_tour_2 = Label(tk_tour, text="doit effectuer (1000 tour ~= 20 min).")
tk_tour_3 = Spinbox(tk_tour, from_ = 0, to = 9999999)

tk_me = LabelFrame(fenetre, text="Mode d'emploi", padx=2, pady=2)
tk_me_1 = Label(tk_me, text="Pour les couleurs, choisissez une seul couleur")
tk_me_2 = Label(tk_me, text="OU aléatoire avec les couleurs que vous voulez")
tk_me_3 = Label(tk_me, text="et qui vont apparaitre aléatoirement OU juste")
tk_me_4 = Label(tk_me, text="aléatoire pour mettre toutes les couleurs.")
tk_me_5 = Label(tk_me, text="Pour le mode nuit, cochez une seul case.")
tk_me_6 = Label(tk_me, text="Appuyez sur Ok une fois les paramètres choisi.")
tk_me_7 = Label(tk_me, text="Appuyez sur Aléatoire/Auto et sur Ok pour cocher")
tk_me_8 = Label(tk_me, text="les modes aléatoires et mode nuit auto.")

tk_ok = Button(fenetre, text="→ OK ←", command=fenetre.destroy, cursor="clock")
tk_ok_1 = Checkbutton(fenetre, text="→ Aléatoire/Auto ←", variable = v_tk_ok_1)

titre.pack()
tk_alea.pack(side=LEFT, fill="both", expand="yes")
tk_alea_h1.pack()
tk_alea_h1_1.grid(row=1, column=1, sticky = W)
tk_alea_h1_2.grid(row=2, column=1, sticky = W)
tk_alea_h1_3.grid(row=3, column=1, sticky = W)
tk_alea_h1_4.grid(row=1, column=2, sticky = W)
tk_alea_h1_5.grid(row=2, column=2, sticky = W)
tk_alea_h1_6.grid(row=3, column=2, sticky = W)
tk_alea_h1_7.grid(row=1, column=3, sticky = W)
tk_alea_h1_8.grid(row=2, column=3, sticky = W)
tk_alea_h1_9.grid(row=3, column=3, sticky = W)
tk_alea_h1_10.grid(row=1, column=4, sticky = W)
tk_alea_h1_11.grid(row=2, column=4, sticky = W)
tk_alea_h1_12.grid(row=3, column=4, sticky = W)

tk_alea_h2.pack()
tk_alea_h2_1.grid(row=1, column=1, sticky = W)
tk_alea_h2_2.grid(row=2, column=1, sticky = W)
tk_alea_h2_3.grid(row=3, column=1, sticky = W)
tk_alea_h2_4.grid(row=1, column=2, sticky = W)
tk_alea_h2_5.grid(row=2, column=2, sticky = W)
tk_alea_h2_6.grid(row=3, column=2, sticky = W)
tk_alea_h2_7.grid(row=1, column=3, sticky = W)
tk_alea_h2_8.grid(row=2, column=3, sticky = W)
tk_alea_h2_9.grid(row=3, column=3, sticky = W)
tk_alea_h2_10.grid(row=1, column=4, sticky = W)
tk_alea_h2_11.grid(row=2, column=4, sticky = W)
tk_alea_h2_12.grid(row=3, column=4, sticky = W)

tk_alea_m1.pack()
tk_alea_m1_1.grid(row=1, column=1, sticky = W)
tk_alea_m1_2.grid(row=2, column=1, sticky = W)
tk_alea_m1_3.grid(row=3, column=1, sticky = W)
tk_alea_m1_4.grid(row=1, column=2, sticky = W)
tk_alea_m1_5.grid(row=2, column=2, sticky = W)
tk_alea_m1_6.grid(row=3, column=2, sticky = W)
tk_alea_m1_7.grid(row=1, column=3, sticky = W)
tk_alea_m1_8.grid(row=2, column=3, sticky = W)
tk_alea_m1_9.grid(row=3, column=3, sticky = W)
tk_alea_m1_10.grid(row=1, column=4, sticky = W)
tk_alea_m1_11.grid(row=2, column=4, sticky = W)
tk_alea_m1_12.grid(row=3, column=4, sticky = W)

tk_alea_m2.pack()
tk_alea_m2_1.grid(row=1, column=1, sticky = W)
tk_alea_m2_2.grid(row=2, column=1, sticky = W)
tk_alea_m2_3.grid(row=3, column=1, sticky = W)
tk_alea_m2_4.grid(row=1, column=2, sticky = W)
tk_alea_m2_5.grid(row=2, column=2, sticky = W)
tk_alea_m2_6.grid(row=3, column=2, sticky = W)
tk_alea_m2_7.grid(row=1, column=3, sticky = W)
tk_alea_m2_8.grid(row=2, column=3, sticky = W)
tk_alea_m2_9.grid(row=3, column=3, sticky = W)
tk_alea_m2_10.grid(row=1, column=4, sticky = W)
tk_alea_m2_11.grid(row=2, column=4, sticky = W)
tk_alea_m2_12.grid(row=3, column=4, sticky = W)

tk_nuit.pack(side=TOP, fill="both")
tk_nuit_1.pack()
tk_nuit_2.pack()
tk_nuit_3.pack()

tk_tour.pack(side=TOP, fill="both")
tk_tour_1.pack()
tk_tour_2.pack()
tk_tour_3.pack()

tk_me.pack(side=TOP, fill="both")
tk_me_1.pack()
tk_me_2.pack()
tk_me_3.pack()
tk_me_4.pack()
tk_me_5.pack()
tk_me_6.pack()
tk_me_7.pack()
tk_me_8.pack()

tk_ok.pack()
tk_ok_1.pack()

fenetre.mainloop()

v_tk_alea_h1_1 = v_tk_alea_h1_1.get()
v_tk_alea_h1_2 = v_tk_alea_h1_2.get()
v_tk_alea_h1_3 = v_tk_alea_h1_3.get()
v_tk_alea_h1_4 = v_tk_alea_h1_4.get()
v_tk_alea_h1_5 = v_tk_alea_h1_5.get()
v_tk_alea_h1_6 = v_tk_alea_h1_6.get()
v_tk_alea_h1_7 = v_tk_alea_h1_7.get()
v_tk_alea_h1_8 = v_tk_alea_h1_8.get()
v_tk_alea_h1_9 = v_tk_alea_h1_9.get()
v_tk_alea_h1_10 = v_tk_alea_h1_10.get()
v_tk_alea_h1_11 = v_tk_alea_h1_11.get()
v_tk_alea_h1_12 = v_tk_alea_h1_12.get()

v_tk_alea_h2_1 = v_tk_alea_h2_1.get()
v_tk_alea_h2_2 = v_tk_alea_h2_2.get()
v_tk_alea_h2_3 = v_tk_alea_h2_3.get()
v_tk_alea_h2_4 = v_tk_alea_h2_4.get()
v_tk_alea_h2_5 = v_tk_alea_h2_5.get()
v_tk_alea_h2_6 = v_tk_alea_h2_6.get()
v_tk_alea_h2_7 = v_tk_alea_h2_7.get()
v_tk_alea_h2_8 = v_tk_alea_h2_8.get()
v_tk_alea_h2_9 = v_tk_alea_h2_9.get()
v_tk_alea_h2_10 = v_tk_alea_h2_10.get()
v_tk_alea_h2_11 = v_tk_alea_h2_11.get()
v_tk_alea_h2_12 = v_tk_alea_h2_12.get()

v_tk_alea_m1_1 = v_tk_alea_m1_1.get()
v_tk_alea_m1_2 = v_tk_alea_m1_2.get()
v_tk_alea_m1_3 = v_tk_alea_m1_3.get()
v_tk_alea_m1_4 = v_tk_alea_m1_4.get()
v_tk_alea_m1_5 = v_tk_alea_m1_5.get()
v_tk_alea_m1_6 = v_tk_alea_m1_6.get()
v_tk_alea_m1_7 = v_tk_alea_m1_7.get()
v_tk_alea_m1_8 = v_tk_alea_m1_8.get()
v_tk_alea_m1_9 = v_tk_alea_m1_9.get()
v_tk_alea_m1_10 = v_tk_alea_m1_10.get()
v_tk_alea_m1_11 = v_tk_alea_m1_11.get()
v_tk_alea_m1_12 = v_tk_alea_m1_12.get()

v_tk_alea_m2_1 = v_tk_alea_m2_1.get()
v_tk_alea_m2_2 = v_tk_alea_m2_2.get()
v_tk_alea_m2_3 = v_tk_alea_m2_3.get()
v_tk_alea_m2_4 = v_tk_alea_m2_4.get()
v_tk_alea_m2_5 = v_tk_alea_m2_5.get()
v_tk_alea_m2_6 = v_tk_alea_m2_6.get()
v_tk_alea_m2_7 = v_tk_alea_m2_7.get()
v_tk_alea_m2_8 = v_tk_alea_m2_8.get()
v_tk_alea_m2_9 = v_tk_alea_m2_9.get()
v_tk_alea_m2_10 = v_tk_alea_m2_10.get()
v_tk_alea_m2_11 = v_tk_alea_m2_11.get()
v_tk_alea_m2_12 = v_tk_alea_m2_12.get()

v_tk_nuit_1 = v_tk_nuit_1.get()
v_tk_nuit_2 = v_tk_nuit_2.get()
v_tk_nuit_3 = v_tk_nuit_3.get()

v_tk_tour_3 = v_tk_tour_3.get()

v_tk_ok_1 = v_tk_ok_1.get()

if v_tk_ok_1 == 1:
	v_tk_alea_h1_1 = 1
	v_tk_alea_h2_1 = 1
	v_tk_alea_m1_1 = 1
	v_tk_alea_m2_1 = 1
	v_tk_nuit_1 = 1
	v_tk_tour_3 = 1000


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
turtle.title("Horloge v5.0")

# Boucle qui permet de faire tourner le rectangle du milieu et d'actualiser
# l'heure. La boucle fait 1000 tours donc environ 20 minutes (selon la vitesse
# du PC). Peut-être augmenté ou diminué.
for i in range(1000):
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
	
	# Détermine si il fait jour ou nuit (nuit entre 18h et 08h), et en
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
	
	# Si l'utilisateur choisi les couleurs aléatoires, choisir une couleur,
	# sinon, selon si il fait nuit ou jour, choisi noir ou blanc.
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

		
	# Choisi un chiffre selon l'heure.
	if hh1 == 1:
		if h1 == 0:
			main("0", -100, 0, fondcolor, 3)
		elif h1 == 1:
			main("1", -100, 0, fondcolor, 3)
		elif h1 == 2:
			main("2", -100, 0, fondcolor, 3)
			
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
		
	if hh2 == 1:
		if h2 == 0:
			main("0", 0, 0, fondcolor, 3)
		elif h2 == 1:
			main("1", 0, 0, fondcolor, 3)
		elif h2 == 2:
			main("2", 0, 0, fondcolor, 3)
		elif h2 == 3:
			main("3", 0, 0, fondcolor, 3)
		elif h2 == 4:
			main("4", 0, 0, fondcolor, 3)
		elif h2 == 5:
			main("5", 0, 0, fondcolor, 3)
		elif h2 == 6:
			main("6", 0, 0, fondcolor, 3)
		elif h2 == 7:
			main("7", 0, 0, fondcolor, 3)
		elif h2 == 8:
			main("8", 0, 0, fondcolor, 3)
		elif h2 == 9:
			main("9", 0, 0, fondcolor, 3)
		
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
		
	if mm1 == 1:
		if m1 == 0:
			main("0", 190, 0, fondcolor, 3)
		elif m1 == 1:
			main("1", 190, 0, fondcolor, 3)
		elif m1 == 2:
			main("2", 190, 0, fondcolor, 3)
		elif m1 == 3:
			main("3", 190, 0, fondcolor, 3)
		elif m1 == 4:
			main("4", 190, 0, fondcolor, 3)
		elif m1 == 5:
			main("5", 190, 0, fondcolor, 3)
		
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
		
	if mm2 == 1:
		if m2 == 0:
			main("0", 295, 0, fondcolor, 3)
		elif m2 == 1:
			main("1", 295, 0, fondcolor, 3)
		elif m2 == 2:
			main("2", 295, 0, fondcolor, 3)
		elif m2 == 3:
			main("3", 295, 0, fondcolor, 3)
		elif m2 == 4:
			main("4", 295, 0, fondcolor, 3)
		elif m2 == 5:
			main("5", 295, 0, fondcolor, 3)
		elif m2 == 6:
			main("6", 295, 0, fondcolor, 3)
		elif m2 == 7:
			main("7", 295, 0, fondcolor, 3)
		elif m2 == 8:
			main("8", 295, 0, fondcolor, 3)
		elif m2 == 9:
			main("9", 295, 0, fondcolor, 3)
	
	# Fait tourner le rectangle du milieu à chaque boucle. La boucle est
	# nécessaire si on change time.sleep et le nombre de tour (change le
	# temps d'actualisation sans toucher au rectangle qui bouge.
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
			main("0", -100, 0, ifondcolor, 3)
		elif h1 == 1:
			main("1", -100, 0, ifondcolor, 3)
		elif h1 == 2:
			main("2", -100, 0, ifondcolor, 3)
   
	if h21 != h2:
		hh2 = 1
		if h2 == 0:
			main("0", 0, 0, ifondcolor, 3)
		elif h2 == 1:
			main("1", 0, 0, ifondcolor, 3)
		elif h2 == 2:
			main("2", 0, 0, ifondcolor, 3)
		elif h2 == 3:
			main("3", 0, 0, ifondcolor, 3)
		elif h2 == 4:
			main("4", 0, 0, ifondcolor, 3)
		elif h2 == 5:
			main("5", 0, 0, ifondcolor, 3)
		elif h2 == 6:
			main("6", 0, 0, ifondcolor, 3)
		elif h2 == 7:
			main("7", 0, 0, ifondcolor, 3)
		elif h2 == 8:
			main("8", 0, 0, ifondcolor, 3)
		elif h2 == 9:
			main("9", 0, 0, ifondcolor, 3)
   
	if m11 != m1:
		mm1 = 1
		if m1 == 0:
			main("0", 190, 0, ifondcolor, 3)
		elif m1 == 1:
			main("1", 190, 0, ifondcolor, 3)
		elif m1 == 2:
			main("2", 190, 0, ifondcolor, 3)
		elif m1 == 3:
			main("3", 190, 0, ifondcolor, 3)
		elif m1 == 4:
			main("4", 190, 0, ifondcolor, 3)
		elif m1 == 5:
			main("5", 190, 0, ifondcolor, 3)
   
	if m21 != m2:
		mm2 = 1
		if m2 == 0:
			main("0", 295, 0, ifondcolor, 3)
		elif m2 == 1:
			main("1", 295, 0, ifondcolor, 3)
		elif m2 == 2:
			main("2", 295, 0, ifondcolor, 3)
		elif m2 == 3:
			main("3", 295, 0, ifondcolor, 3)
		elif m2 == 4:
			main("4", 295, 0, ifondcolor, 3)
		elif m2 == 5:
			main("5", 295, 0, ifondcolor, 3)
		elif m2 == 6:
			main("6", 295, 0, ifondcolor, 3)
		elif m2 == 7:
			main("7", 295, 0, ifondcolor, 3)
		elif m2 == 8:
			main("8", 295, 0, ifondcolor, 3)
		elif m2 == 9:
			main("9", 295, 0, ifondcolor, 3)


"""

Changelog :
v5.0
Fenètre de commande avec tkinter.

v4.0
Optimisation du code.
Ajout de commentaires pour rendre le code plus clair.
Ajout d'une marque aléatoire sur le rectangle du milieu.

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
