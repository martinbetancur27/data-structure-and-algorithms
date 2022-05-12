
#Martín Betancur Sánchez

#Solucion que entendi en:
#https://www.youtube.com/watch?v=3_vD60LQ8Ec

def partirLista(lista_):
    
    pivot = lista_[0] #el primer numero de la lista sera el que comparara a todos los demas
    lista_i = [] #LISTA IZQUIERDA. tendra los numeros menores al pivote
    lista_d = [] #LISTA DERECHA. tendra los numeros mayores al pivote

    for i in range(1, (len(lista_))): #arranca en 1 porque el 0 es el pivote
        if(lista_[i] < pivot):
            #el append permite ingresar al final de la lista.
            lista_i.append(lista_[i])
        else:
            lista_d.append(lista_[i])

    #Probar la particion
    #print("lista i: ", lista_i)
    #print("lista d: ", lista_d)

    return lista_i, pivot, lista_d

def quickSort(lista_):
    
    #Caso base para detener la recursion
    if(len(lista_)<2):
        return lista_
    
    #el metodo partirLista() retorna 3 valores
    lista_i, pivot, lista_d = partirLista(lista_)

    #el pivot sera el numero ordenado. Las listas quedaran con un solo numero que como base ya estara ordenado.
    return quickSort(lista_i) + [pivot] + quickSort(lista_d)


if __name__ == '__main__':

    '''lista_ = [1, 1, 2, 2, 3, 3, 6, 8, 8, 9, 10, 10, 12, 15, 17, 17, 17, 
    19, 22, 23, 24, 25, 25, 25, 26, 28, 30, 30, 30, 31, 32, 32, 33, 34, 
    36, 38, 39, 41, 41, 42, 43, 43, 44, 44, 44, 44, 45, 45, 47, 48, 50, 
    52, 53, 54, 56, 57, 57, 57, 58, 59, 60, 60, 61, 64, 65, 65, 67, 67, 
    68, 69, 72, 72, 74, 74, 76, 77, 78, 79, 80, 82, 82, 82, 82, 86, 86, 
    87, 87, 87, 89, 90, 90, 94, 95, 98, 98, 98, 98, 99, 99, 100]'''

    
    lista_ = [3,2,2,10,1,11,78,4,15,85,6]

    print("Lista inicial:", lista_)
    lista_ = quickSort(lista_)
    print("Lista final:", lista_)