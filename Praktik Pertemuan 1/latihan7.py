import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class TextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Load UI langsung dari file .ui yang baru dibuat
        loadUi('latihan7.ui', self)
        
        # Hubungkan QAction (dari Menu dan Toolbar) ke fungsi masing-masing
        self.new_action.triggered.connect(self.new_file)
        self.open_action.triggered.connect(self.open_file)
        self.save_action.triggered.connect(self.save_file)
        self.exit_action.triggered.connect(self.close)

    # Implementasikan fungsi New, Open, Save sesuai instruksi PDF
    def new_file(self):
        self.text_area.clear()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, 'r') as f:
                self.text_area.setText(f.read())

    def save_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, 'w') as f:
                f.write(self.text_area.toPlainText())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextEditor()
    window.show()
    sys.exit(app.exec_())