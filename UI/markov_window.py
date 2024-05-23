import sys
import numpy as np
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, \
    QScrollArea, QMessageBox, QSpinBox, QTextEdit


class Matrix_markov_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.rows_1 = 3
        self.columns_1 = 3
        self.setWindowTitle("Cadena de Markov")
        self.setGeometry(400, 210, 850, 400)

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

        title_label = QLabel("Cadena de Markov")
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

        string_label = QLabel("Ingrese las veces a operar: ")
        string_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout.addWidget(string_label)

        self.spin_box = QSpinBox(self)
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(1000)
        self.spin_box.setValue(1)
        self.spin_box.setStyleSheet("""
            QSpinBox {
                height: 33px;
                border-radius: 10px;
                border: 2px ;
                padding-right: 11px; /* Ajustar el padding para evitar problemas con los botones */
            }
            QSpinBox::up-button, QSpinBox::down-button {
                width: 18px;
                border-radius: 9px;  /* Bordes redondeados */
                background-color: #a9e159;  /* Color de fondo */
                border: 1px solid #6b8e23;  /* Color del borde */
            }
            QSpinBox::up-button {
                subcontrol-position: top right;
                subcontrol-origin: border;
                margin: 1px; /* Margen opcional para espacio */
            }
            QSpinBox::down-button {
                subcontrol-position: bottom right;
                subcontrol-origin: border;
                margin: 1px; /* Margen opcional para espacio */
            }
            QSpinBox::up-arrow, QSpinBox::down-arrow {
                width: 10px;
                height: 10px;
                background-color: transparent; /* Fondo transparente para las flechas */
            }
            QSpinBox::up-arrow {
                image: url(arriba.png);  /* Ruta a la imagen de la flecha hacia arriba */
            }
            QSpinBox::down-arrow {
                image: url(abajo.png);  /* Ruta a la imagen de la flecha hacia abajo */
            }
        """)
        layout.addWidget(self.spin_box)

        layout_matrix = QHBoxLayout()
        layout_matrix_principal = QVBoxLayout()
        layout_matrix_markov = QVBoxLayout()

        matrix_label = QLabel("Matriz (principal): ")
        matrix_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout_matrix_principal.addWidget(matrix_label)

        self.create_matrix_input_1(layout_matrix_principal)

        matrix_label_porcentaje = QLabel("Matriz (porcentaje): ")
        matrix_label_porcentaje.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout_matrix_markov.addWidget(matrix_label_porcentaje)

        self.create_matrix_input_2(layout_matrix_markov)

        layout_matrix.addLayout(layout_matrix_principal)

        x_layout = QVBoxLayout()

        q_label = QLabel("             ")
        x_layout.addWidget(q_label)

        x_layout.addWidget(q_label)

        layout_matrix.addLayout(x_layout)

        layout_matrix.addLayout(layout_matrix_markov)

        layout.addLayout(layout_matrix)

        self.confirm_button = QPushButton("Confirmar")
        self.confirm_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.confirm_button.setFont(QFont("Arial", 11))
        self.confirm_button.clicked.connect(self.calculate_markov)

        result_layout = QVBoxLayout()
        result_label = QLabel("Resultado:")
        result_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        result_layout.addWidget(result_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        self.result_text.setFont(QFont("Arial", 12))
        self.scroll_area.setWidget(self.result_text)
        result_layout.addWidget(self.scroll_area)

        aux_layout.addLayout(layout)
        aux_layout.addLayout(result_layout)

        main_layout.addLayout(aux_layout)
        main_layout.addWidget(self.confirm_button)

        self.setLayout(main_layout)

    def create_matrix_input_1(self, layout: QVBoxLayout):
        matrix_layout = QVBoxLayout()
        self.matrix_inputs_1 = []
        for row_index in range(self.rows_1):
            row_layout = QHBoxLayout()
            row_inputs = []
            for column_index in range(self.columns_1):
                input_field = QLineEdit()
                input_field.setObjectName(f"input_row_1_{row_index}_{column_index}")
                input_field.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
                row_layout.addWidget(input_field)
                row_inputs.append(input_field)
            self.matrix_inputs_1.append(row_inputs)
            matrix_layout.addLayout(row_layout)
        layout.addLayout(matrix_layout)

    def create_matrix_input_2(self, layout: QVBoxLayout):
        matrix_layout = QVBoxLayout()
        self.matrix_inputs_2 = []
        for row_index in range(self.rows_1):
            row_layout = QHBoxLayout()
            row_inputs = []
            input_field = QLineEdit()
            input_field.setObjectName(f"input_row_2_{row_index}_0")
            input_field.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
            row_layout.addWidget(input_field)
            row_inputs.append(input_field)
            self.matrix_inputs_2.append(row_inputs)
            matrix_layout.addLayout(row_layout)
        layout.addLayout(matrix_layout)

    def get_matrix_data(self, inputs):
        rows = len(inputs)
        cols = len(inputs[0])
        matrix = np.zeros((rows, cols))
        for i in range(rows):
            for j in range(cols):
                try:
                    matrix[i, j] = float(inputs[i][j].text())
                except ValueError:
                    raise ValueError(f"Entrada inválida en la posición [{i + 1}, {j + 1}]. Por favor, ingrese un número.")
        return matrix

    def check_column_sums(self, matrix):
        cols = matrix.shape[1]
        for col in range(cols):
            col_sum = np.sum(matrix[:, col])
            if not np.isclose(col_sum, 1.0):
                return False, col + 1  # Devolver el índice de la columna que no suma 1
        return True, None

    def calculate_markov(self):
        try:
            transicion = self.get_matrix_data(self.matrix_inputs_1)
            matriz = self.get_matrix_data(self.matrix_inputs_2)
            iteraciones = self.spin_box.value()
        except ValueError as e:
            QMessageBox.warning(self, "Error de entrada", str(e))
            return

        valid_transicion, col_transicion = self.check_column_sums(transicion)
        valid_matriz, col_matriz = self.check_column_sums(matriz)

        if not valid_transicion:
            QMessageBox.warning(self, "Error de validación", f"La columna {col_transicion} de la matriz principal no suma 1.")
            return
        if not valid_matriz:
            QMessageBox.warning(self, "Error de validación", f"La columna {col_matriz} de la matriz de porcentaje no suma 1.")
            return

        estado_actual = matriz
        resultado_texto = "Método de Markov:\n"
        for i in range(iteraciones):
            resultado = np.dot(transicion, estado_actual)
            resultado_texto += f"\nIteración {i + 1}:\n"
            resultado_texto += "Matriz Resultante:\n"
            resultado_texto += f"{resultado}\n"
            estado_actual = resultado

        resultado_texto += "\nResultado Final:\n"
        resultado_texto += "Matriz Resultante:\n"
        resultado_texto += f"{estado_actual}\n"
        self.result_text.setPlainText(resultado_texto)

    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Matrix_markov_window()
    window.show()
    sys.exit(app.exec())


