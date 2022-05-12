'''ERRORES DE LA CLASE // INTENCIONALES // *****************************

************* Lo mejore en hacer el QUEUE DINAMICO (AUMENTAR Y DISMINUIR)
                y en añadirle nuevos metodos
'''

class Queue:

    def __init__(self, list):

        self.front = -1
        self.rear = -1
        self.values = list
        self.SIZE = len(self.values)
        

    def enqueue(self, num):
    
        if(self.rear == self.SIZE-1):
            print(f'Queue lleno')
        else:
            if(self.front == -1):
                self.front = 0
        
            self.rear += 1
            self.values[self.rear] = num
            print("Se inserto el elemento", num)


    def dequeue(self):

        if(self.front == -1):
            print("Nuestro Queue esta vacio")
        else:
            print("se elimino el valor", self.values[self.front])
            #este es el codigo que me permite tener una lista dinamica
            for i in range(self.rear):
                self.values[i] = self.values[i+1]
                
            self.values[self.rear] = None
            self.rear -= 1
            #este es el codigo que me permite tener una lista dinamica
            if(self.front > self.rear):
                self.front = self.rear = -1


    def peek(self):
        
        if(self.rear == -1):
            print("Nuestro Queue esta vacio")     
        else:
            print("El primer elemento es:", self.values[self.front])
               
    
    def size(self):
        
        if(self.front == -1):
            print("Nuestro Queue esta vacio")
        else:
            print("El numero de elementos es:", (self.rear-self.front)+1)
            

    def isEmpty(self):

        if(self.rear == -1):
            print("Nuestro Queue esta vacio")
            return True
        else:
            print("Nuestro Queue no esta vacio")
            return False


    def isFull(self):

        if(self.front == 0 and self.rear == self.SIZE-1):
            print("Queue esta lleno")
            return True
        else:
            print("Nuestro Queue no esta lleno")
            return False


    def returnValues(self):

        #No es un metodo propio de Queue. Se utiliza para retornar la lista

        return self.values

def main():

#Especificar el tamaño de la lista
    values =[None]*5
#Crear objeto que instancia la clase Queue
    queue = Queue(values)



#********************** PRUEBAS *************
    print("PRIMERA PRUEBA\n")

    print("enqueue()")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print("peak()")
    queue.peek()

    print("size()")
    queue.size()

    print("isEmpty()")
    queue.isEmpty()

    print("isFull()")
    queue.isFull()

    print("returnValues()")
    print(queue.returnValues())

    print("dequeue() (5)")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print("peak()")
    queue.peek()

    print("size()")
    queue.size()

    print("isEmpty()")
    queue.isEmpty()

    print("isFull()")
    queue.isFull()

    print("returnValues()")
    print(queue.returnValues())

    print("\n******** SEGUNDA PRUEBA - DINAMICA ********\n")
    
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.returnValues())
    queue.dequeue()
    queue.dequeue()
    print(queue.returnValues())
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue.returnValues())
    queue.dequeue()
    print(queue.returnValues())

    
    
    #Prueba clasica
    '''queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()'''

#********************** PRUEBAS *************


if __name__ == '__main__':
    main()
    
