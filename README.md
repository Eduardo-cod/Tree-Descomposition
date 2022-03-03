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
    1. for i 1 to n  do
    2.       Compute-Degree(i)
    3.       i.bagged  false
    4.       i.bag-pointer  nil
    5. end
    6. bag-counter  0
    7. while  Q1      Q2    do
    8.       if  Q1    then
    9.             Two-Bag(G)
    10.       else
    11.              Three-Bag(G)
    12.       end
    13. end
    14. Sort x.vertex1 and x.vertex2 in each object x of C 
    15. Use Counting-Sort to sort all the objects of C according to vertex2.
    16. Use Counting-Sort to sort all the objects of C according to vertex1.
    17. for i 1 to C1 do
    18.       if  i.vertex1 (i1).vertex1  i.vertex2 (i1).vertex2  then
    19.             if  i.bag-address.bag-id  (i1).bag-address.bag-id  then
    20.                   (i1).bag-address.parent  i.bag-address
    21.             else
    22.                   i.bag-address.parent  (i1).bag-address
    23.             end
    24.       end
    25. end


Two_Bag
    1. v  Dequeue(Q1)
    2. if bagged(v)  false then
    3.       bag-counter  bag-counter  1                                            Creación de la bolsa para el vértice v
    4.       x   Allocate Object-Type-1
    5.       x.vertex1  v
    6.       x.vertex2  Extract-Single(v)
    7.       x.vertex3  
    8.       x.bag-id  bag-counter
    9.       x.parent  nil
    10.       List-Insert(B, x)
    11.       x.vertex1.bag-pointer  x
    12.       x.vertex1.bagged  true
    13.       if  deg(x.vertex2)  1  then                              Condición de paro (al encontrar el último clique de tamaño 2)
    14.             x.vertex2.bag-pointer  x
    15.             x.vertex2.bagged  true
    16.             for each  u  x.vertex2.adj-list  do                                 Pegado de bolsas de tamaño 2 para x.vertex2
    17.                   if (u.bagged = true)  (u.bag-pointer.vertex3 = )  (u.bag-pointer.parent = nil)  then
    18.                         u.bag-pointer.parent.  x
    19.                   end
    20.             end
    21.       else                                                                                         Actualización de vecinos
    22.             deg(x.vertex2)  deg(x.vertex2)  1
    23.             if  deg(x.vertex2)  2  then  Enqueue(Q2, x.vertex2)  end
    24.             if  deg(x.vertex2)  1  then  Enqueue(Q1, x.vertex2)  end
    25.       end
    26.       for each  u  x.vertex1.adj-list  do                                         Pegado de bolsas de tamaño 2 para  x.vertex1
    27.             if (u.bagged = true)  (u.bag-pointer.vertex3 = )  (u.bag-pointer.parent = nil)  then
    28.                   u.bag-pointer.parent  x
    29.             end
    30.       end
    31.       return
    32. end

Three-Bag
    1. v. Dequeue(Q2)
    2. if  bagged(v)  false  then
    3.       bag-counter  bag-counter  1                                          Creación de la bolsa para el vértice v
    4.       x   Allocate-Object-Type-1                                                 
    5.       x.vertex1  v
    6.       x.vertex2, x.vertex3  Extract-Pair(v)
    7.       x.bag-id  bag-counter
    8.       x.parent  nil
    9.       List-Insert(B, x)
    10.       x.vertex1.bag-pointer  x
    11.       x.vertex1.bagged  true
    12.       y   Allocate-Object-Type-2                                           Creación de objetos para las aristas de la bolsa en x
    13.       (y.vertex1, y.vertex2, y.bag-address)  (x.vertex1, x.vertex2, x)
    14.       List-Insert(C, y))
    15.       y   Allocate-Object -Type-2
    16.       (y.vertex1, y.vertex2, y.bag-address)  (x.vertex2, x.vertex3, x)
    17.       List-Insert(C, y))
    18.       y   Allocate-Object -Type-2
    19.       (y.vertex1, y.vertex2, y.bag-address)  (x.vertex3, x.vertex1, x)
    20.       List-Insert(C, y))
    21.       if  (x.vertex2, x.vertex3)  E  then                                                Actualización de vecinos
    22.             x.vertex2.deg  x.vertex2.deg  1
    23.             x.vertex3.deg  x.vertex3.deg  1
    24.             if  x.vertex2.deg  2  then  Enqueue(Q2, x.vertex2)  end
    25.             if  x.vertex2.deg  1  then  Enqueue(Q1, x.vertex2)  end
    26.             if  x.vertex3.deg  2  then  Enqueue(Q2, x.vertex3)  end
    27.             if  x.vertex3.deg  1  then  Enqueue(Q1, x.vertex3)  end
    28.       else
    29.             List-Insert(x.vertex2.adj-list, x.vertex3)
    30.             List-Insert(x.vertex3.adj-list, x.vertex2)
    31.       end
    32.       for each  u  adj-list(x.vertex1)  do                             Pegado de bolsas de tamaño 2 para  x.vertex1
    33.             if (u.bagged = true)  (u.bag-pointer.vertex3 = )  (u.bag-pointer.parent) = nil)  then
    34.                   u.bag-pointer.parent  x
    35.             end
    36.       end
    37.       return
    38. end
