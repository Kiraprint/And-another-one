import sqlite3
import sys

from PyQt5 import uic, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.connect = sqlite3.connect('coffee_db.sqlite')
        '''
        self.add_pack.clicked.connect(self.add_f)
        self.add_sort.clicked.connect(self.add_g)
        self.delete_pack.clicked.connect(self.delete_film)
        self.delete_sort.clicked.connect(self.delete_genre)
        self.edit_pack.clicked.connect(self.edit_f)
        self.edit_sort.clicked.connect(self.edit_g)
        '''
        self.coffee_table.setColumnCount(7)
        self.sorts_table.setColumnCount(2)
        self.sorts_table.setHorizontalHeaderLabels(['ID', 'Sort name'])
        self.coffee_table.setHorizontalHeaderLabels(['ID', 'Pack title',
                                                   'Coffee sort', 'Degree of roast',
                                                   'Volume of pack', 'Ground or whole', 'Taste'])

        self.coffee_load()
        self.sorts_load()

    def coffee_load(self):
        cursor = self.connect.cursor()
        res = cursor.execute("""select coffee.id, coffee.title,  sorts.name, degree_of_roast, coffee.volume_of_pack, 
         ground, taste from coffee, sorts where sorts.id = coffee.sort_id""").fetchall()
        for i, info in enumerate(res):
            self.coffee_table.setRowCount(i + 1)
            for j, inf in enumerate(info):
                self.coffee_table.setItem(i, j, QTableWidgetItem(str(inf)))

    def sorts_load(self):
        cursor = self.connect.cursor()
        res = cursor.execute("""select * from sorts""").fetchall()
        for i, info in enumerate(res):
            self.sorts_table.setRowCount(i + 1)
            for j, inf in enumerate(info):
                self.sorts_table.setItem(i, j, QTableWidgetItem(str(inf)))

    '''
    self.add_film_action = AddPack()
    self.add_genre_action = AddSort()
    self.edit_film_action = EditPack()
    self.edit_genre_action = EditSort()
    

def delete_film(self):
    cur = self.connect.cursor()
    for i in self.film_table.selectedItems():
        cur.execute("""delete from coffee where title = ?""", (i.text(),))
    self.connect.commit()
    self.coffee_load()

def delete_genre(self):
    cur = self.connect.cursor()
    for i in self.genre_table.selectedItems():
        cur.execute("""delete from sorts where name = ?""", (i.text(),))
    self.connect.commit()
    self.sorts_load()
    self.coffee_load()

def edit_f(self):
    a = self.film_table.selectedItems()
    if a:
        cur = self.connect.cursor()
        id_new, name, year, genre, length = map(str, cur.execute("""select * from coffee 
        where title = ?""", (a[0].text(),)).fetchall()[0])
        genres = list(map(lambda x: x[0], cur.execute("""select distinct name 
        from sorts""").fetchall()))
        self.edit_film_action.film_genre.addItems(genres)
        self.edit_film_action.id = id_new
        self.edit_film_action.film_name.setText(name)
        self.edit_film_action.film_year.setText(year)
        self.edit_film_action.film_length.setText(length)
        self.edit_film_action.film_genre.setCurrentText(cur.execute("""select title 
        from genres 
        where id = ?""", (genre,)).fetchall()[0][0])
        self.edit_film_action.show()

def edit_g(self):
    a = self.genre_table.selectedItems()
    if a:
        cur = self.connect.cursor()
        id_new, name = map(str, cur.execute("""select * from genres where title = ?""",
                                            (a[0].text(),)).fetchall()[0])
        self.edit_genre_action.name_edit.setText(name)
        self.edit_genre_action.id = id_new
        self.edit_genre_action.show()

def add_f(self):
    cur = self.connect.cursor()
    self.add_film_action.genres = list(map(lambda x: x[0], cur.execute("""select distinct title 
                                    from genres""").fetchall()))
    self.add_film_action.film_genre.addItems(self.add_film_action.genres)
    self.add_film_action.show()

def add_g(self):
    self.add_genre_action.show()


'''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
