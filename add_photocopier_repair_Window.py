from photocopiers_repairs_Interface import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from connection import get_mac_address_photocopier
from connection import insert_photocopier_repair


class AddPhotocopierRepair(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.insert_btn.clicked.connect(self.insert_bttn_clicked)

    def insert_bttn_clicked(self):
        mac_address = self.macAddressLine.text()
        photocopier_repair = self.repair_line.text()
        date = self.date_line.text()
        repair_description = self.repair_description_line.text()
        photocopier_repair_insertion = (mac_address, photocopier_repair, date, repair_description)
        mac_addresses = get_mac_address_photocopier()
        if mac_address not in mac_addresses:
            print('Photocopier with this mac address doesnt exists, please make an insertion for an existing Photocopier.')
        else:
            insert_photocopier_repair(photocopier_repair_insertion)
            print('Photocopier repair inserted for mac address.', mac_address)
