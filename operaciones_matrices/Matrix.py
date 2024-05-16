from fractions import Fraction

from UI.List import List


class Matrix():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = List()
        self.matrix_sum = None
        self.matrix_subtract = None
        self.matrix_multiply= None
        self.matrix_inverse = None
        self.matrix_determinant = None

    def insert(self, data: str):
        data = Fraction(data)
        self.matrix.append(data)

    def sum(self, Matrix_2):
        if self.rows != Matrix_2.rows or self.columns != Matrix_2.columns:
            raise ValueError("Las matrices deben tener las mismas dimensiones para restarse")

        self.matrix_sum = Matrix(self.rows, self.columns)  # Crear una matriz para almacenar el resultado
        result_str = "Proceso de resta:\n"

        for i in range(self.rows):
            for j in range(self.columns):
                # Restar los elementos correspondientes de las dos matrices
                subtract_value = self.get_value(i, j) + Matrix_2.get_value(i, j)
                self.matrix_sum.insert(str(subtract_value))  # Insertar el valor en la matriz de resultado
                result_str += f"{self.get_value(i, j)} + {Matrix_2.get_value(i, j)} = {subtract_value}\n"

        return result_str

    def get_value(self, row, column):
        index = row * self.columns + column
        current_node = self.matrix.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data

    def subtract(self, Matrix_2):
        if self.rows != Matrix_2.rows or self.columns != Matrix_2.columns:
            raise ValueError("Las matrices deben tener las mismas dimensiones para restarse")

        self.matrix_subtract = Matrix(self.rows, self.columns)  # Crear una matriz para almacenar el resultado
        result_str = "Proceso de resta:\n"

        for i in range(self.rows):
            for j in range(self.columns):
                # Restar los elementos correspondientes de las dos matrices
                subtract_value = self.get_value(i, j) - Matrix_2.get_value(i, j)
                self.matrix_subtract.insert(str(subtract_value))  # Insertar el valor en la matriz de resultado
                result_str += f"{self.get_value(i, j)} - {Matrix_2.get_value(i, j)} = {subtract_value}\n"

        return result_str

    def multiply(self, Matrix_2):
        if self.columns != Matrix_2.rows:
            raise ValueError(
                "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz "
                "para multiplicarlas")

        self.matrix_multiply = Matrix(self.rows, Matrix_2.columns)  # Crear una matriz para almacenar el resultado
        result_str = "Proceso de multiplicación:\n"

        for i in range(self.rows):
            for j in range(Matrix_2.columns):
                result = 0
                for k in range(self.columns):
                    result += self.get_value(i, k) * Matrix_2.get_value(k, j)
                self.matrix_multiply.insert(str(result))  # Insertar el valor en la matriz de resultado
                result_str += f"({self.get_value(i, 0)} * {Matrix_2.get_value(0, j)}) + "
                for k in range(1, self.columns):
                    result_str += f"({self.get_value(i, k)} * {Matrix_2.get_value(k, j)})"
                    if k < self.columns - 1:
                        result_str += " + "
                result_str += f" = {result}\n"

        return result_str

    def inverse_matrix(self):
        if self.rows != self.columns:
            raise ValueError("Solo las matrices cuadradas pueden tener una inversa")

        # Crear una matriz identidad de las mismas dimensiones
        identity = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                identity.insert(str(1 if i == j else 0))

        # Crear una copia de la matriz original para trabajar en ella
        augmented = Matrix(self.rows, self.columns * 2)
        for i in range(self.rows):
            for j in range(self.columns):
                augmented.insert(str(self.get_value(i, j)))
            for j in range(self.columns):
                augmented.insert(str(identity.get_value(i, j)))

        # Aplicar eliminación de Gauss-Jordan
        result_str = "Proceso de encontrar la inversa usando Gauss-Jordan:\n"

        for i in range(self.rows):
            # Hacer el elemento diagonal 1
            diag = augmented.get_value(i, i)
            if diag == 0:
                raise ValueError("La matriz no es invertible")
            for j in range(augmented.columns):
                augmented.set_value(i, j, augmented.get_value(i, j) / diag)

            result_str += f"Fila {i} después de dividir por el elemento diagonal {diag}:\n{augmented}\n"

            # Hacer cero los otros elementos en la columna actual
            for k in range(self.rows):
                if k != i:
                    factor = augmented.get_value(k, i)
                    for j in range(augmented.columns):
                        augmented.set_value(k, j, augmented.get_value(k, j) - factor * augmented.get_value(i, j))

                    result_str += f"Fila {k} después de eliminar el elemento {i} usando el factor {factor}:\n{augmented}\n"

        # Extraer la matriz inversa de la parte augmentada
        self.matrix_inverse = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                self.matrix_inverse.insert(str(augmented.get_value(i, j + self.columns)))

        result_str += f"Matriz inversa final:\n{self.matrix_inverse}\n"
        return result_str

    def set_value(self, row, column, value):
        index = row * self.columns + column
        current_node = self.matrix.head
        for _ in range(index):
            current_node = current_node.next
        current_node.data = value

    def value(self):
        x = self.matrix.shift()
        value = x
        self.insert(x)
        return Fraction(value)



    def determinant(self):
        pass

    def range(self):
        pass

    def __str__(self):
        result = ""
        count = 0
        for i in self.matrix:
            count += 1
            if count == 1:
                result += f"[{i} "
            elif count == self.columns:
                result += f"{i}]\n"
                count = 0
            else:
                result += f"{i} "
        return result


# Ejemplo de uso
matrix1 = Matrix(2, 2)
matrix1.insert('1')
matrix1.insert('3')
matrix1.insert('4')
matrix1.insert('5')

matrix2 = Matrix(2, 2)
matrix2.insert('3')
matrix2.insert('4')
matrix2.insert('5')
matrix2.insert('6')

print(matrix1.sum(matrix2))
print(matrix1.matrix_sum)