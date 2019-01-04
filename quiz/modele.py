#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *

baza_plik = 'quiz.db'
baza = SqliteDatabase(baza_plik) #instalacja bazy

#### MODELE DANYCH
class BazaModel(Model):
    class Meta:
        database = baza

class Kategoria(BazaModel):
    
    kategoria = CharField(null=False)
    
class Pytanie(BazaModel):
    
    pytanie = CharField(null=False)
    id_kat = ForeignKeyField(Kategoria, related_name='pytania')
        
class Odpowiedz(BazaModel):
    
    odpowiedz = CharField(null=False)
    id_p = ForeignKeyField(Pytanie, related_name='odpowiedzi')
    odpok = IntegerField(default=0)
