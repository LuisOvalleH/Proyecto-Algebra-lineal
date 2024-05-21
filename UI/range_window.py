import sys
from operaciones_matrices.Matrix import Matrix
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, \
    QScrollArea, QComboBox


class Matrix_range_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.rows_1 = 0
        self.columns_1 = 0
        self.result = None
        self.matrix_result = None
        self.setWindowTitle("Rango de una matriz")
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

        title_label = QLabel("Rango de una matriz")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        aux_label = QLabel()
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(title_label)
        encabezado_layout.addWidget(aux_label)
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

        self.matrix_1_text = QLabel("Matriz: ")
        self.matrix_1_text.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        matrix_1.addWidget(self.matrix_1_text)

        self.rows_label = QLabel("Ingresar numero de filas y columnas:")
        self.rows_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        rows_layout_1.addWidget(self.rows_label)

        options = ["1", "2", "3", "4", "5", "6"]

        self.input_rows_1 = QComboBox()
        self.input_rows_1.addItems(options)
        rows_layout_1.addWidget(self.input_rows_1)

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
        rows = int(self.input_rows_1.currentText())
        columns = int(self.input_rows_1.currentText())
        self.rows_1 = int(self.input_rows_1.currentText())
        self.columns_1 = int(self.input_rows_1.currentText())
        self.matrix_1_ = QLabel("Matriz 1: ")
        self.matrix_1_.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        matrix_layout.addWidget(self.matrix_1_)

        for row_index in range(rows):
            row_layout = QHBoxLayout()
            for column_index in range(columns):
                self.input_row_1_ = QLineEdit()
                self.input_row_1_.setObjectName(f"input_row_1_{row_index}_{column_index}")  # Asignar un nombre único
                self.input_row_1_.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
                row_layout.addWidget(self.input_row_1_)
                setattr(self, f"input_row_1_{row_index}_{column_index}",
                        self.input_row_1_)  # Establecer el atributo dinámico

            matrix_layout.addLayout(row_layout)

        layout.addLayout(matrix_layout)

    def calculate_reverse(self):
        prefix_1 = "input_row_1"
        matrix = self.get_matrix_input_text(self.rows_1, self.columns_1, prefix_1)
        self.result = matrix.range()
        self.matrix_result = matrix.matrix_rref
        self.create_result_area()

    def get_matrix_input_text(self, rows, columns, prefix):
        matrix = Matrix(rows, columns)
        for row_index in range(rows):
            for column_index in range(columns):
                input_row = getattr(self, f"{prefix}_{row_index}_{column_index}")
                matrix.matrix.append(input_row.text())
        return matrix

    def delete_create_matrix_button(self):
        self.matrix_1_text.deleteLater()
        self.rows_label.deleteLater()
        self.input_rows_1.deleteLater()
        self.confirm_button.deleteLater()

    def init_op_sistem(self, layout: QVBoxLayout):

        self.delete_create_matrix_button()

        self.setGeometry(550, 60, 450, 680)

        self.create_matrix_input_1(layout)

        result_label = QLabel("Resultado:")
        result_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        layout.addWidget(result_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        layout.addWidget(self.scroll_area)

        self.reverse_button = QPushButton("Calcular Determinante")
        self.reverse_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.reverse_button.clicked.connect(self.calculate_reverse)
        self.reverse_button.setFont(QFont("Arial", 11))

        layout.addWidget(self.reverse_button)

    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)

    def create_result_area(self):
        # Layout principal vertical
        main_layout = QVBoxLayout()

        title_label = QLabel("Proceso y resultado: ")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        main_layout.addWidget(title_label)

        result_label = QLabel(f"{self.result}")
        result_label.setFont(QFont("Arial", 11))
        main_layout.addWidget(result_label)

        matrix_result_layout = QVBoxLayout()

        x = QLabel("Matrix Resultante: ")
        x.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        matrix_result_layout.addWidget(x)

        matrix_result = self.print_matrix()
        matrix_result_layout.addLayout(matrix_result)

        main_layout.addLayout(matrix_result_layout)

        # Widget contenedor para el layout principal
        container_widget = QWidget()
        container_widget.setLayout(main_layout)
        self.scroll_area.setWidget(container_widget)

    def print_matrix(self):
        layout = QVBoxLayout()
        second_layout = QHBoxLayout()
        count = 0
        for i in self.matrix_result.matrix:
            count += 1
            if count != self.matrix_result.columns:
                x = QLabel(f"{i}")
                x.setFont(QFont("Arial", 13, QFont.Weight.Bold))
                x.setAlignment(Qt.AlignmentFlag.AlignCenter)
                second_layout.addWidget(x)
            else:
                x = QLabel(f"{i}")
                x.setFont(QFont("Arial", 13, QFont.Weight.Bold))
                x.setAlignment(Qt.AlignmentFlag.AlignCenter)
                second_layout.addWidget(x)
                layout.addLayout(second_layout)
                second_layout = QHBoxLayout()
                count = 0

        return layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Matrix_range_window()
    window.show()
    sys.exit(app.exec())