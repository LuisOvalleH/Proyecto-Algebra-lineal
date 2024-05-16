import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit

class Op_matrices_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selección de proporción")
        self.setGeometry(550, 210, 450, 400)

        # Establecer logo de la ventana
        icono = QIcon("calculadora.png")
        self.setWindowIcon(icono)

        layout = QVBoxLayout()
        encabezado_layout = QHBoxLayout()

        logo_label = QLabel()
        pixmap = QPixmap("Calculadora.png").scaled(65, 65)
        logo_label.setPixmap(pixmap)
        encabezado_layout.addWidget(logo_label)

        title_label = QLabel("Operaciones con Matrices")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        aux_label = QLabel()
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(title_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)

        # Área de opciones
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

        self.rows_label = QLabel("Ingresar número de filas:")
        self.rows_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        rows_layout_1.addWidget(self.rows_label)

        self.input_rows_1 = QLineEdit()
        self.input_rows_1.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        rows_layout_1.addWidget(self.input_rows_1)

        self.columns_label = QLabel("Ingresar número de Columnas:")
        self.columns_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        columns_layout_1.addWidget(self.columns_label)

        self.input_columns_1 = QLineEdit()
        self.input_columns_1.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        columns_layout_1.addWidget(self.input_columns_1)

        self.matrix_2_text = QLabel("Matriz 2: ")
        self.matrix_2_text.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        matrix_2.addWidget(self.matrix_2_text)

        self.rows_label_2 = QLabel("Ingresar número de filas:")
        self.rows_label_2.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        rows_layout_2.addWidget(self.rows_label_2)

        self.input_rows_2 = QLineEdit()
        self.input_rows_2.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        rows_layout_2.addWidget(self.input_rows_2)

        self.columns_label_2 = QLabel("Ingresar número de Columnas:")
        self.columns_label_2.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        columns_layout_2.addWidget(self.columns_label_2)

        self.input_columns_2 = QLineEdit()
        self.input_columns_2.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        columns_layout_2.addWidget(self.input_columns_2)

        self.confirm_button = QPushButton("Confirmar")
        self.confirm_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.confirm_button.setFont(QFont("Arial", 11))
        self.confirm_button.clicked.connect(lambda: self.init_op_sistem(layout))

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

        for row_index in range(rows):
            row_layout = QHBoxLayout()
            for column_index in range(columns):
                input_row = QLineEdit()
                input_row.setObjectName(f"input_row_1_{row_index}_{column_index}")  # Asignar un nombre único
                input_row.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
                row_layout.addWidget(input_row)
                setattr(self, f"input_row_1_{row_index}_{column_index}", input_row)  # Establecer el atributo dinámico

            matrix_layout.addLayout(row_layout)

        layout.addLayout(matrix_layout)

    def create_matrix_input_2(self, layout: QVBoxLayout):
        matrix_layout = QVBoxLayout()
        rows = int(self.input_rows_2.text())
        columns = int(self.input_columns_2.text())

        self.matrix_2_ = QLabel("Matriz 2: ")
        self.matrix_2_.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        matrix_layout.addWidget(self.matrix_2_)

        for row_index in range(rows):
            row_layout = QHBoxLayout()
            for column_index in range(columns):
                input_row = QLineEdit()
                input_row.setObjectName(f"input_row_2_{row_index}_{column_index}")  # Asignar un nombre único
                input_row.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
                row_layout.addWidget(input_row)
                setattr(self, f"input_row_2_{row_index}_{column_index}", input_row)  # Establecer el atributo dinámico

            matrix_layout.addLayout(row_layout)

        layout.addLayout(matrix_layout)

    def get_matrix_input_text(self, rows, columns, prefix):
        matrix_text = []
        for row_index in range(rows):
            row_text = []
            for column_index in range(columns):
                input_row = getattr(self, f"{prefix}_{row_index}_{column_index}")
                row_text.append(input_row.text())
            matrix_text.append(row_text)
        return matrix_text

    def init_op_sistem(self, layout: QVBoxLayout):
        self.matrix_1_text.deleteLater()
        self.rows_label.deleteLater()
        self.input_rows_1.deleteLater()
        self.columns_label.deleteLater()
        self.input_columns_1.deleteLater()
        self.matrix_2_text.deleteLater()
        self.rows_label_2.deleteLater()
        self.input_rows_2.deleteLater()
        self.columns_label_2.deleteLater()
        self.input_columns_2.deleteLater()

        self.setGeometry(550, 90, 450, 400)

        self.create_matrix_input_1(layout)
        self.create_matrix_input_2(layout)

        self.sum_button = QPushButton("Sumar")
        self.sum_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.sum_button.setFont(QFont("Arial", 11))
        self.sum_button.clicked.connect(self.sum_matrices)

        self.rest_button = QPushButton("Restar")
        self.rest_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.rest_button.setFont(QFont("Arial", 11))

        self.multiplicacion_button = QPushButton("Multiplicar")
        self.multiplicacion_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.multiplicacion_button.setFont(QFont("Arial", 11))

        self.product_button = QPushButton("Producto punto a punto")
        self.product_button.setStyleSheet(            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.product_button.setFont(QFont("Arial", 11))

        layout.addWidget(self.sum_button)
        layout.addWidget(self.rest_button)
        layout.addWidget(self.multiplicacion_button)
        layout.addWidget(self.product_button)

    def sum_matrices(self):
        rows_1 = int(self.input_rows_1.text())
        columns_1 = int(self.input_columns_1.text())
        matrix_1_text = self.get_matrix_input_text(rows_1, columns_1, "input_row_1")

        rows_2 = int(self.input_rows_2.text())
        columns_2 = int(self.input_columns_2.text())
        matrix_2_text = self.get_matrix_input_text(rows_2, columns_2, "input_row_2")

        # Aquí puedes realizar la suma de las matrices
        print("Matriz 1:")
        for row in matrix_1_text:
            print(row)
        print("Matriz 2:")
        for row in matrix_2_text:
            print(row)

        # Suponiendo que ambas matrices tienen las mismas dimensiones
        result_matrix = []
        for i in range(rows_1):
            result_row = []
            for j in range(columns_1):
                sum_value = float(matrix_1_text[i][j]) + float(matrix_2_text[i][j])
                result_row.append(sum_value)
            result_matrix.append(result_row)

        print("Resultado de la suma:")
        for row in result_matrix:
            print(row)

    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Op_matrices_window()
    window.show()
    sys.exit(app.exec())


