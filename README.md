# compu-karnaugh

Calcula el mapa de Karnaugh para una serie de números dados. Automáticamente se remplaza el número repetido por todas las posibilidades.
Se muestra la tabla de transiciones completa, así como el número de puertas lógicas utilizadas con el fin de encontrar la solución más
eficiciente.

<!-- Resuelve la primera parte de la práctica de Karnaugh, para cualquier set de números. -->

## Uso

Es necesario tener instalado Python 3.10 y ejecutar este comando:

```
python3 main.py
```

## Ejemplo

Entrada:

```
Números: 0 1 1 2 3 5 8 13
```

Salida:

```
Numbers: ['0000', '0001', '0001', '0010', '0011', '0101', '1000', '1101']
Found permutations for 0001: ['1001']
Switched numbers (len 1): [[0, 9, 1, 2, 3, 5, 8, 13]]
===================
Working with list 0: ['0000', '1001', '0001', '0010', '0011', '0101', '1000', '1101']
Switched number list 0: [0, 9, 1, 2, 3, 5, 8, 13]
Table: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 1001 | 1 x | 0 x | 0 x | 1 x
0001 -> 0010 | 0 x | 0 x | 1 x | x 1
0010 -> 0011 | 0 x | 0 x | x 0 | 1 x
0011 -> 0101 | 0 x | 1 x | x 1 | x 0
0100 -> xxxx | x x | x x | x x | x x
0101 -> 1000 | 1 x | x 1 | 0 x | x 1
0110 -> xxxx | x x | x x | x x | x x
0111 -> xxxx | x x | x x | x x | x x
1000 -> 1101 | x 0 | 1 x | 0 x | 1 x
1001 -> 0001 | x 1 | 0 x | 0 x | x 0
1010 -> xxxx | x x | x x | x x | x x
1011 -> xxxx | x x | x x | x x | x x
1100 -> xxxx | x x | x x | x x | x x
1101 -> 0000 | x 1 | x 1 | 0 x | x 1
1110 -> xxxx | x x | x x | x x | x x
1111 -> xxxx | x x | x x | x x | x x

Equation j_0: 1
Equation j_1: Q0nQ2nQ3
Equation j_2: nQ0Q3 + Q0Q1
Equation j_3: nQ0nQ1 + Q2
Equation k_0: nQ1nQ3 + Q2
Equation k_1: Q0
Equation k_2: 1
Equation k_3: Q0

Table filled: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 1001 | 1 x | 0 x | 0 x | 1 x
0001 -> 0010 | 0 x | 0 x | 1 x | x 1
0010 -> 0011 | 0 x | 0 x | x 0 | 1 x
0011 -> 0101 | 0 x | 1 x | x 1 | x 0
0100 -> 1001 | 1 x | x 1 | 0 x | 1 x
0101 -> 1000 | 1 x | x 1 | 0 x | x 1
0110 -> 1011 | 1 x | x 1 | x 0 | 1 x
0111 -> 1000 | 1 x | x 1 | x 1 | x 1
1000 -> 1101 | x 0 | 1 x | 0 x | 1 x
1001 -> 0001 | x 1 | 0 x | 0 x | x 0
1010 -> 1111 | x 0 | 1 x | x 0 | 1 x
1011 -> 0101 | x 1 | 1 x | x 1 | x 0
1100 -> 1001 | x 0 | x 1 | 0 x | 1 x
1101 -> 0000 | x 1 | x 1 | 0 x | x 1
1110 -> 1011 | x 0 | x 1 | x 0 | 1 x
1111 -> 0000 | x 1 | x 1 | x 1 | x 1

Circuit has 8.5 gates. (Gates can have more than 2 inputs, each input costs .5)
5.5 AND gates
3.0 OR gates
**This doesn't count the module to replace numbers**
```

## Ejemplo 2

Entrada:

```
Números: 0 9 15 13 12 8 12 2
```

Salida

```
Numbers: ['0000', '1001', '1111', '1101', '1100', '1000', '1100', '0010']
Found permutations for 1100: ['1110', '0100']
Switched numbers (len 2): [[0, 9, 15, 13, 14, 8, 12, 2], [0, 9, 15, 13, 4, 8, 12, 2]]
===================
Working with list 0: ['0000', '1001', '1111', '1101', '1110', '1000', '1100', '0010']
Switched number list 0: [0, 9, 15, 13, 14, 8, 12, 2]
Table: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 1001 | 1 x | 0 x | 0 x | 1 x
0001 -> xxxx | x x | x x | x x | x x
0010 -> 0000 | 0 x | 0 x | x 1 | 0 x
0011 -> xxxx | x x | x x | x x | x x
0100 -> xxxx | x x | x x | x x | x x
0101 -> xxxx | x x | x x | x x | x x
0110 -> xxxx | x x | x x | x x | x x
0111 -> xxxx | x x | x x | x x | x x
1000 -> 1100 | x 0 | 1 x | 0 x | 0 x
1001 -> 1111 | x 0 | 1 x | 1 x | x 0
1010 -> xxxx | x x | x x | x x | x x
1011 -> xxxx | x x | x x | x x | x x
1100 -> 0010 | x 1 | x 1 | 1 x | 0 x
1101 -> 1110 | x 0 | x 0 | 1 x | x 1
1110 -> 1000 | x 0 | x 1 | x 1 | 0 x
1111 -> 1101 | x 0 | x 0 | x 1 | x 0

Equation j_0: nQ1nQ3
Equation j_1: Q0 + Q2
Equation j_2: Q3
Equation j_3: nQ1
Equation k_0: nQ1Q2
Equation k_1: 1
Equation k_2: nQ0
Equation k_3: nQ0nQ1Q2

Table filled: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 1001 | 1 x | 0 x | 0 x | 1 x
0001 -> 1011 | 1 x | 0 x | 1 x | x 0
0010 -> 0000 | 0 x | 0 x | x 1 | 0 x
0011 -> 0001 | 0 x | 0 x | x 1 | x 0
0100 -> 1011 | 1 x | x 1 | 1 x | 1 x
0101 -> 1110 | 1 x | x 0 | 1 x | x 1
0110 -> 0000 | 0 x | x 1 | x 1 | 0 x
0111 -> 0101 | 0 x | x 0 | x 1 | x 0
1000 -> 1100 | x 0 | 1 x | 0 x | 0 x
1001 -> 1111 | x 0 | 1 x | 1 x | x 0
1010 -> 1100 | x 0 | 1 x | x 1 | 0 x
1011 -> 1101 | x 0 | 1 x | x 1 | x 0
1100 -> 0010 | x 1 | x 1 | 1 x | 0 x
1101 -> 1110 | x 0 | x 0 | 1 x | x 1
1110 -> 1000 | x 0 | x 1 | x 1 | 0 x
1111 -> 1101 | x 0 | x 0 | x 1 | x 0

Circuit has 4.5 gates. (Gates can have more than 2 inputs, each input costs .5)
3.5 AND gates
1.0 OR gates
**This doesn't count the module to replace numbers**

===================
Working with list 1: ['0000', '1001', '1111', '1101', '0100', '1000', '1100', '0010']
Switched number list 1: [0, 9, 15, 13, 4, 8, 12, 2]
Table: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 1001 | 1 x | 0 x | 0 x | 1 x
0001 -> xxxx | x x | x x | x x | x x
0010 -> 0000 | 0 x | 0 x | x 1 | 0 x
0011 -> xxxx | x x | x x | x x | x x
0100 -> 1000 | 1 x | x 1 | 0 x | 0 x
0101 -> xxxx | x x | x x | x x | x x
0110 -> xxxx | x x | x x | x x | x x
0111 -> xxxx | x x | x x | x x | x x
1000 -> 1100 | x 0 | 1 x | 0 x | 0 x
1001 -> 1111 | x 0 | 1 x | 1 x | x 0
1010 -> xxxx | x x | x x | x x | x x
1011 -> xxxx | x x | x x | x x | x x
1100 -> 0010 | x 1 | x 1 | 1 x | 0 x
1101 -> 0100 | x 1 | x 0 | 0 x | x 1
1110 -> xxxx | x x | x x | x x | x x
1111 -> 1101 | x 0 | x 0 | x 1 | x 0

Equation j_0: nQ1nQ2nQ3
Equation j_1: nQ0Q2Q3 + Q0nQ2
Equation j_2: Q3
Equation j_3: nQ1
Equation k_0: nQ1Q2
Equation k_1: 1
Equation k_2: nQ0
Equation k_3: nQ1Q2

Table filled: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 1001 | 1 x | 0 x | 0 x | 1 x
0001 -> 1011 | 1 x | 0 x | 1 x | x 0
0010 -> 0000 | 0 x | 0 x | x 1 | 0 x
0011 -> 0001 | 0 x | 0 x | x 1 | x 0
0100 -> 1000 | 1 x | x 1 | 0 x | 0 x
0101 -> 1100 | 1 x | x 0 | 0 x | x 1
0110 -> 0000 | 0 x | x 1 | x 1 | 0 x
0111 -> 0101 | 0 x | x 0 | x 1 | x 0
1000 -> 1100 | x 0 | 1 x | 0 x | 0 x
1001 -> 1111 | x 0 | 1 x | 1 x | x 0
1010 -> 1100 | x 0 | 1 x | x 1 | 0 x
1011 -> 1101 | x 0 | 1 x | x 1 | x 0
1100 -> 0010 | x 1 | x 1 | 1 x | 0 x
1101 -> 0100 | x 1 | x 0 | 0 x | x 1
1110 -> 1000 | x 0 | x 1 | x 1 | 0 x
1111 -> 1101 | x 0 | x 0 | x 1 | x 0

Circuit has 7.0 gates. (Gates can have more than 2 inputs, each input costs .5)
6.0 AND gates
1.0 OR gates
**This doesn't count the module to replace numbers**
```
La primera solución solo utiliza 4.5 puertas lógicas, mientras que la segunda, 7. Por tanto, reemplazar 12 por 14 es
más eficiente que reemplazarlo por 4, puesto que utiliza menos puertas lógicas.
