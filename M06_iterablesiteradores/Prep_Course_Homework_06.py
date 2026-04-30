#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:

lista = []
n = -15
while n <= -1:
    lista.append(n)
    n += 1
    print(lista)



# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:

i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        print(lista[i])
    i += 1 



# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:

for numero in lista:
    if numero % 2 == 0:
        print(numero)



# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
for numero in lista[:3]:
    print(numero)



# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
for indice, numero in enumerate(lista):
    print(indice, numero)



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:

lista = [1,2,5,7,10,13,14,15,17,28]

for n in range(1,21):
    if n not in lista:
        lista.append(n)
    lista.sort()
    print(lista)    



# In[11]:


n = 1



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:
fibonacci = [0,1]
while len(fibonacci) < 30:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
    print(fibonacci)




# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:

print(sum(fibonacci))


# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:

for i in range(len(fibonacci)-1, len(fibonacci)-6, -1):
    print(fibonacci[i -1] / fibonacci[i])


# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:

cadena = "Hola Mundo, esto es una practica de lenguaje python"
for i, letra in enumerate(cadena):
    if letra == 'n':
        print(i)




# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:

diccionario = {"nombe":"Kobac","edad":30, "pais":"Peru"}
for clave in diccionario:
    print(clave)



# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:
diccionario = {"nombe":"Kobac","edad":30, "pais":"Peru"}
for clave in diccionario:
    print(clave)




# In[45]:

lista_cadena = list(cadena)
for letra in lista_cadena:
    print(letra)



# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:
lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]

tupla_zip = tuple(zip(lista1, lista2))
print(tupla_zip) 




# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:

lis = [18, 21, 29, 32, 35, 42, 56, 60, 63, 71, 84, 90, 91, 100 ]
nueva = []
for num in lis:
    if num % 7 == 0:
        nueva.append(num)
        print(nueva)



# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:

lis = [[1, 2, 3, 4],"rojo","verde",[True, False, False],["uno","dos", "tres"]]
       
contador = 0

for elemento in lis:
        if type(elemento) == list:
           contador += len(elemento)
        else:
           contador += 1
print(contador)

# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:

nueva_lista = []
for elemento in lis:
    if type(elemento) == list:
        nueva_lista.append(elemento)
    else:
        nueva_lista.append([elemento])
print(nueva_lista)

