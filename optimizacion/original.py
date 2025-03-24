def procesar_datos_original(datos):
    resultado = []
    for i in range(len(datos)):
        if datos[i] % 2 == 0:
            resultado.append(datos[i] * 2)
        else:
            resultado.append(datos[i] * 3)
    return resultado