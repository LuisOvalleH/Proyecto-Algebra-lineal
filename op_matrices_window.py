import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QComboBox, QLineEdit


class Op_matrices_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selcción de proporción")
        self.setGeometry(550, 210, 450, 400)

        # establecer logo de la ventana

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

        # option area
        option_layout = QVBoxLayout()
        rows_layout = QHBoxLayout()
        columns_layout = QHBoxLayout()

        self.rows_label = QLabel("Ingresar numero de filas:")
        self.rows_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        rows_layout.addWidget(self.rows_label)

        self.input_rows = QLineEdit()
        self.input_rows.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        rows_layout.addWidget(self.input_rows)

        self.columns_label = QLabel("Ingresar numero de Columnas:")
        self.columns_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        columns_layout.addWidget(self.columns_label)

        self.input_columns = QLineEdit()
        self.input_columns.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        columns_layout.addWidget(self.input_columns)

        self.confirm_button = QPushButton("Confirmar")
        self.confirm_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.confirm_button.setFont(QFont("Arial", 11))

        option_layout.addLayout(rows_layout)
        option_layout.addLayout(columns_layout)
        option_layout.addWidget(self.confirm_button)

        self.matrix_1_text = QLabel("Matriz 1: ")
        self.matrix_1_text.setFont(QFont("Arial", 10, QFont.Weight.Bold))

        self.matrix_2_text = QLabel("Matriz 2: ")
        self.matrix_2_text.setFont(QFont("Arial", 10, QFont.Weight.Bold))

        self.sum_button = QPushButton("Sumar")
        self.sum_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.sum_button.setFont(QFont("Arial", 11))

        self.rest_button = QPushButton("Restar")
        self.rest_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.rest_button.setFont(QFont("Arial", 11))

        self.multiplicacion_button = QPushButton("Multiplicar")
        self.multiplicacion_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.multiplicacion_button.setFont(QFont("Arial", 11))

        self.product_button = QPushButton("Producto punto a punto")
        self.product_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.product_button.setFont(QFont("Arial", 11))

        layout.addLayout(encabezado_layout)
        layout.addLayout(option_layout)
        layout.addWidget(self.matrix_1_text)
        layout.addWidget(self.matrix_2_text)
        layout.addWidget(self.sum_button)
        layout.addWidget(self.rest_button)
        layout.addWidget(self.multiplicacion_button)
        layout.addWidget(self.product_button)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Op_matrices_window()
    window.show()
    sys.exit(app.exec())
