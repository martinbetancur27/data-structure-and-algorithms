
# Martín Betancur Sánchez

#Bubble Sort: hacer comparaciones de elementos adyacentes. Dos en dos.

import random


def entryDates():
    #Pedir el tamaño de la lista al usuario
    #llenar lista con numeros aleatorios del 0 al 100
    #retornar la lista

    sizeDates = int(input("Ingresa el tamaño de la lista: "))
    arrayNumbers = []

    for i in range(sizeDates):
        
        arrayNumbers.append(random.randint(0,100))

    print(f"Lista inicial:\n{arrayNumbers}")

    return arrayNumbers

    
def bubbleSort(arrayNumbers):
    #recibe una lista como parametro
    #ordena la lista de menor a mayor
    #muestra la lista ordenada

    #utilizamos for porque sabemos cual sera el fin. Numero finito
    for j in range(len(arrayNumbers)-1):
        contador = len(arrayNumbers)
        
        for i in range(len(arrayNumbers)-j-1): 
            #La segunda condición FOR disminuira un ciclo por cada ciclo de j completado
            #Con esto ya no se comparan los elementos ya ordenados a la derecha del arreglo, es decir, 
            #los elementos mayores. 
            
            if(arrayNumbers[i] > arrayNumbers[i+1]):
                #colocar mayor a la derecha.
                #si la siguiente  caracteristica no estuviera disponible en Python (asignar dos posiciones 
                #en una misma linea), necesitaria una variable auxiliar para 
                #guardar el valor y evitar perderlo. Ventaja de Python.
                arrayNumbers[i], arrayNumbers[i+1] = arrayNumbers[i+1], arrayNumbers[i]
                contador -= 1
            
        if contador == len(arrayNumbers):
            #Condicional para evaluar si el array esta ordenado. 
            #Evitar ciclos innecesarios del primer FOR

            #Mensaje que informa la cantidad de ciclos realizados
            print("Programa terminado. Itero: ",j,"veces")
            break
    
    print(f"Lista final:\n{arrayNumbers}")
    

if __name__ == '__main__':

    arrayNumbers = entryDates()
    bubbleSort(arrayNumbers)
    