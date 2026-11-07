import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.uic import loadUi

class LoginApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load UI langsung dari file .ui bawaanmu
        loadUi('latihan2.ui', self) 
        
        # Nama tombol disesuaikan dengan XML (pushButton dan pushButton_2)
        self.pushButton.clicked.connect(self.handle_login)
        self.pushButton_2.clicked.connect(self.clear_form)
        self.plainTextEdit.setFocus()

    def handle_login(self):
        # QPlainTextEdit menggunakan toPlainText(), bukan text()
        username = self.plainTextEdit.toPlainText().strip()
        password = self.plainTextEdit_2.toPlainText().strip()
        
        if username == "admin" and password == "123":
            QMessageBox.information(self, "Login Sukses", "Selamat datang Admin!")
        else:
            QMessageBox.warning(self, "Login Gagal", "Username atau password salah!")
            self.plainTextEdit_2.clear()
            self.plainTextEdit_2.setFocus()
            
    def clear_form(self):
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.plainTextEdit.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())