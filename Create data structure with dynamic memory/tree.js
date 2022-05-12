//LOGICA. Conocido como binary tree balanceado.
//los números que van en aumentos están en el lado derecho. 
//Los números que van decrementando están en la izquierda. 
//      10
//   4     20
// 2  8  17  170

class Node {
    constructor(value) {
      this.left = null;
      this.right = null;
      this.value = value;
    }
    }
  
class BinarySearchTree {
    constructor() {
      this.root = null;
    }

    insert(value) {
      const newNode = new Node(value);
      if (this.root === null) {
        this.root = newNode;
      } else {
        let currentNode = this.root;

        while (true) { //cuando el tamaño es incierto pero el fin se conoce, 
                        //un true en el While es perfecto
          if (value < currentNode.value) {
            if (!currentNode.left) {
              currentNode.left = newNode;
              return this;
            }
            currentNode = currentNode.left;
          } else {
            if (!currentNode.right) {
              currentNode.right = newNode;
              return this;
            }
            currentNode = currentNode.right;
          }
        }
      }
    }
    
    //Mi implementacion.
    //Logica = si le paso un numero debera regresar el nodo en el que existe y con hijos
    search(value){
      
      let currentNode = this.root; //Tomar el puntero de la raiz

      while (currentNode != null){ //Cuando se llega al fin el puntero quedara con null
        if(currentNode.value === value){ // Validar que el valor del nodo sea igual al buscado
          return currentNode; // Retornar el nodo encontrado y salir de la funcion

        }else{ //Sino es igual al buscado ejecutara esta logica donde tomara la direccion
        if (value < currentNode.value){ 
          currentNode = currentNode.left; // Ir al puntero del nodo izquierdo
        }else{
          currentNode = currentNode.right; // Ir al puntero del nodo derecho
        }
        }
      } 
      return "No se encontro"; //el while valido un null, por lo tanto no se encontro.

    }

    //Mi implementacion: Search con logica recursiva.
    //Divide y venceras
    searchR(value){
      let currentNode = this.root;
      return this.recursion(value, currentNode);
    }

    recursion(value, pointer){
      if(pointer === null){
        return "No se encontro";
      }
      if(pointer.value === value){
        return pointer;
      }
      //Se aplica la recursion
      if(value < pointer.value){
        return this.recursion(value, pointer.left);
      }
      else{
        return this.recursion(value, pointer.right);
      }
    }
}
  
  const tree = new BinarySearchTree();

  // Ingreso de datos
  tree.insert(10);
  tree.insert(4);
  tree.insert(20);
  tree.insert(2);
  tree.insert(8);
  tree.insert(17);
  tree.insert(170);
  tree.searchR(10);