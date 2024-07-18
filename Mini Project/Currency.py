import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class CurrencyConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.exchange_rates = {
            "USD": 1.0,
            "INR": 83.26, 
            "EUR": 0.8,
            "GBP": 0.95,
            "JPY": 151.0,
        }

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Currency Converter")
        self.setGeometry(100, 100, 400, 250)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.amount_label = QLabel("Amount:")
        self.amount_input = QLineEdit()

        self.from_currency_label = QLabel("From Currency:")
        self.from_currency_input = QLineEdit()
        self.from_currency_input.setText("INR")  # Set the default 'From Currency' to INR

        self.to_currency_label = QLabel("To Currency :")
        self.to_currency_input = QLineEdit()
        self.to_currency_input.setText("USD")  # Set the default 'To Currency' to USD

        self.convert_button = QPushButton("Convert")
        self.convert_button.clicked.connect(self.convert_currency)

        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)  # Align text to center using Qt.AlignCenter

        self.layout.addWidget(self.amount_label)
        self.layout.addWidget(self.amount_input)
        self.layout.addWidget(self.from_currency_label)
        self.layout.addWidget(self.from_currency_input)
        self.layout.addWidget(self.to_currency_label)
        self.layout.addWidget(self.to_currency_input)
        self.layout.addWidget(self.convert_button)
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

    def convert_currency(self):
        amount_text = self.amount_input.text()
        from_currency_text = self.from_currency_input.text().upper()
        to_currency_text = self.to_currency_input.text().upper()

        # Validate input format
        if not amount_text.isdigit():
            self.result_label.setText("Invalid amount format. Please enter a number.")
            return

        if from_currency_text not in self.exchange_rates:
            self.result_label.setText("Invalid 'From Currency' code. Please check your input.")
            return

        if to_currency_text not in self.exchange_rates:
            self.result_label.setText("Invalid 'To Currency' code. Please check your input.")
            return

        amount = float(amount_text)

        conversion_rate = self.exchange_rates[to_currency_text] / self.exchange_rates[from_currency_text]
        converted_amount = amount * conversion_rate
        self.result_label.setText(f"{amount} {from_currency_text} is equal to {converted_amount} {to_currency_text}")

def main():
    app = QApplication(sys.argv)
    converter_app = CurrencyConverterApp()
    converter_app.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
