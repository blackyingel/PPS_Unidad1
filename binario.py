numero = input("Introduce un número binario: ")

numComprobacion = {"0", "1"}
numCompar = set(numero)

if (numCompar == numComprobacion or numCompar == {"0"} or numCompar == {"1"}):
    print ("True")
    conversionBinario = int(numero, 2)
    print (conversionBinario)
else:
    print ("False")
    print ("El número introducido no es un binario, vuelva a intentarlo")
    
