import math

def brute_force(g, p, A, B):
    r = 0 
    #r je hodnota soukromého parametru, který cyklicky zvyšujeme a testujeme, jestli platí modulární mocnění
    while True:
        r = r + 1
        if pow(g,r,p) == A:
            a = r #pokud platí, uloží se jako soukromý parametr
            K = pow(B, r, p) #výpočet klíče
            print("\nTajná hodnota 'a': "+ str(a))
            print("Tajný klíč: " + str(K))
            return None