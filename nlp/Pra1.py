'''Axel Hervey Cruz Baez'''
'''Oswaldo Carrillo Zepeda'''
'''Procesamiento del lenguaje natural'''

print("Procesamiento del lenguaje natural")

suma = 7 + 5
resultado = suma * 5

print(suma)
print("Total =", resultado)

print("-----------------------------------------------------")
archivo = open("C:\\Users\\axelb\\Desktop\\nlp\\doc3.txt")
print(archivo.read())
archivo.close()

archivo2 = open("C:\\Users\\axelb\\Desktop\\nlp\\doc3.txt", "w")
cadena1 = "primer clase de programación python en procesamiento"
archivo2.write(cadena1)

archivo2 = open("C:\\Users\\axelb\\Desktop\\nlp\\doc3.txt")
print(archivo2.read())
archivo2.close()