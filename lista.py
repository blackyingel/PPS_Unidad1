numero = int(input("Introduce un numero entre el 1 y el 20(Incluidos): "))
lista = [6,14,11,3,2,1,15,19]

#Funcion para mirar si estan en el rango asignado 
# (Devuelve true or false)
def estaEnRango(valor, minimo, maximo):
 
 if (valor >= minimo and valor <= maximo):
    return True
 else:
    return False

#Funcion para ver si un valor está en la lista 
# (Devuelve true or false)
def estaEnLista(valor, lista):
    estado = False
    for x in lista:
        if x == valor:
            estado = True
            
    if estado == True:
        return True
    else: 
        return False

if estaEnRango(numero, 1, 20) == True:
    if estaEnLista(numero, lista) == True:
        print("El valor introducido se encuentra dentro de la lista.")
    else:
        print("El valor introducido NO se encuentra dentro de la lista, vuelva a intentarlo.")
else: 
    print("El valor introducido no se encuentra entre el 1 y el 20, intenteló de nuevo.") 







