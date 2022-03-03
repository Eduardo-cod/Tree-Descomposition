# Tree-Descomposition - Katsikarelis
    • Q1: Cola FIFO que almacena todos los vértices de grado 1 del grafo de entrada G.
    • Q2: Cola FIFO que almacena todos los vértices de grado 2 del grafo de entrada G.
    • Dequeue(Q): Esta función extrae el vértice en turno de la cola Q.
    • Enqueue(Q, v): Esta función inserta el vértice v en la cola Q. 
    • B: Lista enlazada para almacenar objetos tipo 1. Esta lista inicialmente está vacía.
    • C: Lista enlazada para almacenar objetos tipo 2. Esta lista inicialmente está vacía.
    • List-Insert(A, x): Esta función inserta el objeto con dirección x en la lista A.
    • Allocate-Register-Type-: Esta función crea un objeto tipo  cuya dirección es x.
    • Objeto tipo 1. Este objeto tiene cinco atributos:
        ◦ x.vertex1, x.vertex2, x.vertex3: Almacenan los tres vértices de la bolsa. Para bolsas con dos vértices, el último es nil.
        ◦ x.bag-id: Almacena un identificador secuencial del instante en que se formó la bolsa almacenada en el objeto con dirección x.
        ◦ x.parent: Para la bolsa almacenada en el objeto con dirección x, apunta al objeto con dirección y, donde se almacena la bolsa padre.
    • Objeto tipo 2. Este objeto tiene tres atributos:
        ◦ x.vertex1, x.vertex2: Almacenan los dos vértices de una arista de la bolsa almacenada en el objeto con dirección x. 
        ◦ x.bag-address: Almacena la dirección  del objeto donde se almacena la bolsa, a partir del cual se generó la arista (x.vertex1, x.vertex2).
    • v.adj-list: Apuntador a la lista de adyacencias del vértice v.
    • v.deg: Atributo que indica el grado del vértice v. Se inicializa con la información de G. 
    • v.bag-pointer: Apuntador que, para cada vértice v en G, indica la dirección del objeto donde se encuentra su bolsa.
    • v.bagged: Bandera que es verdadera si ya se procesó el vértice v y se construyó su bolsa. Esta bandera es falsa en caso contrario.
    • Compute-Degree(i): Calcula el grado del vértice i.
    • Extract-Single(v): Función que extrae de la lista v.adj-list al único vértice u tal que u.bagged = false.
    • Extract-Pair(v): Función que extrae de la lista v.adj-list a los únicos dos vértices u, w tal que    u.bagged = false y w.bagged = false.

Tree-Decomposition(G)

     for i <- 1 to n  do
           Compute-Degree(i)
           i.bagged <- false
           i.bag-pointer <- nil
     end
     bag-counter  0
     while  (Q1 != empty) and (Q2 1= empty)  do
           if  Q1 != empty  then
                 Two-Bag(G)
           else
                  Three-Bag(G)
           end
     end
     Sort x.vertex1 and x.vertex2 in each object x of C 
     Use Counting-Sort to sort all the objects of C according to vertex2.
     Use Counting-Sort to sort all the objects of C according to vertex1.
     for i <- 1 to |C| -1 do
           if  i.vertex1 = (i+1).vertex1 and i.vertex2 (i+1).vertex2  then
                 if  i.bag-address.bag-id > (i1).bag-address.bag-id  then
                       (i+1).bag-address.parent <- i.bag-address
                 else
                       i.bag-address.parent <- (i+1).bag-address
                 end
           end
     end


Two_Bag
     v <- Dequeue(Q1)
     if bagged(v) = false then
           bag-counter <- bag-counter + 1                                     Creación de la bolsa para el vértice v
           x  <- Allocate Object-Type-1
           x.vertex1 <- v
           x.vertex2 <- Extract-Single(v)
           x.vertex3 <- empty
           x.bag-id <- bag-counter
           x.parent <- nil
           List-Insert(B, x)
           x.vertex1.bag-pointer <- x
           x.vertex1.bagged <- true
           if  deg(x.vertex2) = 1  then                             Condición de paro (al encontrar el último clique de tamaño 2)
                 x.vertex2.bag-pointer <- x
                 x.vertex2.bagged <- true
                 for each  u ∈ x.vertex2.adj-list  do                                 Pegado de bolsas de tamaño 2 para x.vertex2
                       if (u.bagged = true) and (u.bag-pointer.vertex3 = empty) and (u.bag-pointer.parent = nil)  then
                             u.bag-pointer.parent. <- x
                       end
                 end
           else                                                                                        Actualización de vecinos
                 deg(x.vertex2) <- deg(x.vertex2)  1
                 if  deg(x.vertex2) = 2  then  Enqueue(Q2, x.vertex2)  end
                 if  deg(x.vertex2) = 1  then  Enqueue(Q1, x.vertex2)  end
           end
           for each  u ∈ x.vertex1.adj-list  do                                        Pegado de bolsas de tamaño 2 para  x.vertex1
                 if (u.bagged = true) and (u.bag-pointer.vertex3 = empty) and (u.bag-pointer.parent = nil)  then
                       u.bag-pointer.parent <- x
                 end
           end
           return
     end

Three-Bag
     v.<- Dequeue(Q2)
     if  bagged(v) = false  then
           bag-counter <- bag-counter + 1                                         Creación de la bolsa para el vértice v
           x  <- Allocate-Object-Type-1                                                 
           x.vertex1 <- v
           x.vertex2, x.vertex3 <- Extract-Pair(v)
           x.bag-id <- bag-counter
           x.parent <- nil
           List-Insert(B, x)
           x.vertex1.bag-pointer <- x
           x.vertex1.bagged <- true
           y  <- Allocate-Object-Type-2                                          Creación de objetos para las aristas de la bolsa en x
           (y.vertex1, y.vertex2, y.bag-address) <- (x.vertex1, x.vertex2, x)
           List-Insert(C, y))
           y  <- Allocate-Object -Type-2
           (y.vertex1, y.vertex2, y.bag-address) <- (x.vertex2, x.vertex3, x)
           List-Insert(C, y))
           y  <- Allocate-Object -Type-2
           (y.vertex1, y.vertex2, y.bag-address) <- (x.vertex3, x.vertex1, x)
           List-Insert(C, y))
           if  (x.vertex2, x.vertex3) ∈ E  then                                               Actualización de vecinos
                 x.vertex2.deg <- x.vertex2.deg - 1
                 x.vertex3.deg <- x.vertex3.deg - 1
                 if  x.vertex2.deg = 2  then  Enqueue(Q2, x.vertex2)  end
                 if  x.vertex2.deg = 1  then  Enqueue(Q1, x.vertex2)  end
                 if  x.vertex3.deg = 2  then  Enqueue(Q2, x.vertex3)  end
                 if  x.vertex3.deg = 1  then  Enqueue(Q1, x.vertex3)  end
           else
                 List-Insert(x.vertex2.adj-list, x.vertex3)
                 List-Insert(x.vertex3.adj-list, x.vertex2)
           end
           for each  u ∈ adj-list(x.vertex1)  do                            Pegado de bolsas de tamaño 2 para  x.vertex1
                 if (u.bagged = true) and (u.bag-pointer.vertex3 = empty) and (u.bag-pointer.parent) = nil)  then
                       u.bag-pointer.parent <- x
                 end
           end
           return
     end
