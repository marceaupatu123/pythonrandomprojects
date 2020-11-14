import requests
from requests import exceptions
from requests.sessions import HTTPAdapter
from tokenwebhook import tokensncf


def message(whattosay):
    """Envoie un mesage au webhook"""
    r = requests.post(tokensncf, json={'content': whattosay})
    if r.status_code == 204:
        return "Votre nom \"{0}\" à été envoyé avec succès.".format(whattosay)
    else:
        return "Erreur \"{0}\"".format(r.status_code)


def changename(message, name):
    """change le nom"""
    r = requests.post(tokensncf, json={'content': message, 'username': name})
    if r.status_code == 204:
        return "Votre nom \"{0}\" à été envoyé avec succès.".format(name)
    else:
        return "Erreur \"{0}\"".format(r.status_code)


def changeavatar(message, name, url):
    """change l'avatar"""
    r = requests.post(
        tokensncf, json={'content': message, 'username': name, 'avatar_url': url})
    if r.status_code == 204:
        return "Votre avatar \"{0}\" à été envoyé avec succès.".format(url)
    else:
        return "Erreur \"{0}\"".format(r.status_code)


name = ""
avatar = ""
print("Voulez vous changer de nom de webhook ? (o/n)")
inputed = str(input()).lower()
if inputed == "o":
    print("Nom ?")
    name = str(input())
print("Voulez vous changer l'avatar de webhook ? (o/n)")
inputed = str(input()).lower()
if inputed == "o":
    print("Avatar ?")
    avatar = str(input())
if name != "" and avatar != "":
    while True:
        print("Message ?")
        send = str(input())
        changeavatar(send, name, avatar)
elif name != "":
    while True:
        print("Message ?")
        send = str(input())
        changename(send, name)
else:
    while True:
        print("Message ?")
        send = str(input())
        message(send)