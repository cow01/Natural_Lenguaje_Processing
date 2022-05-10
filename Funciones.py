'''Axel Hervey Cruz Baez'''
'''Oswaldo Carrillo Zepeda'''

import nltk

carpeta_nombre="C:\\Users\\axelb\\Desktop\\nlp\\Docs\\"
archivo_nombre="Arfinal.txt"

with open(carpeta_nombre+archivo_nombre,"r") as archivo:
    texto=archivo.read()
tokens=nltk.word_tokenize(texto,"spanish")

texto_nltk=nltk.Text(tokens)
palabra=input("Escribe la palabra a buscar: ")

texto_nltk.similar(palabra)
tokens=nltk.word_tokenize(texto,"spanish") 
print("\nFuncion collocations\n") 
texto_nltk=nltk.Text(tokens)  
texto_nltk.collocations() 
print() 

distri=nltk.FreqDist(texto_nltk)
distri.plot(20)
print("Funcion de mas comunes en base a freqdist\n")
lista=distri.most_common() 
print(lista)
