
def temperaturaa(temp):
    suma_de_temp = 0

    for tempe in temp:
        suma_de_temp += tempe  # vamos a sumar los valores denro delarreglo
    # len cuenta cuanos valores hay denro del arreglo
    return suma_de_temp / len(temp)


if __name__ == "__main__":

    temp = [25, 15, 12, 30, 20]

    average = temperaturaa(temp)
    print('la temperatura promedio es:', average)
