
#Martín Betancur Sánchez

'''Merge entendido de un comentario de la clase. Se realizaron modificaciones/ comentarios'''

def mergeSort(lista_):
    #dividir la lista en 2
    #lista izquierda = lista_i
    #lista derecha = lista_d
    #merge: compara y las une.
    
    if (len(lista_)>1):
        #Uso de los slices en Python.
        #Se hace uso de la logica propia de Python
        lista_i = mergeSort(lista_[:len(lista_)//2])
        lista_d = mergeSort(lista_[len(lista_)//2:])
        
        #retornar la union ya ordenada.
        return merge(lista_i, lista_d)
    
    return lista_
    

def merge(lista_i, lista_d):

    #Array donde se guardara la union de la division.
    union = []
    
    #Inicializar punteros para las dos listas que se recibieron
    i_index = 0
    d_index = 0

    #Recorre hasta que una de las dos lista se recorra en su totalidad
    while i_index < len(lista_i) and d_index < len(lista_d):

        #condicion que valida el numero menor.
        if lista_i[i_index] < lista_d[d_index]:
            union.append(lista_i[i_index])
            i_index += 1
        else:
            union.append(lista_d[d_index])
            d_index += 1

    #se pasa los numeros que faltan de la lista que no se recorrio completamente
    if i_index == len(lista_i):
        union.extend(lista_d[d_index:])
    else:
        union.extend(lista_i[i_index:])

    return union


if __name__ == '__main__':

    '''lista_ = [1, 1, 2, 2, 3, 3, 6, 8, 8, 9, 10, 10, 12, 15, 17, 17, 17, 
    19, 22, 23, 24, 25, 25, 25, 26, 28, 30, 30, 30, 31, 32, 32, 33, 34, 
    36, 38, 39, 41, 41, 42, 43, 43, 44, 44, 44, 44, 45, 45, 47, 48, 50, 
    52, 53, 54, 56, 57, 57, 57, 58, 59, 60, 60, 61, 64, 65, 65, 67, 67, 
    68, 69, 72, 72, 74, 74, 76, 77, 78, 79, 80, 82, 82, 82, 82, 86, 86, 
    87, 87, 87, 89, 90, 90, 94, 95, 98, 98, 98, 98, 99, 99, 100]'''

    lista_ = [3,2,10,1,11,78,4,15,85,6]

    print("Lista Inicial: ", lista_)
    print("Lista Final: ", mergeSort(lista_))