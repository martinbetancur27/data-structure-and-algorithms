import time

class Queue:

    def __init__(self, SIZE):

        self.front = -1
        self.rear = -1
        self.values = [None]*SIZE
        self.SIZE = SIZE
        

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
    size = int(input("Ingrese el tamaño de la lista: "))
    queue = Queue(size)
    print("Lista creada:")
    print(queue.returnValues())
    time.sleep(2)

    salir = False
    opciones ={
        1: "enqueue()      - Ingresar",
        2: "dequeue()      - Eliminar",
        3: "peak()         - Mostrar primer numero",
        4: "size()         - Cantidad de numeros",
        5: "isEmpty()      - ¿Esta vacio?",
        6: "isFull()       - ¿Esta lleno?",
        7: "returnValues() - Retornar valores",
        8: "Salir"}

    while not salir:
        for key, value in opciones.items():
            print ("{:<5} {:<5}".format(key, value))
            
        opcion = int(input("Ingrese el numero el metodo: "))

        if opcion == 1:
            numero = (input("Ingresar numeros (separe por coma y sin espacio): "))
            numero += ","
            numero_enviar = ""
            for i in numero:
                if i != ",":
                    numero_enviar += i
                if (i == ","):
                    queue.enqueue(int(numero_enviar))
                    numero_enviar = ""
            time.sleep(2)
        elif opcion == 2:
            queue.dequeue()
            time.sleep(1)
        elif opcion == 3:
            queue.peek()
            time.sleep(1)
        elif opcion == 4:
            queue.size()
            time.sleep(1)
        elif opcion == 5:
            queue.isEmpty()
            time.sleep(1)
        elif opcion == 6:
            queue.isFull()
            time.sleep(1)
        elif opcion == 7:
            print("**********")
            print(queue.returnValues())
            print("**********")
            time.sleep(3)
        else:
            salir = True
        

if __name__ == '__main__':
    main()
    
