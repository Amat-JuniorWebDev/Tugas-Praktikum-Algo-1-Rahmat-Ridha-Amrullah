import sys
from PyQt5 import QtWidgets, uic
import db_helper

class LaporanWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LaporanWindow, self).__init__()
        uic.loadUi('laporan.ui', self)

        self.btnRefresh.clicked.connect(self.load_reports)
        self.btnKembali.clicked.connect(self.close)

        self.tablePopuler.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.load_reports()

    def load_reports(self):
        stats = db_helper.get_general_statistics()
        self.lblTotalBuku.setText(f"Total Koleksi Buku: {stats['total_buku']}")
        self.lblPinjamAktif.setText(f"Peminjaman Aktif: {stats['active_loans']}")
        self.lblTotalDenda.setText(f"Total Denda Terkumpul: Rp {stats['total_denda']:,.0f}")

        self.tablePopuler.setRowCount(0)
        popular_books = db_helper.get_most_borrowed_books()
        for row_number, row_data in enumerate(popular_books):
            self.tablePopuler.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(data))
                self.tablePopuler.setItem(row_number, column_number, item)