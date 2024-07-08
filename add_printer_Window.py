from printer_Interface import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from connection import insert_printer
from connection import get_mac_address_printer


class AddPrinterPanel(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.insert_btn.clicked.connect(self.insert_bttn_clicked)

    def insert_bttn_clicked(self):
        mac_address = self.macAddressLine.text()
        brand = self.brand_line.text()
        model = self.model_line.text()
        ink_storage = self.ink_storage_line.text()
        arrival_date = self.arrival_date_line_2.text()
        section_id = self.section_id_line.text()
        printer = (mac_address, brand, model, ink_storage, section_id, arrival_date)
        mac_addresses = get_mac_address_printer()
        if mac_address not in mac_addresses:
            insert_printer(printer)
            print('Printer inserted.')
        else:
            print('Printer with this mac_address already exists.')
