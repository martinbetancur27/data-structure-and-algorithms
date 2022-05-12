
#Martín Betancur Sánchez

'''Tarea puesta en clase:
implementa un algoritmo de ordenamiento 
que sea capaz de ordenar de mayor a menor el set de datos dado'''


'''Selection Sort: Buscar el numero mayor de la lista y colocarlo en la primer indice, asi sucesivamente'''

#Definicion de Wikipedia
'''Buscar el mínimo elemento de la lista
Intercambiarlo con el primero
Buscar el siguiente mínimo en el resto de la lista
Intercambiarlo con el segundo'''

#Libreria para leer un documento del computador
from asyncore import write
import os 
FILE_PATH=os.path.dirname(__file__)

def read():
#Leer un .txt e ingresar sus valores en una lista. 
# Imprimir la lista
    
    numbers = []

    with open(f"{FILE_PATH}/numbers.txt", "r", encoding="utf-8") as f: 
        for line in f:
            numbers.append(int(line))

    print("Documento leido")

def write(numbers):
    #Colocar los valores de la lista recibida en un .txt y guardarlo en el computador.

    size = len(numbers)
    #con "w" va a sobreescribir en el archivo
    #Se crea documento "selection_sort.txt"
    with open("./selection_sort.txt", "w", encoding="utf-8") as f:

        for i in range(0, size):
            f.write(str(numbers[i]))
            if(i < size-1): #evitar un espacio al final.
                f.write("\n")
    
    print("Documento creado")

def selectionSort(numbers):
    n = len(numbers)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    print("Ordenamiento realizado")
    

if __name__ == '__main__':
    numbers = read()
    selectionSort(numbers)
    write(numbers)
    