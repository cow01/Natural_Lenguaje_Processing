'''Axel Hervey Cruz Baez'''
'''Oswaldo Carrillo Zepeda'''
'''Procesamiento del lenguaje natural'''

import re

carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre="UNIR.txt"

with open(carpeta_nombre+archivo_nombre) as archivo:
    texto.archivo.read()
expre_reg=re.compile(r"CPU")

resultados_busqueda=expre_reg.finditer(texto)
for resultado in resultados_busqueda:
    print(resultado.group(0))