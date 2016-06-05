import sys

from PyQt5.QtWidgets import *


class Hydraulique_menu(QMainWindow):
    def __init__(self, parent=None):
        super(Hydraulique_menu, self).__init__(parent)
        self.resize(670, 350)

        layout = QHBoxLayout()
        bar = self.menuBar()
        file = bar.addMenu("&Fichier")
        file.addAction("Nouvelle operation")

        save = QAction("Sauvegarde", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)

        edit = file.addMenu("Test")
        # d

        ville = QAction("Ville", self)
        ville.setStatusTip('Ville')
        ville.triggered.connect(self.ville)
        file.addAction(ville)

        pluie = QAction("Pluie", self)
        pluie.setStatusTip('Pluie')
        pluie.triggered.connect(self.pluie)
        file.addAction(pluie)

        quit = QAction("Quitter", self)
        file.addAction(quit)
        file.triggered[QAction].connect(self.processtrigger)
        self.setLayout(layout)
        self.setWindowTitle("Hydraulique Urbaine")

    def processtrigger(self, q):
        print(q.text() + " ok")

    def ville(self):
        print("ville")

    def pluie(self):
        print("Pluie")
        self.childWindow = PRINCIPAL.Principal()


def main():
    app = QApplication(sys.argv)
    ex = Hydraulique_menu()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
