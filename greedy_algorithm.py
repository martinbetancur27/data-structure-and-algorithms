'''Simulacion de un cajero. Devolver la minima cantidad de billetes.
greedy_algorithm_ATM.py En la carpeta 'algorithms - my practice' se encuentra
realizado con el repositorio de monedas dinamico
'''


#Esta funcion es de un comentario de clase. Logica de recursion
def greedy_change(coins_set, change, coins):

    for i in range(len(coins_set)):
        if change == 0:
            
            return coins
        
        if change < max(coins_set) and len(coins_set) > 1:
            coins_set.remove(max(coins_set))
        
        if change >= max(coins_set):
            coins.append(max(coins_set))
            return greedy_change(coins_set, change - max(coins_set), coins)

#Programado por mi. Hacerlo con iteracion
def greedyChangeWhile(coins_set, change):
    devuelta = []
    numero_billetes = 0
    while change > 0 and len(coins_set) > 0:
        billete_maximo = max(coins_set)
        if billete_maximo <= change:
            devuelta.append(billete_maximo)
            numero_billetes +=1
            change -= billete_maximo
        else:
            coins_set.remove(billete_maximo)

    return devuelta, numero_billetes


if __name__ == '__main__':

    change = int(input("Ingresa el valor a devolver: "))
    
    #print(f'Se devolveran {change} pesos de vuelto\n')
    coins_set = [1, 5 ,10, 20]
    
    coins = []
    print('(Recursion) Entregaremos las siguientes monedas: ', greedy_change(coins_set, change, coins))

    coins_set = [1, 5 ,10, 20]
    devuelta, numero_billetes = greedyChangeWhile(coins_set, change)
    print('(WHILE) Entregaremos las siguientes monedas: ', devuelta, "\n"
    "Cantidad de billetes", numero_billetes)
