from pc_repairs_Interface import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from connection import get_mac_address_pc
from connection import insert_pc_repair


class AddPCRepair(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.insert_btn.clicked.connect(self.insert_bttn_clicked)

    def insert_bttn_clicked(self):
        mac_address = self.macAddressLine.text()
        repair = self.repair_line.text()
        date = self.date_line.text()
        repair_description = self.repair_description_line.text()
        pc_repair = (mac_address, repair, date, repair_description)
        mac_addresses = get_mac_address_pc()
        if mac_address not in mac_addresses:
            print('PC with this mac address doesnt exists, please make an insertion for an existing PC.')
        else:
            insert_pc_repair(pc_repair)
            print('PC repair inserted for mac address.', mac_address)
