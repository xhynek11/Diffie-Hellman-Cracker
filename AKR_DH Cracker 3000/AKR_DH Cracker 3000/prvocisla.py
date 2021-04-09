from random import randrange, getrandbits

def is_prime(n, k=128):

    """    Testuje zda je číslo prvočíslo
           n -> int -> číslo které testujeme
           k -> int -> počet testů které provedeme, standartně 128
    """
    #K ověření prvočísla použijeme Miller-Rabinův test
    #Testujeme zda je číslo dvojka nebo trojka
    if n == 2 or n == 3:
        return True
    #testujeme zda je číslo menší jak jedna nebo dělitelné dvěma
    if n <= 1 or n % 2 == 0:
        return False
    # najdeme parametry "s" a "r" pro které platí n=2^s*r+1
    s = 0
    r = n - 1
    #dokud je poslední bit "r" roven 0, tak se opakuje while => to znamená dokud je číslo dělitelné 2 tak se "s" inkrementuje a "r" dělí 2
    while r & 1 == 0:
        s += 1
        r //= 2
    #Test se provede "k"-krát, když se provede pouze jednou šance že číslo je složené je 1/4
    #My provádíme test 124-krát to znamená že šance že číslo je složené je (1/4)^124
    for _ in range(k):
        #Náhodně vybereme "a", které budeme testovat zda to není svědek složenosti
        a = randrange(2, n - 1)
        #pokud je "x" 1 nebo n-1 zkusí se ověřit další "a"
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True
def generate_prime_candidate(length):
    """ Vygeneruje náhodné liché číslo
        length -> int -> délka vygenerovyných náhodných bitů
    """
    # vygeneruje náhodné bity
    p = getrandbits(length)
    # nastaví MSB a LSB na 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length):
    """ Vygeneruje prvočíslo
        length -> int -> délka generovaného prvočíslačísla v bitech
    """
    #musí se nastavit neprvočíselné číslo(třeba sudé), aby první test neprošel a první hodnta while byla true
    p = 4
    #Bude generovat čísla tak dlouho dokud nenajde prvočíslo
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    return p
# print(generate_prime_number())

