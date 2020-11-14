import requests
from requests import exceptions
from requests.sessions import HTTPAdapter
from tokenwebhook import tokensncf

def message(whattosay):
    """Envoie un mesage au webhook"""
    try:
        r = requests.post(tokensncf, json={'content':whattosay})
        print("Votre message \"{}\" à été envoyé avec succès.".format(whattosay))
    except requests.exceptions.HTTPAdapter as e:
        print(e)
    
while True:
    inputed = str(input())
    message(inputed)
