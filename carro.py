
'''for i in range(0, 11, 2):
    print(i)'''

# lista o arreglo
'''lista = [12, 23, 6, [3, 4, "alberto", 5]]

print(lista)  # mostrar toda la lista

print(lista[2])  # mostrar una posicion de la lisa
print(lista[3])  # muestra la lista dentro de la otra lista
# muestra la lista dentro de la otra lista en la posicionn 2
print(lista[3][2])

lista2 = lista[0:3]  # coger solo los 3 primeros posiciones de la lista
print(lista2)
lista[1] = "andres" # reemplaza la posicion 1 por andres
print(lista)'''

# tuplas
tupla = (1, 2, "juan", False)
print(tupla)
# se recorren lo mismo que las listas
# a la tupla no le puede agrgar elementos ni tampoco modificar ese es la diferencia con las listas

diccionario = {
    'clave': 2,
    'variable': "cinco",
    5: 'alberto'
}

print(diccionario['clave'])
print(diccionario[5])
diccionario['clave'] = False  # reemplazo  el valor de variable
