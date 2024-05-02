import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QPixmap, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton


class Main_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana principal")
        self.setGeometry(550, 210, 450, 400)

        # establecer logo de la ventana

        icono = QIcon("calculadora.png")
        self.setWindowIcon(icono)

        main_layout = QVBoxLayout()
        encabezado_layout = QHBoxLayout()

        logo_label = QLabel()
        pixmap = QPixmap("Calculadora.png").scaled(65, 65)
        logo_label.setPixmap(pixmap)
        encabezado_layout.addWidget(logo_label)

        title_label = QLabel("Calculadora Algebra Lineal")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        aux_label = QLabel()
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(title_label)
        encabezado_layout.addWidget(aux_label)
        encabezado_layout.addWidget(aux_label)

        button_layout = QVBoxLayout()

        self.op_matrices = QPushButton("Operaciones con matrices")
        self.op_matrices.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.op_matrices.setFont(QFont("Arial", 11))
        button_layout.addWidget(self.op_matrices)

        self.matriz_inversa = QPushButton("Matriz Inversa")
        self.matriz_inversa.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.matriz_inversa.setFont(QFont("Arial", 11))
        button_layout.addWidget(self.matriz_inversa)

        self.matriz_determinante = QPushButton("Determinante de una Matriz")
        self.matriz_determinante.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.matriz_determinante.setFont(QFont("Arial", 11))
        button_layout.addWidget(self.matriz_determinante)

        self.matriz_rango = QPushButton("Rango de una Matriz")
        self.matriz_rango.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.matriz_rango.setFont(QFont("Arial", 11))
        button_layout.addWidget(self.matriz_rango)

        self.matriz_cifrado = QPushButton("Cifrado por Matrices")
        self.matriz_cifrado.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.matriz_cifrado.setFont(QFont("Arial", 11))
        button_layout.addWidget(self.matriz_cifrado)

        self.matriz_markov = QPushButton("Cadena De Markov")
        self.matriz_markov.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.matriz_markov.setFont(QFont("Arial", 11))
        button_layout.addWidget(self.matriz_markov)

        self.op_vectores = QPushButton("Operaciones con vectores")
        self.op_vectores.setStyleSheet(
            "height: 30px; background-color: #a9e159; color: white; border: 2x solid black; border-radius: 13px;")
        self.op_vectores.setFont(QFont("Arial", 11))
        button_layout.addWidget(self.op_vectores)

        main_layout.addLayout(encabezado_layout)
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_window()
    window.show()
    sys.exit(app.exec())
