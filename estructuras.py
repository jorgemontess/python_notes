'''
    Estructuras de Datos
    
    Listas

        - Mutables
    
    Tuplas

        - Inmutables 

    Conjuntos
    
        - NO Ordenados  --> Los valores se desordenan cada que imprimes
        - Hetereogeneos
        - Mutables
        - Sin repeticion
        
        USOS
        
        - Eliminar elementos repetidos de la secuencia que se le pase
        - Se puede hacer la interseccion de los conjuntos A ∩ B
        - Se puede hacer la union de los conjuntos A ∪ B
        - Comprobar si los elementos de un conjunto estan incluidos en otro
        
    
    Diccionarios
        
        - Relaccionar pares de elementos --> {clave : valor}    
        - No tiene Orden
        - Hetereogeneo con clave inmutable, no se cambia la clave
        - Mutable

'''

# Listas --> Lists

def listas():
    lista = [30, 40, True, 'String', 4.5]

    print(lista)
    print(lista[2]) #Accediendo a valor 3 de la lista
    print(lista[-1])   # Accediendo a la lista al reves, del ultimo
    print(lista[0 : 3])  # Sublista para definir rango del que queremos imprimir, pos de la 0 a la 2

    # Cambiar elemento

    lista[0] = 20   # Accedemos al indice y cambiamos el valor que esta en este
    print(lista)

    # Metodos de las listas

    lista_nueva = ['Hola', 'Hola', 1, 2, 3, 4]

    lista_nueva.append(1)             # Agregar un elemento al final
    print(lista_nueva.count(1))   # Me muestra el numero de veces que se repite el valor que le de como argumento
    print(lista_nueva.count('Hola'))  # Sirve con strings tambien
    print(lista_nueva.index('Hola'))  # Nos devuelve el indice de la primera aparicion del valor que le demos
    lista_nueva.remove('Hola')        # Elimina la primera aparicion de un elemento

#listas()

# ======================= // ======================== // ===========================

# Tuplas --> Tuples

def tuplas():

    tupla = ("Hola", 1, 2, False, False, 1)
    print(tupla)

    #print(tupla[0])     # Acceder al elemento de una tupla por el indice, igual que con las listas

    
    # Metodos de las tuplas
    print(tupla.count(True))  # Al hacer esto en una tupla, aunque no tengo True, agarra las coincidencias
                              # y hace una especie de operacion, False == False --> True
    print(tupla.count(False)) # Aca si me cuenta normal cuantos false tengo en la tupla

    print(tupla.index('Hola'))     # Devuelve el indice en el cual esta el valor que le estoy pasando

#tuplas()


# ====================== // ======================== // =============================    

# Conjuntos --> Sets 

def sets():

    print(type(set()))  # Se declara de esta forma
    print(set([1, 2, 'Hola']))    # Para inicializarlo se le pasa como argumento alguna secuencia
                                  # Puede ser una lista, tupla o un strin
    print(set((1, 2, 4, 5, )))
    print(set('M555,2333'))       # Si colocamos un string lo que obtenemos es un Char, conjunto de caracteres

    lista = [1,2,3,3,4]
    conjuntos = set(lista)        # Elimina objetos repetidos de la secuencia que se le pase
    print(conjuntos)

    
    # METODOS
    
    conjunto = set(['El', 'perro', 'de'])    

    conjunto.add('Jorge')         # Agregar elemento al final
    print(conjunto)

    conjunto.remove('Jorge')      # Eliminar elemento
    print(conjunto)

    
    conjunto_1 = set(['Si', 3, 4, 7])
    conjunto_2 = set([3, 5, 7, 7, 8,])
    conjunto_3 = set([1, 2, 3.4, 1, 1, 9])

    print(conjunto_1, conjunto_2, conjunto_3)

    print(conjunto_1.intersection(conjunto_2))   # Realizamos operacion de intersection entre C1 y C2
    print(conjunto_1 & conjunto_2)               # Realizamos operacion de intersection entre C1 y C2

    print(conjunto_1.union(conjunto_2))          # Realizamos operacion de union entre C1 y C2
    print(conjunto_2.issubset(conjunto_1))       # Comprobar si todos los elementos estan incluidos en el conjunto

    # ----- Operadores y fucion que realizan ------
    # A|B --> Union
    # A&B --> Interseccion
    # A-B --> Diferencia
    # A^B --> Diferencia Simetrica
    # A>=B --> Superconjunto
    #A<=B --> Subconjunto

#sets()

# ====================== // ======================== // =============================    

#Diccionarios --> Dictionaries

def diccionarios():
    
    diccionario = {1 : 'Jorge', 2 : 'Angie', 3 : 'Bebe'}    
    print(diccionario)
    
    diccionario[2] = 'Mamita'        # Cambiar el Value por medio de la Key
    print(diccionario[2])    

    # Diferentes maneras de crear un diccionario
    
    dict_lista_tupla = dict([(1, 'Uno'), (2, 'Dos')])   # IMPORTANTE la sentencia "dict"
    print(dict_lista_tupla)

    dict_lista_string = dict(Uno = 1, Dos = 2, Tres = 3)  # Strings como Keys
    print(dict_lista_string)

    
    # Imprimir informacion del diccionario
    print(diccionario)
    print(diccionario.keys())
    print(diccionario.values())
    print(diccionario.items())

    diccionario.pop(3)     # Eliminar un elemento con la Key y a la vez se le elimina la clave y el valor
    print(diccionario)
#diccionarios()


# ====================== // ======================== // =============================    


# EJERCICIOSSSS

def ejercicios():
    
    # Ejercicio de LISTA    
    personajes = ["Kakyoin", "Joseph", "Jotaro"]
    personajes.remove("Kakyoin")
    personajes.append("Polnareff")
    resultado_1 = personajes[1:2]

    # Ejercicio de TUPLAS
    respuesta = ("Yes", "Yes", "Yes")
    resultado_2 = (respuesta.count("Yes"), respuesta.index("Yes"))

    
    # Ejercicio de CONJUNTOS
    temporada_2 = set(["Joseph", "Caesar"])
    temporada_3 = set(["Jotaro", "Joseph", "Avdol", "Kakyoin", "Polnareff"])
    resultado_3 = temporada_2 & temporada_3

    
    # Ejercicio de DICCIONARIOS
    protas = {1:"Jonnathan", 2: "Joseph", 3: "Jotaro"}
    jojos = {"Jonnathan": "Phantom Blood", "Joseph": "Battle Tendency", "Jotaro": "Stardust Crusaders"}
    resultado_4 = jojos[protas[3]]

    
    print("Ejercicio LISTA\n", resultado_1 )
    print("Ejercicio TUPLA\n", resultado_2 )
    print("Ejercicio CONJUNTO\n", resultado_3 )
    print("Ejercicio DICCIONARIO\n", resultado_4 )

ejercicios()