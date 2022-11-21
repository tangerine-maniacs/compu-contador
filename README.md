# compu-karnaugh

![Meme de stonks pero con un hombre mandarina](https://user-images.githubusercontent.com/7889022/143682566-336201e8-8f4c-4119-914e-f3b70402d219.png)

Calcula el mapa de Karnaugh para una serie de números dados. Automáticamente se remplaza el número repetido por todas las posibilidades.
Se muestra la tabla de transiciones completa, así como el número de puertas lógicas utilizadas con el fin de encontrar la solución más
eficiciente.

## Contribuir

Aceptamos PRs y Issues. Muchas gracias. 😊

<!-- Resuelve la primera parte de la práctica de Karnaugh, para cualquier set de números. -->

## Uso

### Google Colab
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/tangerine-maniacs/compu-contador/blob/main/compu_contador.ipynb)
Clona el notebook de Google Colab haciendo click en el icono de arriba y sigue las instrucciones ahí. 
   
### Localmente
Clona el repositorio y ejecuta el siguiente comando:
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
Found permutations for 0001: ['1001']
Switched numbers (len 2): [[0, 9, 1, 2, 3, 5, 8, 13], [0, 1, 9, 2, 3, 5, 8, 13]]
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

The equation for switching the repeated number is: nQ0Q3 + Q2Q3

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

Circuit has 35.5 gates. (Gates can have more than 2 inputs, each input costs .5)
24 JK registers
7.5 AND gates
4.0 OR gates
**This COUNTS the module to replace numbers**
**Remember that wires can be shared, so the real number might be lower**

===================
Working with list 1: ['0000', '0001', '1001', '0010', '0011', '0101', '1000', '1101']
Switched number list 1: [0, 1, 9, 2, 3, 5, 8, 13]
Table: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 0001 | 0 x | 0 x | 0 x | 1 x
0001 -> 1001 | 1 x | 0 x | 0 x | x 0
0010 -> 0011 | 0 x | 0 x | x 0 | 1 x
0011 -> 0101 | 0 x | 1 x | x 1 | x 0
0100 -> xxxx | x x | x x | x x | x x
0101 -> 1000 | 1 x | x 1 | 0 x | x 1
0110 -> xxxx | x x | x x | x x | x x
0111 -> xxxx | x x | x x | x x | x x
1000 -> 1101 | x 0 | 1 x | 0 x | 1 x
1001 -> 0010 | x 1 | 0 x | 1 x | x 1
1010 -> xxxx | x x | x x | x x | x x
1011 -> xxxx | x x | x x | x x | x x
1100 -> xxxx | x x | x x | x x | x x
1101 -> 0000 | x 1 | x 1 | 0 x | x 1
1110 -> xxxx | x x | x x | x x | x x
1111 -> xxxx | x x | x x | x x | x x

The equation for switching the repeated number is: nQ0Q3 + Q2Q3

Equation j_0: 1
Equation j_1: Q0nQ2Q3
Equation j_2: nQ0Q3 + Q0Q1
Equation j_3: Q0nQ1
Equation k_0: Q2 + Q3
Equation k_1: Q0
Equation k_2: 1
Equation k_3: Q0

Table filled: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 0001 | 0 x | 0 x | 0 x | 1 x
0001 -> 1001 | 1 x | 0 x | 0 x | x 0
0010 -> 0011 | 0 x | 0 x | x 0 | 1 x
0011 -> 0101 | 0 x | 1 x | x 1 | x 0
0100 -> 0001 | 0 x | x 1 | 0 x | 1 x
0101 -> 1000 | 1 x | x 1 | 0 x | x 1
0110 -> 0011 | 0 x | x 1 | x 0 | 1 x
0111 -> 0000 | 0 x | x 1 | x 1 | x 1
1000 -> 1101 | x 0 | 1 x | 0 x | 1 x
1001 -> 0010 | x 1 | 0 x | 1 x | x 1
1010 -> 1111 | x 0 | 1 x | x 0 | 1 x
1011 -> 0100 | x 1 | 1 x | x 1 | x 1
1100 -> 1001 | x 0 | x 1 | 0 x | 1 x
1101 -> 0000 | x 1 | x 1 | 0 x | x 1
1110 -> 1011 | x 0 | x 1 | x 0 | 1 x
1111 -> 0000 | x 1 | x 1 | x 1 | x 1

Circuit has 33.5 gates. (Gates can have more than 2 inputs, each input costs .5)
24 JK registers
6.5 AND gates
3.0 OR gates
**This COUNTS the module to replace numbers**
**Remember that wires can be shared, so the real number might be lower**

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
Found permutations for 1100: ['1110', '0100']
Switched numbers (len 4): [[0, 9, 15, 13, 14, 8, 12, 2], [0, 9, 15, 13, 4, 8, 12, 2], [0, 9, 15, 13, 12, 8, 14, 2], [0, 9, 15, 13, 12, 8, 4, 2]]
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

The equation for switching the repeated number is: Q1nQ2 + Q0Q1

Equation j_0: nQ1nQ3
Equation j_1: Q2 + Q0
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

Circuit has 31.5 gates. (Gates can have more than 2 inputs, each input costs .5)
24 JK registers
5.5 AND gates
2.0 OR gates
**This COUNTS the module to replace numbers**
**Remember that wires can be shared, so the real number might be lower**

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

The equation for switching the repeated number is: Q3 + Q2

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

Circuit has 32.0 gates. (Gates can have more than 2 inputs, each input costs .5)
24 JK registers
6.0 AND gates
2.0 OR gates
**This COUNTS the module to replace numbers**
**Remember that wires can be shared, so the real number might be lower**

===================
Working with list 2: ['0000', '1001', '1111', '1101', '1100', '1000', '1110', '0010']
Switched number list 2: [0, 9, 15, 13, 12, 8, 14, 2]
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
1000 -> 1110 | x 0 | 1 x | 1 x | 0 x
1001 -> 1111 | x 0 | 1 x | 1 x | x 0
1010 -> xxxx | x x | x x | x x | x x
1011 -> xxxx | x x | x x | x x | x x
1100 -> 1000 | x 0 | x 1 | 0 x | 0 x
1101 -> 1100 | x 0 | x 0 | 0 x | x 1
1110 -> 0010 | x 1 | x 1 | x 0 | 0 x
1111 -> 1101 | x 0 | x 0 | x 1 | x 0

The equation for switching the repeated number is: Q1nQ2 + Q0Q1

Equation j_0: nQ1nQ3
Equation j_1: nQ2Q3
Equation j_2: Q3
Equation j_3: nQ1
Equation k_0: nQ1Q2
Equation k_1: nQ3 + Q0
Equation k_2: nQ0
Equation k_3: nQ0Q1

Table filled: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 1001 | 1 x | 0 x | 0 x | 1 x
0001 -> 1001 | 1 x | 0 x | 0 x | x 0
0010 -> 0000 | 0 x | 0 x | x 1 | 0 x
0011 -> 0001 | 0 x | 0 x | x 1 | x 0
0100 -> 1001 | 1 x | x 1 | 0 x | 1 x
0101 -> 1100 | 1 x | x 0 | 0 x | x 1
0110 -> 0000 | 0 x | x 1 | x 1 | 0 x
0111 -> 0101 | 0 x | x 0 | x 1 | x 0
1000 -> 1110 | x 0 | 1 x | 1 x | 0 x
1001 -> 1111 | x 0 | 1 x | 1 x | x 0
1010 -> 0110 | x 1 | 1 x | x 0 | 0 x
1011 -> 1101 | x 0 | 1 x | x 1 | x 0
1100 -> 1000 | x 0 | x 1 | 0 x | 0 x
1101 -> 1100 | x 0 | x 0 | 0 x | x 1
1110 -> 0010 | x 1 | x 1 | x 0 | 0 x
1111 -> 1101 | x 0 | x 0 | x 1 | x 0

Circuit has 32.0 gates. (Gates can have more than 2 inputs, each input costs .5)
24 JK registers
6.0 AND gates
2.0 OR gates
**This COUNTS the module to replace numbers**
**Remember that wires can be shared, so the real number might be lower**

===================
Working with list 3: ['0000', '1001', '1111', '1101', '1100', '1000', '0100', '0010']
Switched number list 3: [0, 9, 15, 13, 12, 8, 4, 2]
Table: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 1001 | 1 x | 0 x | 0 x | 1 x
0001 -> xxxx | x x | x x | x x | x x
0010 -> 0000 | 0 x | 0 x | x 1 | 0 x
0011 -> xxxx | x x | x x | x x | x x
0100 -> 0010 | 0 x | x 1 | 1 x | 0 x
0101 -> xxxx | x x | x x | x x | x x
0110 -> xxxx | x x | x x | x x | x x
0111 -> xxxx | x x | x x | x x | x x
1000 -> 0100 | x 1 | 1 x | 0 x | 0 x
1001 -> 1111 | x 0 | 1 x | 1 x | x 0
1010 -> xxxx | x x | x x | x x | x x
1011 -> xxxx | x x | x x | x x | x x
1100 -> 1000 | x 0 | x 1 | 0 x | 0 x
1101 -> 1100 | x 0 | x 0 | 0 x | x 1
1110 -> xxxx | x x | x x | x x | x x
1111 -> 1101 | x 0 | x 0 | x 1 | x 0

The equation for switching the repeated number is: Q3 + Q2

Equation j_0: nQ1nQ2nQ3
Equation j_1: Q2nQ3 + Q0nQ2
Equation j_2: Q3
Equation j_3: nQ1nQ2
Equation k_0: nQ1Q2
Equation k_1: 1
Equation k_2: nQ0
Equation k_3: nQ0nQ2

Table filled: 
prev -> next | J K3| J K2| J K1| J K0
0000 -> 1001 | 1 x | 0 x | 0 x | 1 x
0001 -> 1011 | 1 x | 0 x | 1 x | x 0
0010 -> 0000 | 0 x | 0 x | x 1 | 0 x
0011 -> 0001 | 0 x | 0 x | x 1 | x 0
0100 -> 0010 | 0 x | x 1 | 1 x | 0 x
0101 -> 0110 | 0 x | x 0 | 1 x | x 1
0110 -> 0000 | 0 x | x 1 | x 1 | 0 x
0111 -> 0101 | 0 x | x 0 | x 1 | x 0
1000 -> 0100 | x 1 | 1 x | 0 x | 0 x
1001 -> 1111 | x 0 | 1 x | 1 x | x 0
1010 -> 0100 | x 1 | 1 x | x 1 | 0 x
1011 -> 1101 | x 0 | 1 x | x 1 | x 0
1100 -> 1000 | x 0 | x 1 | 0 x | 0 x
1101 -> 1100 | x 0 | x 0 | 0 x | x 1
1110 -> 1000 | x 0 | x 1 | x 1 | 0 x
1111 -> 1101 | x 0 | x 0 | x 1 | x 0

Circuit has 32.5 gates. (Gates can have more than 2 inputs, each input costs .5)
24 JK registers
6.5 AND gates
2.0 OR gates
**This COUNTS the module to replace numbers**
**Remember that wires can be shared, so the real number might be lower**

```
