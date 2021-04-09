import math
import generator

# Funguje, jistota

def baby_step(g, A, B, p):
    babystep_count = int(math.ceil(math.sqrt(p - 1)))
    pole = {}

    #baby step
    for i in range(babystep_count):
        pole[pow(g, i, p)] = i
        # giant step
    c = pow(g, babystep_count * (p - 2), p)
    for j in range(babystep_count):
        y = ((A * pow(c, j, p)) % p)
        if y in pole:
            tajnaAlice = int(j * babystep_count + pole[y])
            print("\nTajná hodnota 'a': " + str(int(tajnaAlice)))
            klic = pow(B, tajnaAlice, p)
            print("Tajný klíč: " + str(klic))
            break
    return None


# Pokus o zpracování větších čísel
# pole nabere příliš velkou velikost a počítač už to nezvládá, pro 8GB RAM
# NEFUNGUJE :(

"""
def baby_step3(g, A, p):
    N = int(math.ceil(math.sqrt(p - 1)))
    print("N:  " + str(N))
    pole = {}
    if N > 1:
        M = int(N / 2)
        print(M)
    else:
        M = N
    hodnota = 0
    while hodnota < N:
        # Baby step.
        pole.clear()
        for i in range(M):
            if hodnota == N:
                break
            if hodnota != N:
                pole[pow(g, hodnota, p)] = hodnota
            hodnota += 1
        c = pow(g, N * (p - 2), p)

        promena = 0
        for j in range(N):
            y = ((A * pow(c, promena, p)) % p)
            promena += 1
            if y in pole:
                print(pole[y])
                list1 = {}
                list1[pole[y]] = promena
    for j in range(N):
        y = ((A * pow(c, j, p)) % p)
        if y in list1:
            return j * N + list1[y]
"""

