'''Axel Hervey Cruz Baez'''
'''Oswaldo Carrillo Zepeda'''
'''Procesamiento del lenguaje natural'''

carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\"

archivo_nombre="doc3.txt"

palabra=input("Ingresa la palabra a buscar en el documento: ")

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()

if palabra in texto:
    print("La palabra",palabra,"fue encontrada en el texto")

else:
    print("La palabra",palabra," no fue encontrada en el texto")

        