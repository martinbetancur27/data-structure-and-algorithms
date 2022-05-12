#Programado por mi. Inventario de monedas guardado en un diccionario
#Añadi funcionalidades-> Repositorio de monedas dinamico (disminuye en las devueltas)
#Sin POO. Practicar Logica

def greedyChange(coins_set, cambio):

    devuelta = []
    cambio_a_descontar = cambio
    #Obtener el valor de las monedas en una lista.
    list_coins = list(coins_set.keys())
    #sort min -> max
    list_coins.sort()

    numero_billetes_entregar = 0
    indice_billete_mayor = len(list_coins)-1
    
    while cambio_a_descontar > 0 or indice_billete_mayor >= 0:

        if indice_billete_mayor < 0 and cambio_a_descontar > 0:
            #esta fraccion de codigo es por si no se puede devolver
            #Restaurar el repositorio de monedas
            for valor in devuelta:
                coins_set[valor] += 1
            return cambio, None
            
        valor_moneda = list_coins[indice_billete_mayor]
        cantidad_moneda = coins_set[valor_moneda]

        if valor_moneda <= cambio_a_descontar and cantidad_moneda > 0:
            devuelta.append(valor_moneda)
            coins_set[valor_moneda] -= 1
            numero_billetes_entregar +=1
            cambio_a_descontar -= valor_moneda
        else:
            indice_billete_mayor -= 1

    print("Inventario de Monedas", coins_set)

    return devuelta, numero_billetes_entregar


if __name__ == '__main__':

    #diccionario. Tiene la clave el valor de la moneda que es unico. En valor tendra la cantidad disponible
    coins_set = {1: 0, 5: 2, 10: 3, 20: 1}
    
    eleccion = 1

    while eleccion == 1:

        change = int(input("Ingresa el valor a devolver: "))
        devuelta, numero_billetes = greedyChange(coins_set, change)

        if numero_billetes != None:
            print('Entregaremos las siguientes monedas: ', devuelta, "\n"
            "Cantidad de billetes:", numero_billetes, "\n")
        else:
            print('No hay dinero suficiente. En una oficina RECLAMAR devolucion de', devuelta, "\n")
        
        eleccion = int(input("Ingresa 1 y ENTER para generar otra devolucion // Cualquier tecla y ENTER para SALIR: "))