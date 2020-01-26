#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from peewee import *

#if os.path.exists('rej.db'):
#    os.remove('rej.db')
# tworzymy instancję bazy używanej przez modele
baza = SqliteDatabase('rej.db')  # ':memory:'


class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza



class Lekarz(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(default=False)
    specjalizacja =CharField(null=False)



class Pacjent(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    PESEL = CharField(null=False)
    data_urodzenia = CharField(null=True)
    opis_choroby = CharField(default='')



class Wizyta(BazaModel):
    data = DateField(null= False)
    godzina = TimeField(null=False)
    lekarz = ForeignKeyField(Lekarz)
    pacjent= ForeignKeyField(Pacjent)




def dodaj_wizyte(data,godzina,lekarz,pacjent):
    inst_wizyta = Wizyta(data=data,godzina=godzina,lekarz=lekarz,pacjent=pacjent)
    inst_wizyta.save()




def dodaj_lekarza_wczytaj():
    imie = input("Podaj imie: ")
    nazwisko = input("Nazwisko: ")
    specjalizacja = input("Specjalizacje: ")
    inst_lekarz = Lekarz(imie=imie, nazwisko=nazwisko,specjalizacja=specjalizacja)
    inst_lekarz.save()

def dodaj_lekarza(imie,nazwisko,specjalizacja):
    inst_lekarz = Lekarz(imie=imie, nazwisko=nazwisko,specjalizacja=specjalizacja)
    inst_lekarz.save()

def dodaj_pacjenta_wczytaj():
    imie = input("Podaj imie: ")
    nazwisko = input("Nazwisko: ")
    pesel = input("PESEL: ")
    inst_pacjent = Pacjent(imie=imie, nazwisko = nazwisko, PESEL=pesel)
    inst_pacjent.save()

def dodaj_pacjenta_pesel(pesel):
    imie = input("Podaj imie: ")
    nazwisko = input("Nazwisko: ")
    inst_pacjent = Pacjent(imie=imie, nazwisko = nazwisko, PESEL=pesel)
    inst_pacjent.save()

def dodaj_pacjenta(imie,nazwisko,pesel):
    inst_pacjent = Pacjent(imie=imie, nazwisko = nazwisko, PESEL=pesel)
    inst_pacjent.save()


def czy_pacjent_jest_w_bazie(pesel):
    istnieje = True
    for p in Pacjent.select().where(Pacjent.PESEL == pesel):
        print(p.imie, p.nazwisko)
        istnieje = False
    return istnieje

def dostępni_lekarze():
    print("Dostępni lekarze")
    for lekarz in Lekarz.select():
        print(lekarz.id, lekarz.imie, lekarz.nazwisko, lekarz.specjalizacja)

def wypisz_wizyty_ld(lekarz, dzien):
    print("Wizyty: ",lekarz.imie,lekarz.nazwisko,"Dnia:", dzien )
    for wizyta in Wizyta.select().where(Wizyta.lekarz.id==lekarz.id and Wizyta.data == dzien):
        print(wizyta.id, "PESEL pacjenta: ", wizyta.pacjent.PESEL)
        print("Data: ", wizyta.data, wizyta.godzina)
        print()

def wypisz_wizyty():
    print("Umowione wizyty:")
    for wizyta in Wizyta.select():
        print(wizyta.id, "PESEL pacjenta: ",wizyta.pacjent.PESEL)
        print("Lekarz: ", wizyta.lekarz.nazwisko, wizyta.lekarz.imie)
        print("Godzina: ", wizyta.godzina)
        print()


def zapisz_pacjenta():

    pesel = input("PESEL pacjenta: ")


    if czy_pacjent_jest_w_bazie(pesel):
        print("Brak pacjenta w bazie")
        dodaj_pacjenta_pesel(pesel)

    dostępni_lekarze()

    id = input("Podaj ID lekarza: ")

    lekarz = Lekarz.select().where(Lekarz.id==id)[0]
    pacjent = Pacjent.select().where(Pacjent.PESEL==pesel)[0]

    data = input("Data: ")

    print("Zajete godziny")
    wypisz_wizyty_ld(lekarz,data)

    godzina = input("Godzina: ")


    dodaj_wizyte(data,godzina,lekarz,pacjent)

#    print("Zajęte terminy")
#
#    for  wizyta in Wizyty.select().join(Lekarz):
#        if Wizyty.lekarz.ID == id:
#            print("Data: ", wizyta.data)



#baza.connect()  # nawiązujemy połączenie z bazą
#baza.create_tables([Lekarz, Pacjent, Wizyta])  # tworzymy tabele

#dodaj_lekarza("Jan","Kowalski","aaa")
#dodaj_lekarza("Adam","Nowak","bbb")
#dodaj_lekarza("Jan","Kowalski","ccc")

#dodaj_pacjenta("Krzysztof","Ibisz","112")
#dodaj_pacjenta("Zygmunt","Jok","1111")
#dodaj_pacjenta("Ewa","Ibisz","2222")

#zapisz_pacjenta()

#zapisz_pacjenta()
#wypisz_wizyty()
#print()
#dostępni_lekarze()

#zapisz_pacjenta()
#wypisz_wizyty_ld(Lekarz.select().where(Lekarz.id==2)[0],12)


