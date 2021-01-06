import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QWidget


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

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


class AddCoffee(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
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


class EditCoffee(QWidget):
    def __init__(self, coid):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
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
