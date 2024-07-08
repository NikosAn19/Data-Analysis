from pc_updates_Interface import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from connection import get_mac_address_pc
from connection import insert_pc_update


class AddPCUpdate(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.insert_btn.clicked.connect(self.insert_bttn_clicked)

    def insert_bttn_clicked(self):
        mac_address = self.macAddressLine.text()
        pc_update = self.update_line.text()
        date = self.date_line.text()
        update_description = self.update_description_line.text()
        pc_update_insertion = (mac_address, pc_update, date, update_description)
        mac_addresses = get_mac_address_pc()
        if mac_address not in mac_addresses:
            print('PC with this mac address doesnt exists, please make an insertion for an existing PC.')
        else:
            insert_pc_update(pc_update_insertion)
            print('PC update inserted for mac address.', mac_address)
