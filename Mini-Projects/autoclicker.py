import sys
import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal, QTimer

TOGGLE_KEY = KeyCode(char="z")

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
            time.sleep(0.0001)

class AutoClickerApp(QWidget):
    update_status_signal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

        self.click_thread = threading.Thread(target=clicker, daemon=True)
        self.click_thread.start()

        self.listener = Listener(on_press=self.toggle_event)
        self.listener.start()

        self.update_status_signal.connect(self.update_status)

    def initUI(self):
        self.setWindowTitle("Auto Clicker")
        self.setFixedSize(300, 200)

        font = "Calibre"
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: """ + font + """;
            }
            QPushButton {
                padding: 10px;
                border-radius: 10px;
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
                cursor: pointer;
            }
            QPushButton:hover {
                background-color: #45a049;
                color: white;
            }
            QLabel {
                font-size: 18px;
                text-align: center;
                padding: 10px;
            }
        """)

        self.status_label = QLabel("Clicking: INACTIVE", self)
        self.toggle_button = QPushButton("Toggle Auto-Clicker", self)

        self.toggle_button.clicked.connect(self.toggle_clicker)

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.toggle_button)
        self.setLayout(layout)

    def toggle_clicker(self):
        global clicking
        if not clicking:
            self.toggle_button.setEnabled(False)
            QTimer.singleShot(2000, self.start_clicking)
            self.status_label.setText("Clicking: WAITING 2s...")
        else:
            clicking = False
            self.update_status()

    def start_clicking(self):
        global clicking
        clicking = True
        self.update_status()

    def update_status(self):
        if clicking:
            self.status_label.setText("Clicking: ACTIVE")
        else:
            self.status_label.setText("Clicking: INACTIVE")

    def toggle_event(self, key):
        global clicking
        if key == TOGGLE_KEY:
            clicking = not clicking
            self.update_status_signal.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AutoClickerApp()
    window.show()
    sys.exit(app.exec_())
