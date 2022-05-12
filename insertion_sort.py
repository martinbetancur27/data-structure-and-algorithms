
#Martín Betancur Sánchez

#************ ALGORITMO DE LA CLASE CON MODIFICACIONES Y COMETARIOS PROPIOS **********

'''recorremos nuestro set de datos posición por posición y comparamos el 
número con los valores anteriores, en caso de ser menor, lo colocamos en 
su posición indicada para ordenar de menor a mayor.'''

#   O(n2) Eficiente para datos pequeños.

def insertionSort(arrayNumbers, sizeArrayNumbers):
        
    for i in range(1,sizeArrayNumbers):
        
        currentVal = arrayNumbers[i]
        j = i-1
        
        while j >= 0 and arrayNumbers[j] > currentVal: # "arr[j] > currentVal" Esta condicion es porque el lado izquierdo es el lado organizado.
                                                #la logica es ordenar el lado izquierdo. Si "arr[j]" es menor la condicion se detiene
                                                # y en el espacio donde se detuvo se asigna currentVal.
            
            #la siguiente linea copia los valores un indice a la derecha. El valor sobreescrito en el desplazamiento es 
            #el currentval, por eso se guardo en esa variable auxiliar.
            arrayNumbers[j+1] = arrayNumbers[j]
            #puntero que indica hasta que indice a la izquierda se debe guardar el valor menor.
            j -= 1

        #Si la condicion del while no se cumple continua en la misma posicion. En caso de que la condicion del
        #while se cumpla al menor una vez sera movido al lado izquierdo donde indique el puntero j
        arrayNumbers[j+1] = currentVal
    
if __name__ == '__main__':

    arrayNumbers = [6,4,3,11,10,1,100,200,65,87,85,56,99,2000,648,2,7]

    sizeArrayNumbers = len(arrayNumbers)
    print("Array Inicial", arrayNumbers)
    insertionSort(arrayNumbers, sizeArrayNumbers)
    print("\nArray Final", arrayNumbers)
    