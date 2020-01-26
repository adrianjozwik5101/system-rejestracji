import baza

while True:
    print("1. Dodaj lekarza")
    print("2. Dodaj pacjenta")
    print("3. wypisz wizyty")
    print("4. Zapisz pacjenta")

    k = input("Wynierz operacje ")

    if k == "1":
        baza.dodaj_lekarza_wczytaj()
    elif k== "2":
        baza.dodaj_pacjenta_wczytaj()
    elif k== "3":
        #baza.wypisz_wizyty()
        print("1. Wszystkie")
        print("2. Dany lekarz w danym dniu")
        n = input("Wynierz operacje")
        if n=="1" :
            baza.wypisz_wizyty()
        else:
            baza.dostępni_lekarze()
            lekarz = input("Wybierz lekarza ")
            dzien = input("Dnia ")
            print()
            baza.wypisz_wizyty_ld(baza.Lekarz.select().where(baza.Lekarz.id==lekarz)[0],dzien)
    else:
        baza.zapisz_pacjenta()


    print()
    print()