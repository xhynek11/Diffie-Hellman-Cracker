"""
Autoři: Asszonyi Jakub, Hynek Vojtěch, Jiřikovský Jakub

Program ustanoví parametry pro komunikaci DH protokolu, které využije při napodobení jejich odposlechu.
Program pracuje se dvěma metodami - bruteforcem a Babystep algoritmem. Uživatel volí, kterou metodu prolamování využije. 

Síň rekordů (Babystep, i7 8th gen, 16GB RAM):
1. 53bit - 25 min
2. 52bit - 16 min
3. 50bit - 6 min
4. 45bit - 33 s
5. 35bit - 0,7 s
"""

import math
import time
from random import randint
import Babystep
import bruteforce
import generator
import prvocisla

#zadávání bitů prvočísla
bity = 0
while bity < 2:
    bity = int(input("Zadejte pocet bitů prvocila: "))
    if bity < 2:
        print("Alespoň 2bit číslo!\n")
    else:
        break

zacatek_generovani = time.time() #uložení času zahájení generování parametrů

prvocislo = prvocisla.generate_prime_number(bity)
generator = generator.generatory(generator.faktorizace(prvocislo -1),prvocislo)

print("\n\nParametry odposlouchávané komunikace:")

print("\nVeřejné prvočíslo \t\t'p': " + str(prvocislo))
print("Veřejný generátor \t\t'g': " + str(generator))

tajna_alice = randint(1, prvocislo - 1)
print("Tajná hodnota alice \t\t'a': " + str(tajna_alice))

tajna_bob = randint(1, prvocislo - 1)
print("Tajná hodnota boba \t\t'b': " + str(tajna_bob) )

verejna_alice = pow(generator,tajna_alice,prvocislo)
print("Veřejná hodnota alice \t\t'A': " + str(verejna_alice))

verejny_bob = pow(generator,tajna_bob,prvocislo)
print("Veřejná hodnota boba \t\t'B': " + str(verejny_bob))

klic_alice = pow(verejny_bob,tajna_alice,prvocislo)
klic_boba = pow(verejna_alice,tajna_bob,prvocislo)
print("\nTajný klíč 'K'\nAlice:\t" + str(klic_alice) + "\nBoba:\t" + str(klic_boba))

casGenerovani = str(round(float(str(time.time() - zacatek_generovani)),4)) #čas generování parametrů na 4 des. místa, je to samý str a float ale jinak to nefungovalo
print("\nČas generování parametrů je: " + str(casGenerovani) + " s") 

#výběr metody prolamování
print("\n[1] Metoda Brute Force")
print("[2] Metoda Baby step - Giant step")

#podm výběru metody
volba = 0
while (volba != 1 and volba != 2):
    volba = int(input("Zvotle metodu: "))
    if (volba != 1 and volba != 2):
        print ("\nChybná volba!")
    else:
        break

zacatek_sifrovani = time.time() #uložení času zahájení prolamování

if volba == 1:
    bruteforce.brute_force(generator,prvocislo,verejna_alice,verejny_bob)
else:
    Babystep.baby_step(generator, verejna_alice, verejny_bob, prvocislo)

konec = time.time() #uložení času ukončení prolamování
casProlamovani = str(round(float(str(konec - zacatek_sifrovani)),4)) #čas prolamovani
print("\n\nČas prolamovaní: " + str(casProlamovani) + " s")
print("\n\n")