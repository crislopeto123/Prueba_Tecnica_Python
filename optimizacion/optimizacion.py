def procesar_datos(datos):

    resultado = []
    for numero in datos:
        if numero % 2 == 0:
            resultado.append(numero * 2)
        else:
            resultado.append(numero * 3)
    return resultado
