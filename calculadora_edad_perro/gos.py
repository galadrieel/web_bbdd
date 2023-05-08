#!usr/bin/python3
import flask
import json


class Gos():
    def __init__(self, edat):
        self._edat = edat
        self._equivalencia = None
        
    def calcula_equivalencia(self):
        if self._edat <= 2:
            resultat = self._edat * 10.5
        else:
            resultat = 21 + 4 * (self._edat - 2)
        self._equivalencia = resultat
        return resultat
    
    def __str__(self):
        dictionary_gos = {"edat_del_gos": self._edat, "equivalencia_humana": self._equivalencia}
        return json.dumps(dictionary_gos)
            