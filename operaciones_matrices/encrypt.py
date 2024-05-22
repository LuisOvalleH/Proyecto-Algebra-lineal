from UI.List import List
# Diccionarios de mapeo
letra_a_numero = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
    'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26, ' ': 27
}

numero_a_letra = {v: k for k, v in letra_a_numero.items()}

def cifrar(mensaje):
    mensaje = mensaje.upper()
    lista_cifrada = List()
    for letra in mensaje:
        lista_cifrada.append(letra_a_numero[letra])
    return lista_cifrada

def descifrar(lista_cifrada):
    descifrado = ''
    for numero in lista_cifrada:
        descifrado += numero_a_letra[numero]
    return descifrado

