# -*- coding: utf-8 -*-
# Auteur : Alexandreou
print("----------------------------------------------------------------------")
print("PyTime v15.0")
print("----------------------------------------------------------------------")

# Initialisation des variables communes et importation des modules.
import time
import turtle
import random
from tkinter import *
from tkinter.messagebox import *
from Add_PyTime_150 import *
numerique = 0			# Sert à séléctionner le mode numérique.
analogique = 0			# Sert à séléctionner le mode analogique.
version1 = "15.0"
version = "PyTime v" + version1	# Permet de définir la version de PyTime pour l'afficher.

v_tk_textaf_2_1 = 30		# Permet de verifier si il y a un message.
mesaffoui = 0 			# Permet de savoir si le message a déjà été affiché.
egea_1 = 0				# 
colorachif = 0			# Compte le nombre de couleur choisi par l'utilisateur.
stop = 0				# Permet d'arrêter la boucle une fois le temps écoulé.
stop_min = 0			# Contient les minutes de l'heure d'arrêt de la boucle.

debut = Tk()
debut.title(version)

def v_tk_debut_1():
	global numerique
	numerique = 1
	debut.destroy()
	
def v_tk_debut_2():
	global analogique
	analogique = 1
	debut.destroy()
	
tk_debut = Label(debut, text="Choisissez le type d'affichage de l'horloge", height=2, width=50)
tk_debut_1 = Button(debut, text="Numérique", command=v_tk_debut_1, height=2)
tk_debut_2 = Button(debut, text="Analogique", command=v_tk_debut_2, height=2)

tk_debut.pack()
tk_debut_1.pack(side=LEFT)
tk_debut_2.pack(side=RIGHT)

debut.mainloop()

if numerique == 1:
	# Initialisation des variables "numerique".
	hh1 = 1		# Savoir si l'heure a changée après la boucle.
	hh2 = 1		# Savoir si l'heure a changée après la boucle.
	mm1 = 1		# Savoir si les minutes ont changées après la boucle.
	mm2 = 1		# Savoir si les minutes ont changées après la boucle.
	cadredate = 0	# Permet de faire le cadre et la date une seule fois.
	colora = []		# Permet de sauvegarder les couleurs choisi.
	
	# Début : Fenètre de commande.
	fenetre = Tk()
	fenetre.title(version)
	
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
	
	v_tk_speed_1 = IntVar()
	v_tk_speed_2 = IntVar()
	v_tk_speed_3 = IntVar()
	
	v_tk_epais_1 = IntVar()
	v_tk_epais_2 = IntVar()
	v_tk_epais_3 = IntVar()
	
	v_tk_textaf_1_1 = StringVar()
	v_tk_textaf_2_1 = IntVar()
	v_tk_textaf_2_3 = IntVar()
	
	v_tk_ok_1 = IntVar()
	
	tk_save_oui = 0
	tk_save_exe = 0
	fenetre3 = 0
	
	# Fenètres tiers.
	def creersave():
		global tk_save_oui
		global fenetre3
		tk_save_oui = 1
		fenetre3.destroy()
		fenetre.destroy()
	def exesave():
		global tk_save_exe
		global fenetre3
		tk_save_exe = 1
		fenetre3.destroy()
		fenetre.destroy()
	def save():
		global fenetre3
		fenetre3 = Tk()
		fenetre3.title("Sauvegarde")
		tk_save_1 = Label(fenetre3, text="Pour créer une sauvegarde, cocher les")
		tk_save_2 = Label(fenetre3, text="options et cliquer sur Créer une sauvegarde.")
		tk_save_3 = Label(fenetre3, text="Pour exécuter une sauvegarde,")
		tk_save_4 = Label(fenetre3, text="cliquer sur Exécuter une sauvegarde")
		tk_save_5 = Button(fenetre3, text="Créer une sauvegarde", command=creersave)
		tk_save_6 = Button(fenetre3, text="Exécuter une sauvegarde", command=exesave)
		tk_save_1.pack()
		tk_save_2.pack()
		tk_save_3.pack()
		tk_save_4.pack()
		tk_save_5.pack()
		tk_save_6.pack()
		
	def aproposde():
		fenetre2 = Tk()
		fenetre2.title("A propos")
		titre = Label(fenetre2, text="PyTime", height=1, width=10)
		titre.config(font=('Arial', 30, 'italic', 'bold'))
		tk_aproposde_1 = Label(fenetre2, text="L'horloge en python")
		tk_aproposde_2 = Label(fenetre2, text="Mode numérique")
		tk_aproposde_3 = Label(fenetre2, text=("(Version " + version1 + ")"))
		tk_aproposde_4 = Label(fenetre2, text="Auteur : Alexandre l'Heritier")
		titre.pack()
		tk_aproposde_1.pack()
		tk_aproposde_2.pack()
		tk_aproposde_3.pack()
		tk_aproposde_4.pack()
	
	def aide():
		fenetre1 = Tk()
		fenetre1.title("Aide")
		tk_aide = Label(fenetre1, text="Pour les couleurs, choisissez une seul couleur")
		tk_aide_1 = Label(fenetre1, text="OU aléatoire avec les couleurs que vous voulez")
		tk_aide_2 = Label(fenetre1, text="et qui vont apparaitre aléatoirement OU juste")
		tk_aide_3 = Label(fenetre1, text="aléatoire pour mettre toutes les couleurs.")
		tk_aide_4 = Label(fenetre1, text="---")
		tk_aide_5 = Label(fenetre1, text="Pour le mode nuit, cochez une seul case.")
		tk_aide_6 = Label(fenetre1, text="---")
		tk_aide_7 = Label(fenetre1, text="Appuyez sur Ok une fois les paramètres choisi.")
		tk_aide_8 = Label(fenetre1, text="Le mode automatique est coché par défaut, appuyer")
		tk_aide_9 = Label(fenetre1, text="sur Ok pour l'activer, plus besoin non plus de")
		tk_aide_10 = Label(fenetre1, text="tout cocher pour éviter un crash.")
		tk_aide_11 = Label(fenetre1, text="---")
		tk_aide_12 = Label(fenetre1, text="Attention, l'arrêt de l'horloge n'est pas très")
		tk_aide_13 = Label(fenetre1, text="précise au niveau des secondes.")
		tk_aide_14 = Label(fenetre1, text="---")
		tk_aide_15 = Button(fenetre1, text="A propos", command=aproposde)
		tk_aide.pack()
		tk_aide_1.pack()
		tk_aide_2.pack()
		tk_aide_3.pack()
		tk_aide_4.pack()
		tk_aide_5.pack()
		tk_aide_6.pack()
		tk_aide_7.pack()
		tk_aide_8.pack()
		tk_aide_9.pack()
		tk_aide_10.pack()
		tk_aide_11.pack()
		tk_aide_12.pack()
		tk_aide_13.pack()
		tk_aide_14.pack()
		tk_aide_15.pack()
	
	# Création du titre.
	titre_1 = LabelFrame(fenetre, text="", padx=2, pady=2)
	titre = Label(titre_1, text="PyTime", height=1)
	titre.config(font=('Arial', 30, 'italic', 'bold'))
	
	# Création de la partie "Couleur des chiffres".
	tk_alea = LabelFrame(fenetre, text="Couleur des chiffres", padx=2, pady=2)
	
	tk_alea_h1 = LabelFrame(tk_alea, text="1er chiffre des heures", padx=2, pady=2)
	tk_alea_h1_1 = Checkbutton(tk_alea_h1, text="Aléatoire", variable = v_tk_alea_h1_1)
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
	
	tk_alea_h2 = LabelFrame(tk_alea, text="2ème chiffre des heures", padx=2, pady=2)
	tk_alea_h2_1 = Checkbutton(tk_alea_h2, text="Aléatoire", variable = v_tk_alea_h2_1)
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
	tk_alea_m1_1 = Checkbutton(tk_alea_m1, text="Aléatoire", variable = v_tk_alea_m1_1)
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
	
	tk_alea_m2 = LabelFrame(tk_alea, text="2ème chiffre des minutes", padx=2, pady=2)
	tk_alea_m2_1 = Checkbutton(tk_alea_m2, text="Aléatoire", variable = v_tk_alea_m2_1)
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
	
	
	# Création de la partie "Mode nuit".
	tk_nuit = LabelFrame(fenetre, text="Mode nuit", padx=2, pady=2)
	tk_nuit_1 = Checkbutton(tk_nuit, text="Auto", variable = v_tk_nuit_1)
	tk_nuit_2 = Checkbutton(tk_nuit, text="Oui", variable = v_tk_nuit_2)
	tk_nuit_3 = Checkbutton(tk_nuit, text="Non", variable = v_tk_nuit_3)
	
	
	# Création de la partie "Tour".
	tk_tour = LabelFrame(fenetre, text="Minute", padx=2, pady=2)
	tk_tour_1 = Label(tk_tour, text="Choisissez le nombre de minutes que")
	tk_tour_2 = Label(tk_tour, text=" l'horloge doit fonctionner.")
	tk_tour_3 = Spinbox(tk_tour, from_ = 0, to = 9999999, textvariable = v_tk_tour_3, relief=FLAT)
	
	
	# Création de la partie "Mode d'emploi".
	tk_me = LabelFrame(fenetre, text="Autres", padx=2, pady=2)
	tk_me_1 = Button(tk_me, text="→ Mode d'emploi ←", command=aide, relief=FLAT)
	tk_me_2 = Button(tk_me, text="→ Save ←", command=save, relief=FLAT)
	
	
	# Création de la partie "Vitesse".
	tk_speed = LabelFrame(fenetre, text="Vitesse", padx=2, pady=2)
	tk_speed_1 = Checkbutton(tk_speed, text="Normal", variable = v_tk_speed_1)
	tk_speed_2 = Checkbutton(tk_speed, text="Rapide", variable = v_tk_speed_2)
	tk_speed_3 = Checkbutton(tk_speed, text="Très rapide", variable = v_tk_speed_3)
	
	
	# Création de la partie "Epaisseur des chiffres".
	tk_epais = LabelFrame(fenetre, text="Epaisseur des chiffres", padx=2, pady=2)
	tk_epais_1 = Checkbutton(tk_epais, text="Fin", variable = v_tk_epais_1)
	tk_epais_2 = Checkbutton(tk_epais, text="Normal", variable = v_tk_epais_2)
	tk_epais_3 = Checkbutton(tk_epais, text="Gros", variable = v_tk_epais_3)

	# Création de la partie "Texte à afficher".
	tk_textaf = LabelFrame(fenetre, text="Texte à afficher", padx=2, pady=2)
	tk_textaf_1 = LabelFrame(tk_textaf, text="Entrer le texte voulu", padx=2, pady=2)
	tk_textaf_1_1 = Entry(tk_textaf_1, textvariable=v_tk_textaf_1_1, width=35)
	tk_textaf_2 = LabelFrame(tk_textaf, text="Entrer l'heure à laquelle afficher le texte", padx=2, pady=2)
	tk_textaf_2_1 = Spinbox(tk_textaf_2, from_ = 0, to = 23, textvariable=v_tk_textaf_2_1, width=5)
	tk_textaf_2_2 = Label(tk_textaf_2, text=":")
	tk_textaf_2_3 = Spinbox(tk_textaf_2, from_ = 0, to = 59, textvariable=v_tk_textaf_2_3, width=5)
	
	# Création des deux boutons.
	tk_ok = Button(fenetre, text="→ OK ←", command=fenetre.destroy, cursor="clock", height=2, relief=FLAT)
	tk_ok.config(font=('Arial', 12, 'italic', 'bold'))
	
	
	# Formation des différents objets.
	titre.pack()
	titre_1.pack()
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
	tk_nuit_1.pack(side=LEFT)
	tk_nuit_2.pack(side=LEFT)
	tk_nuit_3.pack(side=LEFT)
	
	tk_speed.pack(fill="both")
	tk_speed_1.pack(side=LEFT)
	tk_speed_2.pack(side=LEFT)
	tk_speed_3.pack(side=LEFT)
	
	tk_epais.pack(fill="both")
	tk_epais_1.pack(side=LEFT)
	tk_epais_2.pack(side=LEFT)
	tk_epais_3.pack(side=LEFT)
	
	tk_tour.pack(side=TOP, fill="both")
	tk_tour_1.pack()
	tk_tour_2.pack()
	tk_tour_3.pack()
	tk_tour_3.get()
	
	tk_textaf.pack(fill="both")
	tk_textaf_1.pack()
	tk_textaf_1_1.pack(side=LEFT)
	tk_textaf_2.pack(side=TOP)
	tk_textaf_2_1.pack(side=LEFT)
	tk_textaf_2_2.pack(side=LEFT)
	tk_textaf_2_3.pack(side=LEFT)

	tk_me.pack(side=TOP, fill="both")
	tk_me_1.pack(side=LEFT)
	tk_me_2.pack(side=LEFT)
	
	tk_ok.pack(side=BOTTOM, fill="both")
	
	# Permet de laisser afficher la fenètre de commande tant que l'utilisateur
	# n'appui pas sur OK.
	fenetre.mainloop()
	
	# Met les résultats obtenu dans les variables correspondantes.
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
	
	v_tk_speed_1 = v_tk_speed_1.get()
	v_tk_speed_2 = v_tk_speed_2.get()
	v_tk_speed_3 = v_tk_speed_3.get()
	
	v_tk_epais_1 = v_tk_epais_1.get()
	v_tk_epais_2 = v_tk_epais_2.get()
	v_tk_epais_3 = v_tk_epais_3.get()
	
	v_tk_textaf_1_1 = v_tk_textaf_1_1.get()
	v_tk_textaf_2_1 = v_tk_textaf_2_1.get()
	v_tk_textaf_2_3 = v_tk_textaf_2_3.get()
		
	# Rempli les options incomplète pour éviter les crashs.
	if v_tk_alea_h1_1 == 0 and v_tk_alea_h1_2 == 0 and v_tk_alea_h1_3 == 0\
	and v_tk_alea_h1_4 == 0 and v_tk_alea_h1_5 == 0 and v_tk_alea_h1_6 == 0\
	and v_tk_alea_h1_7 == 0 and v_tk_alea_h1_8 == 0 and v_tk_alea_h1_9 == 0\
	and v_tk_alea_h1_10 == 0 and v_tk_alea_h1_11 == 0 and v_tk_alea_h1_12 ==\
	0:
		v_tk_alea_h1_1 = 1
	if v_tk_alea_h2_1 == 0 and v_tk_alea_h2_2 == 0 and v_tk_alea_h2_3 == 0\
	and v_tk_alea_h2_4 == 0 and v_tk_alea_h2_5 == 0 and v_tk_alea_h2_6 == 0\
	and v_tk_alea_h2_7 == 0 and v_tk_alea_h2_8 == 0 and v_tk_alea_h2_9 == 0\
	and v_tk_alea_h2_10 == 0 and v_tk_alea_h2_11 == 0 and v_tk_alea_h2_12 ==\
	0:
		v_tk_alea_h2_1 = 1
	if v_tk_alea_m1_1 == 0 and v_tk_alea_m1_2 == 0 and v_tk_alea_m1_3 == 0\
	and v_tk_alea_m1_4 == 0 and v_tk_alea_m1_5 == 0 and v_tk_alea_m1_6 == 0\
	and v_tk_alea_m1_7 == 0 and v_tk_alea_m1_8 == 0 and v_tk_alea_m1_9 == 0\
	and v_tk_alea_m1_10 == 0 and v_tk_alea_m1_11 == 0 and v_tk_alea_m1_12 ==\
	0:
		v_tk_alea_m1_1 = 1
	if v_tk_alea_m2_1 == 0 and v_tk_alea_m2_2 == 0 and v_tk_alea_m2_3 == 0\
	and v_tk_alea_m2_4 == 0 and v_tk_alea_m2_5 == 0 and v_tk_alea_m2_6 == 0\
	and v_tk_alea_m2_7 == 0 and v_tk_alea_m2_8 == 0 and v_tk_alea_m2_9 == 0\
	and v_tk_alea_m2_10 == 0 and v_tk_alea_m2_11 == 0 and v_tk_alea_m2_12 ==\
	0:
		v_tk_alea_m2_1 = 1
	if v_tk_nuit_1 == 0 and v_tk_nuit_2 == 0 and v_tk_nuit_3 == 0:
		v_tk_nuit_1 = 1
	if v_tk_tour_3 == 0:
		v_tk_tour_3 = 20
	if v_tk_speed_1 == 0 and v_tk_speed_2 == 0 and v_tk_speed_3 == 0:
		v_tk_speed_2 = 1
	if v_tk_epais_1 == 0 and v_tk_epais_2 == 0 and v_tk_epais_3 == 0:
		v_tk_epais_2 = 1		
		
	if tk_save_oui == 1:
		ecrire = open("num_pytime_v1.save", "w")
		ecrire.write("Fichier de sauvegarde pour PyTime partie numerique\n\
------------------------------------------------------------------------------\n\
Chaques lignes contient un 1 ou un 0 (sauf pour les minutes) pour savoir quelles options\
 doivent être activé ou non.\nListe des options dans l'ordre :\nv_tk_alea_h1_1\
;v_tk_alea_h1_2;v_tk_alea_h1_3;v_tk_alea_h1_4;v_tk_alea_h1_5;v_tk_alea_h1_6\
;v_tk_alea_h1_7;v_tk_alea_h1_8;v_tk_alea_h1_9;v_tk_alea_h1_10;v_tk_alea_h1_11\
;v_tk_alea_h1_12;v_tk_alea_h2_1;v_tk_alea_h2_2;v_tk_alea_h2_3;v_tk_alea_h2_4\
;v_tk_alea_h2_5;v_tk_alea_h2_6;v_tk_alea_h2_7;v_tk_alea_h2_8;v_tk_alea_h2_9\
;v_tk_alea_h2_10;v_tk_alea_h2_11;v_tk_alea_h2_12;v_tk_alea_m1_1;v_tk_alea_m1_2\
;v_tk_alea_m1_3;v_tk_alea_m1_4;v_tk_alea_m1_5;v_tk_alea_m1_6;v_tk_alea_m1_7\
;v_tk_alea_m1_8;v_tk_alea_m1_9;v_tk_alea_m1_10;v_tk_alea_m1_11;v_tk_alea_m1_12\
;v_tk_alea_m2_1;v_tk_alea_m2_2;v_tk_alea_m2_3;v_tk_alea_m2_4;v_tk_alea_m2_5\
;v_tk_alea_m2_6;v_tk_alea_m2_7;v_tk_alea_m2_8;v_tk_alea_m2_9;v_tk_alea_m2_10\
;v_tk_alea_m2_11;v_tk_alea_m2_12;v_tk_nuit_1;v_tk_nuit_2;v_tk_nuit_3\
;v_tk_tour_3;v_tk_speed_1;v_tk_speed_2;v_tk_speed_3;v_tk_epais_1;v_tk_epais_2\
;v_tk_epais_3;v_tk_textaf_1_1;v_tk_textaf_2_1;v_tk_textaf_2_3\nOption :\n")
		ecrire.write(str(v_tk_alea_h1_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_4))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_5))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_6))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_7))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_8))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_9))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_10))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_11))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_12))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_4))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_5))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_6))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_7))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_8))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_9))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_10))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_11))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h2_12))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_4))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_5))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_6))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_7))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_8))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_9))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_10))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_11))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m1_12))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_4))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_5))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_6))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_7))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_8))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_9))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_10))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_11))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_m2_12))
		ecrire.write(";")
		ecrire.write(str(v_tk_nuit_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_nuit_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_nuit_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_tour_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_speed_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_speed_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_speed_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_epais_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_epais_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_epais_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_textaf_1_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_textaf_2_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_textaf_2_3))
		ecrire.write("\n")
		ecrire.write(version)
		ecrire.close()
		
	if tk_save_exe == 1:
		lire = open("num_pytime_v1.save", "r")
		liste = []
		for ligne in lire:
			liste.append(ligne)
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
		
	#Configure la vitesse.
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
	
	# Fin : Fenètre de commande.
	
	
	# Construction des chiffres par Turtle : a désigne le positionnement gauche/
	# droite, b désigne le positionnement haut/bas, f désigne la couleur du crayon,
	# g désigne l'épaisseur du crayon et t désigne la class Turtle().

		
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
		chif(a, b, f, g, t, v_tk_speed)
		
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



if analogique == 1:
	# Initialisation des variables "analogique".
	mm = 1		# Savoir si l'heure a changée après la boucle.
	hh = 1		# Savoir si les minutes ont changées après la boucle.
	unefois = 0		# Permet de faire la parie aléatoire et le cadre une seule fois.
	
	# Début : Fenètre de commande.
	fenetre = Tk()
	fenetre.title(version)

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
	
	v_tk_nuit_1 = IntVar()
	v_tk_nuit_2 = IntVar()
	v_tk_nuit_3 = IntVar()
	
	v_tk_chco_1 = IntVar()
	v_tk_chco_2 = IntVar()	
	
	v_tk_tour_3 = IntVar()
	
	v_tk_speed_1 = IntVar()
	v_tk_speed_2 = IntVar()
	v_tk_speed_3 = IntVar()
	
	v_tk_tyai_1 = IntVar()
	v_tk_tyai_2 = IntVar()
	v_tk_tyai_3 = IntVar()
	
	v_tk_textaf_1_1 = StringVar()
	v_tk_textaf_2_1 = IntVar()
	v_tk_textaf_2_3 = IntVar()
	
	v_tk_ok_1 = IntVar()
	
	tk_save_oui = 0
	tk_save_exe = 0
	fenetre3 = 0
	
	# Fenètres tiers.
	def acreersave():
		global tk_save_oui
		global fenetre3
		tk_save_oui = 1
		fenetre3.destroy()
		fenetre.destroy()
	def aexesave():
		global tk_save_exe
		global fenetre3
		tk_save_exe = 1
		fenetre3.destroy()
		fenetre.destroy()
	def asave():
		global fenetre3
		fenetre3 = Tk()
		fenetre3.title("Sauvegarde")
		tk_save_1 = Label(fenetre3, text="Pour créer une sauvegarde, cocher les")
		tk_save_2 = Label(fenetre3, text="options et cliquer sur Créer une sauvegarde.")
		tk_save_3 = Label(fenetre3, text="Pour exécuter une sauvegarde,")
		tk_save_4 = Label(fenetre3, text="cliquer sur Exécuter une sauvegarde")
		tk_save_5 = Button(fenetre3, text="Créer une sauvegarde", command=acreersave)
		tk_save_6 = Button(fenetre3, text="Exécuter une sauvegarde", command=aexesave)
		tk_save_1.pack()
		tk_save_2.pack()
		tk_save_3.pack()
		tk_save_4.pack()
		tk_save_5.pack()
		tk_save_6.pack()
		
	def aaproposde():
		fenetre2 = Tk()
		fenetre2.title("A propos")
		titre = Label(fenetre2, text="PyTime", height=1, width=10)
		titre.config(font=('Arial', 30, 'italic', 'bold'))
		tk_aproposde_1 = Label(fenetre2, text="L'horloge en python")
		tk_aproposde_2 = Label(fenetre2, text="Mode analogique")
		tk_aproposde_3 = Label(fenetre2, text=("(Version " + version1 + ")"))
		tk_aproposde_4 = Label(fenetre2, text="Auteur : Alexandre l'Heritier")
		titre.pack()
		tk_aproposde_1.pack()
		tk_aproposde_2.pack()
		tk_aproposde_3.pack()
		tk_aproposde_4.pack()
		
	def aaide():
		fenetre1 = Tk()
		fenetre1.title("Aide")
		tk_aide = Label(fenetre1, text="Pour les couleurs, choisissez une seul couleur")
		tk_aide_1 = Label(fenetre1, text="OU aléatoire avec les couleurs que vous voulez")
		tk_aide_2 = Label(fenetre1, text="OU juste aléatoire.")
		tk_aide_4 = Label(fenetre1, text="---")
		tk_aide_5 = Label(fenetre1, text="Pour le mode nuit, cochez une seul case.")
		tk_aide_6 = Label(fenetre1, text="---")
		tk_aide_7 = Label(fenetre1, text="Appuyez sur Ok une fois les paramètres choisi.")
		tk_aide_8 = Label(fenetre1, text="Le mode automatique est coché par défaut, appuyer")
		tk_aide_9 = Label(fenetre1, text="sur Ok pour l'activer, plus besoin non plus de")
		tk_aide_10 = Label(fenetre1, text="tout cocher pour éviter un crash.")
		tk_aide_11 = Label(fenetre1, text="---")
		tk_aide_12 = Label(fenetre1, text="Attention, l'arrêt de l'horloge n'est pas très")
		tk_aide_13 = Label(fenetre1, text="précise au niveau des secondes.")
		tk_aide_14 = Label(fenetre1, text="---")
		tk_aide_15 = Button(fenetre1, text="A propos", command=aaproposde)
		tk_aide.pack()
		tk_aide_1.pack()
		tk_aide_2.pack()
		tk_aide_4.pack()
		tk_aide_5.pack()
		tk_aide_6.pack()
		tk_aide_7.pack()
		tk_aide_8.pack()
		tk_aide_9.pack()
		tk_aide_10.pack()
		tk_aide_11.pack()
		tk_aide_12.pack()
		tk_aide_13.pack()
		tk_aide_14.pack()
		tk_aide_15.pack()
	# Création du titre.
	titre_1 = LabelFrame(fenetre, text="", padx=2, pady=2)
	titre = Label(titre_1, text="PyTime", height=1)
	titre.config(font=('Arial', 30, 'italic', 'bold'))
	
	# Création de la partie "Couleur de l'horloge".
	tk_alea_h1 = LabelFrame(fenetre, text="Couleur de l'horloge", padx=2, pady=2)
	tk_alea_h1_1 = Checkbutton(tk_alea_h1, text="Aléatoire", variable = v_tk_alea_h1_1)
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
	
	# Création de la partie "Mode nuit".
	tk_nuit = LabelFrame(fenetre, text="Mode nuit", padx=2, pady=2)
	tk_nuit_1 = Checkbutton(tk_nuit, text="Auto", variable = v_tk_nuit_1)
	tk_nuit_2 = Checkbutton(tk_nuit, text="Oui", variable = v_tk_nuit_2)
	tk_nuit_3 = Checkbutton(tk_nuit, text="Non", variable = v_tk_nuit_3)
	
	# Création de la partie "Tour".
	tk_tour = LabelFrame(fenetre, text="Minute", padx=2, pady=2)
	tk_tour_1 = Label(tk_tour, text="Choisissez le nombre de minutes que")
	tk_tour_2 = Label(tk_tour, text=" l'horloge doit fonctionner.")
	tk_tour_3 = Spinbox(tk_tour, from_ = 0, to = 9999999, textvariable = v_tk_tour_3, relief=FLAT)

	# Création de la partie "Mode d'emploi".
	tk_me = LabelFrame(fenetre, text="Autres", padx=2, pady=2)
	tk_me_1 = Button(tk_me, text="→ Mode d'emploi ←", command=aaide, relief=FLAT)
	tk_me_2 = Button(tk_me, text="→ Save ←", command=asave, relief=FLAT)

	# Création de la partie "Vitesse".
	tk_speed = LabelFrame(fenetre, text="Vitesse", padx=2, pady=2)
	tk_speed_1 = Checkbutton(tk_speed, text="Normal", variable = v_tk_speed_1)
	tk_speed_2 = Checkbutton(tk_speed, text="Rapide", variable = v_tk_speed_2)
	tk_speed_3 = Checkbutton(tk_speed, text="Très rapide", variable = v_tk_speed_3)

	# Création de la partie "Changement de couleur à chaque tours".
	tk_chco = LabelFrame(fenetre, text="Changement de couleur à chaque tours", padx=2, pady=2)
	tk_chco_1 = Checkbutton(tk_chco, text="Oui", variable = v_tk_chco_1)
	tk_chco_2 = Checkbutton(tk_chco, text="Non", variable = v_tk_chco_2)

	# Création de la partie "Aiguilles".
	tk_tyai = LabelFrame(fenetre, text="Type d'aiguilles", padx=2, pady=2)
	tk_tyai_1 = Checkbutton(tk_tyai, text="Flèches", variable = v_tk_tyai_1)
	tk_tyai_2 = Checkbutton(tk_tyai, text="Triangle au bout", variable = v_tk_tyai_2)
	tk_tyai_3 = Checkbutton(tk_tyai, text="Triangle", variable = v_tk_tyai_3)
	
	# Création de la partie "Texte à afficher".
	tk_textaf = LabelFrame(fenetre, text="Texte à afficher", padx=2, pady=2)
	tk_textaf_1 = LabelFrame(tk_textaf, text="Entrer le texte voulu", padx=2, pady=2)
	tk_textaf_1_1 = Entry(tk_textaf_1, textvariable=v_tk_textaf_1_1, width=35)
	tk_textaf_2 = LabelFrame(tk_textaf, text="Entrer l'heure à laquelle afficher le texte", padx=2, pady=2)
	tk_textaf_2_1 = Spinbox(tk_textaf_2, from_ = 0, to = 23, textvariable=v_tk_textaf_2_1, width=5)
	tk_textaf_2_2 = Label(tk_textaf_2, text=":")
	tk_textaf_2_3 = Spinbox(tk_textaf_2, from_ = 0, to = 59, textvariable=v_tk_textaf_2_3, width=5)

	# Création des deux boutons.
	tk_ok = Button(fenetre, text="→ OK ←", command=fenetre.destroy, cursor="clock", height=2, relief=FLAT)
	tk_ok.config(font=('Arial', 12, 'italic', 'bold'))
	
	# Formation des différents objets.
	titre.pack()
	titre_1.pack()
	tk_alea_h1.pack()
	tk_alea_h1_1.grid(row=1, column=1, sticky = W)
	tk_alea_h1_2.grid(row=2, column=1, sticky = W)
	tk_alea_h1_3.grid(row=3, column=1, sticky = W)
	tk_alea_h1_4.grid(row=4, column=1, sticky = W)
	tk_alea_h1_5.grid(row=1, column=2, sticky = W)
	tk_alea_h1_6.grid(row=2, column=2, sticky = W)
	tk_alea_h1_7.grid(row=3, column=2, sticky = W)
	tk_alea_h1_8.grid(row=4, column=2, sticky = W)
	tk_alea_h1_9.grid(row=1, column=3, sticky = W)
	tk_alea_h1_10.grid(row=2, column=3, sticky = W)
	tk_alea_h1_11.grid(row=3, column=3, sticky = W)
	tk_alea_h1_12.grid(row=4, column=3, sticky = W)

	tk_nuit.pack(side=TOP, fill="both")
	tk_nuit_1.pack(side=LEFT)
	tk_nuit_2.pack(side=LEFT)
	tk_nuit_3.pack(side=LEFT)
	
	tk_speed.pack(fill="both")
	tk_speed_1.pack(side=LEFT)
	tk_speed_2.pack(side=LEFT)
	tk_speed_3.pack(side=LEFT)
	
	tk_tyai.pack(fill="both")
	tk_tyai_1.pack(side=LEFT)
	tk_tyai_2.pack(side=LEFT)
	tk_tyai_3.pack(side=LEFT)
	
	tk_chco.pack(side=TOP, fill="both")
	tk_chco_1.pack(side=LEFT)
	tk_chco_2.pack(side=LEFT)	
	
	tk_tour.pack(side=TOP, fill="both")
	tk_tour_1.pack()
	tk_tour_2.pack()
	tk_tour_3.pack()
	tk_tour_3.get()
	
	tk_textaf.pack(fill="both")
	tk_textaf_1.pack()
	tk_textaf_1_1.pack(side=LEFT)
	tk_textaf_2.pack(side=TOP)
	tk_textaf_2_1.pack(side=LEFT)
	tk_textaf_2_2.pack(side=LEFT)
	tk_textaf_2_3.pack(side=LEFT)
	
	tk_me.pack(side=TOP, fill="both")
	tk_me_1.pack(side=LEFT)
	tk_me_2.pack(side=LEFT)
	
	tk_ok.pack(side=BOTTOM, fill="both")
	
	# Permet de laisser afficher la fenètre de commande tant que l'utilisateur
	# n'appui pas sur OK.
	fenetre.mainloop()
	
	# Met les résultats obtenu dans les variables correspondantes.
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
	
	v_tk_nuit_1 = v_tk_nuit_1.get()
	v_tk_nuit_2 = v_tk_nuit_2.get()
	v_tk_nuit_3 = v_tk_nuit_3.get()
	
	v_tk_tour_3 = v_tk_tour_3.get()
	
	v_tk_speed_1 = v_tk_speed_1.get()
	v_tk_speed_2 = v_tk_speed_2.get()
	v_tk_speed_3 = v_tk_speed_3.get()
	
	v_tk_tyai_1 = v_tk_tyai_1.get()
	v_tk_tyai_2 = v_tk_tyai_2.get()
	v_tk_tyai_3 = v_tk_tyai_3.get()

	v_tk_chco_1 = v_tk_chco_1.get()
	v_tk_chco_2 = v_tk_chco_2.get()	

	v_tk_textaf_1_1 = v_tk_textaf_1_1.get()
	v_tk_textaf_2_1 = v_tk_textaf_2_1.get()
	v_tk_textaf_2_3 = v_tk_textaf_2_3.get()
	
	# Rempli les options incomplète pour éviter les crashs.
	if v_tk_alea_h1_1 == 0 and v_tk_alea_h1_2 == 0 and v_tk_alea_h1_3 == 0\
	and v_tk_alea_h1_4 == 0 and v_tk_alea_h1_5 == 0 and v_tk_alea_h1_6 == 0\
	and v_tk_alea_h1_7 == 0 and v_tk_alea_h1_8 == 0 and v_tk_alea_h1_9 == 0\
	and v_tk_alea_h1_10 == 0 and v_tk_alea_h1_11 == 0 and v_tk_alea_h1_12 ==\
	0:
		v_tk_alea_h1_1 = 1
	if v_tk_nuit_1 == 0 and v_tk_nuit_2 == 0 and v_tk_nuit_3 == 0:
		v_tk_nuit_1 = 1
	if v_tk_tour_3 == 0:
		v_tk_tour_3 = 20
	if v_tk_speed_1 == 0 and v_tk_speed_2 == 0 and v_tk_speed_3 == 0:
		v_tk_speed_2 = 1
	if v_tk_tyai_1 == 0 and v_tk_tyai_2 == 0 and v_tk_tyai_3 == 0:
		v_tk_tyai_1 = 1
	if v_tk_chco_1 == 0 and v_tk_chco_2 == 0:
		v_tk_chco_1 = 1	
	
	if tk_save_oui == 1:
		ecrire = open("ana_pytime_v1.save", "w")
		ecrire.write("Fichier de sauvegarde pour PyTime partie analogique\n\
------------------------------------------------------------------------------\n\
Chaques lignes contient un 1 ou un 0 (sauf pour les minutes) pour savoir quelles options\
 doivent être activé ou non.\nListe des options dans l'ordre :\nv_tk_alea_h1_1\
;v_tk_alea_h1_2;v_tk_alea_h1_3;v_tk_alea_h1_4;v_tk_alea_h1_5;v_tk_alea_h1_6\
;v_tk_alea_h1_7;v_tk_alea_h1_8;v_tk_alea_h1_9;v_tk_alea_h1_10;v_tk_alea_h1_11\
;v_tk_alea_h1_12;v_tk_nuit_1;v_tk_nuit_2;v_tk_nuit_3\
;v_tk_tour_3;v_tk_speed_1;v_tk_speed_2;v_tk_speed_3;v_tk_tyai_1;v_tk_tyai_2\
;v_tk_tyai_3;v_tk_chco_1;v_tk_chco_2;v_tk_textaf_1_1;v_tk_textaf_2_1\
;v_tk_textaf_2_3\nOption :\n")
		ecrire.write(str(v_tk_alea_h1_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_4))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_5))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_6))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_7))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_8))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_9))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_10))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_11))
		ecrire.write(";")
		ecrire.write(str(v_tk_alea_h1_12))
		ecrire.write(";")
		ecrire.write(str(v_tk_nuit_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_nuit_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_nuit_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_tour_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_speed_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_speed_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_speed_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_tyai_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_tyai_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_tyai_3))
		ecrire.write(";")
		ecrire.write(str(v_tk_chco_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_chco_2))
		ecrire.write(";")
		ecrire.write(str(v_tk_textaf_1_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_textaf_2_1))
		ecrire.write(";")
		ecrire.write(str(v_tk_textaf_2_3))
		ecrire.write("\n")
		ecrire.write(version)
		ecrire.close()
		
	if tk_save_exe == 1:
		lire = open("ana_pytime_v1.save", "r")
		liste = []
		for ligne in lire:
			liste.append(ligne)
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
		
	#Configure la vitesse.
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
	
		
	turtle.setup(width=450,height=450)
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
			petitmil(0, fondcolor, turtle.Turtle(), v_tk_speed)
			if v_tk_tyai_1 == 1:
				aiguillem(m1, fondcolor, turtle.Turtle(), v_tk_speed)
			elif v_tk_tyai_2 == 1:
				aiguillem1(m1, fondcolor, turtle.Turtle(), v_tk_speed)
			else:
				aiguillem2(m1, fondcolor, turtle.Turtle(), v_tk_speed)
		if hh == 1:
			petitmil(0, fondcolor, turtle.Turtle(), v_tk_speed)
			if v_tk_tyai_1 == 1:
				aiguilleh(h1, fondcolor, turtle.Turtle(), v_tk_speed)
			elif v_tk_tyai_2 == 1:
				aiguilleh1(h1, fondcolor, turtle.Turtle(), v_tk_speed)
			else:
				aiguilleh2(h1, fondcolor, turtle.Turtle(), v_tk_speed)
		if unefois == 0:
			acontour(0, fondcolor, turtle.Turtle(), v_tk_speed, v_tk_chco_2)
			heurmin(fondcolor, turtle.Turtle(), v_tk_speed)
			posdouze(fondcolor, turtle.Turtle(), v_tk_speed)
			postrois(fondcolor, turtle.Turtle(), v_tk_speed)
			possix(fondcolor, turtle.Turtle(), v_tk_speed)
			posneuf(fondcolor, turtle.Turtle(), v_tk_speed)
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
				aiguilleh(h1, fondcolor, turtle.Turtle(), v_tk_speed)
			elif v_tk_tyai_2 == 1:
				aiguilleh1(h1, fondcolor, turtle.Turtle(), v_tk_speed)
			else:
				aiguilleh2(h1, fondcolor, turtle.Turtle(), v_tk_speed)
		
		# Fait tourner le grand cercle à chaque boucle. La boucle est
		# nécessaire si on change time.sleep et le nombre de tour (change le
		# temps d'actualisation sans toucher au grand cercle qui bouge).
		for i in range(1):
			alea = random.randint(0, 9)
			colr = ['blue', 'red', 'green', 'violet', 'yellow', 'brown',\
			'pink', 'purple', 'grey', 'orange']
			mfondcolor = colr[alea]
				
			acontour(1, mfondcolor, turtle.Turtle(), v_tk_speed, v_tk_chco_2)
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
				aiguillem(m1, ifondcolor, turtle.Turtle(), v_tk_speed)
			elif v_tk_tyai_2 == 1:
				aiguillem1(m1, ifondcolor, turtle.Turtle(), v_tk_speed)
			else:
				aiguillem2(m1, ifondcolor, turtle.Turtle(), v_tk_speed)
		if h11 != h1:
			hh = 1
			if v_tk_tyai_1 == 1:
				aiguilleh(h1, ifondcolor, turtle.Turtle(), v_tk_speed)
			elif v_tk_tyai_2 == 1:
				aiguilleh1(h1, ifondcolor, turtle.Turtle(), v_tk_speed)
			else:
				aiguilleh2(h1, ifondcolor, turtle.Turtle(), v_tk_speed)

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

Changelog :
v15.0 :
Mise en place d'un deuxième fichier contenant le nécessaire pour PyTime.

v14.0 (Super Stable) :
Correction de quelque bugs.

v13.0 (Stable) :
Modification du mode automatique, activer par défaut pour qu'en cas d'option
non paramétré, le programme ne crash pas.

v12.0 :
Possibilité de faire une sauvegarde pour les deux types d'horloge.

v11.1 (Stable) :
Correction de bugs.
Ajout d'une marque aléatoire sur le contour de l'horloge analogique (comme sur
le rectangle du milieu de l'horloge numérique.

v11.0 :
Ajout d'un choix d'aiguilles.
Ajout de la possibilité d'afficher un texte à un moment donné.
Optimisation du code.

v10.1 (Stable) :
Correction de quelques bugs de l'horloge analogique.
Ajout de quelques commentaires.

v10.0 :
Mise en place d'une fenètre de commande pour la partie analogique.

v9.0 :
Mise en place d'une fenètre pour choisir entre analogique et numérique.
Ajout de commentaire dans la partie analogique.

v8.0 :
Fusion du projet AnalogiTime (v1.0) avec PyTime.
Adaptation du code pour le support de AnalogiTime.

v7.0 (Stable) :
(Version envoyée au prof de ISN)
Ajout d'une option pour l'épaisseur.

v6.1 (Stable) :
Correction de bugs.
Ajout du choix de la vitesse.
Renommage du programme en PyTime.

v6.0 :
Ouverture sans la console de commande.
Les tours sont remplacés par des minutes.
Correction de bugs.

v5.0 :
Fenètre de commande avec tkinter :
- Adaptation du code pour soutenir la fenètre de commande.
- Adaptation des commentaires.
La fenètre contient :
- Une partie "Couleur des chiffres" avec trois sous-partie : 1er chiffre des 
  heures, 2eme chiffre des heures, 1er chiffre des minutes et 2eme chiffre 
  des minutes.
- Une partie "Mode nuit" avec les options : Auto, Oui, Non.
- Une partie "Tour" avec un texte et un Spinbox.
- Une partie "Mode d'emploi" avec un texte.
- Un bouton OK
- Un bouton Aléatoire/Auto.

v4.0 (Stable) :
(Version envoyée au prof de ISN)
Optimisation du code.
Ajout de commentaires pour rendre le code plus clair.
Ajout d'une marque aléatoire sur le rectangle du milieu.

v3.2 (Stable) :
(Version présentée en classe)
Réglage de la taille de la fenètre.
Améliorations de l'affichage de la date.
Ajout d'un titre pour la fenètre.
Optimisation du code.

v3.1 :
Correction de quelques bugs.

v3.0 :
Ajout d'un cadre.
Ajout de la date.

v2.2 (Stable) :
Correction d'un problème de ralentissement.

v2.1 :
Ajout de quelques couleurs.

v2.0 :
Ajout des couleurs aléatoire.
Ajout du mode nuit.

v1.0 :
Version final de Projet Pytime, renommée Horloge.

Initialisation du Projet PyTime le 24/11/15.
"""
