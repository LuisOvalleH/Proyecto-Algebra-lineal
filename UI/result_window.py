from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class Result_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self, result: str):
        super().__init__()

        self.setWindowTitle("Operaciones con matrices")
        self.setGeometry(550, 210, 250, 200)

        icono = QIcon("calculadora.png")
        self.setWindowIcon(icono)

        layout = QVBoxLayout()

        title_label = QLabel("Proceso y resultado")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        layout.addWidget(title_label)

        result_label = QLabel(f"{result}")
        result_label.setFont(QFont("Arial", 11))
        layout.addWidget(result_label)

        self.setLayout(layout)