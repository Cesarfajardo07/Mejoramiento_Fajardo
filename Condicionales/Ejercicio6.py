#Un obrero necesita calcular su salario semanal, el cual se obtiene de la sig.
#manera:
#Si trabaja 40 horas o menos se le paga $2600 por hora
#Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40
#horas y $5000 por cada hora extra

horas= int(input("Ingrese el numero de horas trabajadas en la semana: "))
extras= int(input("Ingrese el numero de horas extra trabajadas en la semana: "))
 
def salario_obrero():
    h1= horas * 2600
    h2= extras * 5000
    h3= h1 + h2
   
    if horas > 40:
        print("El maximo de horas permitidas en  el primer campo son 40")
    elif extras == 0:
        print(f"El salario semanal calculado es: {h1}")
    else:
        extras >= 1
        print(f"El salario mensual calculado es: {h3}")

    

salario_obrero()