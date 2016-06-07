import sys

from PRINCIPAL import *
from Pluie import *


class Hydraulique_menu(QMainWindow):
    def __init__(self, parent=None):
        super(Hydraulique_menu, self).__init__(parent)
        self.resize(670, 350)
        self.childWindowHyd = None
        layout = QHBoxLayout()

        self.bar = self.menuBar()
        self.file = self.bar.addMenu("Fichier")
        self.file.addAction("Nouvelle operation")

        self.save = QAction("Sauvegarde", self)
        self.save.setShortcut("Ctrl+S")
        self.file.addAction(self.save)

        self.test = self.file.addMenu("Test")

        self.ville = QAction("Ville", self)
        self.ville.setStatusTip('Ville')
        self.ville.triggered.connect(self.ville_process)
        self.test.addAction(self.ville)

        self.pluie = QAction("Pluie", self)
        self.pluie.setStatusTip('Pluie')
        self.pluie.triggered.connect(self.pluie_process)
        self.test.addAction(self.pluie)

        self.quit = QAction("Quitter", self)
        self.quit.triggered.connect(self.processtrigger)
        self.file.addAction(self.quit)

        self.setLayout(layout)
        self.setWindowTitle("Hydraulique urbaine")

    def processtrigger(self, q):
        print(q.text() + " ok")
        self.QApplication.exit()

    def ville_process(self):
        self.childWindowHyd = Principal()
        self.childWindowHyd.show()

    def pluie_process(self):
        self.childWindowHyd = pluie()
        self.childWindowHyd.show()


def main():
    app = QApplication(sys.argv)
    ex = Hydraulique_menu()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
