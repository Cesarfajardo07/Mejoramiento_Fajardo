#Determinar los divisores de un número introducido por teclado 

def divisores_numero():
    num=int(input("ingrese un numero:"))
    print (f"los divisores de {num} son:")
    for i in range(1,num+1):
        if num%i==0:
            print(i)

divisores_numero()


