import math
import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, \
    QScrollArea, QMessageBox, QMainWindow
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.plot_cartesian_plane()

    def plot_vector(self, x, y):
        self.axes.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1)
        self.draw()

    def plot_cartesian_plane(self):
        self.axes.axhline(y=0, color='k')  # Eje X
        self.axes.axvline(x=0, color='k')  # Eje Y
        self.axes.set_xlim(-15, 15)
        self.axes.set_ylim(-15, 15)
        self.axes.set_xticks(range(-15, 16, 1))
        self.axes.set_yticks(range(-15, 16, 1))
        self.axes.grid(True)


class Vectores_grafic(QMainWindow):

    def __init__(self,x ,y ,*args, **kwargs):
        super(Vectores_grafic, self).__init__(*args, **kwargs)
        self.setGeometry(185, 100, 1150, 650)
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        # Aquí defines tus vectores (x, y)

        self.canvas.plot_vector(x, y)

        self.show()


class Vectores_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.rows_1 = 0
        self.columns_1 = 0
        self.result = None
        self.x = None
        self.y = None
        self.matrix_result = None
        self.setWindowTitle("Vectores")
        self.setGeometry(550, 210, 450, 400)

        # establecer logo de la ventana

        icono = QIcon("calculadora.png")
        self.setWindowIcon(icono)

        self.layout = QVBoxLayout()

        encabezado_layout = QHBoxLayout()

        self.logo_label = QLabel()
        pixmap = QPixmap("Calculadora.png").scaled(65, 65)
        self.logo_label.setPixmap(pixmap)
        encabezado_layout.addWidget(self.logo_label)

        title_label = QLabel("Operaciones con vectores")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        aux_label = QLabel()
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(title_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)

        self.layout.addLayout(encabezado_layout)

        self.button_sum_vectores = QPushButton("Suma de vectores")
        self.button_sum_vectores.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.button_sum_vectores.setFont(QFont("Arial", 11))
        self.button_sum_vectores.clicked.connect(self.sum_vectores_funtion)
        self.layout.addWidget(self.button_sum_vectores)

        self.button_product_punto = QPushButton("Producto punto de vectores")
        self.button_product_punto.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.button_product_punto.setFont(QFont("Arial", 11))
        self.button_product_punto.clicked.connect(self.produc_vectores_fuction)
        self.layout.addWidget(self.button_product_punto)

        self.setLayout(self.layout)

    def delete_button(self):
        self.button_sum_vectores.deleteLater()
        self.button_product_punto.deleteLater()

    def grafic(self):
        if self.x is not None and self.y is not None:
            self.window_grafic = Vectores_grafic(self.x, self.y)
            self.window_grafic.show()
        else:
            inputs = [
                self.x_1.text(),
                self.x_2.text(),
                self.y_1.text(),
                self.y_2.text(),
            ]

            for x in inputs:
                if self.is_number(x):
                    pass
                else:
                    QMessageBox.warning(self, "Error de validación",
                                        "Únicamente se pueden ingresar datos numéricos.")
                    return
            self.calculate_sum_fuction()
            self.window_grafic = Vectores_grafic(self.x, self.y)
            self.window_grafic.show()


    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False


    def calculate_sum_fuction(self):
        inputs = [
            self.x_1.text(),
            self.x_2.text(),
            self.y_1.text(),
            self.y_2.text(),
        ]

        for x in inputs:
            if self.is_number(x):
                pass
            else:
                QMessageBox.warning(self, "Error de validación",
                                    "Únicamente se pueden ingresar datos numéricos.")
                return

        x_1 = float(self.x_1.text())
        x_2 = float(self.x_2.text())
        y_1 = float(self.y_1.text())
        y_2 = float(self.y_2.text())

        result = f"{x_1} + {x_2} = {x_1 + x_2}\n"
        result += f"{y_1} + {y_2} = {y_1 + y_2}\n"

        x = x_1 + x_2
        self.x = x
        y = y_1 + y_2
        self.y = y
        magnitude = math.sqrt(x ** 2 + y ** 2)
        angle_radians = math.atan2(y, x)
        angle_degrees = math.degrees(angle_radians)

        result += f"Vector: ({x},{y})\n"
        result += f"Magnitud: {magnitude}\n"
        result += f"Angulo: {angle_degrees}"

        self.result = result
        self.create_result_area()




    def calculate_product_punto(self):

        inputs = [
            self.input_1.text(),
            self.input_2.text(),
            self.input_3.text(),
            self.input_4.text(),
            self.input_5.text(),
            self.input_6.text()
        ]

        for x in inputs:
            if self.is_number(x):
                pass
            else:
                QMessageBox.warning(self, "Error de validación",
                                    "Únicamente se pueden ingresar datos numéricos.")
                return

        x_1 = float(self.input_1.text())
        x_2 = float(self.input_2.text())
        x_3 = float(self.input_3.text())
        x_4 = float(self.input_4.text())
        x_5 = float(self.input_5.text())
        x_6 = float(self.input_6.text())

        result = f"{x_1} * {x_4} = {x_1 * x_4}\n"
        result += f"{x_2} * {x_5} = {x_2 * x_5}\n"
        result += f"{x_3} * {x_6} = {x_3 * x_6}\n"

        value = 0
        for i in range(3):
            if i == 0:
                x = x_1 * x_4
                value += x
            if i == 1:
                x = x_2 * x_5
                value += x
            if i == 2:
                x = x_3 * x_6
                value += x

        result += f"\nEl producto punto es: {value}"

        self.result = result
        self.create_result_area()




    def produc_vectores_fuction(self):
        self.delete_button()

        layout = QHBoxLayout()
        layout_1 = QVBoxLayout()
        layout_2 = QVBoxLayout()

        vector_1_label = QLabel("Vector 1:")
        vector_1_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout_1.addWidget(vector_1_label)

        self.input_1 = QLineEdit()
        self.input_1.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_1.addWidget(self.input_1)

        self.input_2 = QLineEdit()
        self.input_2.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_1.addWidget(self.input_2)

        self.input_3 = QLineEdit()
        self.input_3.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_1.addWidget(self.input_3)

        vector_2_label = QLabel("Vector 2:")
        vector_2_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout_2.addWidget(vector_2_label)

        self.input_4 = QLineEdit()
        self.input_4.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_2.addWidget(self.input_4)

        self.input_5 = QLineEdit()
        self.input_5.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_2.addWidget(self.input_5)

        self.input_6 = QLineEdit()
        self.input_6.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_2.addWidget(self.input_6)

        layout.addLayout(layout_1)
        layout.addLayout(layout_2)

        self.layout.addLayout(layout)

        result_label = QLabel("Resultado:")
        result_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        self.layout.addWidget(result_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        self.produc_button = QPushButton("Producto Punto Vectores")
        self.produc_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.produc_button.clicked.connect(self.calculate_product_punto)
        self.produc_button.setFont(QFont("Arial", 11))
        self.layout.addWidget(self.produc_button)



    def sum_vectores_funtion(self):
        self.delete_button()
        layout = QHBoxLayout()
        layout_1 = QVBoxLayout()
        layout_1_1 = QHBoxLayout()
        layout_2 = QVBoxLayout()
        layout_2_1 = QHBoxLayout()

        vector_1_label = QLabel("Vector 1:")
        vector_1_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout_1.addWidget(vector_1_label)

        x_1_label = QLabel("x:")
        x_1_label.setFont(QFont("Arial", 11))
        layout_1_1.addWidget(x_1_label)

        self.x_1 = QLineEdit()
        self.x_1.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_1_1.addWidget(self.x_1)

        y_1_label = QLabel("y:")
        y_1_label.setFont(QFont("Arial", 11))
        layout_1_1.addWidget(y_1_label)

        self.y_1 = QLineEdit()
        self.y_1.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_1_1.addWidget(self.y_1)

        layout_1.addLayout(layout_1_1)

        vector_2_label = QLabel("Vector 2:")
        vector_2_label.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        layout_2.addWidget(vector_2_label)

        x_2_label = QLabel("x:")
        x_2_label.setFont(QFont("Arial", 11))
        layout_2_1.addWidget(x_2_label)

        self.x_2 = QLineEdit()
        self.x_2.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_2_1.addWidget(self.x_2)

        y_2_label = QLabel("y:")
        y_2_label.setFont(QFont("Arial", 11))
        layout_2_1.addWidget(y_2_label)

        self.y_2 = QLineEdit()
        self.y_2.setStyleSheet("height: 23px; border-radius: 10px; border: 2px  white;")
        layout_2_1.addWidget(self.y_2)

        layout_2.addLayout(layout_2_1)

        layout.addLayout(layout_1)
        layout.addLayout(layout_2)

        self.layout.addLayout(layout)

        result_label = QLabel("Resultado:")
        result_label.setFont(QFont("Arial", 11, QFont.Weight.Bold))
        self.layout.addWidget(result_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        self.sum_button = QPushButton("Sumar Vectores")
        self.sum_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.sum_button.clicked.connect(self.calculate_sum_fuction)
        self.sum_button.setFont(QFont("Arial", 11))
        self.layout.addWidget(self.sum_button)

        self.grafic_button = QPushButton("Mostrar grafico")
        self.grafic_button.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.grafic_button.clicked.connect(self.grafic)
        self.grafic_button.setFont(QFont("Arial", 11))
        self.layout.addWidget(self.grafic_button)

    def create_result_area(self):
        # Layout principal vertical
        main_layout = QVBoxLayout()

        title_label = QLabel("Proceso y resultado: ")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        main_layout.addWidget(title_label)

        result_label = QLabel(f"{self.result}")
        result_label.setFont(QFont("Arial", 11))
        main_layout.addWidget(result_label)

        # Widget contenedor para el layout principal
        container_widget = QWidget()
        container_widget.setLayout(main_layout)
        self.scroll_area.setWidget(container_widget)

    def closeEvent(self, event):
        self.window_closed.emit()
        super().closeEvent(event)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Vectores_window()
    window.show()
    sys.exit(app.exec())