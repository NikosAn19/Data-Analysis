from routers_Interface import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from connection import insert_router
from connection import get_mac_address_router


class AddRouterPanel(QDialog, Ui_Dialog):
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
        router = (mac_address, section_id, brand, model, arrival_date)
        mac_adresses = get_mac_address_router()
        if mac_address not in mac_adresses:
            insert_router(router)
            print('Router inserted.')
        else:
            print('Router with this mac_address already exists.')
