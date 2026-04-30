#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:

a = 8
if (a < 8):
    print('La varriable es mayor a cero ')
elif (a > 0):
    print('La variable es mayor a cero')
else:
    print('lavariable es igual a cero')



# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:

a = 4
b = 'Hola'
  
if ( type(a) == type(b)):
    print('Las Variables son del mismo tipo de dato')

else:
    print('Las variables son de datos distintos')



# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar

# In[7]:

for i in range(1, 21):
    if i % 2 == 0:
        print('El numero', str(i), 'es par')
    else:
        print('El numero', str(i), 'es impar')



# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

for i in range(0,6):
     print('Valor:', str(i), 'Elevado a la 3° potencia', str(i ** 3))



# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

numero = 5

for i in range(numero):
    print("Ciclo", i + 1)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
numero = 5 

if type(numero) == int and numero > 0:
    factorial = 1
    while numero > 0:
        factorial *= numero
        numero -= 1

        print(factorial)
    else:
        print("Debe ingresar un numero entero mayor a 0")




# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:

contador = 1

while contador <= 3:
    print("vuelta del While", contador)

    for i in range(1, 4):
       print(" Ciclo for:", i)
    contador += 1



# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:
for i in range(1, 4):
    print("Vuelta del for:", i)
    contador = 1

    while contador <= 3:
        print (" Ciclo While:", contador)
               
        contador += 1




# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

for numero in range (0, 31):
    es_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False

        break
    
    if es_primo:
        print(numero)


# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:
Tope_rango = 30
n = 0
primo = True
while(n < Tope_rango):
    for div in range(2, n):
        if (n % div == 0):
            primo = False
    if (primo):
        print(n)
    else:
        primo = True

    n += 1 




# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:

# CON BREAK
ciclos_con_break = 0
n = 2

while n < tope_rango:
    primo = True

    for div in range(2, n):
        ciclos_con_break += 1

        if n % div == 0:
            primo = False
            break

    n += 1

print("Cantidad de ciclos con break:", ciclos_con_break)


# In[57]:

tope_rango = 30

# SIN BREAK
ciclos_sin_break = 0
n = 2

while n < tope_rango:
    primo = True

    for div in range(2, n):
        ciclos_sin_break += 1

        if n % div == 0:
            primo = False

    n += 1

print("Cantidad de ciclos sin break:", ciclos_sin_break)




# 12) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:

n = 100
while n <= 300:
    if n % 12 != 0:
        n += 1
        continue
    print(n)
    n += 1



# 13) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:

numero = int(input("Ingrese un numero: "))
while True:
    if numero > 1:
        primo = True

        for div in range(2, numero):
            if numero % div == 0:
                primo = False
                break

        if primo:
            print(numero, "es primo")
        else:
            print(numero, "no es primo")
    else:
        print("Debe ingresar un numero mayor a 1")

    opcion = input("¿Desea buscar el siguiente numero (s/n):")
    
    if opcion.lower() == "s":
            numero += 1
    else:
        break



# 14) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]:

numero = 100

while numero <= 300:
    if numero % 3 == 0 and numero % 6 == 0:
        print(numero)
        break
    numero +=1

