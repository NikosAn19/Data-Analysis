from scanners_Interface import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from connection import insert_scanner
from connection import get_mac_address_scanner


class AddScannerPanel(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.insert_btn.clicked.connect(self.insert_bttn_clicked)

    def insert_bttn_clicked(self):
        mac_address = self.macAddressLine.text()
        brand = self.brand_line.text()
        model = self.model_line.text()
        arrival_date = self.arrival_date_line.text()
        section_id = self.section_id_line.text()
        scanner = (mac_address, brand, model, arrival_date, section_id)
        mac_addresses = get_mac_address_scanner()
        if mac_address not in mac_addresses:
            insert_scanner(scanner)
            print('Scanner inserted.')
        else:
            print('Scanner with this mac address already exists.')
