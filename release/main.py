import sqlite3
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 860)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1121, 801))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_pb = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add_pb.setObjectName("add_pb")
        self.verticalLayout.addWidget(self.add_pb)
        self.edit_pb = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.edit_pb.setObjectName("edit_pb")
        self.verticalLayout.addWidget(self.edit_pb)
        self.coffee_table = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.coffee_table.setObjectName("coffee_table")
        self.coffee_table.setColumnCount(0)
        self.coffee_table.setRowCount(0)
        self.verticalLayout.addWidget(self.coffee_table)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.add_pb.setText(_translate("MainWindow", "Add coffee pack"))
        self.edit_pb.setText(_translate("MainWindow", "Edit cofee pack"))


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(619, 374)
        self.formLayoutWidget = QtWidgets.QWidget(Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 10, 581, 297))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.title = QtWidgets.QLabel(self.formLayoutWidget)
        self.title.setObjectName("title")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.title)
        self.title_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.title_le.setObjectName("title_le")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.title_le)
        self.sort = QtWidgets.QLabel(self.formLayoutWidget)
        self.sort.setObjectName("sort")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.sort)
        self.dor_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.dor_label.setObjectName("dor_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.dor_label)
        self.vop_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.vop_label.setObjectName("vop_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.vop_label)
        self.dor_cb = QtWidgets.QComboBox(self.formLayoutWidget)
        self.dor_cb.setObjectName("dor_cb")
        self.dor_cb.addItem("")
        self.dor_cb.addItem("")
        self.dor_cb.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dor_cb)
        self.vop_sb = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.vop_sb.setObjectName("vop_sb")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.vop_sb)
        self.whole = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.whole.setObjectName("whole")
        self.gow_bg = QtWidgets.QButtonGroup(Form)
        self.gow_bg.setObjectName("gow_bg")
        self.gow_bg.addButton(self.whole)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.whole)
        self.sort_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.sort_le.setObjectName("sort_le")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.sort_le)
        self.taste = QtWidgets.QLabel(self.formLayoutWidget)
        self.taste.setObjectName("taste")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.taste)
        self.taste_le = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.taste_le.setObjectName("taste_le")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.taste_le)
        self.price = QtWidgets.QLabel(self.formLayoutWidget)
        self.price.setObjectName("price")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.price)
        self.price_sb = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.price_sb.setObjectName("price_sb")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.price_sb)
        self.ground = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.ground.setObjectName("ground")
        self.gow_bg.addButton(self.ground)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.ground)
        self.mixed = QtWidgets.QRadioButton(self.formLayoutWidget)
        self.mixed.setObjectName("mixed")
        self.gow_bg.addButton(self.mixed)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.mixed)
        self.gow_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.gow_label.setObjectName("gow_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.gow_label)
        self.confirm_pb = QtWidgets.QPushButton(Form)
        self.confirm_pb.setGeometry(QtCore.QRect(500, 330, 93, 28))
        self.confirm_pb.setObjectName("confirm_pb")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.title.setText(_translate("Form", "Title"))
        self.sort.setText(_translate("Form", "Sort of coffee"))
        self.dor_label.setText(_translate("Form", "Degree of roast"))
        self.vop_label.setText(_translate("Form", "Volume of pack (mg)"))
        self.dor_cb.setItemText(0, _translate("Form", "1 (rare)"))
        self.dor_cb.setItemText(1, _translate("Form", "2 (medium)"))
        self.dor_cb.setItemText(2, _translate("Form", "3 (well done)"))
        self.whole.setText(_translate("Form", "Whole"))
        self.taste.setText(_translate("Form", "Taste"))
        self.price.setText(_translate("Form", "Price"))
        self.ground.setText(_translate("Form", "Ground"))
        self.mixed.setText(_translate("Form", "Mixed"))
        self.gow_label.setText(_translate("Form", "Ground or whole"))
        self.confirm_pb.setText(_translate("Form", "PushButton"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.connect = sqlite3.connect('coffee_db.sqlite')
        self.coffee_table.setColumnCount(8)
        self.coffee_table.setHorizontalHeaderLabels(['ID', 'Pack title',
                                                     'Degree of roast', 'Volume of pack', 'Ground or whole',
                                                     'Taste', 'Coffee sort', 'Price'])

        self.modified = {}

        self.add_pb.clicked.connect(self.add)
        self.edit_pb.clicked.connect(self.edit)

        self.add_screen = AddCoffee()
        self.load()

    def load(self):
        cursor = self.connect.cursor()
        res = cursor.execute("""select * from coffee""").fetchall()
        for i, info in enumerate(res):
            self.coffee_table.setRowCount(i + 1)
            for j, inf in enumerate(info):
                self.coffee_table.setItem(i, j, QTableWidgetItem(str(inf)))

    def add(self):
        self.add_screen.show()

    def edit(self):
        ed_f = self.coffee_table.takeItem(self.coffee_table.currentRow(), 0).text()
        self.edit_screen = EditCoffee(ed_f)
        self.edit_screen.show()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE films SET\n"
            for key in self.modified.keys():
                que += "{}='{}'\n".format(key, self.modified.get(key))
            que += "WHERE id = ?"
            cur.execute(que, (self.spinBox.text(),))
            self.con.commit()
            self.modified.clear()


class AddCoffee(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.confirm_pb.setText('Add')
        self.confirm_pb.clicked.connect(self.add)

        self.connect = sqlite3.connect('coffee_db.sqlite')

    def add(self):
        try:
            title = self.title_le.text()
            sort = self.sort_le.text()
            dor = self.dor_cb.currentText()
            vop = int(self.vop_sb.value())
            gow = self.gow_bg.checkedButton().text()
            taste = self.taste_le.text()
            price = int(self.price_sb.value())

            cur = self.connect.cursor()
            new_id = cur.execute("""select max(id) from coffee""").fetchall()[0][0] + 1
            cur.execute("""insert into coffee 
                        values (?, ?, ?, ?, ?, ?, ?, ?)""",
                        (new_id, title, dor, vop, gow, taste, sort, price))

            self.connect.commit()
            self.close()
        except ValueError:
            self.close()

    def closeEvent(self, event):
        self.title_le.clear()
        self.sort_le.clear()
        self.taste.clear()
        form.load()


class EditCoffee(QWidget, Ui_Form):
    def __init__(self, coid):
        super().__init__()
        self.setupUi(self)

        self.confirm_pb.setText('Edit')
        self.confirm_pb.clicked.connect(self.edit)

        self.id = coid
        self.con = sqlite3.connect('coffee_db.sqlite')
        self.cur = self.con.cursor()
        self.data = self.cur.execute("""select * from coffee where id=?""", (int(coid),)).fetchone()
        self.title_le.setText(self.data[1])
        self.sort_le.setText(self.data[6])

    def edit(self):
        try:
            title = self.title_le.text()
            sort = self.sort_le.text()
            dor = self.dor_cb.currentText()
            vop = int(self.vop_sb.value())
            gow = self.gow_bg.checkedButton().text()
            taste = self.taste_le.text()
            price = int(self.price_sb.value())

            self.cur.execute("""update coffee 
            set title = ?, degree_of_roast = ?, volume_of_pack = ?, 
            ground = ?, taste=?, sort=?, price=? where id = ?""",
                             (title, dor, vop, gow,
                              taste, sort, price, self.id))
            self.con.commit()
            self.close()
        except ValueError:
            self.close()

    def closeEvent(self, event):
        form.load()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
