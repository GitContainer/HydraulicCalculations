# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu_HU.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All dddd  changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(782, 395)
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 782, 21))
        self.menubar.setObjectName("menubar")
        self.menuFichier = QtWidgets.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")
        self.menuHydraulique = QtWidgets.QMenu(self.menubar)
        self.menuHydraulique.setObjectName("menuHydraulique")
        self.menuBassins = QtWidgets.QMenu(self.menubar)
        self.menuBassins.setObjectName("menuBassins")
        Menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Menu)
        self.statusbar.setObjectName("statusbar")
        Menu.setStatusBar(self.statusbar)
        self.actionNouvelle_affaire = QtWidgets.QAction(Menu)
        self.actionNouvelle_affaire.setObjectName("actionNouvelle_affaire")
        self.actionChargement_affaire = QtWidgets.QAction(Menu)
        self.actionChargement_affaire.setObjectName("actionChargement_affaire")
        self.actionQuitter = QtWidgets.QAction(Menu)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionVilles = QtWidgets.QAction(Menu)
        self.actionVilles.setObjectName("actionVilles")
        self.actionMontana = QtWidgets.QAction(Menu)
        self.actionMontana.setObjectName("actionMontana")
        self.actionR_tention = QtWidgets.QAction(Menu)
        self.actionR_tention.setObjectName("actionR_tention")
        self.actionInfiltration = QtWidgets.QAction(Menu)
        self.actionInfiltration.setObjectName("actionInfiltration")
        self.menuFichier.addAction(self.actionNouvelle_affaire)
        self.menuFichier.addAction(self.actionChargement_affaire)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuHydraulique.addAction(self.actionVilles)
        self.menuHydraulique.addAction(self.actionMontana)
        self.menuBassins.addAction(self.actionR_tention)
        self.menuBassins.addAction(self.actionInfiltration)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuHydraulique.menuAction())
        self.menubar.addAction(self.menuBassins.menuAction())

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Hydraulique Urbaine"))
        self.menuFichier.setTitle(_translate("Menu", "Fichier"))
        self.menuHydraulique.setTitle(_translate("Menu", "Hydraulique"))
        self.menuBassins.setTitle(_translate("Menu", "Bassins"))
        self.actionNouvelle_affaire.setText(_translate("Menu", "Nouvelle affaire"))
        self.actionChargement_affaire.setText(_translate("Menu", "Chargement affaire"))
        self.actionQuitter.setText(_translate("Menu", "Quitter"))
        self.actionVilles.setText(_translate("Menu", "Villes"))
        self.actionMontana.setText(_translate("Menu", "Montana"))
        self.actionR_tention.setText(_translate("Menu", "Rétention"))
        self.actionInfiltration.setText(_translate("Menu", "Infiltration"))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Ui_Menu = Ui_Menu()
    Ui_Menu.main()
    app.exec_()
