class HashTable{
    constructor(size){
        this.data = new Array(size);
    }
    hashMethod(key){
        //Hash Function. metodo que crea el hash.
        let hash = 0;
        for(let i = 0; i < key.length;i++){
            hash = (hash + key.charCodeAt(i)*i) % this.data.length;
        }
        return hash;
    }

    /*set(key, value){
        //el hash se va a convertir en el address donde vamos
        //a guardar el valor
        const address = this.hashMethod(key);

        //validamos si el address ya existe.
        //en caso de que no exista generamos un nuevo array.
        if(!this.data[address]){
            //creamos el nuevo array
            this.data[address] = [];
        }
        // si ya existe (hay un valor ahi), le agregamos el key value como 
        //otro array lo que queremos es no borrar los valores que ya estan.
        //si ya existe debemos evitar una colision, evitar
        //que sobreescriba lo que hay.
        //Lo agregamos de tal forma que tengamos dos keys y dos values adentro
        //de un bucket, no perder info
        this.data[address].push([key, value]);
        //con el push le decimos que no sobreescriba. Le decimos agregue otro 
        //array a ese bucket

        return this.data;
    }*/

    get(key){
        const address = this.hashMethod(key);
        const currentBucket = this.data[address] 
        //currentBucket: bucket en el que estamos en ese momento. Address donde
        //se encuentra nuestra info. [address] es como pasarle el indice donde
        //se encuentra el valor. Regresa el valor de ese indice.
        if(currentBucket){
        //verificar que exista el bucket
            for(let i=0; i < currentBucket.length; i ++){
                if(currentBucket[i][0] === key){
                // i es cada una de las listas. [0] es el key
                //validamos porque es como si fuera un array de arrays (lista de listas)
                    return currentBucket[i][1];
                    //[0] donde guarda el key
                    //[1] donde guarda el valor
                }
            }
        }
        //si el key enviado no existe
        return undefined;
    }
    //Podria modularizar la obtencion del key pero JS no permite metodos privados
    /*getKey(){

    }*/
    //Eliminar un elemento con el key. Se elimina con el value.
    remove(key){
        const address = this.hashMethod(key);
        const currentBucket = this.data[address];

        if(currentBucket){
            for(let i=0; i < currentBucket.length; i ++){
                if(currentBucket[i][0] === key){
                // i es cada una de las listas. [0] es el key
                //validamos porque es como si fuera un array de arrays (lista de listas)
                    if(currentBucket.length > 0){
                        for (let j=i; j <  currentBucket.length; i ++){
                        currentBucket[j] = currentBucket[j+1];
                    }
                    const valueDelete = currentBucket[currentBucket.length-1][1];
                    delete currentBucket[currentBucket.length-1];
                    return valueDelete;
                }
                    else{
                        const valueDelete = currentBucket[i][1];
                        delete currentBucket[0];
                        return valueDelete;
                }                    
                }
            }
        }
    }
    //obtener todos los keys
    getAllKeys() {
        const keys = [];
        for (let i = 0; i < this.data.length; i++) {
          if (this.data[i]) {
            for (let j = 0; j < this.data[i].length; j++) {
              keys.push(this.data[i][j][0]);
            }
          }
        }
        return keys;
      }

    remove(key) {
        const address = this.hashMethod(key);
        const currentBucket = this.data[address];
        if (currentBucket) {
          for (let i = 0; i < currentBucket.length; i++) {
            if (currentBucket[i][0] === key) {
              const deletedValue = this.data[address][i];
              this.data[address].splice(i, 1);
              return deletedValue;
            }
          }
        }
        return undefined;
    }


    //De comentario. Metodo para sobreescribir sobre una clave ya existente.
    set(key, value) {
        const address = this.hashMethod(key);
        if (!this.data[address]) {
          this.data[address] = [];
        }
        if (this.data[address].find((element) => element[0] === key)) {
          for (let i = 0; i < this.data[address].length; i += 1) {
            if (this.data[address][i][0] === key) {
              this.data[address][i][1] = value;
            }
          }
        } else {
          this.data[address].push([key, value]);
        }
        return this.data;
      }
}

const myHashTable = new HashTable(50);
// definimos 50 budgets de espacio para ver mas claro el ejemplo