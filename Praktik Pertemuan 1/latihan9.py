import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()
        
        # Load UI langsung dari file .ui
        loadUi('latihan9.ui', self)
        
        # Rates to IDR
        self.rates = {
            "USD (Dolar)": 15500,
            "EUR (Euro)": 16800,
            "SGD (Dolar Singapura)": 11500,
            "JPY (Yen)": 105,
            "IDR (Rupiah)": 1
        }
        
        # Masukkan item ke dalam Combo Box dari UI
        self.from_combo.addItems(self.rates.keys())
        self.to_combo.addItems(self.rates.keys())
        
        # Signals
        self.amount_input.valueChanged.connect(self.convert)
        self.from_combo.currentTextChanged.connect(self.convert)
        self.to_combo.currentTextChanged.connect(self.convert)
        
        self.convert()

    def convert(self):
        amount = self.amount_input.value()
        from_curr = self.from_combo.currentText()
        to_curr = self.to_combo.currentText()
        
        # Convert to IDR first
        in_idr = amount * self.rates[from_curr]
        
        # Convert to target currency
        result = in_idr / self.rates[to_curr]
        
        self.result_label.setText(f"Hasil: {result:,.2f} {to_curr.split()[0]}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyConverter()
    window.show()
    sys.exit(app.exec_())