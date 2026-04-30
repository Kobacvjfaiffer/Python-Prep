#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

ciudades = ["Lima","Madrid","Tokio","Roma","Paris","Bogota"]
print(ciudades)


# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

print(ciudades[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

print(ciudades[1:4])



# 4) Visualizar el tipo de dato de la lista

# In[12]:

print(type(ciudades))



# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:


print(ciudades[2:])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:

print(ciudades[:4])

    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

ciudades.append("Lima")
ciudades.append("Santiago")
print(ciudades)







# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

ciudades.insert(3, "Buenos Aires")
print(ciudades)



# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:
otras = ("Miami","Toronto")
ciudades += otras
print(ciudades)



# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

print(ciudades.index("Lima"))



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

print(ciudades.index(Berlin))



# 12) Eliminar un elemento de la lista

# In[25]:

ciudades.remove("Roma")
print(ciudades)



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

ciudades.remove("Berlin")



# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:

ultima = ciudades.pop()
print(ultima)
print(ciudades)



# 15) Mostrar la lista multiplicada por 4

# In[29]:

print(ciudades * 4)


# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:

tupla = tuple(range(1, 21))
print(tupla)


# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:

print(tupla[10:16])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:


print(20 in tupla)
print(30 in tupla)


# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:

mensaje = " "
if "Paris" in ciudades:
    mensaje = "Paris ya existe"

else:
    ciudades.append("Paris")
    mensaje = "Paris fue agregada"

print(mensaje)



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

print(tupla.count(10))
print(ciudades.count("Lima"))



# 21) Convertir la tupla en una lista

# In[52]:

lista_tupla = list(tupla)
print (lista_tupla)



# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:


a, b, c = tupla[:3]
print(a, b, c)


# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:

diccionario = {
    "ciudad": ciudades, "Paris":"Varios", "Continente":"Varios"
}
print(diccionario)




# 24) Imprimir las claves del diccionario

# In[59]:

print(diccionario.keys())



# 25) Imprimir las ciudades a través de su clave

# In[61]:

print(diccionario["ciudad"])


