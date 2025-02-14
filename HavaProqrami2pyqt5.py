import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.setGeometry(200, 200, 400, 300)
        
        self.layout = QVBoxLayout()

        self.city_input = QLineEdit(self)
        self.city_input.setPlaceholderText('Enter city name')
        self.layout.addWidget(self.city_input)

        self.get_weather_button = QPushButton('Get Weather', self)
        self.get_weather_button.clicked.connect(self.get_weather)
        self.layout.addWidget(self.get_weather_button)

        self.weather_label = QLabel('Weather details will appear here', self)
        self.layout.addWidget(self.weather_label)

        self.setLayout(self.layout)

    def get_weather(self):
        city = self.city_input.text()
        if city:
            api_key = "your_api_key_here"
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url).json()
            
            if response.get('cod') != 200:
                self.weather_label.setText("City not found")
            else:
                weather = response['weather'][0]['description']
                temperature = response['main']['temp']
                self.weather_label.setText(f"Weather: {weather}\nTemperature: {temperature}°C")
        else:
            self.weather_label.setText("Please enter a city name.")

def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
