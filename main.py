import math
numeros = list(range(2,101))

def verificarAte(lista):
    return math.floor(math.sqrt(lista[-1]))

def removerMultiplo(lista,divisor):
    i = 0
    while i < len(lista):
        if lista[i] != divisor and lista[i] % divisor == 0:
            del lista[i]
        else:
            i += 1
    return lista

def crivo(lista):
    novaLista = []
    i = 2
    while i <= verificarAte(lista):
        novaLista = removerMultiplo(lista,i)
        i += 1
    return novaLista

print(crivo(numeros))