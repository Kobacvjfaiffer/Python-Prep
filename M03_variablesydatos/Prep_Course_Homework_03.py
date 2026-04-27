#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

numero = 10 
print ( numero)



# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))




# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(typt(numero))



# 4) Crear una variable que contenga tu nombre

# In[2]:

nombre = "Kobac_vj_fai"


# 5) Crear una variable que contenga un número complejo

# In[3]:

numero_complejo = 4 + 5j




# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


print(type(numero_complejo))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:
import math
pi = round(math.pi, 4)
print(pi)



# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

texto = 'True'
booleano = True

print(texto)
print(booleano)
print(type(texto))
print(type(booleano))



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(texto))
print(type(booleano))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

resultado = 5 + 3.2
print(resultado)



# 11) Realizar una operación de suma de números complejos

# In[2]:
resultado = (2 + 3j) + (4 + 5j)
print(resultado)




# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
resultado = 5 + (2 + 3j)
print(resultado)




# 13) Realizar una operación de multiplicación

# In[5]:

resultado = 4 * 3
print(resultado)





# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

resultado = 2 ** 8
print(resultado)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

cociente = 27 / 4
print(cociente)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

parte_entera = 27 // 4
print(parte_entera)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

resto = 27 % 4
print(resto)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:

resultado = (3 * 4) + 3
print(resultado)



# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

nombre = "kobac"
apellido = "Faiffer"

resultado = nombre + " "+ apellido
print(resultado)

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:

print("2" == 2)



# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

print(int("2") == 2)



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:

# Da error porque Python espera que los números decimales usen punto (.) y no coma (,).



# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

numero = 3
numero -= 1

print(numero)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

resultado = 1 << 2
print(resultado)

#respuesta 4 (El operador << es un desplazamiento de bits hacia la izquierda. 1 = 0001 ; 4 = 0100



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

TypeError

# 2 → número entero (int)
'# '2' → cadena de texto (str)




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

resultado = str(5) +'3'

