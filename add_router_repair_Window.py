from routers_repairs_Interface import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from connection import get_mac_address_router
from connection import insert_router_repair


class AddRouterRepair(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.insert_btn.clicked.connect(self.insert_bttn_clicked)

    def insert_bttn_clicked(self):
        mac_address = self.macAddressLine.text()
        router_repair = self.repair_line.text()
        date = self.date_line.text()
        repair_description = self.repair_description_line.text()
        router_repair_insertion = (mac_address, router_repair, date, repair_description)
        mac_addresses = get_mac_address_router()
        if mac_address not in mac_addresses:
            print('Router with this mac address doesnt exists, please make an insertion for an existing Router.')
        else:
            insert_router_repair(router_repair_insertion)
            print('Printer repair inserted for mac address.', mac_address)