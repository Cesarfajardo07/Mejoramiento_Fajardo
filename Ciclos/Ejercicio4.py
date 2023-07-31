#Determinar cuales y cuantos números perfectos hay entre 1 y 1000?

def es_numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero

def encontrar_numeros_perfectos(rango_inicio, rango_fin):
    numeros_perfectos = []
    for numero in range(rango_inicio, rango_fin + 1):
        if es_numero_perfecto(numero):
            numeros_perfectos.append(numero)
    return numeros_perfectos

rango_inicio = 1
rango_fin = 1000
numeros_perfectos_en_rango = encontrar_numeros_perfectos(rango_inicio, rango_fin)

print("Números perfectos entre 1 y 1000:")
print(numeros_perfectos_en_rango)
print("Cantidad de números perfectos:", len(numeros_perfectos_en_rango))
