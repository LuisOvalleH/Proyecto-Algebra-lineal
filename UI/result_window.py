from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QSizePolicy


class Result_window(QWidget):
    window_closed = pyqtSignal()

    def __init__(self, result: str):
        super().__init__()

        self.setWindowTitle("Operaciones con matrices")
        self.setGeometry(550, 210, 250, 200)

        icono = QIcon("calculadora.png")
        self.setWindowIcon(icono)

        # Layout principal vertical
        main_layout = QVBoxLayout()

        title_label = QLabel("Proceso y resultado")
        title_label.setFont(QFont("Arial", 15, QFont.Weight.Bold))
        main_layout.addWidget(title_label)

        result_label = QLabel(f"{result}")
        result_label.setFont(QFont("Arial", 11))
        result_label.setWordWrap(True)  # Permitir que el texto se envuelva
        main_layout.addWidget(result_label)

        # Widget contenedor para el layout principal
        container_widget = QWidget()
        container_widget.setLayout(main_layout)

        # ScrollArea para contener el widget contenedor
        scroll_area = QScrollArea()
        scroll_area.setWidget(container_widget)
        scroll_area.setWidgetResizable(True)

        # Layout horizontal para centrar el scroll area
        outer_layout = QHBoxLayout()
        outer_layout.addStretch()
        outer_layout.addWidget(scroll_area)
        outer_layout.addStretch()

        self.setLayout(outer_layout)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.resize(400, 300)  # Tamaño inicial de la ventana



