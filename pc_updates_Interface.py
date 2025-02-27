# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pc_updates.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 620)
        Dialog.setStyleSheet("background-color : black;\n"
"color : white;")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setStyleSheet("color : white;\n"
"font-size : 28px;")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.macAddress = QtWidgets.QLabel(Dialog)
        self.macAddress.setStyleSheet("color:white;")
        self.macAddress.setObjectName("macAddress")
        self.verticalLayout.addWidget(self.macAddress)
        self.macAddressLine = QtWidgets.QLineEdit(Dialog)
        self.macAddressLine.setStyleSheet("color:white;")
        self.macAddressLine.setObjectName("macAddressLine")
        self.verticalLayout.addWidget(self.macAddressLine)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.date_line = QtWidgets.QLineEdit(Dialog)
        self.date_line.setObjectName("date_line")
        self.verticalLayout.addWidget(self.date_line)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.update_line = QtWidgets.QLineEdit(Dialog)
        self.update_line.setObjectName("update_line")
        self.verticalLayout.addWidget(self.update_line)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.update_description = QtWidgets.QLineEdit(Dialog)
        self.update_description.setObjectName("update_description")
        self.verticalLayout.addWidget(self.update_description)
        self.insert_btn = QtWidgets.QPushButton(Dialog)
        self.insert_btn.setStyleSheet("background-color: white;\n"
"color : black;\n"
"")
        self.insert_btn.setObjectName("insert_btn")
        self.verticalLayout.addWidget(self.insert_btn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "PC UPDATES"))
        self.macAddress.setText(_translate("Dialog", "Mac Address"))
        self.label_3.setText(_translate("Dialog", "Date"))
        self.label_4.setText(_translate("Dialog", "Update"))
        self.label_5.setText(_translate("Dialog", "Update Description"))
        self.insert_btn.setText(_translate("Dialog", "Insert"))
