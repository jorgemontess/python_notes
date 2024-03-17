'''
FUNCION

    - def
    - NoneType
    - return
    - None

ARGUMENTOS de una Funcion
    - def funcion(argumento_1, argumento_2):
    - Keywords Arguments.
    - Como ordenar como queramos el valor de los argumentos.

Return vs Print
    - Cuando tenemos un print en una funcion, al tratar de pasarla a la variable esta nos va a marcar None y va a ser una 
      Variable tipo NoneType, esto debido a que no tiene ningun valor.
    
    - Cuando retornamos, lo que se retorna si es un valor, por ende cuando lo declaramos en una variable esta si
      va a almacenar el valor de lo que retornemos de la funcion.

SCOPE
Concepto de Variable local y Variable Local.
    - Uso de la sentencia Global.

'''

def nombre_funcion():
    pass

nombre_funcion()


def saludar(argumento_nombre): #Lo que tiene la function es el argumento.
    print(f'Hola {argumento_nombre}')

#saludar('Jorge') # Parametro.

#---------------------- /// --------------- /// ---------------------

# Llamando None Type

def despedir(nombre):
    print(f'Chao {nombre}')

#llamar = despedir('Jorge')
#print(llamar)
#print(type(llamar)) # Imprime class 'NoneType

# Arreglando el error NoneType
def media(num_1, num_2, num_3):
    resultado = (num_1 + num_2 + num_3) / 3
    return resultado

#llamada = media(4, 4, 5)
#print(llamada)

#---------------- // ----------------- // ------------------------
def resta(num_1, num_2):
    return num_1 - num_2

#print(resta(5, 2))
#print(resta(2, 5))

#print(resta(num_2 = 2, num_1 = 5))  # Declarar el orden...


#Puedo pasar el valor directamente en el argumento

def suma(num_1 = 5, num_2 = 3):
    return num_1 + num_2

#print(f'Usando valores por defecto: {suma()}')
#print(f'Usando el orden con solo 1 valor: {suma(3)}')
#print(f'Usando el orden con todos los valores: {suma(3,2)}')
#print(f'Con Keywords Arguments: {suma(num_1 = 1, num_2 = 1)}')
#print(f'Con  un solo Keyword Argument: {suma(num_1 = 1)}')


#--------------- // --------------------- // ------------------------

#SCOPE ----> Alcance de las variables

variable = 3  # Variable Global

def funcion():
    global variable  # Puedo llamar a la variable global y alterar su valor en la funcion
    variable = 1   # La variable local esta cambiandose por la de afuera que es la global
    print(variable)

#funcion()
#print(variable)