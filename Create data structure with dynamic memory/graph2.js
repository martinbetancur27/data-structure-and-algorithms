class Graph{
    constructor(){
        this.nodes = 0; //lllevar la cuenta de los nodos que se agregan
        this.adjacentList = {};//lleva el nombre del metodo que vamos a utilizar 
                                //para representar. = al objeto
    }
    //los grafos tienen dos particularidades: vertices y bordes.
    //necesitamos agregar el grafo y despues los bordes que conectan


    //añadir nodo/ vertice
    //este nodo no tiene mas valores solo tenemos que interconectarlos
    //se representan como un array de arrays. Tenmos que agregar arrays por
    //cada nodo que vamos poniendo

    addVertex(node){
        this.adjacentList[node] = []; //ese nuevo array va ser parte del objeto
        this.nodes++; // contar los nodos

        //deberia de dar la lista completa cuando llamemos este metodo
    }


    //metodo que agrega los bordes/edges (conexiones)
    addEdge(node1, node2){
        //logica de conexion
        this.adjacentList[node1].push(node2); // Es un diccionario. utiliza la logica del diccionario para guardar. 
                                                //Clave-valor. El valor es un array
        //es un grafo no dirigido. Hacemos hacia el otro lado
        this.adjacentList[node2].push(node1);
    }
}

    let myGraph = new Graph();
    
    myGraph.addVertex("1");
    myGraph.addVertex("3");
    myGraph.addVertex("4");
    myGraph.addVertex("5");
    myGraph.addVertex("6");
    myGraph.addVertex("8");

    myGraph.addEdge("8","4");
    myGraph.addEdge("4","5");
    myGraph.addEdge("5","3");
    myGraph.addEdge("3","6");
    myGraph.addEdge("6","1");
    myGraph.addEdge("1","3");
    myGraph.addEdge("1","4");
    
// De un comentario
/*Hace ya un buen tiempo hice un curso de estructuras de datos en Python, 
y en unos de los ejercicios nos daban un grafo, en el cual nos pedían 
crear tres funciones las cuales retornaran un edge list, un adjacency list 
y un adjacency matrix. Me tomé el tiempo de pasar el código de Python a JS, aquí lo dejo*/
/*
class Node{
    constructor(value){
        this.value = value
        this.edges = []
    }
}
        
class Edge{
    constructor(nodeFrom, nodeTo){
        this.nodeFrom = nodeFrom
        this.nodeTo = nodeTo
    }
}

class Graph{
    constructor(nodes = [], edges = []){
        this.nodes = nodes
        this.edges = edges
    }
    insertNode(value){
        this.nodes.push(new Node(value))
    }
    insertEdge(fromValue, toValue){
        let fromFound = null
        let toFound = null

        this.nodes.forEach(node=>{
            if(fromValue === node.value){
                fromFound = node
            }
            if(toValue === node.value){
                toFound = node
            }
        })

        if(!fromFound){
            fromFound = new Node(fromValue)
            this.nodes.push(fromFound)
        }
        if(!toFound){
            toFound = new Node(toValue)
            this.nodes.push(toFound)
        }
        const newEdge = new Edge(fromFound, toFound)
        fromFound.edges.push(newEdge)
        toFound.edges.push(newEdge)
        this.edges.push(newEdge)
    }
    getEdgeList(){
        const edgeList = []
        for(let edge of this.edges){
            edgeList.push([edge.nodeFrom.value, edge.nodeTo.value])
        }
        return edgeList
    }
    getAdjacencyList(){
        const maxIndex = this.edges.length
        // Create a list with maxIndex +1 elements, all null
        const adjacencyList = Array.from(new Array(maxIndex+1), x => null)

        for(let edge of this.edges){
            if(adjacencyList[edge.nodeFrom.value]){
                adjacencyList[edge.nodeFrom.value].push(edge.nodeTo.value)
            }
            else{
                adjacencyList[edge.nodeFrom.value] = [edge.nodeTo.value]
            }
        }
        return adjacencyList
    }
    getAdjacencyMatrix(){
        const len = this.nodes.length + 1
        //Create a matrix of dimensions len x len, filled with zeros 
        const adjacencyMatrix = Array.from(new Array(len), x => new Array(len).fill(0))
        for(let edge of this.edges){
            adjacencyMatrix[edge.nodeFrom.value][edge.nodeTo.value] = 1
        }
        return adjacencyMatrix
    }
}
        const graph = new Graph()
        graph.insertEdge(1,2)
        graph.insertEdge(1,3)
        graph.insertEdge(1,4)
        graph.insertEdge(3,4)

        // Should be [[1, 2], [1, 3], [1, 4], [3, 4]]
        console.log(graph.getEdgeList())
        // Should be [ null, [ 2, 3, 4 ], null, [ 4 ], null ]
        console.log(graph.getAdjacencyList())
        // Should be [[0,0,0,0,0],[0,0,1,1,1],[0,0,0,0,0],[0,0,0,0,1],[0,0,0,0,0]]
        console.log(graph.getAdjacencyMatrix())
        */