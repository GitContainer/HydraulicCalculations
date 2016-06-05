from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import SECONDAIRE


class Communicate(QObject):
    closeApp = pyqtSignal(list)


class MyPopupDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        layout = QFormLayout()
        self.setWindowTitle("New data")

        self.c2 = Communicate()

        print("Popup created")
        self.listInfo = None
        self.label_name1 = QLabel()
        self.qline_name1 = QLineEdit()

        self.label_name2 = QLabel()
        self.qline_name2 = QLineEdit()

        self.label_name3 = QLabel()
        self.qline_name3 = QLineEdit()

        self.button_ok = QPushButton()
        self.button_ok.setText("Send information")
        self.button_ok.clicked.connect(self.button_clicked_method)

        layout.addRow(self.label_name1, self.qline_name1)
        layout.addRow(self.label_name2, self.qline_name2)
        layout.addRow(self.label_name3, self.qline_name3)
        layout.addWidget(self.button_ok)

        self.setLayout(layout)
        self.show()

    def button_clicked_method(self):
        self.listInfo = [self.qline_name1.text(), self.qline_name2.text(), self.qline_name3.text()]
        print(self.listInfo)
        self.c2.closeApp.emit(self.listInfo)


class Principal(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.childWindow = None

        self.resize(670, 350)
        self.setWindowTitle("TEST")
        self.objectDatabase = SECONDAIRE.DatabaseClass()

        exit_button = QPushButton("Quitter")
        exit_button.setParent(self)
        exit_button.setFont(QFont("Arial", 10))
        exit_button.setFixedSize(120, 30)
        exit_button.move(520, 10)
        exit_button.clicked.connect(self.exit_button_method)

        self.newrow_button = QPushButton("New row")
        self.newrow_button.setParent(self)
        self.newrow_button.setFont(QFont("Arial", 10))
        self.newrow_button.setFixedSize(120, 30)
        self.newrow_button.move(520, 50)
        self.newrow_button.clicked.connect(self.create_button_method)

        click_button = QPushButton("Click")
        click_button.setParent(self)
        click_button.setFont(QFont("Arial", 10))
        click_button.setFixedSize(120, 30)
        click_button.move(520, 90)
        click_button.clicked.connect(self.click_button_method)

        self.list = QTableWidget()
        self.table_element_message_storage = None
        self.list.setParent(self)
        self.list.move(20, 10)
        self.list.setFixedSize(468, 320)
        self.list.setHorizontalHeaderLabels(('Ville', 'Identification', 'Station'))
        self.list.setColumnWidth(0, 120)
        self.list.setColumnWidth(1, 80)
        self.list.setColumnWidth(2, 250)

        database_list_storage = self.objectDatabase.list_database()
        print(len(database_list_storage))
        self.list.setRowCount(len(database_list_storage))
        # len(database_list_storage) corresponds to how many values
        #  there are in database_list_storage horizontally, e.g: rows
        self.list.setColumnCount(len(database_list_storage[0]) - 1)
        # len(database_list_storage) corresponds to the values in
        #  database_list_storage vertically speaking, e.g: columns
        for row in range(len(database_list_storage)):
            for column in range(1, len(database_list_storage[0])):
                '''print(row)
                print(column)
                print(database_list_storage[row][column])'''
                self.list.setItem(row, column - 1, QTableWidgetItem(str(database_list_storage[row][column])))
        self.list.itemClicked.connect(lambda test=self: setattr(self, 'table_element_message_storage',
                                                                self.list.currentItem().text()))
        self.list.itemChanged.connect(self.item_changed)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Delete:
            print("Delete pressed")
            if len(self.list.selectedItems()) == 3:
                caution_message = "Are you sure you want to delete the data (in the table and in the database)?"
                yes_no_dialog = QMessageBox.question(self, "Delete?", caution_message,
                                                     QMessageBox.Yes, QMessageBox.Cancel)
                if yes_no_dialog == QMessageBox.Yes:
                    indexes = self.list.verticalHeader().selectionModel().selectedRows()
                    for index in indexes:
                        self.objectDatabase.delete_to_database(self.list.item(index.row(), 1).text())
                        self.list.removeRow(index.row())

    def exit_button_method(self):
        print("Quitter")
        self.close()

    def create_button_method(self):
        print("Create new data row")

        self.childWindow = MyPopupDialog()
        self.childWindow.c2.closeApp.connect(self.closed_emit)

    @pyqtSlot(list)
    def closed_emit(self, list_info_received):
        print("Worked!!!")
        print(list_info_received)
        rowPosition = self.list.rowCount()
        print(rowPosition)
        self.list.insertRow(rowPosition)
        self.list.blockSignals(True)
        for i in range(0, 3):
            print(i)
            self.list.setItem(rowPosition, i, QTableWidgetItem(list_info_received[i]))
        self.list.blockSignals(False)
        print(list_info_received[0], list_info_received[1], list_info_received[2])
        self.objectDatabase.add_to_database(list_info_received[0], list_info_received[1], list_info_received[2])

    @staticmethod
    def click_button_method():
        print("Has been clicked and is working")

    def item_changed(self):
        print("works")
        caution_message_for_item = "Change data?"
        change_data_caution_form = QMessageBox.question(self, "Confirm", caution_message_for_item,
                                                        QMessageBox.Yes, QMessageBox.Cancel)
        if change_data_caution_form == QMessageBox.Yes:
            text_content = self.list.currentItem().text()
            item_row = self.list.currentItem().row()
            item_column = self.list.currentItem().column()
            print(str(text_content), item_row, item_column)
            self.objectDatabase.update_database(text_content, item_row, item_column)
        else:
            self.list.blockSignals(True)
            self.list.currentItem().setText(self.table_element_message_storage)
            self.list.blockSignals(False)

# app = QApplication(sys.argv)
# form = Principal()
# form.show()
# app.exec_()
