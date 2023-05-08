#!usr/bin/python3

    """    Correcte": Quan la velocitat real del cotxe sigui inferior o igual a la velocitat màxima permesa a la via.
    "Marge de seguretat": Quan la velocitat real del cotxe sigui més gran que la permesa però no la superi en més del 10%.
    "Multa": Quan la velocitat real sigui superior a la permesa més un 10%.

Exemple de JSON resultat:
{"resultat": "Marge de seguretat"}
    """



import flask
import json



class Radar():
    
    def __init__(self, velocidat):
        self._velocidat = velocidat
        self._parametres = None

def calcula_velocidat(self):
    if self._velocidat <= 80
        resultat = self._velocidat 
    else:
        resultat = 80
    else:
        resultat = self._velocidat * 0.10
        
    else:
        resultat 
    self._velocitat = resultat
    return resultat
    
