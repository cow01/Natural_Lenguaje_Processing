'''Axel Hervey Cruz Baez'''
'''Oswaldo Carrillo Zepeda'''
'''Procesamiento del lenguaje natural'''

import re

carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\"

archivo_nombre="doc3.txt"

with open(carpeta_nombre + archivo_nombre, "r") as archivo:
    texto = archivo.read()

expresion_regular = re.compile(r"apuestas")

'''resultado_busqueda = expresion_regular.search(texto)
    print(resultado_busqueda.group(0))'''

resultados_busqueda = expresion_regular.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))
print("\n")

expresion_regular2 = re.compile(r"proc+")
resultado_busqueda = expresion_regular2.finditer(texto)
for resultado2 in resultados_busqueda:
    print(resultado2.group(0))