'''
PROBLEMA
Dado un numero, encontrar dos enteros que sumados den el objetivo. Utilizar un solo for. Retornar los indices

ISSUE
Given a number, find two integers that add up to the goal. Use a single for. return the indices
'''

#### Mi primera solucion. Logica solo para positivos. Solucion ingenua
#My solution. Logic only for positives. naive solution

number = int(input("Enter positive number: "))
numbers_list = [2, 5, 7, 9, 4, 54, 12]

final = number - 1
start = 1
message = "Unsuccessfully"

for i in range(0, number):
    
    if(start in numbers_list and final in numbers_list):
        print(numbers_list)
        print("found: " + str(start) + " + " + str(final) + " = " + str(number))
        print("Indexes: [" + str(numbers_list.index(start)) + ", " + str(numbers_list.index(final)) + "]")
        message = "successfully"
        break
    start += 1
    final -= 1

print(message)


#Improved logic for negatives with the algorithm I found on the internet

number = int(input("enter number: "))
lista = [2, 5, 7, -2, -1, 9, 4, 54, 12, -3]
message = "Unsuccessfully"

for i in range(0, len(lista)):
    value = number - lista[i]
    #restar valor. El numero de la resta, si se le suma el valor que resto, dara el objetivo.
    #subtract value. The number of the subtraction, if the value that remains is added, will give the objective.
    if(value in lista):
        print(lista)
        print("found: " + str(lista[i]) + " and " + str(value) + " = " + str(number))
        print("Indexes: [" + str(i) + ", " + str(lista.index(value)) + "]")
        message = "successfully"
        break

print(message)

#################### EXTRACTED FROM THE INTERNET.
#I don't remember the source
#It makes use of enumarate. It is used to mark the index.

'''def two_sum2(list_num, target):
    for index, item in enumerate(list_num):
        if (target-item in list_num) and (target-item != item):
            print('found one')
            return [index, list_num.index(target-item) ]
    return 'not found'
            
dataset = [-2, 9, 4, -1, 10, 3, 39, 12, 1, 4, 5, 6, -9, -3, -8]
print(two_sum2(dataset, -3))'''