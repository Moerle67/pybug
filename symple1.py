import sys
from PyQt6.QtWidgets import QApplication, QWidget

def main():

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(400, 250)
    w.move(300, 300)

    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec())


if __name__ == '__main__':
    main()
