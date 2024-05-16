def sumar_matrices(matrix_1, matrix_2):
    # Verificar si las matrices tienen las mismas dimensiones
    if len(matrix_1) != len(matrix_2) or len(matrix_1[0]) != len(matrix_2[0]):
        raise ValueError("Las matrices deben tener las mismas dimensiones.")

    # Sumar las matrices elemento por elemento
    resultado = []
    for i in range(len(matrix_1)):
        fila = []
        for j in range(len(matrix_1[0])):
            suma = float(matrix_1[i][j]) + float(matrix_2[i][j])
            fila.append(suma)
        resultado.append(fila)
    return resultado