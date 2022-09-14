import sys
import sqlite3
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from ui_functions import *
from ui_main import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
from matplotlib import font_manager


class Bar(FigureCanvas):
    def __init__(self, labels, scores, color1, color2):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(3,3), facecolor='#f3f3f3')
        super().__init__(self.fig)
        font_files = font_manager.findSystemFonts(fontpaths=["E:\Python_projects\Budget_pyqt5\_fonts"])
        [font_manager.fontManager.addfont(x) for x in font_files]
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Ubuntu']
        colors = plt.get_cmap('YlOrRd')(np.linspace(color1, color2, len(labels)))
        self.ax.bar(labels, scores, color=colors, width=0.4, )
        self.ax.set(facecolor='#f3f3f3')
        bars = np.arange(len(labels))
        labels = [x[:7] for x in labels]
        plt.xticks(bars, labels, fontsize=8, rotation=20)
        cols = [x for x in plt.yticks()]
        plt.yticks(cols[0], [str(x) + '%' for x in cols[0]], fontsize=8)
        plt.xlim(-1, len(labels))
        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.draw()

    def close(self):
        plt.close('all')


class Pie(FigureCanvas):
    def __init__(self, label, scores):
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(6, 6), facecolor='#f3f3f3')
        super().__init__(self.fig)
        font_files = font_manager.findSystemFonts(fontpaths=["E:\Python_projects\Budget_pyqt5\_fonts"])
        [font_manager.fontManager.addfont(x) for x in font_files]
        rcParams['font.family'] = 'sans-serif'
        rcParams['font.sans-serif'] = ['Ubuntu']
        colors = plt.get_cmap('YlOrRd')(np.linspace(0.8, 0.2, len(label)))
        plt.pie(scores, labels=label, autopct='%1.1f%%', explode=[0.15, 0], shadow=False, colors=colors,
                startangle=90, textprops={'fontsize': 8})
        self.draw()

    def close(self):
        plt.close('all')


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setGeometry(100, 20, 1280, 800)
        self.ui.setupUi(self)

        def movewindow(event):
            if ui_functions.return_status() == 1:
                ui_functions.maximize_restore(self)
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.Frame1_Control_btns.mouseMoveEvent = movewindow
        self.ui.Frame1_Control_panel.mouseMoveEvent = movewindow

        ui_functions.ui_definitions(self)

        # creating db and db.tables
        def get_stat(table_name):
            with sqlite3.connect('database.db') as conn1:
                cursor1 = conn1.cursor()
                select_info = f'SELECT unique_id FROM {table_name}'
                cursor1.execute(select_info)
                number = cursor1.fetchall()
            return number[-1][0]

        def create_db_and_main_table():
            global operation_id
            try:
                with sqlite3.connect('database.db') as conn2:
                    cursor2 = conn2.cursor()
                    create_table = """CREATE TABLE Info (
                    unique_id INTEGER PRIMARY KEY, 
                    IncEx text NOT NULL,
                    Item text NOT NULL,
                    Sum REAL NOT NULL,
                    date datetime NOT NULL
                    )"""
                    cursor2.execute(create_table)
                operation_id = 0
            except sqlite3.Error as error_fte_info_exists:
                if error_fte_info_exists.args == ('table Info already exists',):
                    print(f"Напоминаю, таблица уже создана {error_fte_info_exists}")
                    try:
                        operation_id = get_stat("Info")
                    except IndexError:
                        # IndexError raises when table is empty
                        operation_id = 0
                else:
                    print("Ошибка при подключении к sqlite", error_fte_info_exists)

        create_db_and_main_table()

        def create_category_table():
            global category_id
            try:
                with sqlite3.connect('database.db') as conn2:
                    cursor2 = conn2.cursor()
                    create_table = """CREATE TABLE Items (
                    unique_id INTEGER PRIMARY KEY, 
                    IncEx text NOT NULL,
                    Item text NOT NULL
                    )"""
                    cursor2.execute(create_table)
                    category_id = 0
            except sqlite3.Error as error_items_exists:
                if error_items_exists.args == ('table Items already exists',):
                    print(f"Напоминаю, таблица уже создана {error_items_exists}")
                    try:
                        category_id = get_stat("Items")
                    except IndexError:
                        # IndexError raises when table is empty
                        category_id = 0
                else:
                    print("Ошибка при подключении к sqlite", error_items_exists)

        create_category_table()

        def get_categories():
            with sqlite3.connect('database.db') as conn1:
                cursor1 = conn1.cursor()
                select_info = f'SELECT IncEx, Item from Items'
                cursor1.execute(select_info)
                items = cursor1.fetchall()
                Inc = [x[1] for x in items if x[0] == "Доход"]
                Ex = [x[1] for x in items if x[0] == "Расход"]
            return Inc, Ex

        def combo():
            self.ui.Choose_option = self.findChild(QComboBox, "Choose_option")
            Inc, Ex = get_categories()[0], get_categories()[1]
            Choose_option_items = [self.ui.Choose_option.addItem(x[0], x[1]) for x
                                   in (("", [""]), ("Доход", Inc), ("Расход", Ex))]
            self.ui.Choose_category = self.findChild(QComboBox, "Choose_category")
            self.ui.Choose_option.activated.connect(self.chose_item)

        combo()

        def combo2():
            self.ui.Choose_option_2 = self.findChild(QComboBox, "Choose_option_2")
            Choose_option_2_items = [self.ui.Choose_option_2.addItem(x) for x in ('', 'Доход', 'Расход')]

        combo2()

        def insert_category(data_tuple):
            global category_id
            with sqlite3.connect('database.db') as conn5:
                cursor5 = conn5.cursor()
                insert_info = '''INSERT INTO Items (unique_id, IncEx, Item) VALUES (?, ?, ?)'''
                cursor5.execute(insert_info, data_tuple)

        def time_delay():
            self.ui.Insert_info_2.setText("")
            self.ui.New_category.setText("")
            self.ui.Choose_option_2.clear()
            combo2()
            self.ui.Choose_option.clear()
            self.ui.Choose_category.clear()
            combo()

        def insert_category_b():
            global category_id
            category_id += 1
            data_tuple = (category_id, self.ui.Choose_option_2.currentText(), self.ui.New_category.text())
            if all(data_tuple):
                try:
                    insert_category(data_tuple)
                    self.ui.Insert_info_2.setText("Данные внесены в базу")
                    timer = QTimer()
                    timer.singleShot(1000, time_delay)

                except Exception as e:
                    self.ui.Insert_info_2.setText("Ошибка, попробуйте заново")
                    timer = QTimer()
                    timer.singleShot(1000, time_delay)
            else:
                self.ui.Insert_info_2.setText("Ошибка, попробуйте заново")
                timer = QTimer()
                timer.singleShot(1000, time_delay)

        self.ui.Insert_2.clicked.connect(lambda: insert_category_b())

        def insert_into_db(data_tuple):
            with sqlite3.connect('database.db') as conn5:
                cursor5 = conn5.cursor()
                insert_info = '''INSERT INTO Info (unique_id, IncEx, Item, Sum, date) VALUES (?, ?, ?, ?, ?)'''
                cursor5.execute(insert_info, data_tuple)

        def time_delay2():
            self.ui.Insert_info.setText("")
            self.ui.Sum.setText("")
            self.ui.Choose_option.clear()
            self.ui.Choose_category.clear()
            combo()

        def insert_into_db_b():
            global operation_id
            operation_id += 1
            date = self.ui.Date.text().split('.')
            date = f"{date[2]}-{date[1]}-{date[0]}"
            data_tuple = (operation_id, self.ui.Choose_option.currentText(),
                          self.ui.Choose_category.currentText(), self.ui.Sum.text(), date)
            if all(data_tuple):
                try:
                    insert_into_db(data_tuple)
                    self.ui.Insert_info.setText("Данные внесены в базу")
                    timer = QTimer()
                    timer.singleShot(1000, time_delay2)

                except Exception as e:
                    self.ui.Insert_info.setText("Ошибка, попробуйте заново")
                    timer = QTimer()
                    timer.singleShot(1000, time_delay2)
            else:
                self.ui.Insert_info.setText("Ошибка, попробуйте заново")
                timer = QTimer()
                timer.singleShot(1000, time_delay2)

        self.ui.Insert.clicked.connect(lambda: insert_into_db_b())

        def select_month_operations():
            now_m = dt.datetime.now().strftime("%m")
            now_y = dt.datetime.now().strftime("%Y")

            self.ui.Page2_Main.clear()
            self.ui.Page2_Main.setHorizontalHeaderLabels(['Доход / Расход', 'Категория', 'Сумма', 'Дата'])
            self.ui.Page2_Main.setStyleSheet(u"color:rgb(67, 67, 67)")
            font = QFont()
            font.setFamily(u"Ubuntu Medium")
            font.setPointSize(8)
            font.setBold(True)
            header_new = [self.ui.Page2_Main.horizontalHeaderItem(x).setFont(font) for x in range(4)]

            with sqlite3.connect('database.db') as conn1:
                cursor1 = conn1.cursor()
                select_info = f"SELECT * FROM Info where date BETWEEN '{now_y}-{now_m}-01' " \
                              f"and '{now_y}-{now_m}-31' ORDER BY date"
                cursor1.execute(select_info)
                number = cursor1.fetchall()
                self.ui.Page2_Main.setColumnCount(4)
                self.ui.Page2_Main.setRowCount(len(number))
                new_row_heigh = [self.ui.Page2_Main.setRowHeight(x, 1) for x in range(len(number))]

                for row_num, row in enumerate(number):
                    self.ui.Page2_Main.setItem(row_num, 0, QTableWidgetItem(row[1]))
                    self.ui.Page2_Main.setItem(row_num, 1, QTableWidgetItem(row[2]))
                    self.ui.Page2_Main.setItem(row_num, 2, QTableWidgetItem(str(row[3])))
                    self.ui.Page2_Main.setItem(row_num, 3, QTableWidgetItem(row[4]))

        self.ui.Button2.clicked.connect(lambda: select_month_operations())

        def select_operations_period():
            self.ui.Page2_Main.clear()
            self.ui.Page2_Main.setHorizontalHeaderLabels(['Доход / Расход', 'Категория', 'Сумма', 'Дата'])
            self.ui.Page2_Main.setStyleSheet(u"color:rgb(67, 67, 67)")

            font = QFont()
            font.setFamily(u"Ubuntu Medium")
            font.setPointSize(8)
            font.setBold(True)
            header_new = [self.ui.Page2_Main.horizontalHeaderItem(x).setFont(font) for x in range(4)]

            date_from = self.ui.Date_From_2.text().split('.')
            date_from = f"{date_from[2]}-{date_from[1]}-{date_from[0]}"
            date_to = self.ui.Date_To_2.text().split('.')
            date_to = f"{date_to[2]}-{date_to[1]}-{date_to[0]}"
            self.ui.Current_option.setText(f"Операции за период")

            with sqlite3.connect('database.db') as conn1:
                cursor1 = conn1.cursor()
                select_info = f"SELECT * FROM Info WHERE date BETWEEN '{date_from}' AND '{date_to}' ORDER BY date"
                cursor1.execute(select_info)
                number = cursor1.fetchall()
                self.ui.Page2_Main.setColumnCount(4)
                self.ui.Page2_Main.setRowCount(len(number))
                new_row_heigh = [self.ui.Page2_Main.setRowHeight(x, 1) for x in range(len(number))]

                for row_num, row in enumerate(number):
                    self.ui.Page2_Main.setItem(row_num, 0, QTableWidgetItem(row[1]))
                    self.ui.Page2_Main.setItem(row_num, 1, QTableWidgetItem(row[2]))
                    self.ui.Page2_Main.setItem(row_num, 2, QTableWidgetItem(str(row[3])))
                    self.ui.Page2_Main.setItem(row_num, 3, QTableWidgetItem(row[4]))

        self.ui.Show2.clicked.connect(lambda: select_operations_period())

        def create_inc_bar (labels, scores, color1, color2):
            self.ui.canvas1.deleteLater()
            self.ui.canvas1 = Bar(labels, scores, color1, color2)
            self.ui.horizontalLayout_canvas1.addWidget(self.ui.canvas1)
            self.ui.canvas1.close()

        def create_ex_bar(labels, scores, color1, color2):
            self.ui.canvas2.deleteLater()
            self.ui.canvas2 = Bar(labels, scores, color1, color2)
            self.ui.horizontalLayout_canvas2.addWidget(self.ui.canvas2)
            self.ui.canvas2.close()

        def create_incex_pie(labels, scores):
            self.ui.canvas.deleteLater()
            self.ui.canvas = Pie(labels, scores)
            self.ui.horizontalLayout_canvas.addWidget(self.ui.canvas)
            self.ui.canvas.close()

        self.ui.canvas1 = Bar([], [], 1, 0.7)
        self.ui.horizontalLayout_canvas1.addWidget(self.ui.canvas1)

        self.ui.canvas2 = Bar([], [], 1, 0.7)
        self.ui.horizontalLayout_canvas2.addWidget(self.ui.canvas2)

        self.ui.canvas = Pie(('Доход   ', '   Расход'), (5, 6))
        self.ui.horizontalLayout_canvas.addWidget(self.ui.canvas)

        def table_show():

            now_m = dt.datetime.now().strftime("%m")
            now_y = dt.datetime.now().strftime("%Y")

            self.ui.Page3_Main.clear()
            self.ui.Page3_Main.setHorizontalHeaderLabels(['Доход / Расход', 'Категория', 'Сумма'])
            self.ui.Page3_Main.setStyleSheet(u"color:rgb(67, 67, 67)")

            font = QFont()
            font.setFamily(u"Ubuntu Medium")
            font.setPointSize(8)
            font.setBold(True)
            header_new = [self.ui.Page3_Main.horizontalHeaderItem(x).setFont(font) for x in range(3)]

            with sqlite3.connect('database.db') as conn1:
                cursor1 = conn1.cursor()
                select_info = f"SELECT IncEx, Item, sum(Sum) FROM Info WHERE date BETWEEN " \
                              f"'{now_y}-{now_m}-01' and '{now_y}-{now_m}-31' GROUP BY Item"
                cursor1.execute(select_info)
                operations = cursor1.fetchall()
                self.ui.Page3_Main.setColumnCount(3)
                self.ui.Page3_Main.setRowCount(len(operations) + 5)
                new_row_heigh = [self.ui.Page3_Main.setRowHeight(x, 1) for x in range(len(operations) + 2)]
                Inc = [('Доход', 'Итого', sum([x[2] for x in operations if x[0] == 'Доход']))] + [('', '', '')] + \
                      [x for x in operations if x[0] == 'Доход'] + [('', '', '')]
                Ex = [('Расход', 'Итого', sum([x[2] for x in operations if x[0] == 'Расход']))] + [('', '', '')] + \
                     [x for x in operations if x[0] == 'Расход']

                for row_num, row in enumerate(Inc):
                    self.ui.Page3_Main.setItem(row_num, 0, QTableWidgetItem(row[0]))
                    self.ui.Page3_Main.setItem(row_num, 1, QTableWidgetItem(row[1]))
                    self.ui.Page3_Main.setItem(row_num, 2, QTableWidgetItem(str(row[2])))
                    if row_num == 0:
                        font = QFont()
                        font.setFamily(u"Ubuntu Medium")
                        font.setPointSize(8)
                        font.setBold(True)
                        header = [self.ui.Page3_Main.item(row_num, x).setFont(font) for x in range(3)]
                    last_row = row_num + 1

                for row_num, row in enumerate(Ex):
                    self.ui.Page3_Main.setItem(row_num + last_row, 0, QTableWidgetItem(row[0]))
                    self.ui.Page3_Main.setItem(row_num + last_row, 1, QTableWidgetItem(row[1]))
                    self.ui.Page3_Main.setItem(row_num + last_row, 2, QTableWidgetItem(str(row[2])))
                    if row_num == 0:
                        font = QFont()
                        font.setFamily(u"Ubuntu Medium")
                        font.setPointSize(8)
                        font.setBold(True)
                        header = [self.ui.Page3_Main.item(row_num + last_row, x).setFont(font) for x in range(3)]

                Inc_sum = sum([x[2] for x in operations if x[0] == 'Доход'])
                Inc = {x[1]: round(x[2] / Inc_sum * 100, 1) for x in operations if x[0] == 'Доход'}
                Inc_sorted = sorted(Inc, key=lambda x: Inc[x], reverse=True)
                Inc_to_bar = [Inc[x] for x in Inc_sorted]

                create_inc_bar(Inc_sorted[:10], Inc_to_bar[:10], 0.8, 0.5)

                Ex_sum = sum([x[2] for x in operations if x[0] == 'Расход'])
                Ex = {x[1]: round(x[2] / Ex_sum * 100, 1) for x in operations if x[0] == 'Расход'}
                Ex_sorted = sorted(Ex, key=lambda x: Ex[x], reverse=True)
                Ex_to_bar = [Ex[x] for x in Ex_sorted]

                create_ex_bar(Ex_sorted[:10], Ex_to_bar[:10], 0.4, 0.2)

                create_incex_pie(('Доход   ', '   Расход'), (Inc_sum, Ex_sum))

        self.ui.Button3.clicked.connect(lambda: table_show())

        def table_show_period():
            self.ui.Page3_Main.clear()
            self.ui.Page3_Main.setHorizontalHeaderLabels(['Доход / Расход', 'Категория', 'Сумма'])
            self.ui.Page3_Main.setStyleSheet(u"color:rgb(67, 67, 67)")

            font = QFont()
            font.setFamily(u"Ubuntu Medium")
            font.setPointSize(8)
            font.setBold(True)
            header_new = [self.ui.Page3_Main.horizontalHeaderItem(x).setFont(font) for x in range(3)]

            date_from = self.ui.Date_From_3.text().split('.')
            date_from = f"{date_from[2]}-{date_from[1]}-{date_from[0]}"
            date_to = self.ui.Date_To_3.text().split('.')
            date_to = f"{date_to[2]}-{date_to[1]}-{date_to[0]}"
            self.ui.Current_option.setText(f"Таблица за период")

            with sqlite3.connect('database.db') as conn1:
                cursor1 = conn1.cursor()
                select_info = f"SELECT IncEx, Item, sum(Sum) FROM Info WHERE date BETWEEN '{date_from}' " \
                              f"AND '{date_to}' GROUP BY Item"
                cursor1.execute(select_info)
                operations = cursor1.fetchall()
                self.ui.Page3_Main.setColumnCount(3)
                self.ui.Page3_Main.setRowCount(len(operations) + 5)
                new_row_heigh = [self.ui.Page3_Main.setRowHeight(x, 1) for x in range(len(operations) + 2)]
                Inc = [('Доход', 'Итого', sum([x[2] for x in operations if x[0] == 'Доход']))] + [('', '', '')] + \
                      [x for x in operations if x[0] == 'Доход'] + [('', '', '')]

                Ex = [('Расход', 'Итого', sum([x[2] for x in operations if x[0] == 'Расход']))] + [('', '', '')] + \
                     [x for x in operations if x[0] == 'Расход']

                for row_num, row in enumerate(Inc):
                    self.ui.Page3_Main.setItem(row_num, 0, QTableWidgetItem(row[0]))
                    self.ui.Page3_Main.setItem(row_num, 1, QTableWidgetItem(row[1]))
                    self.ui.Page3_Main.setItem(row_num, 2, QTableWidgetItem(str(row[2])))
                    if row_num == 0:
                        font = QFont()
                        font.setFamily(u"Ubuntu Medium")
                        font.setPointSize(8)
                        font.setBold(True)
                        header = [self.ui.Page3_Main.item(row_num, x).setFont(font) for x in range(3)]
                    last_row = row_num + 1

                for row_num, row in enumerate(Ex):
                    self.ui.Page3_Main.setItem(row_num + last_row, 0, QTableWidgetItem(row[0]))
                    self.ui.Page3_Main.setItem(row_num + last_row, 1, QTableWidgetItem(row[1]))
                    self.ui.Page3_Main.setItem(row_num + last_row, 2, QTableWidgetItem(str(row[2])))
                    if row_num == 0:
                        font = QFont()
                        font.setFamily(u"Ubuntu Medium")
                        font.setPointSize(8)
                        font.setBold(True)
                        header = [self.ui.Page3_Main.item(row_num + last_row, x).setFont(font) for x in range(3)]

                Inc_sum = sum([x[2] for x in operations if x[0] == 'Доход'])
                Inc = {x[1]: round(x[2] / Inc_sum * 100, 1) for x in operations if x[0] == 'Доход'}
                Inc_sorted = sorted(Inc, key=lambda x: Inc[x], reverse=True)
                Inc_to_bar = [Inc[x] for x in Inc_sorted]

                create_inc_bar(Inc_sorted[:10], Inc_to_bar[:10], 0.8, 0.5)

                Ex_sum = sum([x[2] for x in operations if x[0] == 'Расход'])
                Ex = {x[1]: round(x[2] / Ex_sum * 100, 1) for x in operations if x[0] == 'Расход'}
                Ex_sorted = sorted(Ex, key=lambda x: Ex[x], reverse=True)
                Ex_to_bar = [Ex[x] for x in Ex_sorted]

                create_ex_bar(Ex_sorted[:10], Ex_to_bar[:10], 0.4, 0.2)

                create_incex_pie(('Доход   ', '   Расход'), (Inc_sum, Ex_sum))

        self.ui.Show3.clicked.connect(lambda: table_show_period())

        self.show()

    def chose_item(self, index):
        self.ui.Choose_category.clear()
        self.ui.Choose_category.addItems(self.ui.Choose_option.itemData(index))

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
