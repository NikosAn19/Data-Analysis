from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
from add_pc_Window import AddPcPanel
from add_pc_repair_Window import AddPCRepair
from add_pc_update_Window import AddPCUpdate
from add_printer_Window import AddPrinterPanel
from add_printer_repair_Window import AddPrinterRepair
from add_photocopier_Window import AddPhotocopierPanel
from add_photocopier_repair_Window import AddPhotocopierRepair
from add_scanner_Window import AddScannerPanel
from add_scanner_repair_Window import AddScannerRepair
from add_router_Window import AddRouterPanel
from add_router_repair_Window import AddRouterRepair
from main_window_Interface import Ui_MainWindow
from connection import insert_generated_data

from PyQt5 import QtCore, QtGui, QtWidgets


class Main_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_pc_bttn.clicked.connect(self.show_add_pc)
        self.add_pc_bttn_2.clicked.connect(self.show_add_printer)
        self.add_pc_bttn_3.clicked.connect(self.show_add_photocopier)
        self.add_pc_bttn_4.clicked.connect(self.show_add_scanner)
        self.add_pc_bttn_5.clicked.connect(self.show_add_pc_repair)
        self.add_pc_bttn_6.clicked.connect(self.show_add_pc_update)
        self.add_pc_bttn_7.clicked.connect(self.show_add_router)
        self.add_pc_bttn_8.clicked.connect(self.show_add_printer_repair)
        self.add_pc_bttn_9.clicked.connect(self.show_add_photocopier_repair)
        self.add_pc_bttn_10.clicked.connect(self.show_add_scanner_repair)
        self.add_pc_bttn_11.clicked.connect(self.show_add_router_repair)


    def show_add_pc(self):
        self.add_pc_panel = AddPcPanel()
        self.add_pc_panel.show()


    def show_add_pc_repair(self):
        self.add_pc_repair_panel = AddPCRepair()
        self.add_pc_repair_panel.show()

    def show_add_pc_update(self):
        self.add_pc_update_panel = AddPCUpdate()
        self.add_pc_update_panel.show()

    def show_add_printer(self):
        self.add_printer_panel = AddPrinterPanel()
        self.add_printer_panel.show()

    def show_add_printer_repair(self):
        self.add_printer_repair_panel = AddPrinterRepair()
        self.add_printer_repair_panel.show()

    def show_add_photocopier(self):
        self.add_photocopier_panel = AddPhotocopierPanel()
        self.add_photocopier_panel.show()

    def show_add_photocopier_repair(self):
        self.add_photocopier_repair_panel = AddPhotocopierRepair()
        self.add_photocopier_repair_panel.show()

    def show_add_scanner(self):
        self.add_scanner_panel = AddScannerPanel()
        self.add_scanner_panel.show()

    def show_add_scanner_repair(self):
        self.add_scanner_repair_panel = AddScannerRepair()
        self.add_scanner_repair_panel.show()

    def show_add_router(self):
        self.add_router_panel = AddRouterPanel()
        self.add_router_panel.show()

    def show_add_router_repair(self):
        self.add_router_repair_panel = AddRouterRepair()
        self.add_router_repair_panel.show()


app = QApplication(sys.argv)
window = Main_Window()
window.show()
insert_generated_data()
sys.exit(app.exec())
