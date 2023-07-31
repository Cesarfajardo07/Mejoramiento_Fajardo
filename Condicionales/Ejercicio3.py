#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número exceda los límites emita un mensaje y finalice el programa
num=int(input("Ingrese un valor entre 0 y 9999: "))
print(num)

def numero_cifras():
    if num > 9999:
        print("El valor ingresado no cuenta con lo solicitado")
    elif num < 0:
        print("El valor ingresado no cuenta con lo solicitado")
    else:
        if num < 10:
            print("El valor ingresado tiene una cifra")
        elif num < 100:
            print("El valor ingresado tiene 2 cifras")
        elif num < 1000:
            print("El valor ingresado tiene 3 cifras")
        elif num < 10000:
            print("El valor ingresado tiene 4 cifras")

numero_cifras()