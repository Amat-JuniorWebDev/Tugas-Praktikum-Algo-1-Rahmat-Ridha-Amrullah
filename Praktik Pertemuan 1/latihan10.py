import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.uic import loadUi

class WorkerThread(QThread):
    progress = pyqtSignal(int)
    finished = pyqtSignal()

    def __init__(self, duration=5):
        super().__init__()
        self.duration = duration

    def run(self):
        for i in range(101):
            time.sleep(self.duration / 100)
            self.progress.emit(i)
        self.finished.emit()

class ProgressApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Load UI langsung dari file .ui
        loadUi('latihan10.ui', self)
        
        # Signal connections (nama variabel sesuai dengan XML)
        self.start_btn.clicked.connect(self.start_process)
        self.cancel_btn.clicked.connect(self.cancel_process)
        
        self.worker = None

    def start_process(self):
        self.start_btn.setEnabled(False)
        self.cancel_btn.setEnabled(True)
        self.progress.setValue(0)
        self.status_label.setText("Memproses...")
        
        self.worker = WorkerThread(duration=3)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.process_finished)
        self.worker.start()

    def update_progress(self, value):
        self.progress.setValue(value)

    def process_finished(self):
        self.start_btn.setEnabled(True)
        self.cancel_btn.setEnabled(False)
        self.status_label.setText("Selesai!")
        QMessageBox.information(self, "Info", "Proses selesai!")

    def cancel_process(self):
        if self.worker and self.worker.isRunning():
            self.worker.terminate()
            self.worker.wait()
            
        self.start_btn.setEnabled(True)
        self.cancel_btn.setEnabled(False)
        self.status_label.setText("Dibatalkan")
        self.progress.setValue(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressApp()
    window.show()
    sys.exit(app.exec_())