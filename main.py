# tömb/lista létrehozása

#létrehozás konkrét értékekkel és elemszám kiírása
szamok = [2,4,6,8]
print(f"A szamok tömb elemszáma: {len(szamok)}")
print(f"A szamok adatszerkezet 0. eleme: {szamok[0]}")
print(f"A szamok adatszerkezet 1. eleme: {szamok[1]}")

#kiírás ciklussal
for elem in szamok:
    print(elem)

#létrehozás üresen, elemek nélkül
szamok2 = []
print(f"A szamok2 lista elemszáma: {len(szamok2)}")
#elem hozzáfűzése a lista végéhez
szamok2.append(3)
print(f"A szamok2 lista elemszáma: {len(szamok2)}")
szamok2.append(4)
print(f"A szamok2 lista elemszáma: {len(szamok2)}")
# további elemek hozzáadása véletlenszámokat felhasználva
import random
szamok2.append(random.randint(20,100))
szamok2.append(random.randint(20,100))
szamok2.append(random.randint(20,100))
print(f"A szamok2 lista elemszáma: {len(szamok2)}")
for elem in szamok2:
    print(elem)

#elem törlése
print("A törlés utáni elemek:")
szamok2.remove(4)
for elem in szamok2:
    print(elem)

# lista kiírása ciklus nélkül
print(szamok)
print(szamok2)

#beszúrás a listába
szamok2.insert(0,100)
print(szamok2)

# listakezelő metódusok
print(f"A szamok2 lista legkisebb eleme: {min(szamok2)}")
print(f"A szamok2 lista legnagyobb eleme: {max(szamok2)}")
print(f"A szamok2 lista összege: {sum(szamok2)}")

# a lista elemei rendezve:
print(sorted(szamok2))

# lista stringekkel
szavak = ["alma","körte","szilva","alma"]
for elem in szavak:
    print(elem)
print(szavak)
# hányszor szerepel az alma
print(szavak.count("alma"))