'''
Axel Hervey Cruz Baez
'''
import os

'''
Segmentar
'''
carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"

archivos_lista=os.listdir(carpeta_nombre)
for archivo_nombre in archivos_lista:
    print("\n",archivo_nombre,"\n")

    archivo=open(carpeta_nombre+archivo_nombre)    
    lineas_lista=archivo.readlines()
    archivo.close()
    
    longitud=len(lineas_lista)
    print("El archivo ",archivo_nombre,"tiene",longitud,"lineas\n")

    archivo=open(carpeta_nombre+archivo_nombre)    
    texto=archivo.read()
    archivo.close()
    print("La palabras con sort son: ")
    simbolos=["(",")",",",".",",","\","":"]
    for simbolo in simbolos:
        texto=texto.replace(simbolo," "+simbolo+" ")
        palabras_lista=texto.split()
        palabras_lista.sort()


    for palabra in palabras_lista:
        print(palabra)
        ##print(palabras_lista)






