#!/usr/bin/env python
# coding: utf-8

# <div  align="center">
#     <h1>Curso de python basico</h1>
#     <h2>Edain JCC</h2>
# </div>

# <h2>Importaciones</h2>

# In[1]:


import random, string


# <h2>Prueba basica</h2>

# In[2]:


#Funsion de suma
def suma(n1,n2):
    return n1 + n2
    
#variables
n1 = 134
n2 = 456
#imprimir en consola
print("la suma de " + str(n1) + " mas " + str(n2) + " es " + str(suma(n1,n2)))


# ## Arreglo

# In[3]:


#Arreglo vacio
array = []
#for de n a n
for i in range (1, 12):
    #agregar al arreglo 
    array.append(str(i) + " -> " + str(i*2))

print(array)


# # VARIABLES
# * Entero
# * Decimal
# * Booleano

# In[4]:


#Variables
entero = 24
decimal = 24.5
booleano = True
cadena = "texto"

#condicional
if booleano:
    print("Soy un entero " + str(entero) + " -> " + str(type(entero)))
    print("Soy un decimal " + str(decimal) + " -> " + str(type(decimal)))
    print("Soy un booleano " + str(booleano)  + " -> " + str(type(booleano)))
    print("Soy una cadena " + str(cadena)  + " -> " + str(type(cadena)))    


# ## Operaciones
# * Suma
# * Resta
# * Multiplicacion
# * Potencia
# * Division
# * Division entera
# * Resto

# In[5]:


#Operaciones
n1 = 92
n2 = 3
#suma -> +
print("la suma de " + str(n1) + " mas " + str(n2) + " es " + str(n1 + n2))
#resta -> +
print("la resta de " + str(n1) + " menos " + str(n2) + " es " + str(n1 - n2))
#multiplicacion -> *
print("la multiplicacion de " + str(n1) + " por " + str(n2) + " es " + str(n1 * n2))
#potenciacion -> *
print("la potenciacion de " + str(n1) + " elebado a " + str(n2) + " es " + str(n1 ** n2))
#Division normal
print("la division de " + str(n1) + " entre " + str(n2) + " es " + str(n1 / n2))
#Division que devuelve el cociente entero
print("El cosiente entero de la division de " + str(n1) + " entre " + str(n2) + " es " + str(n1 // n2))
#Division que devuelve el resto
print("El resto de la division de " + str(n1) + " entre " + str(n2) + " es " + str(n1 % n2))


# ## Algunos metodos para strings
# ### format
# <p> Sirve para concatenar datos a un string usando {} en los string </p>

# In[6]:


#Datos
nombre = "Edain"
edad = 24
trabajo = "programador"
salario = 15.000
casado = False

if(casado):
    casado = "si"
else:
    casado = "no"

#Mensaje
Mensaje = '''
Hola mi nombre es {} 
tengo {} años
trabajo de {} y gano {}
y {} estoy casado
'''

print(Mensaje.format(nombre, edad, trabajo, salario, casado))


# ### Convercion de textos a mayusculas o minusculas
# <p> upper() convierte a mayuscula </p>

# In[7]:


texto = "hola mundo soy edain"
print(texto)
textoMa = texto.upper()
print(textoMa)


# <p> lower() convierte a minuscula </p>

# In[8]:


texto = "HOLA MUNDO SOY EDAIN"
print(texto)
textoMi = texto.lower()
print(textoMi)


# <p> capitalize() convierte la primera letra en mayuscula </p>

# In[9]:


texto = "HOLA MUNDO SOY EDAIN"
print(texto)
textoMi = texto.capitalize()
print(textoMi)


# ### Separar cadenas y ponerlas en una lista
# <p> split() separa cadenas por un caracter en especifico </p>

# In[10]:


texto = "Hola_amigos"
print(texto.split("_"))


# <p> Asignar a nuevas variables </p>

# In[11]:


texto = "Hola_amigos"
[text1, text2] = texto.split("_")
print(text1)
print(text2)


# ### Remplazar cadenas por otras
# <p> replace() remplasar una sub cadena en especifico por otra </p>

# In[12]:


texto = "Hola mi nombre es Edain"
print(texto)
print(texto.replace("Edain", "Jose"))


# # ESTRUCTURAS DE DATOS
# ## Listas
# #### Creacion y control de elementos
# <p>Crear una lista</p>

# In[13]:


#Lista
lista = ["Pera", "Mango", "Manzana", "Platano", "Sandia"]
print(lista)


# <p>Optener la longitud de una lista con len() </p>

# In[14]:


print("la lista " + str(lista) + " tiene " +  str(len(lista)) + " elementos")


# saber elemento de una lista

# In[15]:


print(lista)
print("El primer elemento de la lista es " + str(lista[0]))
print("El quinto elemento de la lista es " + str(lista[4]))


# optener rangos de la lista (desde / asta)

# In[16]:


print(lista)
print("los datos que siguen despues del segundo elemento son " + str(lista[2:]))
print("los datos que estam antes del penultimo elemento son " + str(lista[:3]))
print("los datos que de la lista desde el segundo al penultimo elemento son " + str(lista[1:4]))


# ultimos elementos

# In[17]:


print(lista)
print("el ultimo elemento de la lista es " + str(lista[-1]))
print("el penultimo elemento de la lista es " + str(lista[-2]))


# #### Buscar elementos
# 
# saber si un elemento esta en la lista

# In[18]:


lista = ["Edain", "Maria", "Jose", "Pedro", "Manuel"]
print(lista)

#nombre a buscar
nombre = "Jose"

#Si n esta en la lista
resultado = nombre in lista
print("¿"+ nombre + " esta en la lista?: " + str(resultado))


# saber el indice de el elemento buscado (index())

# In[19]:


print(lista)
#condicional
if resultado:
    i = lista.index(nombre)
    print(nombre + " esta en el indice {}".format(i))
else:
    print(nombre + " NO esta en la lista")


# #### Eliminar elementos
# 
# utilizando el metodo pop()

# In[20]:


lista = ["Rojo", "Verde", "Azul"]
print(lista)

#Optenemos el indice del ultimo elemento
ultimo = lista.index(lista[-1])
#Eliminamos el ultimo elemento
lista.pop(ultimo)
#Nueva lista
print(lista)


# #### Inserta elemento en n indice
# 
# utilizando insert(i, obj)

# In[21]:


lista = ["Mexico", "Chile"]
print(lista)
#nuevo elemento
ne = "Argentina"
#insertamos en la segunda posicion
lista.insert(1,ne)
print(lista)


# #### Agregar elemento al final de la lista
# 
# usando append(obj)

# In[22]:


lista = ["Perro", "Gato", "Gallina"]
print(lista)
#nuevo elemento
newElement = "Elefante"
#Agregamos al final de la lista
lista.append(newElement)
print(lista)


# #### Ordenado elementos de una lista 
# 
# Normal usando --> sort()
# * De la A a la Z
# * Del menor al mayor

# In[23]:


#Listas
lista = ["Zorro", "Pantera", "Aguila", "Gorila", "Leon"]
listaN = [2, 4, 7, 0, 12, 35, 24, 3, 2, 1, 7]
print(lista)
print(listaN)
#ordenamos
lista.sort()
listaN.sort()
print(lista)
print(listaN)


# A la inverza usando --> sort(reverse=True)
# * De la Z a la A 
# * Del mayor al menor 

# In[24]:


lista = ["Vaca", "Zorra", "Burro", "Pantera", "Aguila", "Gorila", "Leon"]
listaN = [2, 4, 7, 0, 12, 35, 24, 3, 2, 1, 7]
print(lista)
print(listaN)
#ordenamos
lista.sort(reverse=True)
listaN.sort(reverse=True)
print(lista)
print(listaN)


# #### Voltear una lista 
# 
# voltear una lista donde el ultimo elemento sera el primero y asi sucesivamente

# In[25]:


lista = [1,2,3,4,"A","B","C","D"]
print(lista)

#Volteamos la lista
lista.reverse()
print(lista)


# ## Tuplas
#  Son muy similares a las listas pero se definen con parentesis () y no se pueden modificar o alterar

# ### Creacion

# In[26]:


frutas = ("Mango", "Pera", "Manzana", "Melon")
print(frutas)


# ## Diccionarios
# 
# Los diccionarios en Python nos permiten almacenar una serie de mapeos entre dos conjuntos de elementos, llamados keys and values (Claves y Valores). Todos los elementos en el diccionario se encuentran encerrados en un par de corchetes {} 
# 
# ### Creacion

# In[27]:


receta = {"Agua":2, "Aceite":4, "Azucar":7, "Harina":3}
print(receta)


# #### Saber el indice de un elemento

# In[28]:


i = receta["Agua"]
print("El indice de Agua es {}".format(i))


# ### Optener datos
# #### Obtener las claves de un diccionario
# 
# Utilizando keys() y guardadolo en una lista

# In[29]:


lista = list(receta.keys())
print(receta.keys())
print(lista)


# #### Obtener los valores de un diccionario
# 
# Utilizando values() y guardadolo en una lista

# In[30]:


lista = list(receta.values())
print(receta.values())
print(lista)


# #### Saver si un elemento esta en el diccionario
# 
# utilizando in
# 

# In[31]:


res = "Agua" in receta
t = ""
if(res):
    t = "SI"
else:
    t = "NO"

print("Agua {} esta en el diccionario".format(t))


# # ESTRUCTURAS CONDICIONALES
# 
# ### usos de if, elif y else

# In[32]:


#valores
nombre = "Edain"
edad = 60
#Condicional
if edad >= 0 and edad < 17:
    print("{} es un niño".format(nombre))
elif edad >= 17 and edad < 31:
    print("{} es un joven".format(nombre))
elif edad >= 31 and edad < 60:
    print("{} es un adulto".format(nombre))
elif edad >= 60 and edad < 135:
    print("{} es un anciano".format(nombre))
else:
    print("ERROR, Edad invalida")
    


# ### Uso de and ( Y / && )

# In[33]:


#Edades de 3 personas
edadPedro = random.randint(0, 25);
edadMaria = 18;
edadJose = 11;

print("Edad de Maria " + str(edadPedro))
print("Edad de Maria " + str(edadMaria))
print("Edad de Jose " + str(edadJose))


#si pedro es mayor que Maria Y mayor que Jose
if edadPedro > edadMaria and edadPedro > edadJose:
    print("Pedro es el hermano mayor")
#si pedro es mayor que Maria Y menor que Jose O si pedro es menor que Maria Y mayor que Jose
elif edadPedro > edadMaria and edadPedro < edadJose or edadPedro < edadMaria and edadPedro > edadJose:
    print("Pedro es el hermano de enmedio")
else:
    print("Pedro es el hermano menor")
    


# ### Uso de or ( 0 - || )

# In[34]:


#dias de la semana
dias = ["lunes", "martes","miercoles","jueves", "viernes","sabado","domingo"]
#Escojemos un dia de la lista
dia = random.choice(dias)

#Si el dia es sabado o domingo
if dia == "sabado" or dia == "domingo":
    print("{} es fin de semana".format(dia))
elif dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes":
    print("{} es entre semana".format(dia))
    


# ### Uso de !=

# In[35]:


#USO DE !=
#Escojemos 2 numero 
n1 = random.randint(1, 3)
n2 = random.randint(1,3)

#n1 es diferente de n2
if n1 != n2:
    print("{} NO es igual a {}".format(n1,n2))
else:
    print("{} y {} son IGUALES".format(n1,n2))


# ### Uso de not
# * En un booleano

# In[36]:


a = True
#a es falso
if not a:
    print('a es falso.')
else:
    print("a es verdadero")


# * En una cadena

# In[37]:


a = ""
 
if not a:
    print('La cadena esta vacía.')
else:
    print(a)


# * En una lista

# In[38]:


a = []
if not a:
    print('La lista esta vacía.')
else:
    print(a)


# * En un diccionario

# In[39]:


a = dict({})
if not a:
    print('El diccionario esta vacío.')
else:
    print(a)


# * En una tupla

# In[40]:


a = tuple("hola")
if not a:
    print('La tupla esta vacía.')
else:
    print(a)


# # ESTRUCTURAS REPETITIVAS

# ## While
# #### Ejemplo 1

# In[41]:


i = 0
j = 0
cadena = ""
noAleatorio = random.randint(3, 6)
#Estructura 1
while i < noAleatorio:
    j = 0;
    #Estructura 2
    while j < noAleatorio*2:
        cadena += str(random.randint(1,9))
        j +=1
    cadena += "\n"
    i+=1

print(cadena)


# #### Ejemplo 2

# In[42]:


i = 0;
j = 0;
n = random.randint(5, 10)
dic = dict({})

while i < n:
    j = 0
    cad = ""
    while j < random.randint(3, 10):
        cad+=random.choice(string.ascii_letters)
        j+=1
    dic[ random.randint(1000, 9999)] = cad
    i+=1
print(dic)


# #### Ejemplo 3 (Uso de while … else )
# Python ofrece una estructura adicional (else) en el bucle whilw

# In[43]:


alumnos = ["Jose", "Pedro", "Maria", "Pedro", "Karen"]
alumnoBuscar = "Edain"
i = 0
while i < len(alumnos):
    if alumnos[i] == alumnoBuscar:
        print("Es(La) alumno(a) {} tiene es el numero {} de la lista".format(alumnoBuscar, numeros[i]))
        break
    i += 1
else:
    print('No se encontró a el alumno {}'.format(alumnoBuscar))


# ## Uso de for

# #### Ejemplo 1 ( Recooriendo una lista por valor)

# In[44]:


nums = [4, 78, 9, 84]
for n in nums:
    print(n, end=" ")


# #### Ejemplo 2 ( Recooriendo diccionarios)

# In[45]:


#Recorrer las claves del diccionario.
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k in valores:
    print(k, end=" ")
print()
#Iterar sobre los valores del diccionario
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for v in valores.values():
    print(v, end=" ")
print()
#Iterar a la vez sobre la clave y el valor de cada uno de los elementos del diccionario.
valores = {'A': 4, 'E': 3, 'I': 1, 'O': 0}
for k, v in valores.items():
    print('k=', k, ', v=', v, end=" ")


# #### Ejemplo 3 ( for y la clase range)
# * range(max): Un iterable de números enteros consecutivos que empieza en 0 y acaba en max - 1

# In[46]:


#Mostrar datos de una lista
lista = list(["Perro", "Gato", "Vaca"])
for i in range (len(lista)):
    print("El elemento {} de la lista es {}".format(i, lista[i]))


# * range(min, max): Un iterable de números enteros consecutivos que empieza en min y acaba en max - 1

# In[47]:


#Mostrar numeros de n a n-1/5 al 10
for i in range(5, 11):
    print(i, end=" ")


# * range(min, max, step): Un iterable de números enteros consecutivos que empieza en min acaba en max - 1 y los valores se van incrementando de step en step. Este último caso simula el bucle for con variable de control.

# In[48]:


#Por ejemplo, para mostrar por pantalla los números pares del 1 al 10 
#podríamos usar la función range del siguiente modo:
for num in range(0, 11, 2):
    print(num, end=" ")


# #### Ejemplo 4 (Uso de break. Encontrar un elemento en una colección)

# In[49]:


coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e == 7:
        print(e)
        break


# #### Ejemplo 5 (Uso de continue. Imprimir solo los números pares de una colección)

# In[50]:


coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e % 2 != 0:
        continue
    print(e, end=" ")


# #### Ejemplo 6 (Uso de for … else )
# Python ofrece una estructura adicional (else) en el bucle for

# In[51]:


numeros = [1, 2, 4, 6, 5, 8, 6, 4]
for i in numeros:
    if i == 3:
        print("Es numero {}, esta en el indice {}".format(i, numeros[i]))
        break
else:
    print('No se encontró el número 3')


# # CONVERSION DE DATOS
# #### A enteros -> int(x) Convierte x en un entero

# In[52]:


st = "3455"
print("cadena: {}".format(st))
n = int(st)
print("entero: {}".format(n))


# #### A n largos -> int(x) Convierte x en un entero largo

# In[53]:


st = "3434567883555665"
print("cadena: {}".format(st))
n = int(st)
print("numero largo: {}".format(n))


# #### A flotantes -> float(x) Convierte x en un número de punto flotante

# In[54]:


st = "245.3466"
print("cadena: {}".format(st))
n = float(st)
print("numero decimal: {}".format(n))


# #### A cadenas -> str(x) Convierte x a una cadena. x puede ser del tipo float. entero o largo

# In[55]:


n = 123.2
print("numero: {}".format(n))
st = str(n)
print("cadena: {}".format(st))


# #### A hexadecimal -> hex(x) Convierte x entero en una cadena hexadecimal

# In[56]:


n = 46546
print("entero: {}".format(n))
hexs = hex(n)
print("cadena hexadecimal: {}".format(hexs))


# #### A caracter -> chr(x) Convierte x entero a un caracter

# In[57]:


n = 234
print("entero: {}".format(n))
c = chr(n)
print("caracter: {}".format(c))


# #### A Enter C -> ord (x) Convierte el carácter x en un entero

# In[58]:


c = "ê"
print("caracter: {}".format(c))
n = ord(c)
print("entero: {}".format(n))


# # LECTURA DE DATOS
# ## Uso de input

# #### Ejemplo 1

# In[59]:


print("¡Hola! Aqui podras realizar sumas")

#Pedir datos
n1 = input("Por favor ingrese el primer valor: ")
n2 = input("Por favor ingrese el segundo valor: ")

#numero1 será entero, así que usamos int()
n1 = int(n1)

#numero2 será un real, así que usamos float()
n2 = int(n2)

# Mostramos el resultado de la suma
print(n1, "+", n2, "=", n1 + n2)


# #### Ejemplo 2

# In[60]:


print("Adivina el numero aleatorio")

#Numero aleatorio del 1 al 5
nA = random.randint(1, 5)
#No de intentos
intentos = 3
for i in range (intentos):
    n = input("Ingresa el intento {}: ".format(i+1))
    if(int(n) == nA):
        print("GANASTE, El numero aleatorio es {}".format(nA))
        break
else:
    print("PERDISTE, El numero aleatorio era {}".format(nA))


# # FUNCIONES
# 
# ### Se utiliza la pabra recervada def
# 
# #### Ejemplo 1 (Accion)

# In[61]:


def saludo(st):
    print("Hola {}".format(st))

persona = "Pedro"
saludo(persona)


# #### Ejemplo 2 (Retornado un valor)

# In[62]:


def sumarDatosDeUnaLista(lis):
    return sum(lis)

lista = list([1,3,6,2,7,4,9,8,3,6])
print(lista)
print("La suma total de una lista es {}".format(sumarDatosDeUnaLista(lista)))


# #### Ejemplo 3 (Usando *args)
# *args señala que llegaran n parametros a la funcion sin necesidad de ponerlos y se convertiran en una tupla

# In[63]:


#Calcular promedio
def calcularPromedio(*args):
    print("la tupla que se creo es {}".format(args))
    pro = 0
    #Recorremos los n valores que nos llegaron
    for ar in args:
        pro += ar
    #Retornamos promedio
    return pro/len(args)

calificaciones = [7, 9, 10,  6, 9, 6, 7, 9, 10, 3]
prom = calcularPromedio(7, 9, 10,  6, 9, 6, 7, 9, 10, 3)
print("El promedio de las calificaciones {} es de {}".format(calificaciones, prom))


# #### Ejemplo 3 (Usando **kwargs)
# *kwargs (Clave/Valor) señala que llegaran n parametros a la funcion sin necesidad de ponerlos y se convertiran en un diccionario

# In[64]:


def crearDiccionario(**kwargs):
    print("Diccionario que se creo: {}".format(kwargs))
    for kw in kwargs:
        print("clave: {} valor: {}".format(kw, kwargs[kw]))
crearDiccionario(n=345, nombre="Jose", lista=[3,5,7,4]);


# # EXCEPCIONES
# ### Las principales excepciones definidas en Python son:
# * TypeError : Ocurre cuando se aplica una operación o función a un dato del tipo inapropiado.
# * ZeroDivisionError : Ocurre cuando se itenta dividir por cero.
# * OverflowError : Ocurre cuando un cálculo excede el límite para un tipo de dato numérico.
# * IndexError : Ocurre cuando se intenta acceder a una secuencia con un índice que no existe.
# * KeyError : Ocurre cuando se intenta acceder a un diccionario con una clave que no existe.
# * FileNotFoundError : Ocurre cuando se intenta acceder a un fichero que no existe en la ruta indicada.
# * ImportError : Ocurre cuando falla la importación de un módulo.
# 
# ### Control de excepciones
# 
# #### Divicion entre 0

# In[65]:


def division(a, b):
    
    res = ""
    
    try:
        result = a / b
    except ZeroDivisionError:
        res = 'ERROR, ¡No se puede dividir por cero!'
    else:
        res = 'El resultado de {} entre {} es {}'.format(a, b, (a/b))
    finally:
        print(res)
        

division(1, 0)
division(1, 2)


# #### Error en valor

# In[66]:


try:
    n = int(input("Escribe un numero"))
    print("tu valor es {}".format(n))
except ValueError:
    print("ERROR, dato invalido")


# #### Sin espesificar (NO RECOMENDABLE)

# In[67]:


try:
    n = int(input("Escribe un numero"))
    print("tu valor es {}".format(n))
except:
    print("ERROR, dato invalido")


# # POO
# 
# ## Clases 
# * self es como un this
# *  pass es un marcador de posición que evita que el programa emita un mensaje de error. La sentencia conserva la sintaxis

# In[90]:


#Clase
class Animal:
    #Contructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def vacio(self):
        # Método vacío
        pass

    # Moverce
    def moverse(self, n):
        print("Soy un(a) {} y me movi {} metros".format(self.especie, n))

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)


# In[91]:


leon = Animal("Leon",12)
aguila = Animal("Aguila",3)
print(type(Animal))
print(type(leon))
print(leon.moverse(2))
print(type(aguila))
print(aguila.moverse(32))


# ## Herencia

# In[92]:


#Clase heredada
class Perro(Animal):
    def hablar(self):
        print("Guau!")
#Clase heredada
class Vaca(Animal):
    def hablar(self):
        print("Mooo!")


# In[93]:


#Objetos
mi_perro = Perro('mamífero', 10)
mi_vaca = Vaca('mamífero', 23)
#Acciones
mi_perro.describeme()
mi_perro.moverse(33)
mi_perro.hablar()
mi_vaca.describeme()
mi_vaca.moverse(2)
mi_vaca.hablar()


# ## Palabra super

# In[94]:


#Clase heredada
class Oveja(Animal):
    
    #Constructor
    def __init__(self, especie, edad, sexo):
        # Palabra super
        super().__init__(especie, edad)
        self.sexo = sexo
    
    def hablar(self):
        print("Beee!")
    
    def miSexo(self):
        print("Soy del sexo {}".format(self.sexo))


# In[109]:


mi_oveja = Oveja('mamifero', 4, "Hembra")

mi_oveja.describeme()
mi_oveja.moverse(33)
mi_oveja.miSexo()
mi_oveja.hablar()


# ## Herencia multiple
# 
# En Python es posible realizar herencia múltiple. En otros posts hemos visto como se podía crear una clase padre que heredaba de una clase hija, pudiendo hacer uso de sus métodos y atributos. La herencia múltiple es similar, pero una clase hereda de varias clases padre en vez de una sola.
# 
# Veamos un ejemplo. Por un lado tenemos dos clases Clase1 y Clase2, y por otro tenemos la Clase3 que hereda de las dos anteriores. Por lo tanto, heredará todos los métodos y atributos de ambas.

# In[2]:


#Clase 1
class Clase1:
    #Contructor 1
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    
    def dialogo1(self):
        print("Soy la clase 1 y tengo {} y {} como valores".format(self.valor1,self.valor2))
        
#Clase 2
class Clase2:
    #Contructor 2
    def __init__(self, valor3, valor4):
        self.valor3 = valor3
        self.valor4 = valor4
        
    def dialogo2(self):
        print("Soy la clase 2 y tengo {} y {} como valores".format(self.valor3,self.valor4))
        
#Clase con herencia multiple
class Clase3(Clase1, Clase2):
    #Contructor multiple
    def __init__(self, valor1, valor2, valor3, valor4, valor5, valor6):
        #Mandamos argumentos a los padres
        Clase1.__init__(self, valor1, valor2)
        Clase2.__init__(self, valor3, valor4)
        self.valor5 = valor5
        self.valor6 = valor6
    
    def dialogo3(self):
        print("Soy la clase 3 y tengo {} y {} como valores".format(self.valor5,self.valor6))
    


# In[3]:


obj1 = Clase3(1,2,3,4,5,6)
obj1.dialogo1()
obj1.dialogo2()
obj1.dialogo3()


# Es posible también que una clase herede de otra clase y a su vez otra clase herede de la anterior.

# In[4]:


class Clase4:
    pass
class Clase5(Clase4):
    pass
class Clase6(Clase5):
    pass


# # INTERFACES
# En la programación orientada a objetos, un interfaz define al conjunto de métodos que tiene que tener un objeto para que pueda cumplir una determinada función en nuestro sistema. Dicho de otra manera, un interfaz define como se comporta un objeto y lo que se puede hacer con el.
# 
# #### Ejemplo 1 - Interfaces formales
# Los interfaces formales pueden ser definidas en Python utilizando el módulo por defecto llamado ABC (Abstract Base Classes). Los abc fueron añadidos a Python en la PEP3119.
# Simplemente definen una forma de crear interfaces (a través de metaclases) en los que se definen unos métodos (pero no se implementan) y donde se fuerza a las clases que usan ese interfaz a implementar los métodos. 
# 
# El interfaz más sencillo que podemos crear es de la siguiente manera, heredando de abc.ABC.

# In[10]:


from abc import ABC
class Mando(ABC):
    pass


# La siguiente sintaxis es también válida, y aunque se sale del contenido de este capítulo, es importante que asocies el módulo abc con las metaclases.

# In[11]:


from abc import ABCMeta
class Mando(metaclass=ABCMeta):
    pass


# En este ejemplo podemos observar como se usa el decorador @abstractmethod.
# 
# Un método abstracto es un método que no tiene una implementación, es decir, que no lleva código. Un método definido con este decorador, forzará a las clases que implementen dicho interfaz a codificarlo.
# 
# Veamos como queda nuestro interfaz formal Mando.

# In[31]:


#Importaciones
from abc import abstractmethod
from abc import ABCMeta

#Interface
class Mando(metaclass=ABCMeta):
    #Metodo abstracto
    @abstractmethod
    def siguiente_canal(self):
        pass

    @abstractmethod
    def canal_anterior(self):
        pass

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass


# In[32]:


class MandoSamsung(Mando):
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")


# In[35]:


#No se puede crear un obj mando
try:
    mando = Mando()
except TypeError:
    print("Error, No se puede crear un Objeto mando con metodos astraptos", end="\n\n")
#Obj MandoSamsung
mandoSng = MandoSamsung()
mandoSng.siguiente_canal()
mandoSng.canal_anterior()
mandoSng.subir_volumen()
mandoSng.bajar_volumen()


# # HILOS EN PYTHON
# 
# Un hilo es un proceso del sistema operativo con características distintas de las de un proceso normal:
# 
# * Los hilos existen como subconjuntos de los procesos.
# * Los hilos comparten memoria y recursos.
# * Los hilos ocupan una dirección diferente en la memoria
# 
# En Python 2.X se pueden crear hilos utilizando el módulo threads y en Python 3.X se pueden crear utilizando el módulo _threads. El módulo threading será utilizado para interactuar con el módulo _threads.
# 
# ¿Cuando implementar hilos? Cuando se quiera ejecutar una función al mismo tiempo que se ejecuta un programa. Cuando se crea software para servidores se quiere que el servidor no reciba solo una sino múltiples conexiones. En pocas palabras, los hilos permiten completar varias tareas al mismo tiempo.
# 
# ### Ejemplo 1 con hilos ( se iniciaran 10. Cada uno imprimirá su ID)

# In[63]:


#Importacion
import threading
# Clase hilo
class MiHilo(threading.Thread):
    
    #Constructor
    def __init__(self,x):
        self.__x = x
        threading.Thread.__init__(self)
    
     # run() se utiliza para definir el comportamiento del hilo
    def run (self): 
        print(str(self.__x))
            
            
# Iniciamos 3 hilos.
for i in range(3):
    #Iniciamos
    MiHilo(i).start()
    #Pausamos
    sleep(1)


# ### Hilos Cronometrados en Python:
# En python, la clase Timer (temporizador) es una subclase de la clase Threads (hilos). Esto significa que se comporta de manera similar. La clase Timer puede ser utilizada para crear hilos temporizados. Los temporizadores son iniciados con el método .start() al igual que los hilos normales. El siguiente programa crea un hilo que se inicia luego de 3 segundos:

# In[69]:


from threading import *
def hola():
    #Pausamos
    sleep(1)
    print("Hola mundo!, soy el hilo {}".format(1))
# Creacion del hilo
t = Timer(3,hola)      # Timer() recibe como primer parámetro el intervalo de tiempo que será usado
                       # y como segundo parámetro la función a ejecutar. También recibe como 3er parámetro
# Ejecución del Hilo   # argumentos (args) y como 4to parametro argumentos de palabras clave (kwargs)
t.start()              # Por defecto, ambos tienen como valor 'None'


# # FUNCIONES CON TEMPORIZADOR
# 
# ### Uso de la función time.time() en Python
# 
# #### Esta función devuelve el tiempo en segundos. 
# 
# Son los segundos que pasan después de la época: el 1 de enero de 1970, 00:00:00 (UTC). Esta función utiliza el tiempo establecido del sistema informático para devolver la salida, es decir, el número de segundos.

# In[47]:


#Importacion
import time

#Optenemos el tiempo actual
start = time.time()

#Bucle de 1 a 20,0000
for r in range(1,200000):
    pass

#Optenemos el tiempo actual
end = time.time()

#A el final le restamos el inicio
print(format(end-start))


# Entre start y end, aparece el cuerpo principal del código. Aquí, se toma como ejemplo un bucle for.
# Producción:

# ### Uso de la función time.Process_time() en Python
# 
# #### Esta función devuelve el tiempo en fracciones de segundo.
# 
#  La referencia de tiempo de todo el proceso también se registra en la función y no solo el tiempo transcurrido durante el proceso.

# In[49]:


#Importacione
from time import process_time, sleep

#Tiempo inicial
start = process_time()  

#Estructura repetitiva
for r in range(20):
    print(r, end=" ")

#Tiempo final
end = process_time()

#Salida
print(end, start)
print(end-start)


# El tiempo empleado en time.sleep() no se mide con esta función, lo que significa que solo mide la diferencia de tiempo entre dos referencias de tiempo consecutivas.
# 
# ### Uso de la función time.Perf_counter en Python
# 
# #### Esta función solo debe aplicarse a procesos pequeños ya que es muy precisa.
# 
# También conocida como Contador de rendimiento, esta función ayuda a obtener el conteo de tiempo entre dos referencias de una manera más precisa. Esta función solo debe aplicarse a procesos pequeños ya que es muy precisa.
# 
# También podemos usar time.sleep() entre esta función. Con esta función, la ejecución del código puede suspenderse durante varios segundos. La función sleep() toma un valor flotante como argumento.
# 
# 

# In[53]:


#Importaciones
from time import perf_counter, sleep

#Segundos a tardar
segundos = 3

#Inicio
start = perf_counter()  

#Bucle
for r in range(n): 
    #Segundo actual
    print("Segundo {}".format(r+1))
    #Pausa en segundos
    sleep(1)

#Final
end = perf_counter() 

#Calcular tiempo trascurrido
print(end-start)


# In[ ]:




