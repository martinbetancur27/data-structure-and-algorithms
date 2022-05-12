//const array = ["Fernando", "Esteban", "Camila", "Andrea"]

class Array{

    /*
    Para hacerlo funcionar con la sintaxis de for..of
    *[Symbol.iterator]() {
        let index = 0;
        while (index < this.length) {
          yield this.data[index++];
        }
      }
    ***************
    */
    constructor(){
        this.length = 0; //contar el ingreso de un valor
        this.data = {}; //Tipo objeto
    }

get(index){
    //Obtener un valor por medio del indice
    return this.data[index];
}

push(value){
    //Ingresar un valor al final del array
    this.data[this.length] = value;
    this.length ++;
    return this.length - 1
}

pop(){
    //Borrar el ultimo elemento del array

    const lastValue = this.data[this.length-1]; //Retornar el valor eliminado
    delete this.data[this.length-1]; //Delete, Keyword elimina el elemento.
    this.length --;
    return lastValue;
}

/* Mi solucion para el delete. Modularice el Delete.*/
delete(index){
    const deleteValue = this.data[index];
    
    //Coloca el valor que se desea eliminar en la ultima posicion.
    this.sendValuesLeft(index)

    delete this.data[this.length-1];
    this.length --;
    return deleteValue;
}

sendValuesLeft(index){
    //Metodo que envia cada valor desde el final una posicion a la izquierda.
    //Deja el ultimo valor igual al penultimo.
    while(index < this.length-1){
        this.data[index] = this.data[index+1];
        index ++;
    }
    
}

// Solucion del profesor para el delete
/*
delete(index){
    const item = this.data[index]
    this.shiftIndex(index);

    return item;

}
// Solucion del profesor para cambiar los indices
shiftIndex(index){

    for(let i=index; i < this.data[this.length-1]; i++){
        this.data[index] = this.data[index+1];
    }
    delete this.data[this.length-1];
    this.length --;
}
*/

//Tarea: Ingresar un valor al inicio.
unshift(value){
    if(this.length > 0){
    this.sendValuesRight(0)
    }
    this.data[0] = value;
    this.length ++;
    return this.data;
    
}

sendValuesRight(index){
    //Metodo que envia cada valor desde el index una posicion a la derecha.
    let newIndex = this.length;
    while(newIndex >= index){
        this.data[newIndex] = this.data[newIndex-1];
        newIndex --;
    }
}

//Tarea: Eliminar un valor al inicio.
shift(){

    /*if(this.length > 0){
    this.sendValuesLeft(0)
    
    delete this.data[this.length-1]
    this.length --;
    }
    else{
        delete this.data[0]
    }
    return this.data;*/

    return this.delete(0);
    
}
}

const array = new Array();