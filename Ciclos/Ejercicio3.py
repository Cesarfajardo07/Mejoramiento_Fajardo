#Determinar si un numero es o no perfecto. Un numero es perfecto si la suma de sus divisores sin incluir el propio numero es igual a este.
def numeros_perfetcos():
    suma_divisores = 0
    a = int(input('Ingrese un numero: '))
    print(f'Los divisores de {a} son: ')
    for i in range (1,a):
        if a%i==0:
            print(i)
    for i in range(1,a):
        if a % i==0:
            suma_divisores= suma_divisores + i

    if suma_divisores==a:
        print(f'El numero {a} es perfecto')
    else:
        print(f'El numero {a} no es perfecto')

numeros_perfetcos()