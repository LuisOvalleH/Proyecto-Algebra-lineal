import sys
from PyQt6.QtWidgets import QApplication
from UI.main_window import Main_window



def main():
    app = QApplication(sys.argv)
    main_window = Main_window()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
