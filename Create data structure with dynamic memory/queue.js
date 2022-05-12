class Node{
    constructor(value){
        this.value = value;
        this.next = null;
        // Next porque tambien se puede comportar como una linked list. 
                                    //De arriba hacia abajo
    }
}


class Queue{
    constructor(){
        //El elemento que esta en primera fila
        this.first = null;
        // el ultimo elemento
        this.last = null;

        this.length = 0;

        //CADA UNO DE ESTOS ELEMENTOS SERA UN NODO
    }

    peek(){
        //regresa el primer elemento

        return this.first;
    }

    enqueue(value){
        //Metodo para agregar un elemento al final

        const newNode = new Node(value);

        if(this.length == 0){
            // si esta vacia
            this.first = newNode;
            this.last = newNode;
        }
        else{
            // el .next lo envia atrtas
            this.last.next = newNode;
            this.last = newNode;
        }

        this.length++;
        return this;
    }

    dequeue(){
        // Eliminar elemento que esta de primero

        if(this.length > 0){
            if(this.length === 1){
                this.first = null;
                this.last = null;
            } else {
            this.first = this.first.next;
            }
            this.length--;
            return this;
        }
        else{
            return "No hay elementos para eliminar";
        }
    }
}

const queue = new Queue();