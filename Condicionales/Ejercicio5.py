#Pida un numero al usuario que representa días del año. Diga a que mes del año
#corresponde así. Si el número es menor o igual a 31 indica que esta en enero,
#Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en
#cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días

num = int(input("Ingrese un numero del 1 al 365: "))
print(num)

def MesDelAño():
    if num <= 31:
        print("El numero que ingreso corresponde a Enero")
    elif num <= 59:
        print("El numero que ingreso corresponde a Febrero")
    elif num <= 90:
        print("El numero que ingreso correponde al mes de Marzo")
    elif num <= 120:
        print("El numero que ingreso corresponde al mes de Abril")
    elif num <= 151:
        print("El numero que ingreso corresponde al mes de Mayo")
    elif num <= 181:
        print("El numero que ingreso corresponde al mes de Junio")
    elif num <= 212:
        print("El numero que ingreso corresponde al mes de Julio")
    elif num <= 243:
        print("El numero que ingreso corresponde al mes de Agosto")
    elif num <= 273:
        print("El numero ingresado corresponde al mes de Septiembre")
    elif num <= 304:
        print("El numero ingresado corresponde al mes de Octubre")
    elif num <= 334:
        print("El numero ingresado corresponde al mes de Noviembre")
    elif num <= 365:
        print("El numero ingresado corresponde al mes de Diciembre")


MesDelAño()