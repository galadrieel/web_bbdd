#!usr/bin/python3
import json

class Algebra():
    def __init__(self, v1=0, v2=0, op='+'):
        self._valor_1 = v1
        self._valor_2 = v2
        self._operador = op
        
    @property
    def valor_1(self):
        return self._valor_1
        
    @valor_1.setter
    def valor_1(self, valor):
        self._valor_1 = valor
        
    @property
    def valor_2(self):
        return self._valor_2
        
    @valor_2.setter
    def valor_2(self, valor):
        self._valor_2 = valor
        
        
        
    @property
    def operador(self):
        return self._operador
        
    @operador.setter
    def operador(self, valor):
        self._operador = valor
        
    
    def opera(self):
        if self._operador == "+":
            return self._valor_1 + self._valor_2
        
        if self._operador == "-":
            return self._valor_1 - self._valor_2
        
        
    def __str_(self):
        resultat = {"resultat": self.opera()}
        return json.dumps(resultat)
        
        
        
        
        