# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogue_listview_.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(567, 611)
        self.listView_etudiants = QtWidgets.QListView(Dialog)
        self.listView_etudiants.setGeometry(QtCore.QRect(60, 70, 451, 401))
        self.listView_etudiants.setObjectName("listView_etudiants")
        self.label_lst_etudiants = QtWidgets.QLabel(Dialog)
        self.label_lst_etudiants.setGeometry(QtCore.QRect(70, 20, 241, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_lst_etudiants.setFont(font)
        self.label_lst_etudiants.setObjectName("label_lst_etudiants")
        self.pushButton_quitter = QtWidgets.QPushButton(Dialog)
        self.pushButton_quitter.setGeometry(QtCore.QRect(160, 500, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_quitter.setFont(font)
        self.pushButton_quitter.setObjectName("pushButton_quitter")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_lst_etudiants.setText(_translate("Dialog", "La liste des étudiant.e.s"))
        self.pushButton_quitter.setText(_translate("Dialog", "Quitter"))
