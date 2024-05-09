import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit
from operaciones_matrices.sumar import sumar_matrices  # Asegúrate de que la ruta sea correcta

class Op_matrices_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selección de proporción")
        self.setGeometry(550, 210, 450, 400)

        # establecer logo de la ventana
        icono = QIcon("calculadora.png")
        self.setWindowIcon(icono)

        layout = QVBoxLayout()

        encabezado_layout = QHBoxLayout()
        logo_label = QLabel()
        pixmap = QPixmap("calculadora.png").scaled(65, 65)
        logo_label.setPixmap(pixmap)
        encabezado_layout.addWidget(logo_label)

        title_label = QLabel("Operaciones con Matrices")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        aux_label = QLabel()
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(title_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)

        # option area
        option_layout = QVBoxLayout()
        dimensions_layout = QHBoxLayout()
        matrix_1 = QVBoxLayout()
        rows_layout_1 = QHBoxLayout()
        columns_layout_1 = QHBoxLayout()

        matrix_2 = QVBoxLayout()
        rows_layout_2 = QHBoxLayout()
        columns_layout_2 = QHBoxLayout()

        self.matrix_1_text = QLabel("Matriz 1: ")
        self.matrix_1_text.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        matrix_1.addWidget(self.matrix_1_text)

        self.rows_label = QLabel("Ingresar numero de filas:")
        self.rows_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        rows_layout_1.addWidget(self.rows_label)

        self.input_rows_1 = QLineEdit()
        self.input_rows_1.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        rows_layout_1.addWidget(self.input_rows_1)

        self.columns_label = QLabel("Ingresar numero de Columnas:")
        self.columns_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        columns_layout_1.addWidget(self.columns_label)

        self.input_columns_1 = QLineEdit()
        self.input_columns_1.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        columns_layout_1.addWidget(self.input_columns_1)

        self.matrix_2_text = QLabel("Matriz 2: ")
        self.matrix_2_text.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        matrix_2.addWidget(self.matrix_2_text)

        self.rows_label_2 = QLabel("Ingresar numero de filas:")
        self.rows_label_2.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        rows_layout_2.addWidget(self.rows_label_2)

        self.input_rows = QLineEdit()
        self.input_rows.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        rows_layout_2.addWidget(self.input_rows)

        self.columns_label = QLabel("Ingresar numero de Columnas:")
        self.columns_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        columns_layout_2.addWidget(self.columns_label)

        self.input_columns = QLineEdit()
        self.input_columns.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        columns_layout_2.addWidget(self.input_columns)

        self.confirm_button = QPushButton("Confirmar")
        self.confirm_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.confirm_button.setFont(QFont("Arial", 11))
        self.confirm_button.clicked.connect(self.init_op_sistem)

        matrix_1.addLayout(rows_layout_1)
        matrix_1.addLayout(columns_layout_1)
        dimensions_layout.addLayout(matrix_1)

        matrix_2.addLayout(rows_layout_2)
        matrix_2.addLayout(columns_layout_2)
        dimensions_layout.addLayout(matrix_2)
        option_layout.addLayout(dimensions_layout)
        option_layout.addWidget(self.confirm_button)

        layout.addLayout(encabezado_layout)
        layout.addLayout(option_layout)

        self.setLayout(layout)

    def create_matrix_input_1(self, layout: QVBoxLayout):
        matrix_layout = QVBoxLayout()
        rows = int(self.input_rows_1.text())
        columns = int(self.input_columns_1.text())
        self.matrix_1_ = QLabel("Matriz 1: ")
        self.matrix_1_.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        matrix_layout.addWidget(self.matrix_1_)

        for _ in range(rows):
            row_layout = QHBoxLayout()
            for _ in range(columns):
                self.input_row = QLineEdit()
                self.input_row.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
                row_layout.addWidget(self.input_row)

            matrix_layout.addLayout(row_layout)

        layout.addLayout(matrix_layout)

    def create_matrix_input_2(self, layout: QVBoxLayout):
        matrix_layout = QVBoxLayout()
        rows = int(self.input_rows.text())
        columns = int(self.input_columns.text())
        self.matrix_2_ = QLabel("Matriz 2: ")
        self.matrix_2_.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        matrix_layout.addWidget(self.matrix_2_)

        for _ in range(rows):
            row_layout = QHBoxLayout()
            for _ in range(columns):
                self.input_row = QLineEdit()
                self.input_row.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
                row_layout.addWidget(self.input_row)

            matrix_layout.addLayout(row_layout)

        layout.addLayout(matrix_layout)

    def init_op_sistem(self):
        layout = self.layout()
        self.setGeometry(550, 90, 450, 400)

        self.create_matrix_input_1(layout)
        self.create_matrix_input_2(layout)

        self.sum_button = QPushButton("Sumar")
        self.sum_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.sum_button.setFont(QFont("Arial", 11))
        self.sum_button.clicked.connect(self.sumar_matrices)

        layout.addWidget(self.sum_button)

    def sumar_matrices(self):
        # Obtener las matrices ingresadas por el usuario
        matrix_1 = self.get_matrix_from_input(self.input_rows_1, self.input_columns_1)
        matrix_2 = self.get_matrix_from_input(self.input_rows, self.input_columns)

        try:
            # Sumar las matrices utilizando la función importada
            resultado = sumar_matrices(matrix_1, matrix_2)
            self.mostrar_resultado(resultado)
        except ValueError as e:
            self.mostrar_error(str(e))

    def get_matrix_from_input(self, input_rows, input_columns):
        rows = int(input_rows.text())
        columns = int(input_columns.text())
        matrix = []
        for i in range(rows):
            row = []
            for j in range(columns):
                value = self.input_row.text()

                if value.strip():
                    row.append(float(value))
            matrix.append(row)
        return matrix

    def mostrar_resultado(self, resultado):
        print("Resultado:", resultado)  # Implementa cómo deseas mostrar el resultado

    def mostrar_error(self, mensaje):
        print("Error:", mensaje)  # Implementa cómo deseas mostrar el error

    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Op_matrices_window()
    window.show()
    sys.exit(app.exec())