import math

def faktorizace(n):
    prvocisla = []

    def faktor(n):
        x = 2
        c = 2
        x_1 = 2
        prvocislo = 1
        while prvocislo == 1:
            for i in range(c):
                if prvocislo> 1:
                    break
                x = (x*x + 1) % n
                prvocislo = math.gcd(x_1 - x, n)
            c = c*2
            x_1 = x
        return prvocislo
    while n > 1:
        dalsi = faktor(n)
        prvocisla.append(dalsi)
        n //= dalsi

    return prvocisla


def generatory(r,p):
    rozklad = r
    pocet = len(rozklad)
    prvocislo = p
    euler = p-1
    generator = 2
    list = []
    while generator < prvocislo:
        j = 0
        i = 0
        while j != pocet:
            x = 0
            mocnina = int(euler/rozklad[i])
            x = pow(generator,mocnina,prvocislo)

            if x == 1:      # jestli se to bude rovnat jedna tak skončí
                if generator in list:
                    list.remove(generator)
                break
            else:           # pokud dočasně najde tak to zapise do listu, a
                if generator not in list:
                    list.append(generator)
            j +=1
            i +=1
        if generator in list:
            break
        generator += 1
    return list[0]
