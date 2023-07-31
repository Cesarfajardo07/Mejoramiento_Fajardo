#Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien, etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores

def mostrar_nota():
    nota = int(input("Ingrese una nota del 1 al 10: "))
    
    if nota < 5:
        print("Bajo")
    elif nota == 5:
        print("Básico")
    elif nota <= 7:
        print("Medio")
    elif nota <= 9:
        print("Alto")
    else:
        print("Superior")

mostrar_nota()