class Node{
    constructor(value){
        this.value = value;

        // Next porque tambien se puede comportar como una linked list. De arriba hacia abajo
        this.next = null;
    }
}


class Stack{
    constructor(){
        //El elemento que esta hasta arriba
        this.top = null;
        // Elmento que esta en la parte de abajo. Primer elemento
        this.bottom = null;
        //Lognitud del stack
        this.length = 0;

        //CADA UNO DE ESTOS ELEMENTOS SERA UN NODO
    }
    // Mostrar el ultimo elemento ingresado
    peek(){
        return this.top;
    }
    //Agregar elemento al final
    push(value){
        const newNode = new Node(value);
        //cuando tenemos métodos que agregan cosas tenemos que validar las cosas 
        //como por ejemplo que no esté vacía
        if(this.length === 0){
            this.top = newNode;
            this.bottom = newNode;
        }else{
        //no podemos dejar elementos sin pointer. en la variable holdingPointer mantenemos el punter
        // el elemento del top dejara de ser el top y no podemos decirle al nuevo que es top solamente.
        // No hay que perder los elementos de la memoria. El antiguo top quedara en esa constante
        const holdingPointer = this.top;  
        this.top = newNode;
        // this.top.next: es el que esta debajo del top     
        this.top.next = holdingPointer;        
    }
        this.length++;

        return this;
    }

    //Eliminar el ultimo elemento
    pop(){
        //Mi solucion
        /*if(this.length>0){
            if(this.length == 1){
                this.top = null;
                this.bottom = null;
            }
            else{
            this.top = this.top.next;
            }
        }
        this.length--;
        return this;*/

        //Solucion clase
        if (!this.top) {
            return null;
          }
          if (this.top === this.bottom) {
            this.bottom = null;
          }
          this.top = this.top.next;
          this.length--;
      
          return this;
    }

}

const stack = new Stack();

