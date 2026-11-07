import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class DataMahasiswa(QWidget):
    def __init__(self):
        super().__init__()
        
        # Load UI langsung dari file XML .ui
        loadUi('latihan8.ui', self)
        
        # Signal connections (nama variabel sesuai dengan XML)
        self.add_btn.clicked.connect(self.add_data)
        self.update_btn.clicked.connect(self.update_data)
        self.delete_btn.clicked.connect(self.delete_data)
        self.clear_btn.clicked.connect(self.clear_form)
        self.table.itemSelectionChanged.connect(self.on_select)
        
        self.data = []

    def add_data(self):
        nim = self.nim_input.text()
        nama = self.nama_input.text()
        nilai = self.nilai_input.value()
        
        if nim and nama:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(nim))
            self.table.setItem(row, 1, QTableWidgetItem(nama))
            self.table.setItem(row, 2, QTableWidgetItem(str(nilai)))
            self.clear_form()

    def update_data(self):
        current = self.table.currentRow()
        if current >= 0:
            self.table.setItem(current, 0, QTableWidgetItem(self.nim_input.text()))
            self.table.setItem(current, 1, QTableWidgetItem(self.nama_input.text()))
            self.table.setItem(current, 2, QTableWidgetItem(str(self.nilai_input.value())))

    def delete_data(self):
        current = self.table.currentRow()
        if current >= 0:
            self.table.removeRow(current)

    def clear_form(self):
        self.nim_input.clear()
        self.nama_input.clear()
        self.nilai_input.setValue(0)

    def on_select(self):
        current = self.table.currentRow()
        if current >= 0:
            self.nim_input.setText(self.table.item(current, 0).text())
            self.nama_input.setText(self.table.item(current, 1).text())
            self.nilai_input.setValue(int(self.table.item(current, 2).text()))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataMahasiswa()
    window.show()
    sys.exit(app.exec_())