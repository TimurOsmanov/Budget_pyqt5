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
        self.fig, self.ax = plt.subplots(1, dpi=100, figsize=(3, 3), facecolor='#f3f3f3')
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
        if not scores:
            plt.yticks(cols[0], [str(0) + '%' for x in cols[0]], fontsize=8)
        else:
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
        self.setGeometry(90, 20, 1280, 800)
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

        self.ui.Button1.clicked.connect(lambda: self.resize(1280, 900))

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
            Inc, Ex = get_categories()
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

        def insert(data_tuple):
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

        def insert_into_db():
            global operation_id
            operation_id += 1
            date = self.ui.Date.text().split('.')
            date = f"{date[2]}-{date[1]}-{date[0]}"
            data_tuple = (operation_id, self.ui.Choose_option.currentText(),
                          self.ui.Choose_category.currentText(), self.ui.Sum.text(), date)
            if all(data_tuple):
                try:
                    float(data_tuple[3])
                    insert(data_tuple)
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

        self.ui.Insert.clicked.connect(lambda: insert_into_db())

        def delete(row_in_db, row_in_table):
            global index
            with sqlite3.connect('database.db') as conn5:
                cursor5 = conn5.cursor()
                delete_info = f"DELETE FROM Info WHERE unique_id = '{row_in_db}'"
                try:
                    cursor5.execute(delete_info)
                    self.ui.Page2_Main.removeRow(row_in_table)
                except Exception as e:
                    print(e)
            if index == 0:
                self.ui.Current_option.setText("Операции за месяц")
                show_month_operations()
            else:
                date_from = self.ui.Date_From_2.text().split('.')
                date_from = f"{date_from[2]}-{date_from[1]}-{date_from[0]}"
                date_to = self.ui.Date_To_2.text().split('.')
                date_to = f"{date_to[2]}-{date_to[1]}-{date_to[0]}"
                self.ui.Current_option.setText("Операции за период")
                show_operations(date_from, date_to)

        def select_data_for_operations(date_from, date_to):
            with sqlite3.connect('database.db') as conn1:
                cursor1 = conn1.cursor()
                select_info = f"SELECT * FROM Info WHERE date BETWEEN '{date_from}' AND '{date_to}' ORDER BY date"
                cursor1.execute(select_info)
                operations = cursor1.fetchall()
                self.ui.Page2_Main.setColumnCount(6)
                self.ui.Page2_Main.setRowCount(len(operations))
                new_row_heigh = [self.ui.Page2_Main.setRowHeight(x, 1) for x in range(len(operations))]
                return operations

        def set_font(bold):
            font = QFont()
            font.setFamily(u"Ubuntu Medium")
            font.setPointSize(8)
            if bold:
                font.setBold(True)
            else:
                font.setBold(False)
            return font

        def delete_button_cell(row, col, row_delete_in_db):
            self.d_button = QPushButton(self.ui.Page2_Main)
            self.d_button.setCursor(Qt.PointingHandCursor)
            icon4 = QIcon()
            icon4.addFile(u"delete_cell.png", QSize(), QIcon.Normal, QIcon.Off)
            self.d_button.setIcon(icon4)
            self.d_button.clicked.connect(lambda: delete(row_delete_in_db, row))
            self.ui.Page2_Main.setCellWidget(row, col, self.d_button)

        def show_operations(date_from, date_to):
            self.resize(1280, 900)
            self.ui.Page2_Main.clear()
            self.ui.Page2_Main.setHorizontalHeaderLabels(['№', 'Доход / Расход', 'Категория', 'Сумма',
                                                          'Дата', 'Удалить'])
            font = set_font(True)
            header_new = [self.ui.Page2_Main.horizontalHeaderItem(x).setFont(font) for x in range(6)]
            operations = select_data_for_operations(date_from, date_to)
            for row_num, row in enumerate(operations):
                self.ui.Page2_Main.setItem(row_num, 0, QTableWidgetItem(str(row[0])))
                self.ui.Page2_Main.setItem(row_num, 1, QTableWidgetItem(row[1]))
                self.ui.Page2_Main.setItem(row_num, 2, QTableWidgetItem(row[2]))
                self.ui.Page2_Main.setItem(row_num, 3, QTableWidgetItem(
                    "{:,.2f}".format(float(row[3])).replace(',', ' ') + ' р'))
                self.ui.Page2_Main.setItem(row_num, 4, QTableWidgetItem(row[4]))
                delete_button_cell(row_num, 5, row[0])

        def show_month_operations():
            global index
            index = 0
            now_m = dt.datetime.now().strftime("%m")
            now_y = dt.datetime.now().strftime("%Y")
            date_from = f'{now_y}-{now_m}-01'
            date_to = f'{now_y}-{now_m}-31'
            show_operations(date_from, date_to)

        self.ui.Button2.clicked.connect(lambda: show_month_operations())

        def show_operations_period():
            global index
            index = 1
            date_from = self.ui.Date_From_2.text().split('.')
            date_from = f"{date_from[2]}-{date_from[1]}-{date_from[0]}"
            date_to = self.ui.Date_To_2.text().split('.')
            date_to = f"{date_to[2]}-{date_to[1]}-{date_to[0]}"
            show_operations(date_from, date_to)
            self.ui.Current_option.setText(f"Операции за период")

        self.ui.Show2.clicked.connect(lambda: show_operations_period())

        def create_inc_bar(labels, scores, color1, color2):
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
            if any(scores):
                scores = scores
            elif not all(scores):
                scores = [1 for x in scores]
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

        def select_data_for_table(date_from, date_to):
            with sqlite3.connect('database.db') as conn1:
                cursor1 = conn1.cursor()
                select_info = f"SELECT IncEx, Item, sum(Sum) FROM Info WHERE date BETWEEN '{date_from}' " \
                              f"AND '{date_to}' GROUP BY Item"
                cursor1.execute(select_info)
                operations = cursor1.fetchall()
                self.ui.Page3_Main.setColumnCount(3)
                self.ui.Page3_Main.setRowCount(len(operations) + 5)
                new_row_heigh = [self.ui.Page3_Main.setRowHeight(x, 1) for x in range(len(operations) + 5)]
            return operations

        def set_item_page3(operations, i):
            for row_num, row in enumerate(operations):
                self.ui.Page3_Main.setItem(row_num, 0, QTableWidgetItem(row[0]))
                self.ui.Page3_Main.setItem(row_num, 1, QTableWidgetItem(row[1]))
                self.ui.Page3_Main.setItem(row_num, 2, QTableWidgetItem(str(row[2])))
                if row_num in i:
                    font = set_font(True)
                    header = [self.ui.Page3_Main.item(row_num, x).setFont(font) for x in range(3)]

        def show_table(date_from, date_to):
            self.resize(1280, 900)
            self.ui.Page3_Main.clear()
            self.ui.Page3_Main.setHorizontalHeaderLabels(['Доход / Расход', 'Категория', 'Сумма'])
            font = set_font(True)
            header_new = [self.ui.Page3_Main.horizontalHeaderItem(x).setFont(font) for x in range(3)]
            operations = select_data_for_table(date_from, date_to)
            Inc = [('Доход', 'Итого', sum([x[2] for x in operations if x[0] == 'Доход']))] + [('', '', '')] + \
                  [x for x in operations if x[0] == 'Доход'] + [('', '', '')]

            Ex = [('Расход', 'Итого', sum([x[2] for x in operations if x[0] == 'Расход']))] + [('', '', '')] + \
                 [x for x in operations if x[0] == 'Расход']
            i = [x[0] for x in enumerate(Inc + Ex) if x[1][1] in ('Итого', '')]
            IncEx = list(map(lambda x: (x[0], x[1], "{:,.2f}".format(float(x[2])).replace(',', ' ') + ' р') if x[0]
                             else x, Inc + Ex))
            set_item_page3(IncEx, i)

            Inc_sum = sum([x[2] for x in operations if x[0] == 'Доход'])
            Inc = {x[1]: round(x[2] / Inc_sum * 100, 1) for x in operations if x[0] == 'Доход'}
            Inc_sorted = sorted(Inc, key=lambda x: Inc[x], reverse=True)
            Inc_to_bar = [Inc[x] for x in Inc_sorted]

            Ex_sum = sum([x[2] for x in operations if x[0] == 'Расход'])
            Ex = {x[1]: round(x[2] / Ex_sum * 100, 1) for x in operations if x[0] == 'Расход'}
            Ex_sorted = sorted(Ex, key=lambda x: Ex[x], reverse=True)
            Ex_to_bar = [Ex[x] for x in Ex_sorted]

            create_inc_bar(Inc_sorted[:10], Inc_to_bar[:10], 0.8, 0.5)
            create_ex_bar(Ex_sorted[:10], Ex_to_bar[:10], 0.4, 0.2)
            create_incex_pie(('Доход   ', '   Расход'), (Inc_sum, Ex_sum))

        def show_month_table():
            now_m = dt.datetime.now().strftime("%m")
            now_y = dt.datetime.now().strftime("%Y")
            date_from = f'{now_y}-{now_m}-01'
            date_to = f'{now_y}-{now_m}-31'
            show_table(date_from, date_to)

        self.ui.Button3.clicked.connect(lambda: show_month_table())

        def show_table_period():
            date_from = self.ui.Date_From_3.text().split('.')
            date_from = f"{date_from[2]}-{date_from[1]}-{date_from[0]}"
            date_to = self.ui.Date_To_3.text().split('.')
            date_to = f"{date_to[2]}-{date_to[1]}-{date_to[0]}"
            show_table(date_from, date_to)
            self.ui.Current_option.setText(f"Таблица за период")

        self.ui.Show3.clicked.connect(lambda: show_table_period())

        def combo3():
            self.ui.Choose_year = self.findChild(QComboBox, "Choose_year")
            now_year = dt.datetime.now().year
            Choose_year_items = [self.ui.Choose_year.addItem(str(x)) for x in range(now_year - 5, now_year + 5)]
            self.ui.Choose_year.setCurrentText(str(now_year))

        combo3()

        def set_item_page4(operations, month,  i):
            for row_num, row in operations:
                self.ui.Page4_Main.setItem(row_num, month, QTableWidgetItem(str(row)))
                if month != 0:
                    try:
                        self.ui.Page4_Main.item(row_num, month).setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                    except:
                        pass
                if row_num in i:
                    font = set_font(True)
                    header = [self.ui.Page4_Main.item(row_num, month).setFont(font)]

        def show_year_table(year):
            self.resize(1820, 1000)
            self.ui.Page4_Main.clear()
            if year == str(dt.datetime.now().year):
                self.ui.Current_option.setText(f"Таблица за текущий {year} год")
            else:
                self.ui.Current_option.setText(f"Таблица за {year} год")
            self.ui.Page4_Main.setHorizontalHeaderLabels(['Статья'] +
                                                         [f'{str(x).zfill(2)}.{year}' for x in range(1, 13)] + ['Итог'])
            self.ui.Page4_Main.setColumnCount(14)
            Inc, Ex = get_categories()
            self.ui.Page4_Main.setRowCount(len(Inc + Ex) + 7)
            font = set_font(False)
            font.setPointSize(9)
            header_new = [self.ui.Page4_Main.horizontalHeaderItem(x).setFont(font) for x in range(14)]
            new_row_heigh = [self.ui.Page4_Main.setRowHeight(x, 1) for x in range(len(Inc + Ex) + 7)]

            rows = ['Итог', ''] + ['Итого доход', ''] + Inc + [''] + ['Итого расход', ''] + Ex
            bold_text = [x[0] for x in enumerate(rows) if x[1] in ('Итого доход', 'Итого расход', 'Итог')]
            set_item_page4(enumerate(rows), 0, bold_text)

            for m in range(1, 13):
                operations = select_data_for_table(f'{year}-{str(m).zfill(2)}-01', f'{year}-{str(m).zfill(2)}-31')
                operations.append(('Доход', 'Итого доход', sum([x[2] for x in operations if x[0] == 'Доход'])))
                operations.append(('Расход', 'Итого расход', sum([x[2] for x in operations if x[0] == 'Расход'])))
                operations.append(('Доход', 'Итог', operations[-2][2] - operations[-1][2]))
                t = [(rows.index(x[1]), "{:,.2f}".format(int(x[2])).replace(',', ' ') + ' р') for x in operations]
                set_item_page4(t, m, bold_text)

        def show_current_year():
            year = self.ui.Choose_year.currentText()
            show_year_table(year)

        self.ui.Button4.clicked.connect(lambda: show_current_year())

        def show_selected_year():
            year = self.ui.Choose_year.currentText()
            show_year_table(year)

        self.ui.Choose_year.activated.connect(lambda: show_selected_year())

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
