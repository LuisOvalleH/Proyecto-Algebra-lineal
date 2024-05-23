import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
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



