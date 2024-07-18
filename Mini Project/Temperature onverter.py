import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt

class TemperatureConverterApp(QMainWindow):
    def __init(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Temperature Converter")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout()
        input_layout = QHBoxLayout()
        result_layout = QHBoxLayout()

        self.temperature_label = QLabel("Temperature:")
        self.temperature_input = QLineEdit()
        self.temperature_input.setFixedWidth(100)

        self.from_unit_label = QLabel("From Unit (F or C):")
        self.from_unit_input = QLineEdit()
        self.from_unit_input.setFixedWidth(50)

        self.to_unit_label = QLabel("To Unit (F or C):")
        self.to_unit_input = QLineEdit()
        self.to_unit_input.setFixedWidth(50)

        self.convert_button = QPushButton("Convert")
        self.convert_button.setFixedWidth(100)
        self.convert_button.clicked.connect(self.convert_temperature)

        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)

        input_layout.addWidget(self.temperature_label)
        input_layout.addWidget(self.temperature_input)
        input_layout.addWidget(self.from_unit_label)
        input_layout.addWidget(self.from_unit_input)
        input_layout.addWidget(self.to_unit_label)
        input_layout.addWidget(self.to_unit_input)

        result_layout.addWidget(self.convert_button)
        result_layout.addWidget(self.result_label)

        main_layout.addLayout(input_layout)
        main_layout.addLayout(result_layout)

        self.central_widget.setLayout(main_layout)

    def convert_temperature(self):
        temperature_text = self.temperature_input.text()
        from_unit_text = self.from_unit_input.text().upper()
        to_unit_text = self.to_unit_input.text().upper()

        if not temperature_text.replace(".", "").isdigit():
            self.result_label.setText("Invalid temperature format. Please enter a number.")
            return

        if from_unit_text not in ["F", "C"] or to_unit_text not in ["F", "C"]:
            self.result_label.setText("Invalid unit. Please use 'F' for Fahrenheit or 'C' for Celsius.")
            return

        temperature = float(temperature_text)

        if from_unit_text == "F" and to_unit_text == "C":
            converted_temperature = (temperature - 32) * 5/9
        elif from_unit_text == "C" and to_unit_text == "F":
            converted_temperature = (temperature * 9/5) + 32
        else:
            converted_temperature = temperature

        self.result_label.setText(f"{temperature}°{from_unit_text} is equal to {converted_temperature:.2f}°{to_unit_text}")

def main():
    app = QApplication(sys.argv)
    converter_app = TemperatureConverterApp()
    converter_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
