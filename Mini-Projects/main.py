'''
BOILER PLATE CODE!!!

# PyQt5 Introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool First GUI")
        self.setGeometry(550, 325, 800, 400)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

    ~This All Is needed for the First Window Application.
    ~Have Fun Programing And Stay Hydrated. ^^
'''

# PyQt5 GUI Introduction.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Cool First GUI")
        self.setGeometry(550, 325, 800, 400)

def main():
    print("Window Has Opened Successfully.")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()