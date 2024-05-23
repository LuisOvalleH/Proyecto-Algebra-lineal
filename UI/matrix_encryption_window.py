import sys
import numpy as np
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QScrollArea, QMessageBox
from operaciones_matrices.Matrix import Matrix


lista = []
key = []


mapping = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8,
    'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'ñ': 15,
    'o': 16, 'p': 17, 'q': 18, 'r': 19, 's': 20, 't': 21, 'u': 22,
    'v': 23, 'w': 24, 'x': 25, 'y': 26, 'z': 27, ' ': 28, '0': 29,
    '1': 30, '2': 31, '3': 32, '4': 33, '5': 34, '6': 35, '7': 36,
    '8': 37, '9': 38, '.': 39, ',': 40, ':': 41, ';': 42, '?': 43,
    '!': 44, '"': 45, '(': 46, ')': 47, '[': 48, ']': 49,
    '{': 50, '}': 51, '@': 52, '#': 53, '$': 54, '%': 55, '&': 56,
    '*': 57, '+': 58, '-': 59, '/': 60, '|': 61, '<': 62,
    '>': 63, '=': 64, '_': 65, '^': 66, '`': 67, '~': 68
}

def encrypt(text):
    lista.clear()
    for letra in text:
        lista.append(mapping.get(letra.lower(), 'Opción Incorrecta!'))
    size()

def size():
    while len(lista) % 3 != 0:
        lista.append(28)

def matriz_reversed(matriz):
    try:
        inversa = np.linalg.inv(matriz)
        return inversa
    except np.linalg.LinAlgError:
        return None

class Matrix_encryption_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.rows_1 = 0
        self.columns_1 = 0
        self.result = None
        self.matrix_result = None
        self.setWindowTitle("Cifrado de Matrices")
        self.setGeometry(400, 210, 750, 400)

        # establecer logo de la ventana
        icono = QIcon("calculadora.png")
        self.setWindowIcon(icono)

        main_layout = QVBoxLayout()
        aux_layout = QHBoxLayout()
        layout = QVBoxLayout()

        encabezado_layout = QHBoxLayout()
        logo_label = QLabel()
        pixmap = QPixmap("Calculadora.png").scaled(65, 65)
        logo_label.setPixmap(pixmap)
        encabezado_layout.addWidget(logo_label)

        title_label = QLabel("Cifrado de matrices")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        aux_label = QLabel()
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(title_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)

        main_layout.addLayout(encabezado_layout)

        string_label = QLabel("Ingrese el mensaje a encriptar:")
        string_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(string_label)

        self.string_input = QLineEdit()
        self.string_input.setStyleSheet("height: 33px; border-radius: 10px; border: 2px  white;")
        layout.addWidget(self.string_input)

        matrix_label = QLabel("Matriz (llave): ")
        matrix_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(matrix_label)

        self.create_matrix_input_1(layout)

        self.confirm_button = QPushButton("Confirmar")
        self.confirm_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.confirm_button.clicked.connect(self.confirm_button_action)
        self.confirm_button.setFont(QFont("Arial", 11))

        result_layout = QVBoxLayout()
        result_label = QLabel("Resultado:")
        result_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        result_layout.addWidget(result_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        result_layout.addWidget(self.scroll_area)

        aux_layout.addLayout(layout)
        aux_layout.addLayout(result_layout)

        main_layout.addLayout(aux_layout)
        main_layout.addWidget(self.confirm_button)

        self.setLayout(main_layout)

    def confirm_button_action(self):
        message = (self.string_input.text()).strip()
        encrypt(message)
        prefix = "matrix_input"

        key.clear()

        for row_index in range(3):
            row = []
            for column_index in range(3):
                try:
                    element = getattr(self, f"{prefix}_{row_index}_{column_index}")
                    value = float(element.text())
                except ValueError:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Warning)
                    msg.setWindowTitle("Error de caracteres")
                    msg.setText("El valor ingresado no es un número válido. Por favor, revise los datos e intente nuevamente.")
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                    msg.exec()
                    return
                row.append(value)
            key.append(row)

        key_np = np.array(key)
        number_columns = -(-len(lista) // 3)
        matrix = np.zeros((3, number_columns))

        for il, valor in enumerate(lista):
            rows = il % 3
            columns = il // 3
            matrix[rows, columns] = valor

        # Mostrar el proceso de cifrado
        result = f'Texto convertido a números:\n{lista}\n\n'
        result += f'Matriz de texto antes del cifrado:\n{matrix}\n\n'
        result += f'Matriz de llave:\n{key_np}\n\n'

        matrix_cifrada = np.dot(key_np, matrix)
        result += f'Matriz cifrada:\n{matrix_cifrada}\n\n'

        matrix_reversed_np = matriz_reversed(key_np)
        if matrix_reversed_np is None:
            result += "La matriz de llave no es invertible.\n"
            self.result = result
        else:
            matrix_original = np.dot(matrix_reversed_np, matrix_cifrada)
            result += f'Matriz inversa de la llave:\n{matrix_reversed_np}\n\n'
            result += f'Matriz descifrada (texto original):\n{matrix_original}\n\n'

            # Convertir la matriz descifrada de vuelta a texto
            texto_descifrado = []
            for i in range(matrix_original.shape[1]):
                for j in range(3):
                    valor = round(matrix_original[j, i])
                    letra = next((k for k, v in mapping.items() if v == valor), '?')
                    texto_descifrado.append(letra)
            result += f'Texto descifrado:\n{"".join(texto_descifrado).strip()}\n'

            self.result = result
            self.create_result_area()

    def create_matrix_input_1(self, layout: QVBoxLayout):
        matrix_layout = QVBoxLayout()
        rows = 3
        columns = 3
        self.rows_1 = 3
        self.columns_1 = 3
        for row_index in range(rows):
            row_layout = QHBoxLayout()
            for column_index in range(columns):
                self.input_row_1_ = QLineEdit()
                self.input_row_1_.setObjectName(f"input_row_1_{row_index}_{column_index}")  # Asignar un nombre único
                self.input_row_1_.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
                row_layout.addWidget(self.input_row_1_)
                setattr(self, f"matrix_input_{row_index}_{column_index}", self.input_row_1_)  # Establecer el atributo dinámico

            matrix_layout.addLayout(row_layout)

        layout.addLayout(matrix_layout)

    def create_result_area(self):
        # Layout principal vertical
        main_layout = QVBoxLayout()

        title_label = QLabel("Resultados del cifrado")
        title_label.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        title_label.setStyleSheet("margin-top: 5px;")
        main_layout.addWidget(title_label)

        # Layout horizontal para la matriz
        result_matrix_layout = QVBoxLayout()

        # Recorrer las filas de la matriz_result
        result = self.result.split("\n")
        for row_index, row_data in enumerate(result):
            row_layout = QHBoxLayout()
            row_label = QLabel(row_data)
            row_label.setFont(QFont("Arial", 10))
            row_layout.addWidget(row_label)
            result_matrix_layout.addLayout(row_layout)

        # Layout para el resultado
        matrix_layout = QHBoxLayout()

        matrix_widget = QWidget()
        matrix_widget.setLayout(result_matrix_layout)
        self.scroll_area.setWidget(matrix_widget)

        main_layout.addLayout(matrix_layout)

        self.setLayout(main_layout)

    def get_matrix_input_text(self, rows, columns, prefix):
        matrix = Matrix(rows, columns)
        for row_index in range(rows):
            for column_index in range(columns):
                input_row = getattr(self, f"{prefix}_{row_index}_{column_index}")
                matrix.matrix.append(input_row.text())
        return matrix

    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Matrix_encryption_window()
    window.show()
    sys.exit(app.exec())

