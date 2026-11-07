"""
PROGRAM: TO-DO LIST DENGAN WARNA
Fungsi: Menampilkan penggunaan Qt.green untuk foreground
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QFont, QColor
from PyQt5.uic import loadUi # ← IMPORT INI DITAMBAHKAN UNTUK MEMBACA .UI

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Load UI langsung dari file .ui
        loadUi('latihan5.ui', self)
        
        # Signal connections
        self.add_btn.clicked.connect(self.add_task)
        self.complete_btn.clicked.connect(self.complete_task)
        self.delete_btn.clicked.connect(self.delete_task)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            item = QListWidgetItem(task)
            self.task_list.addItem(item)
            self.task_input.clear()

    def complete_task(self):
        """Menandai tugas selesai dengan warna hijau"""
        current_item = self.task_list.currentItem()
        if current_item:
            # === CARA 1: PAKAI Qt.green (PERLU IMPORT Qt) ===
            current_item.setForeground(Qt.green) 
            
            # === CARA 2: PAKAI QColor (TIDAK PERLU IMPORT Qt) ===
            # current_item.setForeground(QColor(0, 255, 0)) # RGB green
            # current_item.setForeground(QColor("#00FF00")) # Hex green
            
            # Tambahkan centang di depan teks
            current_text = current_item.text()
            if not current_text.startswith("✓ "):
                current_item.setText(f"✓ {current_text}")

    def delete_task(self):
        current_row = self.task_list.currentRow()
        if current_row >= 0:
            self.task_list.takeItem(current_row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())