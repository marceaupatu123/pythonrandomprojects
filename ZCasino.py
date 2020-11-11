import os
from math import ceil
from random import randrange
from typing import AsyncGenerator


def check_number(number):
    """
    Vérifie si le nombre est valide
    """
    try:
        number = int(number)
    except ValueError:
        print("Valeur invalide")
        return False
    if number < 0:
        print("Nombre Inférieur à 0")
        return False
    elif number > 49:
        print("Nombre Supérieur à 49")
        return False
    else:
        return True


def check_money(mise, argent):
    """
    Regarde si la mise est possible
    """
    try:
        mise = int(mise)
    except ValueError:
        print("Valeur invalide")
        return False
    if mise > argent:
        print("Vous n'avez pas assez d'argent")
        return False
    elif mise < 0:
        print("Votre mise ne peut pas être négative")
        return False
    else:
        return True


def check_winner(mise, numéro_gagnant):
    mise = int(mise)
    numéro_gagnant = int(numéro_gagnant)
    """
    Regarde combien d'argent atribuer
    """
    if numéro_gagnant == mise:
        print("Nombre exact !")
        return mise*3
    elif numéro_gagnant % 2 == mise % 2:
        print("Couleur Bonne !")
        return ceil(mise/2)
    else:
        print("Perdu")
        return -mise


argent = 1000
rejouer = True

while rejouer == True:
    print("Quel est votre nombre ?")
    number = input()
    while check_number(number) == False:
        print("Quel est votre nombre ?")
        number = input()
        continue
    print("Quel est votre mise ? (Vous avez", argent, "$)")
    mise = input()
    while check_money(mise, argent) == False:
        print("Quel est votre mise ? (Vous avez", argent, "$)")
        mise = input()
        continue
    numéro_gagnant = randrange(50)
    print("Le numéro gagant est...", numéro_gagnant, "!")

    argent += check_winner(mise, numéro_gagnant)

    print("Votre solde est de", argent)

    if input("Voulez vous rejouez (o/n)?") == "o":
        rejouer = True
    else:
        rejouer = False

os.system("pause")
