import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")
        self.setFixedSize(450, 500)

        font_title = QFont("Calibri", 24, QFont.Bold)
        font_input = QFont("sans-serif", 18)
        font_output = QFont("Calibri", 28)
        font_emoji = QFont("Segoe UI Emoji", 60)
        font_description = QFont("Calibri", 20)

        self.city_label = QLabel("Enter city name:")
        self.city_label.setFont(font_title)
        self.city_label.setAlignment(Qt.AlignCenter)

        self.city_input = QLineEdit()
        self.city_input.setFont(font_input)
        self.city_input.setPlaceholderText("e.g. London")
        self.city_input.setAlignment(Qt.AlignCenter)

        self.get_weather_button = QPushButton("Get Weather")
        self.get_weather_button.setFont(font_input)

        self.temperature_label = QLabel("")
        self.temperature_label.setFont(font_output)
        self.temperature_label.setAlignment(Qt.AlignCenter)

        self.emoji_label = QLabel("")
        self.emoji_label.setFont(font_emoji)
        self.emoji_label.setAlignment(Qt.AlignCenter)

        self.description_label = QLabel("")
        self.description_label.setFont(font_description)
        self.description_label.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        vbox.setSpacing(15)
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addStretch()
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        vbox.addStretch()

        self.setLayout(vbox)
        self.apply_styles()

        self.get_weather_button.clicked.connect(self.get_weather)

    def apply_styles(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f7fa;
            }
            QLineEdit, QPushButton {
                padding: 10px;
                border-radius: 10px;
                border: 2px solid #ccc;
            }
            QLineEdit {
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #4caf50;
                color: white;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

    def get_weather(self):
        api_key = "Enter ur api key inside of this string" # API-KEY !IMPORTANT!
        city = self.city_input.text().strip()

        if not city:
            self.display_error("Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=en"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as err:
            if response.status_code == 404:
                self.display_error("City not found.")
            elif response.status_code == 401:
                self.display_error("Invalid API key.")
            else:
                self.display_error(f"HTTP Error: {err}")
        except requests.exceptions.RequestException:
            self.display_error("Network error. Please check your internet connection.")

    def display_weather(self, data):
        temperature_c = data["main"]["temp"]
        weather_id = data["weather"][0]["id"]
        description = data["weather"][0]["description"].capitalize()

        self.temperature_label.setText(f"{temperature_c:.1f}°C")
        self.emoji_label.setText(self.get_weather_emoji(weather_id))
        self.description_label.setText(description)

    def display_error(self, message):
        QMessageBox.critical(self, "Error", message)
        self.temperature_label.clear()
        self.emoji_label.clear()
        self.description_label.clear()

    @staticmethod
    def get_weather_emoji(weather_id):
        if 200 <= weather_id <= 232:
            return "⛈"
        elif 300 <= weather_id <= 321:
            return "🌦"
        elif 500 <= weather_id <= 531:
            return "🌧"
        elif 600 <= weather_id <= 622:
            return "❄"
        elif 701 <= weather_id <= 741:
            return "🌫"
        elif weather_id == 800:
            return "☀"
        elif 801 <= weather_id <= 804:
            return "☁"
        else:
            return "🌈"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
