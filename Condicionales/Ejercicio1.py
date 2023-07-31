#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el valor del medio es 11. No use operadores lógicos
v1=int(input("Ingrese el primer valor: "))
v2=int(input("Ingrese el segundo valor: "))
v3=int(input("Ingrese el tercer valor: "))
print(v1,v2,v3)

def valor_medio():
    if v1 < v2 < v3:
        print(f"{v2} es el numero del medio")
    elif v1 < v3 < v2:
        print(f"{v3} es el numero del medio")
    elif v2 < v1 < v3:
        print(f"{v1} es el numero del medio")
    elif v1 > v2 < v3:
        print(f"{v2} es el numero del medio")
    elif v1 == v2 == v3:
        print(f"Los tres valores son iguales")

valor_medio()







