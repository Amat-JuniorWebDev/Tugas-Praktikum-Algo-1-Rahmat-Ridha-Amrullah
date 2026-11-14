import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QDate
import db_helper

class KembaliBukuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(KembaliBukuWindow, self).__init__()
        uic.loadUi('kembali_buku.ui', self)

        self.dateKembali.setDate(QDate.currentDate())

        # Connect buttons & signals
        self.btnProsesKembali.clicked.connect(self.process_return)
        self.btnBersihkan.clicked.connect(self.clear_fields)
        self.btnKembali.clicked.connect(self.close)
        self.tablePeminjaman.itemSelectionChanged.connect(self.on_table_select)
        self.dateKembali.dateChanged.connect(self.calculate_fine)

        self.tablePeminjaman.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.load_active_loans()

    def load_active_loans(self):
        self.tablePeminjaman.setRowCount(0)
        loans = db_helper.get_active_loans()
        for row_number, row_data in enumerate(loans):
            self.tablePeminjaman.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tablePeminjaman.setItem(row_number, column_number, item)

    def on_table_select(self):
        selected_rows = self.tablePeminjaman.selectionModel().selectedRows()
        if not selected_rows:
            return
        row = selected_rows[0].row()
        self.txtIdPinjam.setText(self.tablePeminjaman.item(row, 0).text())
        self.txtNamaPeminjam.setText(self.tablePeminjaman.item(row, 1).text())
        self.txtJudulBuku.setText(self.tablePeminjaman.item(row, 3).text())
        self.calculate_fine()

    def calculate_fine(self):
        selected_rows = self.tablePeminjaman.selectionModel().selectedRows()
        if not selected_rows:
            return
        row = selected_rows[0].row()
        tgl_pinjam_str = self.tablePeminjaman.item(row, 4).text()
        durasi = int(self.tablePeminjaman.item(row, 5).text())

        tgl_pinjam = QDate.fromString(tgl_pinjam_str, "yyyy-MM-dd")
        batas_kembali = tgl_pinjam.addDays(durasi)
        tgl_kembali = self.dateKembali.date()

        selisih_hari = batas_kembali.daysTo(tgl_kembali)
        denda = max(0, selisih_hari * 1000)
        self.txtDenda.setText(str(denda))

    def process_return(self):
        id_pinjam = self.txtIdPinjam.text().strip()
        if not id_pinjam:
            QtWidgets.QMessageBox.warning(self, "Validasi Gagal", "Pilih transaksi peminjaman dari tabel terlebih dahulu!")
            return

        try:
            denda = float(self.txtDenda.text().strip() or 0)
            if denda < 0:
                raise ValueError()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Validasi Gagal", "Nominal denda harus berupa angka positif!")
            return

        tanggal_kembali = self.dateKembali.date().toString("yyyy-MM-dd")
        success, message = db_helper.return_book(id_pinjam, tanggal_kembali, denda)
        if success:
            QtWidgets.QMessageBox.information(self, "Berhasil", message)
            self.load_active_loans()
            self.clear_fields()
        else:
            QtWidgets.QMessageBox.critical(self, "Gagal", message)

    def clear_fields(self):
        self.txtIdPinjam.clear()
        self.txtNamaPeminjam.clear()
        self.txtJudulBuku.clear()
        self.dateKembali.setDate(QDate.currentDate())
        self.txtDenda.setText("0")
        self.tablePeminjaman.clearSelection()