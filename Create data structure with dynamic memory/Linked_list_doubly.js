class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
      this.prev = null;
    }
  }

  class MyDoublyLinkedList {
    constructor(value) {
      this.head = {
        value: value,
        next: null,
        prev: null,
      };
      this.tail = this.head;
  
      this.length = 1;
    }
    append(value) {
        const newNode = new Node(value);
        newNode.prev = this.tail;
        this.tail.next = newNode;
        this.tail = newNode;
    
        this.length++;
    
        return this;
    }

    prepend(value) {
        const newNode = new Node(value);
    
        newNode.next = this.head;
        this.head.prev = newNode;
        this.head = newNode
        this.length++;
    
        return this;
    }

    insert(index, value){
        
        if (index === 0) {
          return this.prepend(value);
        }
    
        if (index >= this.length) {
          return this.append(value);
        }
    
        const newNode = new Node(value);
        const previousPointer = this.getTheIndex(index - 1);
        const holdingPointer = previousPointer.next;
        previousPointer.next = newNode;
        holdingPointer.prev = newNode;
        newNode.prev = previousPointer;
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
          
          this.tail = this.tail.prev;
          this.tail.next = null
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
          this.pop();
        }
        
        //Colocar el puntero en el nodo anterior al que se desea eliminar.
        const previousPointer = this.getTheIndex(index-1);
        
        //previousPointer.next = previousPointer.next.next;
        //previousPointer.prev.prev = previousPointer.prev;

        //Colocar el puntero en el nodo siguiente al que se desea eliminar.
        const holdingPointer = this.getTheIndex(index + 1);

        previousPointer.next = holdingPointer;
        holdingPointer.prev = previousPointer;
        
         this.length--;
    
         return this;
      }

  }
  
  let myDoublyLinkedList = new MyDoublyLinkedList(1);