from scanners_repairs_Interface import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from connection import get_mac_address_scanner
from connection import insert_scanner_repair


class AddScannerRepair(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.insert_btn.clicked.connect(self.insert_bttn_clicked)

    def insert_bttn_clicked(self):
        mac_address = self.macAddressLine.text()
        scanner_repair = self.repair_line.text()
        date = self.date_line.text()
        repair_description = self.repair_description_line.text()
        scanner_repair_insertion = (mac_address, scanner_repair, date, repair_description)
        mac_addresses = get_mac_address_scanner()
        if mac_address not in mac_addresses:
            print('Scanner with this mac address doesnt exists, please make an insertion for an existing Scanner.')
        else:
            insert_scanner_repair(scanner_repair_insertion)
            print('Scanner repair inserted for mac address.', mac_address)