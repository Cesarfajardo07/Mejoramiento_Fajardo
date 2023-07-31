#Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo
#los cálculos así:
#Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan
#200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que
#permita calcular el costo de una llamada dados los minutos de duración.

def llamada_telefonica():
    duracion=int(input("Ingrese la duracion de la llamada en minutos: "))
    print(f"La duracion de la llamada fue de {duracion} minutos")
    costo=0
    minAdi= duracion - 3

    if duracion <= 3:
        costo=200
        print(f"El costo de la llamada es de: {costo} pesos")
    elif duracion > 3:
        costo=200 + minAdi * 50
        print(f"El costo de la llamada es de: {costo} pesos")



llamada_telefonica()