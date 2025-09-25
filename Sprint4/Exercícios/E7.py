def pares_ate(n:int):
    for c in range (2,n+1):
        if c % 2 == 0:
            yield c
