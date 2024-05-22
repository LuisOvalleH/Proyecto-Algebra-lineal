from fractions import Fraction

from UI.List import List


class Matrix():
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = List()
        self.matrix_sum = None
        self.matrix_subtract = None
        self.matrix_multiply = None
        self.matrix_inverse_result = None
        self.matrix_determinant = None
        self.matrix_gauss = None
        self.matrix_rref = None
        self.matrix_transpose = None

    def insert(self, data: str):
        data = Fraction(data)
        self.matrix.append(data)

    def sum(self, Matrix_2):
        if self.rows != Matrix_2.rows or self.columns != Matrix_2.columns:
            raise ValueError("Las matrices deben tener las mismas dimensiones para sumarse")
        result = "Proceso de la suma:\n"
        matrix_result = Matrix(self.rows, self.columns)

        for _ in range(self.rows):
            for _ in range(self.columns):
                value_1 = self.value()
                value_2 = Matrix_2.value()
                sum_value = value_1 + value_2
                result += f"{value_1} + {value_2} = {sum_value}\n"
                matrix_result.insert(sum_value)

        self.matrix_sum = matrix_result

        return result

    def subtract(self, Matrix_2):
        if self.rows != Matrix_2.rows or self.columns != Matrix_2.columns:
            raise ValueError("Las matrices deben tener las mismas dimensiones para restarse")
        result = "Proceso de la resta:\n"
        matrix_result = Matrix(self.rows, self.columns)

        for _ in range(self.rows):
            for _ in range(self.columns):
                value_1 = self.value()
                value_2 = Matrix_2.value()
                rest_value = value_1 - value_2
                result += f"{value_1} - {value_2} = {rest_value}\n"
                matrix_result.insert(rest_value)


        self.matrix_subtract = matrix_result

        return result

    def multiply(self, Matrix_2):
        if self.columns != Matrix_2.rows:
            raise ValueError(
                "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz "
                "para multiplicarlas")

        result = "Proceso de la multiplicación:\n"
        matrix_result = Matrix(self.rows, Matrix_2.columns)

        for i in range(self.rows):
            for j in range(Matrix_2.columns):
                sum_product = Fraction(0)
                for k in range(self.columns):
                    value_1 = self.get_value(i, k)
                    value_2 = Matrix_2.get_value(k, j)
                    product = value_1 * value_2
                    sum_product += product
                    result += f"{value_1} * {value_2} = {product}\n"
                matrix_result.insert(str(sum_product))
                result += f"Suma de productos para posición ({i + 1},{j + 1}) = {sum_product}\n"

        self.matrix_multiply = matrix_result

        return result

    def inverse_matrix(self):
        if self.rows != self.columns:
            raise ValueError("La matriz debe ser cuadrada para calcular su inversa")

        A = [[self.get_value(i, j) for j in range(self.columns)] for i in range(self.rows)]
        n = self.rows
        I = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
        result = "Proceso del cálculo de la inversa:\n"

        for i in range(n):
            max_el = abs(A[i][i])
            max_row = i
            for k in range(i + 1, n):
                if abs(A[k][i]) > max_el:
                    max_el = abs(A[k][i])
                    max_row = k

            if i != max_row:
                A[i], A[max_row] = A[max_row], A[i]
                I[i], I[max_row] = I[max_row], I[i]
                result += f"Intercambiar fila {i + 1} con fila {max_row + 1}\n"

            diag_element = A[i][i]
            for j in range(n):
                A[i][j] /= diag_element
                I[i][j] /= diag_element
            result += f"Dividir fila {i + 1} por {diag_element}\n"

            for k in range(n):
                if k != i:
                    factor = A[k][i]
                    for j in range(n):
                        A[k][j] -= factor * A[i][j]
                        I[k][j] -= factor * I[i][j]
                    result += f"Fila {k + 1} - ({factor}) * Fila {i + 1}\n"

        self.matrix_inverse_result = Matrix(self.rows, self.columns)
        for row in I:
            for value in row:
                self.matrix_inverse_result.insert(str(value))

        result += f"\nInversa de la matriz: \n{self.matrix_inverse_result}\n"
        return result

    def get_value(self, row, col):
        index = row * self.columns + col
        return Fraction(self.matrix.find_at(index).data)

    def value(self):
        x = self.matrix.shift()
        value = x
        self.insert(x)
        return Fraction(value)

    def determinant(self):
        if self.rows != self.columns:
            raise ValueError("La matriz debe ser cuadrada para calcular su determinante")

        A = [[self.get_value(i, j) for j in range(self.columns)] for i in range(self.rows)]
        n = self.rows
        det = Fraction(1)
        result = "Proceso del cálculo del determinante:\n"

        for i in range(n):

            max_el = abs(A[i][i])
            max_row = i
            for k in range(i + 1, n):
                if abs(A[k][i]) > max_el:
                    max_el = abs(A[k][i])
                    max_row = k

            if i != max_row:
                A[i], A[max_row] = A[max_row], A[i]
                det *= -1
                result += f"Intercambiar fila {i + 1} con fila {max_row + 1}\n"

            for k in range(i + 1, n):
                if A[i][i] == 0:
                    continue
                c = -A[k][i] / A[i][i]
                for j in range(i, n):
                    if i == j:
                        A[k][j] = 0
                    else:
                        A[k][j] += c * A[i][j]
                result += f"Fila {k + 1} - ({-c}) * Fila {i + 1}\n"


        for i in range(n):
            det *= A[i][i]

        self.matrix_gauss = Matrix(self.rows, self.columns)
        for row in A:
            for value in row:
                self.matrix_gauss.insert(str(value))

        self.matrix_determinant = det
        result += f"\nDeterminante: {det}\n"
        return result

    def range(self):
        A = [[self.get_value(i, j) for j in range(self.columns)] for i in range(self.rows)]
        n, m = self.rows, self.columns
        rank = 0
        result = "Proceso del cálculo del rango:\n"

        for row in range(n):
            if all(A[row][j] == 0 for j in range(m)):
                continue
            rank += 1
            for i in range(row + 1, n):
                if A[i][row] != 0:
                    factor = A[i][row] / A[row][row]
                    for j in range(m):
                        A[i][j] -= factor * A[row][j]
                    result += f"Fila {i + 1} - ({factor}) * Fila {row + 1}\n"

        self.matrix_rref = Matrix(n, m)
        for row in A:
            for value in row:
                self.matrix_rref.insert(str(value))

        result += f"\nRango de la matriz: {rank}\n"
        return result

    def transpose(self):
        # Crear una nueva matriz con filas y columnas intercambiadas
        transposed_matrix = Matrix(self.columns, self.rows)

        for i in range(self.rows):
            for j in range(self.columns):
                value = self.get_value(i, j)
                # Insertar el valor en la nueva posición transpuesta
                transposed_matrix.insert(str(value))

        transposed_matrix = self.matrix_transpose

        return transposed_matrix

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



