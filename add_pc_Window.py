from pcs_Interface import Ui_Dialog
from PyQt5.QtWidgets import QDialog
from PyQt5 import QtCore
from connection import get_mac_address_pc
from connection import insert_pc


class AddPcPanel(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.insert_btn.clicked.connect(self.insert_bttn_clicked)

    def insert_bttn_clicked(self):
        mac_address = self.macAddressLine.text()
        pc_name = self.pc_name_line.text()
        ram = self.ram_line.text()
        cpu = self.cpu_line.text()
        office_licence = self.office_licence_line.text()
        windows_licence = self.windows_licence_line.text()
        arrival_date = self.arrival_date_line.text()
        section_id = self.sectionID_line.text()
        pc = (mac_address, pc_name, ram, cpu, office_licence, windows_licence, section_id, arrival_date)
        mac_addresses = get_mac_address_pc()
        if mac_address not in mac_addresses:
            insert_pc(pc)
            print('Pc inserted.')
        else:
            print('PC with this mac address already exists.')
