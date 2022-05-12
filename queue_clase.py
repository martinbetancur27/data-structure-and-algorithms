SIZE = 5
values =[None]*SIZE
front = -1
rear= -1

def enQueue(num):
    
    global front, rear, SIZE, values
    
    if(rear == SIZE-1):
        print(f'Queue lleno')
    else:
        if(front == -1):
            front = 0
        
        rear += 1
        values[rear] = num
        print("Se inserto el elemento", num)
    

def deQueue():
    global front, rear, SIZE, values

    if(front == -1):
        print("Nuestro Queue esta vacio\n")
    else:
        print("se elimino el valor\n", values[front])
        front += 1
        rear += 1
        if(front > rear):
            front = rear = -1



enQueue(1)
enQueue(2)
enQueue(3)
enQueue(4)
enQueue(5)
print(values)
deQueue()
deQueue()
deQueue()
deQueue()
deQueue()


'''ERRORES QUE EL PROFESOR EXPRESEO *****************************
cuando LLENO la lista y elimino un elemento E intento ingresar otro, no lo ingresa.
SE DEBE BORRAR TODOS LOS ELEMENTOS PARA INGRESAR NUEVOS. ERROR solo en la lista llena.
Profesor:
Esto pasa porque solo disminuimos el rear cuando lo vaciamos completamente. 
Es una fila que se tiene que vaciar para recibir nuevas personas

Lo mejore en 'queue_exercise.py' '''