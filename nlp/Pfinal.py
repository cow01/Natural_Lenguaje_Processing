'''Axel Hervey Cruz Baez'''
'''Oswaldo Carrillo Zepeda'''
'''Procesamiento del lenguaje natural'''

'''
1.-Leer 2 docs .txt
2.-debe tener 3 parrafos como minimo
3.-mostrar cuantas lineas(longitud) con texto
4.-cuantas lineas vacias tiene cada documento
5.-que elimine simbolos de puntuacion
6.-que muestre todas las palabras que contiene cada documento de manera ordenada
7.-mostrar cuantas palabras(longitud) contiene cada documento

8.-que una los 2 docs
9.-que elimine los simbolos de puntuacion
10.-que muestre todas las palabras del nuevo doc de forma ordenada
11.- que muestre cuantas palabras (longitud) tiene el doc
12.-escriba 1 palabra y la busque e indique si existe
'''
import os

print("\n-------------------------1.-Leer 2 txt y 2.-tener 3 parrafos-------------------------------------\n")

print("\nArchivo 1 \n")
archivo=open("C:\\Users\\axelb\\Desktop\\nlp\\Docs\\Arfinal.txt","r")
print(archivo.read())
archivo.close()
print("\nArchivo 2 \n")
archivo2=open("C:\\Users\\axelb\\Desktop\\nlp\\Docs\\Arfinal1.txt","r")
print(archivo2.read())
archivo.close()
print("----------------------------------------------------------------------------------------------\n")

print("---------------3.-Mostrar cuantas lineas(longitud) con texto y 4.- Lineas vacias----------------\n")
carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre="Arfinal.txt"

carpeta_nombre1="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre1="Arfinal1.txt"

with open(carpeta_nombre+archivo_nombre,"r") as arch:
    lineas_listas=arch.readlines()
num_lineas=0
num_texto=0
num_vacio=0

for linea in lineas_listas:
    if linea.strip()=='':
        num_lineas=num_lineas+1
        print("LINEA",num_lineas,":","Linea sin texto")
        num_vacio=num_vacio+1

    else:
        num_lineas=num_lineas+1
        print("LINEA",num_lineas,":",linea)
        num_texto=num_texto+1
print("\nLineas totales: ",num_lineas)
print("Lineas con texto: ",num_texto)            
print("Lineas vacias: ",num_vacio)  
print("\n")
arch.close()

with open(carpeta_nombre1+archivo_nombre1,"r") as arch2:
    lineas_listas=arch2.readlines()
num_lineas=0
num_texto=0
num_vacio=0

for linea in lineas_listas:
    if linea.strip()=='':
        num_lineas=num_lineas+1
        print("LINEA",num_lineas,":","Linea sin texto")
        num_vacio=num_vacio+1

    else:
        num_lineas=num_lineas+1
        print("LINEA",num_lineas,":",linea)
        num_texto=num_texto+1
print("\nLineas totales: ",num_lineas)
print("Lineas con texto: ",num_texto)            
print("Lineas vacias: ",num_vacio)  
arch2.close()
print("----------------------------------------------------------------------------------------------\n")


print("---------------5.-Eliminar simbolos de puntuacion y 6.mostrar palabras de todos los docs ordenadaments------------------\n")
carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre="Arfinal.txt"

carpeta_nombre1="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre1="Arfinal1.txt"


with open(carpeta_nombre+archivo_nombre,"r") as archi:
    texto=archi.read()
    print("\nLa palabras con sort del archivo 1 son:\n ")
    simbolos=["(",")",",",".",",","\","":"]
    for simbolo in simbolos:
        texto=texto.replace(simbolo," "+simbolo+" ")
        palabras_lista=texto.split()
        palabras_lista.sort()


    for palabra in palabras_lista:
        print(palabra)
print(palabras_lista)

with open(carpeta_nombre1+archivo_nombre1,"r") as archi1:
    texto=archi1.read()
    print("\nLa palabras con sort del archivo 2 son:\n ")
    simbolos=["(",")",",",".",",","\","":"]
    for simbolo in simbolos:
        texto=texto.replace(simbolo," "+simbolo+" ")
        palabras_lista=texto.split()
        palabras_lista.sort()


    for palabra in palabras_lista:
        print(palabra)
print(palabras_lista)
archi.close()
archi1.close()        
print("---------------------------------------------------------------------------------------------\n")

print("--------------------------------7.Mostrar cuantas palabras tiene cada doc----------------------------------------------\n")
carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre="Arfinal.txt"

carpeta_nombre1="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre1="Arfinal1.txt"

with open(carpeta_nombre+archivo_nombre,"r")as archiv:
    texto=archiv.read()

    palabras_lista=texto.split()

    for palabra in palabras_lista:
        tot=len(palabras_lista)   
print("Numero de palabras totales del archivo 1: ",tot)

with open(carpeta_nombre1+archivo_nombre1,"r")as archiv1:
    texto=archiv1.read()

    palabras_lista=texto.split()

    for palabra in palabras_lista:
        tot1=len(palabras_lista)   
print("\nNumero de palabras totales del archivo 2: ",tot1)
archiv.close()
archiv1.close()
print("---------------------------------------------------------------------------------------------\n")

print("--------------------------------8.-Unir ambos doc----------------------------------------------\n")
carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
carpeta_salida="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_salida="UNIR.txt"

archivos_lista=os.listdir(carpeta_nombre)

union=""

for archivo_nombre in archivos_lista:
    archivo=open(carpeta_nombre+archivo_nombre)
    texto=archivo.read()
    archivo.close()
    union+=texto

with open(carpeta_salida+archivo_salida,"w")as salida:
    salida.write(union)
    print("Archivo creado")

print("---------------------------------------------------------------------------------------------\n")

print("-------------9.Eliminar simbolos de puntuacion y 10.-mostrar doc nuevo de manera ordenada---------------------------------------\n")
carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre="UNIR.txt"


with open(carpeta_nombre+archivo_nombre,"r") as ar:
    texto=ar.read()
    print("\nLa palabras con sort del archivo nuevo son:\n ")
    simbolos=["(",")",",",".",",","\","":"]
    for simbolo in simbolos:
        texto=texto.replace(simbolo," "+simbolo+" ")
        palabras_lista=texto.split()
        palabras_lista.sort()

    for palabra in palabras_lista:
        print(palabra)
print(palabras_lista)
ar.close()

print("---------------------------------------------------------------------------------------------\n")

print("------------------------------11.Mostrar cuantas palabras tiene el nuevo doc-------------------------------------------\n")
carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre="UNIR.txt"

with open(carpeta_nombre+archivo_nombre,"r")as archive:
    texto=archive.read()

    palabras_lista=texto.split()

    for palabra in palabras_lista:
        total=len(palabras_lista)   
print("Numero de palabras totales del archivo nuevo: ",total)

print("---------------------------------------------------------------------------------------------\n")

print("------------------------------12.-Buscar una palabra e indicar si existe o no-----------------------------------------------\n")

carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"

archivo_nombre="UNIR.txt"

palabra=input("Ingresa la palabra a buscar en el documento: ")

with open(carpeta_nombre+archivo_nombre,"r") as archive1:
    texto=archive1.read()

if palabra in texto:
    print("\nLa palabra",palabra,"fue encontrada en el texto")

else:
    print("\nLa palabra",palabra,"no fue encontrada en el texto")
print("---------------------------------------------------------------------------------------------\n")
