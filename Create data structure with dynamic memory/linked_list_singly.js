/*1-- > 2-- > 3-- > 4-- > 5-- > null;

let singlyLinkedList = {
  head: {
    value: 1,
    next: {
      value: 2,
      next: {
        value: 3,
        next: {
          value: 4,
          next: null,
        },
      },
    },
  },
};*/

class Node {
  // crear los nodos nuevos y no tener que repetir
  //la esteuctura de codigo del constructor
  constructor(value) {
    this.value = value;
    this.next = null; //este sera el puntero del siguiente dato. Guarda la direccion de memoria 
  }
}


class MySinglyLinkedList {
  constructor(value) {
    this.head = {
      value: value,
      next: null,
    };
    this.tail = this.head;

    this.length = 1;
  }

  append(value){
    //ingresar un nodo al final
    const newNode = new Node(value);

    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;

    return this;
  }

  prepend(value) {
    const newNode = new Node(value);

    newNode.next = this.head;
    this.head = newNode;

    this.length++;

    return this;
  }

  // mi intento
  /*insert(index, value){
    const newNode = new Node(value);
    let first = {}
    let contador = 0;
    let tile = {}
    while (contador < this.length){
      if(contador < index){
      first = this.head.next;
    }
      else{
        tile = this.head.next;
      }
      contador ++
    }
    
    this.head = first;
    this.next = newNode;
    newNode.next = tile;

    this.length++;

    return this;
  }*/

  insert(index, value){
    //Insertar un nodo en cualquier indice existente.
    // Se utilizaran dos metodos. El actual y otro para encontrar el indice.

    if (index === 0) {
      return this.prepend(value);
    }

    if (index >= this.length) {
      return this.append(value);
    }
    
    const newNode = new Node(value);
    const firstPointer = this.getTheIndex(index - 1);
    const holdingPointer = firstPointer.next;
    firstPointer.next = newNode;
    newNode.next = holdingPointer;

    this.length++;
    return this;
  }

  getTheIndex(index) {
    let counter = 0;
    let currentNode = this.head;

    while (counter !== index) {
      currentNode = currentNode.next;
      counter++;
    }

    return currentNode;
  }

  pop(){
    const firstPointer = this.getTheIndex(index - 1);
    firstPointer.next = null;
    
    this.tail = firstPointer;
    this.length--;

    return this;
  }

  remove(index){

    if( !this.getTheIndex(index) ){
      console.log("Este nodo no existe.");
      }

    if (index === 0){
        this.head = this.head.next;
        this.length--;
        return this;
    }

    if(index  === this.length - 1){
      const firstPointer = this.getTheIndex(index - 1);
      firstPointer.next = null;
      
      this.tail = firstPointer;
      this.length--;

      return this;
    }
    
    const previousPointer = this.getTheIndex(index - 1);
     const holdingPointer = this.getTheIndex(index + 1);

     previousPointer.next = holdingPointer;
        
     this.length--;

     return this;
  }

/********* Pagina web Externa **********/
  /*removeFirst(){

    if(!this.head){
        return;
      }

      this.head = this.head.next;
      return this.head;
      }

      removeLast(){
        if(!this.head){
          return null;
      }
      // if only one node in the list
      if(!this.head.next){
          this.head = null;
          return;
      }
    let previous = this.head;
    let tail = this.head.next;
    
    while(tail.next !== null){
        previous = tail;
        tail = tail.next;
    }
    
    previous.next = null;
    return this.head;

}

getAt(index){
  let counter = 0;
        let node = this.head;
        while (node) {
            if (counter === index) {
               return node;
            }
            counter++;
            node = node.next;
        }
        return null;
    }

  remove_(index){
    // when list is empty i.e. head = null
    if (!this.head) {
      this.head = new Node(data);
      return;
      }
    // node needs to be deleted from the front of the list i.e. before the head.
    if (index === 0) {
        this.head = this.head.next;
        return;
    }
    // else, use getAt() to find the previous node.
    const previous = this.getAt(index - 1);
    
    if (!previous || !previous.next) {
        return;
    }
    
    previous.next = previous.next.next;     
    return this.head
  }

  removeAll(){
    this.head = null;
  }
*/
/***************** Pagina web Externa ****************/



}

let myLinkedList = new MySinglyLinkedList(1);

myLinkedList.append(1);
myLinkedList.append(2);
myLinkedList.append(3);
myLinkedList.append(4);

myLinkedList.insert(4, 5);

//este nodo es el que vamos a colocar al final de nuestra lista.