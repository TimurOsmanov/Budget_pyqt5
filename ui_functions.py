from my_budget import *

global_state = 0
global_state_1 = 0


class ui_functions(MainWindow):
    def maximize_restore(self):
        global global_state
        status = global_state
        if status == 0:
            self.showMaximized()
            global_state = 1
            self.ui.Centralwidget.setContentsMargins(0, 0, 0, 0)
            self.ui.Frame1_Control_panel.setStyleSheet("border-top-left-radius:0px; "
                                                       "border-top-right-radius: 0px; "
                                                       "border-bottom-right-radius: 0px; "
                                                       "border-bottom-left-radius: 0px; "
                                                       "background-color:rgb(200, 200, 200);")
            self.ui.Frame1_Control_btns.setStyleSheet("border-top-left-radius:0px; "
                                                      "border-top-right-radius: 0px; "
                                                      "border-bottom-right-radius: 0px; "
                                                      "border-bottom-left-radius: 0px; "
                                                      "background-color:rgb(200, 200, 200);")
            self.ui.Button2_Max.setToolTip("Восстановить")
        else:
            global_state = 0
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.Centralwidget.setContentsMargins(10, 10, 10, 10)
            self.ui.Frame1_Control_panel.setStyleSheet("border-top-left-radius:12px; "
                                                       "border-top-right-radius: 0px; "
                                                       "border-bottom-right-radius: 0px; "
                                                       "border-bottom-left-radius: 0px; "
                                                       "background-color:rgb(200, 200, 200);")
            self.ui.Frame1_Control_btns.setStyleSheet("border-top-left-radius:0px; "
                                                      "border-top-right-radius: 12px; "
                                                      "border-bottom-right-radius: 0px; "
                                                      "border-bottom-left-radius: 0px; "
                                                      "background-color:rgb(200, 200, 200);")
            self.ui.Button2_Max.setToolTip("Раскрыть")

    def ui_definitions(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.ui.Button2_Max.clicked.connect(lambda: ui_functions.maximize_restore(self))

        self.ui.Button1_Rollup.clicked.connect(lambda: self.showMinimized())

        self.ui.Button3_Exit.clicked.connect(lambda: self.close())

        self.sizegrip = QSizeGrip(self.ui.frame_14)
        self.sizegrip.setStyleSheet("QSizeGrip {"
                                    "background-color: rgb(0,0,0)"
                                    "width 10px;"
                                    "height 10px;"
                                    "margin 5px}"
                                    "QSizeGrip:hover {"
                                    "background-color: rgb(255, 255, 255)}")
        self.sizegrip.setToolTip("Изменить размер")

        self.ui.Button1.setCheckable(True)
        self.ui.Button2.setCheckable(True)
        self.ui.Button3.setCheckable(True)
        self.ui.Button4.setCheckable(True)
        self.ui.Button5.setCheckable(True)
        self.ui.Button6.setCheckable(True)
        self.ui.Button7.setCheckable(True)
        self.ui.Button8.setCheckable(True)

        def controlbtnprssd(num, text, button):
            buttons = [self.ui.Button1, self.ui.Button2, self.ui.Button3, self.ui.Button4, self.ui.Button5,
                       self.ui.Button6, self.ui.Button7, self.ui.Button8]
            self.ui.StackedWidget_frame.setCurrentIndex(num)
            self.ui.Current_option.setText(text)
            for x in buttons:
                x.setStyleSheet(u"QPushButton {\n"
                                "background-color:rgb(243, 243, 243);\n"
                                "border: 0px solid;\n"
                                "text-align: left;\n"
                                "color: rgb(75,75,75)\n"
                                "}\n"
                                "QPushButton:hover {\n"
                                "background-color: rgb(220, 220, 220);\n"
                                "}")
            if button.isChecked():
                button.setStyleSheet(u"QPushButton {\n"
                                     "background-color: rgb(255, 88, 11);\n"
                                     "border: 0px solid;\n"
                                     "text-align: left;\n"
                                     "color: rgb(75,75,75)\n"
                                     "}\n")
                button.setChecked(False)
                new_buttons = [x for x in buttons if x != button]
                for x in new_buttons:
                    x.setStyleSheet(u"QPushButton {\n"
                                    "background-color:rgb(243, 243, 243);\n"
                                    "border: 0px solid;\n"
                                    "text-align: left;\n"
                                    "color: rgb(75,75,75)\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "background-color: rgb(220, 220, 220);\n"
                                    "}")

        self.ui.StackedWidget_frame.setCurrentIndex(0)
        self.ui.Button1.clicked.connect(lambda: controlbtnprssd(1, "Внести операцию / категорию", self.ui.Button1))
        self.ui.Button2.clicked.connect(lambda: controlbtnprssd(2, "Операции за месяц", self.ui.Button2))
        self.ui.Button3.clicked.connect(lambda: controlbtnprssd(3, "Таблица за текущий месяц", self.ui.Button3))
        self.ui.Button4.clicked.connect(lambda: controlbtnprssd(4, "Таблица за текущий год", self.ui.Button4))
        self.ui.Button5.clicked.connect(lambda: controlbtnprssd(5, "Внести часы работы", self.ui.Button5))
        self.ui.Button6.clicked.connect(lambda: controlbtnprssd(6, "Часы работы за текущий месяц", self.ui.Button6))
        self.ui.Button7.clicked.connect(lambda: controlbtnprssd(7, "Таблица часов работы", self.ui.Button7))
        self.ui.Button8.clicked.connect(lambda: controlbtnprssd(8, "Часы работы за текущий год", self.ui.Button8))

        new_columns = [self.ui.Page2_Main.setColumnWidth(x[0], x[1]) for x in enumerate([30, 120, 140, 100, 80, 70])]

        new_columns = [self.ui.Page3_Main.setColumnWidth(x[0], x[1]) for x in enumerate([120, 140, 110])]

        new_columns = [self.ui.Page4_Main.setColumnWidth(x[0], x[1]) for x in enumerate([93] + [102] * 13)]

        new_columns = [self.ui.Page7_Main.setColumnWidth(x[0], x[1]) for x in enumerate([100, 100])]

        new_columns = [self.ui.Page6_Main.setColumnWidth(x[0], x[1]) for x in enumerate([30, 140, 100, 80, 70])]

        new_columns = [self.ui.Page8_Main.setColumnWidth(x[0], x[1]) for x in enumerate([93] + [102] * 13)]

        self.ui.Date.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date.calendarWidget().setSelectedDate(today)
        self.ui.Date.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

        self.ui.Date_From_2.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date_From_2.calendarWidget().setSelectedDate(today)
        self.ui.Date_From_2.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

        self.ui.Date_To_2.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date_To_2.calendarWidget().setSelectedDate(today)
        self.ui.Date_To_2.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

        self.ui.Date_From_3.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date_From_3.calendarWidget().setSelectedDate(today)
        self.ui.Date_From_3.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

        self.ui.Date_To_3.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date_To_3.calendarWidget().setSelectedDate(today)
        self.ui.Date_To_3.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

        self.ui.Date_2.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date_2.calendarWidget().setSelectedDate(today)
        self.ui.Date_2.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

        self.ui.Date_From_6.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date_From_6.calendarWidget().setSelectedDate(today)
        self.ui.Date_From_6.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

        self.ui.Date_To_6.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date_To_6.calendarWidget().setSelectedDate(today)
        self.ui.Date_To_6.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

        self.ui.Date_From_7.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date_From_7.calendarWidget().setSelectedDate(today)
        self.ui.Date_From_7.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

        self.ui.Date_To_7.setCalendarPopup(True)
        today = QDate.currentDate()
        self.ui.Date_To_7.calendarWidget().setSelectedDate(today)
        self.ui.Date_To_7.calendarWidget().setStyleSheet("color: rgb(0,0,0)")

    def return_status():
        return global_state
