# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'my_budgetZsUBQm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 900)
        MainWindow.setStyleSheet(u"")
        self.Centralwidget = QWidget(MainWindow)
        self.Centralwidget.setObjectName(u"Centralwidget")
        self.Centralwidget.setStyleSheet(u"")
        self.background_layout = QVBoxLayout(self.Centralwidget)
        self.background_layout.setSpacing(0)
        self.background_layout.setObjectName(u"background_layout")
        self.background_layout.setContentsMargins(0, 0, 0, 0)
        self.Background_frame = QFrame(self.Centralwidget)
        self.Background_frame.setObjectName(u"Background_frame")
        self.Background_frame.setMinimumSize(QSize(1280, 900))
        self.Background_frame.setStyleSheet(u"background-color: rgb(150, 150, 150);\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius: 12px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.Background_frame.setFrameShape(QFrame.NoFrame)
        self.Background_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Background_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Left_Frame = QFrame(self.Background_frame)
        self.Left_Frame.setObjectName(u"Left_Frame")
        self.Left_Frame.setMinimumSize(QSize(300, 720))
        self.Left_Frame.setMaximumSize(QSize(300, 16777215))
        self.Left_Frame.setStyleSheet(u"background-color: none;\n"
"border-top-left-radius:12px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.Left_Frame.setFrameShape(QFrame.StyledPanel)
        self.Left_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Left_Frame)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 1, 0)
        self.Frame1_Control_panel = QFrame(self.Left_Frame)
        self.Frame1_Control_panel.setObjectName(u"Frame1_Control_panel")
        self.Frame1_Control_panel.setEnabled(True)
        self.Frame1_Control_panel.setMinimumSize(QSize(299, 50))
        self.Frame1_Control_panel.setMaximumSize(QSize(16777215, 50))
        self.Frame1_Control_panel.setStyleSheet(u"border-top-left-radius:12px;\n"
"border-top-right-radius: 0px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color:rgb(200, 200, 200);")
        self.Frame1_Control_panel.setFrameShape(QFrame.StyledPanel)
        self.Frame1_Control_panel.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Frame1_Control_panel)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Control_label = QLabel(self.Frame1_Control_panel)
        self.Control_label.setObjectName(u"Control_label")
        self.Control_label.setEnabled(True)
        font = QFont()
        font.setFamily(u"Ubuntu")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Control_label.setFont(font)
        self.Control_label.setStyleSheet(u"color:rgb(75,75,75)")

        self.horizontalLayout_3.addWidget(self.Control_label)


        self.verticalLayout.addWidget(self.Frame1_Control_panel)

        self.Frame2_Control_btns_2 = QFrame(self.Left_Frame)
        self.Frame2_Control_btns_2.setObjectName(u"Frame2_Control_btns_2")
        self.Frame2_Control_btns_2.setStyleSheet(u"background-color:rgb(243, 243, 243);\n"
"border-radius: 0px")
        self.Frame2_Control_btns_2.setFrameShape(QFrame.StyledPanel)
        self.Frame2_Control_btns_2.setFrameShadow(QFrame.Raised)
        self.Button2 = QPushButton(self.Frame2_Control_btns_2)
        self.Button2.setObjectName(u"Button2")
        self.Button2.setGeometry(QRect(0, 41, 300, 40))
        font1 = QFont()
        font1.setFamily(u"Ubuntu Medium")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50)
        self.Button2.setFont(font1)
        self.Button2.setStyleSheet(u"QPushButton {\n"
"background-color:rgb(243, 243, 243);\n"
"border: 0px solid;\n"
"text-align: left;\n"
"color: rgb(75,75,75)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(220, 220, 220);\n"
"}")
        icon = QIcon()
        icon.addFile(u"b2_list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button2.setIcon(icon)
        self.Button2.setIconSize(QSize(48, 24))
        self.Button1 = QPushButton(self.Frame2_Control_btns_2)
        self.Button1.setObjectName(u"Button1")
        self.Button1.setGeometry(QRect(0, 0, 300, 40))
        self.Button1.setFont(font1)
        self.Button1.setStyleSheet(u"QPushButton {\n"
"background-color:rgb(243, 243, 243);\n"
"border: 0px solid;\n"
"text-align: left;\n"
"color: rgb(75,75,75)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(220, 220, 220);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"b1_input.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button1.setIcon(icon1)
        self.Button1.setIconSize(QSize(48, 24))
        self.Button3 = QPushButton(self.Frame2_Control_btns_2)
        self.Button3.setObjectName(u"Button3")
        self.Button3.setGeometry(QRect(0, 81, 300, 40))
        self.Button3.setFont(font1)
        self.Button3.setStyleSheet(u"QPushButton {\n"
"background-color:rgb(243, 243, 243);\n"
"border: 0px solid;\n"
"text-align: left;\n"
"color: rgb(75,75,75)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(220, 220, 220);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"b3_table.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button3.setIcon(icon2)
        self.Button3.setIconSize(QSize(48, 24))
        self.frame = QFrame(self.Frame2_Control_btns_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 300, 162))
        self.frame.setStyleSheet(u"background-color: rgb(200,200,200)\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.Button4 = QPushButton(self.Frame2_Control_btns_2)
        self.Button4.setObjectName(u"Button4")
        self.Button4.setGeometry(QRect(0, 122, 300, 40))
        self.Button4.setFont(font1)
        self.Button4.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(243, 243, 243);\n"
"border: 0px solid;\n"
"text-align: left;\n"
"color: rgb(75,75,75)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(220, 220, 220);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"b4_table.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button4.setIcon(icon3)
        self.Button4.setIconSize(QSize(48, 24))
        self.frame.raise_()
        self.Button2.raise_()
        self.Button1.raise_()
        self.Button3.raise_()
        self.Button4.raise_()

        self.verticalLayout.addWidget(self.Frame2_Control_btns_2)


        self.horizontalLayout.addWidget(self.Left_Frame)

        self.Right_Frame = QFrame(self.Background_frame)
        self.Right_Frame.setObjectName(u"Right_Frame")
        self.Right_Frame.setMinimumSize(QSize(980, 0))
        self.Right_Frame.setMaximumSize(QSize(16777215, 16777215))
        self.Right_Frame.setStyleSheet(u"background-color: none;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius: 12px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;")
        self.Right_Frame.setFrameShape(QFrame.StyledPanel)
        self.Right_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Right_Frame)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Frame1_Control_btns = QFrame(self.Right_Frame)
        self.Frame1_Control_btns.setObjectName(u"Frame1_Control_btns")
        self.Frame1_Control_btns.setMinimumSize(QSize(980, 50))
        self.Frame1_Control_btns.setMaximumSize(QSize(16777215, 50))
        self.Frame1_Control_btns.setStyleSheet(u"border-top-left-radius:0px;\n"
"border-top-right-radius: 12px;\n"
"border-bottom-right-radius: 0px;\n"
"border-bottom-left-radius: 0px;\n"
"background-color:rgb(200, 200, 200);")
        self.Frame1_Control_btns.setFrameShape(QFrame.StyledPanel)
        self.Frame1_Control_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Frame1_Control_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.Frame1_Control_btns)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.Frame1_Control_btns)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_7 = QFrame(self.Frame1_Control_btns)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_7)

        self.Current_option = QLabel(self.Frame1_Control_btns)
        self.Current_option.setObjectName(u"Current_option")
        self.Current_option.setEnabled(True)
        font2 = QFont()
        font2.setFamily(u"Ubuntu")
        font2.setPointSize(13)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        font2.setKerning(True)
        self.Current_option.setFont(font2)
        self.Current_option.setStyleSheet(u"color:rgb(75, 75, 75)")

        self.horizontalLayout_4.addWidget(self.Current_option)

        self.frame_8 = QFrame(self.Frame1_Control_btns)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_6 = QFrame(self.Frame1_Control_btns)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_3 = QFrame(self.Frame1_Control_btns)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_3)

        self.Buttons_layout = QHBoxLayout()
        self.Buttons_layout.setSpacing(12)
        self.Buttons_layout.setObjectName(u"Buttons_layout")
        self.Buttons_layout.setContentsMargins(-1, -1, 10, -1)
        self.Button1_Rollup = QPushButton(self.Frame1_Control_btns)
        self.Button1_Rollup.setObjectName(u"Button1_Rollup")
        self.Button1_Rollup.setMinimumSize(QSize(20, 20))
        self.Button1_Rollup.setMaximumSize(QSize(21, 21))
        font3 = QFont()
        font3.setKerning(True)
        self.Button1_Rollup.setFont(font3)
        self.Button1_Rollup.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(181, 181, 181);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(0, 170, 0, 150)\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"cp_b1_min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button1_Rollup.setIcon(icon4)
        self.Button1_Rollup.setCheckable(False)

        self.Buttons_layout.addWidget(self.Button1_Rollup)

        self.Button2_Max = QPushButton(self.Frame1_Control_btns)
        self.Button2_Max.setObjectName(u"Button2_Max")
        self.Button2_Max.setMinimumSize(QSize(20, 20))
        self.Button2_Max.setMaximumSize(QSize(21, 21))
        self.Button2_Max.setFont(font3)
        self.Button2_Max.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(181, 181, 181);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 238, 7, 150)\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"cp_b2_resize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button2_Max.setIcon(icon5)
        self.Button2_Max.setIconSize(QSize(16, 16))
        self.Button2_Max.setCheckable(False)

        self.Buttons_layout.addWidget(self.Button2_Max)

        self.Button3_Exit = QPushButton(self.Frame1_Control_btns)
        self.Button3_Exit.setObjectName(u"Button3_Exit")
        self.Button3_Exit.setMinimumSize(QSize(20, 20))
        self.Button3_Exit.setMaximumSize(QSize(21, 21))
        self.Button3_Exit.setFont(font3)
        self.Button3_Exit.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color:rgb(181, 181, 181);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 0, 9, 150)\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"cp_b3_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Button3_Exit.setIcon(icon6)
        self.Button3_Exit.setCheckable(False)

        self.Buttons_layout.addWidget(self.Button3_Exit)


        self.horizontalLayout_4.addLayout(self.Buttons_layout)


        self.verticalLayout_2.addWidget(self.Frame1_Control_btns)

        self.Frame2_Content_frame = QFrame(self.Right_Frame)
        self.Frame2_Content_frame.setObjectName(u"Frame2_Content_frame")
        self.Frame2_Content_frame.setMinimumSize(QSize(980, 0))
        self.Frame2_Content_frame.setMaximumSize(QSize(16777215, 16777215))
        self.Frame2_Content_frame.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 0px")
        self.Frame2_Content_frame.setFrameShape(QFrame.StyledPanel)
        self.Frame2_Content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Frame2_Content_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.StackedWidget_frame = QStackedWidget(self.Frame2_Content_frame)
        self.StackedWidget_frame.setObjectName(u"StackedWidget_frame")
        self.StackedWidget_frame.setMinimumSize(QSize(0, 0))
        self.StackedWidget_frame.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setPointSize(14)
        self.StackedWidget_frame.setFont(font4)
        self.StackedWidget_frame.setStyleSheet(u"background-color:rgb(255, 255, 255);")
        self.StackedWidget_frame.setFrameShape(QFrame.StyledPanel)
        self.StackedWidget_frame.setFrameShadow(QFrame.Raised)
        self.StackedWidget_frame.setLineWidth(1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet(u"background-color:rgb(243, 243, 243)")
        self.StackedWidget_frame.addWidget(self.page)
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.Page1.setStyleSheet(u"background-color:rgb(243, 243, 243)")
        self.Insert_info = QLabel(self.Page1)
        self.Insert_info.setObjectName(u"Insert_info")
        self.Insert_info.setGeometry(QRect(63, 230, 790, 30))
        self.Insert_info.setMinimumSize(QSize(500, 30))
        font5 = QFont()
        font5.setFamily(u"Ubuntu Medium")
        font5.setPointSize(10)
        self.Insert_info.setFont(font5)
        self.Insert_info.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.Choose_option_2 = QComboBox(self.Page1)
        self.Choose_option_2.setObjectName(u"Choose_option_2")
        self.Choose_option_2.setGeometry(QRect(63, 380, 150, 30))
        self.Choose_option_2.setMinimumSize(QSize(150, 30))
        self.Choose_option_2.setFont(font5)
        self.Choose_option_2.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.New_category = QLineEdit(self.Page1)
        self.New_category.setObjectName(u"New_category")
        self.New_category.setGeometry(QRect(225, 380, 150, 30))
        self.New_category.setMinimumSize(QSize(150, 30))
        self.New_category.setFont(font5)
        self.New_category.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.Insert_2 = QPushButton(self.Page1)
        self.Insert_2.setObjectName(u"Insert_2")
        self.Insert_2.setGeometry(QRect(389, 380, 150, 30))
        self.Insert_2.setMinimumSize(QSize(150, 30))
        self.Insert_2.setFont(font5)
        self.Insert_2.setStyleSheet(u"QPushButton {\n"
"background-color:rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color:rgb(67, 67, 67)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 88, 11);\n"
"}")
        self.Insert_info_2 = QLabel(self.Page1)
        self.Insert_info_2.setObjectName(u"Insert_info_2")
        self.Insert_info_2.setGeometry(QRect(63, 430, 790, 30))
        self.Insert_info_2.setMinimumSize(QSize(500, 30))
        self.Insert_info_2.setFont(font5)
        self.Insert_info_2.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.Insert_2_label = QLabel(self.Page1)
        self.Insert_2_label.setObjectName(u"Insert_2_label")
        self.Insert_2_label.setGeometry(QRect(63, 280, 790, 30))
        self.Insert_2_label.setMinimumSize(QSize(500, 30))
        font6 = QFont()
        font6.setFamily(u"Ubuntu Medium")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        self.Insert_2_label.setFont(font6)
        self.Insert_2_label.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.Insert_1_label = QLabel(self.Page1)
        self.Insert_1_label.setObjectName(u"Insert_1_label")
        self.Insert_1_label.setGeometry(QRect(63, 80, 790, 30))
        self.Insert_1_label.setMinimumSize(QSize(500, 30))
        self.Insert_1_label.setFont(font6)
        self.Insert_1_label.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.Choose_option = QComboBox(self.Page1)
        self.Choose_option.setObjectName(u"Choose_option")
        self.Choose_option.setGeometry(QRect(63, 180, 150, 30))
        self.Choose_option.setMinimumSize(QSize(150, 30))
        self.Choose_option.setFont(font5)
        self.Choose_option.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.Choose_category = QComboBox(self.Page1)
        self.Choose_category.setObjectName(u"Choose_category")
        self.Choose_category.setGeometry(QRect(225, 180, 150, 30))
        self.Choose_category.setMinimumSize(QSize(150, 30))
        self.Choose_category.setFont(font5)
        self.Choose_category.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.Sum = QLineEdit(self.Page1)
        self.Sum.setObjectName(u"Sum")
        self.Sum.setGeometry(QRect(387, 180, 150, 30))
        self.Sum.setMinimumSize(QSize(150, 30))
        self.Sum.setFont(font5)
        self.Sum.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.Insert = QPushButton(self.Page1)
        self.Insert.setObjectName(u"Insert")
        self.Insert.setGeometry(QRect(711, 180, 150, 30))
        self.Insert.setMinimumSize(QSize(150, 30))
        self.Insert.setFont(font5)
        self.Insert.setStyleSheet(u"QPushButton {\n"
"background-color:rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color:rgb(67, 67, 67)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 88, 11);\n"
"}")
        self.Date = QDateEdit(self.Page1)
        self.Date.setObjectName(u"Date")
        self.Date.setGeometry(QRect(549, 180, 150, 30))
        self.Date.setMinimumSize(QSize(150, 30))
        self.Date.setFont(font5)
        self.Date.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.label_7 = QLabel(self.Page1)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(225, 130, 150, 30))
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.label_8 = QLabel(self.Page1)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(63, 130, 150, 30))
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.label_9 = QLabel(self.Page1)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(387, 130, 150, 30))
        self.label_9.setFont(font5)
        self.label_9.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.label_10 = QLabel(self.Page1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(549, 130, 150, 30))
        self.label_10.setFont(font5)
        self.label_10.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.label_11 = QLabel(self.Page1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(63, 330, 150, 30))
        self.label_11.setFont(font5)
        self.label_11.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.label_12 = QLabel(self.Page1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(225, 330, 150, 30))
        self.label_12.setFont(font5)
        self.label_12.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.StackedWidget_frame.addWidget(self.Page1)
        self.Page2 = QWidget()
        self.Page2.setObjectName(u"Page2")
        self.Page2.setStyleSheet(u"background-color:rgb(243, 243, 243)")
        self.Page2_Main = QTableWidget(self.Page2)
        if (self.Page2_Main.columnCount() < 6):
            self.Page2_Main.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.Page2_Main.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.Page2_Main.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.Page2_Main.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.Page2_Main.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.Page2_Main.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Page2_Main.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.Page2_Main.setObjectName(u"Page2_Main")
        self.Page2_Main.setGeometry(QRect(62, 135, 590, 690))
        font7 = QFont()
        font7.setFamily(u"Ubuntu Light")
        self.Page2_Main.setFont(font7)
        self.Page2_Main.setStyleSheet(u"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.Date_To_2 = QDateEdit(self.Page2)
        self.Date_To_2.setObjectName(u"Date_To_2")
        self.Date_To_2.setGeometry(QRect(225, 88, 150, 30))
        self.Date_To_2.setFont(font5)
        self.Date_To_2.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.Show2 = QPushButton(self.Page2)
        self.Show2.setObjectName(u"Show2")
        self.Show2.setGeometry(QRect(389, 88, 150, 30))
        self.Show2.setFont(font5)
        self.Show2.setStyleSheet(u"QPushButton {\n"
"background-color:rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color:rgb(67, 67, 67)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 88, 11);\n"
"}")
        self.Date_From_2 = QDateEdit(self.Page2)
        self.Date_From_2.setObjectName(u"Date_From_2")
        self.Date_From_2.setGeometry(QRect(62, 88, 150, 30))
        font8 = QFont()
        font8.setFamily(u"Ubuntu Medium")
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setWeight(50)
        self.Date_From_2.setFont(font8)
        self.Date_From_2.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.label_4 = QLabel(self.Page2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 10, 801, 30))
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.label_5 = QLabel(self.Page2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 45, 150, 30))
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.label_6 = QLabel(self.Page2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 45, 150, 30))
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.StackedWidget_frame.addWidget(self.Page2)
        self.Page3 = QWidget()
        self.Page3.setObjectName(u"Page3")
        self.Page3.setStyleSheet(u"background-color:rgb(243, 243, 243)")
        self.Date_From_3 = QDateEdit(self.Page3)
        self.Date_From_3.setObjectName(u"Date_From_3")
        self.Date_From_3.setGeometry(QRect(62, 88, 150, 30))
        self.Date_From_3.setFont(font8)
        self.Date_From_3.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.Date_To_3 = QDateEdit(self.Page3)
        self.Date_To_3.setObjectName(u"Date_To_3")
        self.Date_To_3.setGeometry(QRect(225, 88, 150, 30))
        self.Date_To_3.setFont(font5)
        self.Date_To_3.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.Show3 = QPushButton(self.Page3)
        self.Show3.setObjectName(u"Show3")
        self.Show3.setGeometry(QRect(389, 88, 150, 30))
        self.Show3.setFont(font5)
        self.Show3.setStyleSheet(u"QPushButton {\n"
"background-color:rgb(255, 255, 255);\n"
"border: 1px solid gray;\n"
"border-radius: 5px;\n"
"color:rgb(67, 67, 67)\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 88, 11);\n"
"}")
        self.Page3_Main = QTableWidget(self.Page3)
        if (self.Page3_Main.columnCount() < 3):
            self.Page3_Main.setColumnCount(3)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Page3_Main.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Page3_Main.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Page3_Main.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        self.Page3_Main.setObjectName(u"Page3_Main")
        self.Page3_Main.setGeometry(QRect(62, 135, 410, 690))
        self.Page3_Main.setFont(font7)
        self.Page3_Main.setStyleSheet(u"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.label_3 = QLabel(self.Page3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 10, 801, 30))
        self.label_3.setFont(font5)
        self.label_3.setStyleSheet(u"color:rgb(67, 67, 67)")

        self.Inc_pie = QLabel(self.Page3)
        self.Inc_pie.setObjectName(u"Inc_pie")
        self.Inc_pie.setGeometry(QRect(480, 120, 480, 360))
        self.Inc_pie.setScaledContents(True)

        self.horizontalLayout_canvas1 = QHBoxLayout(self.Inc_pie)
        self.horizontalLayout_canvas1.setObjectName('horizontalLayout_canvas1')

        self.Ex_pie = QLabel(self.Page3)
        self.Ex_pie.setObjectName(u"Ex_pie")
        self.Ex_pie.setGeometry(QRect(480, 470, 480, 360))
        self.Ex_pie.setScaledContents(True)

        self.horizontalLayout_canvas2 = QHBoxLayout(self.Ex_pie)
        self.horizontalLayout_canvas2.setObjectName('horizontalLayout_canvas2')

        self.IncEx_pie = QLabel(self.Page3)
        self.IncEx_pie.setObjectName(u"IncEx_pie")
        self.IncEx_pie.setGeometry(QRect(570, 40, 300, 200))
        self.IncEx_pie.setScaledContents(False)

        self.horizontalLayout_canvas = QHBoxLayout(self.IncEx_pie)
        self.horizontalLayout_canvas.setObjectName('horizontalLayout_canvas')

        self.label = QLabel(self.Page3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 45, 150, 30))
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.label_2 = QLabel(self.Page3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 45, 150, 30))
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u"color:rgb(67, 67, 67)")
        self.StackedWidget_frame.addWidget(self.Page3)
        self.Page4 = QWidget()
        self.Page4.setObjectName(u"Page4")
        self.Page4.setStyleSheet(u"background-color:rgb(243, 243, 243)")
        self.Choose_year = QComboBox(self.Page4)
        self.Choose_year.setObjectName(u"Choose_year")
        self.Choose_year.setGeometry(QRect(1420, 10, 69, 22))
        self.Choose_year.setFont(font5)
        self.Choose_year.setStyleSheet(u"background-color: rgb(255,255,255);\n"
"border-radius: 5px;\n"
"border: 1px solid gray;\n"
"color:rgb(67, 67, 67);\n"
"selection-background-color: rgb(255, 88, 11)")
        self.Page4_Main = QTableWidget(self.Page4)
        if (self.Page4_Main.columnCount() < 14):
            self.Page4_Main.setColumnCount(14)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(6, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(7, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(8, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(9, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(10, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(11, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(12, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.Page4_Main.setHorizontalHeaderItem(13, __qtablewidgetitem22)
        self.Page4_Main.setObjectName(u"Page4_Main")
        self.Page4_Main.setGeometry(QRect(30, 45, 1460, 870))
        self.Page4_Main.setFont(font7)
        self.Page4_Main.setStyleSheet(u"selection-background-color: rgb(255, 88, 11)")
        self.StackedWidget_frame.addWidget(self.Page4)

        self.verticalLayout_3.addWidget(self.StackedWidget_frame)

        self.Frame3_Bottom = QFrame(self.Frame2_Content_frame)
        self.Frame3_Bottom.setObjectName(u"Frame3_Bottom")
        self.Frame3_Bottom.setMinimumSize(QSize(980, 0))
        self.Frame3_Bottom.setMaximumSize(QSize(16777215, 10))
        self.Frame3_Bottom.setStyleSheet(u"background-color:rgb(243, 243, 243);\n"
"border-radius: 0px")
        self.Frame3_Bottom.setFrameShape(QFrame.StyledPanel)
        self.Frame3_Bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Frame3_Bottom)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.Frame3_Bottom)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 10))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_9)

        self.frame_14 = QFrame(self.Frame3_Bottom)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(10, 0))
        self.frame_14.setMaximumSize(QSize(10, 10))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_14)


        self.verticalLayout_3.addWidget(self.Frame3_Bottom)


        self.verticalLayout_2.addWidget(self.Frame2_Content_frame)


        self.horizontalLayout.addWidget(self.Right_Frame)


        self.background_layout.addWidget(self.Background_frame)

        MainWindow.setCentralWidget(self.Centralwidget)

        self.retranslateUi(MainWindow)

        self.StackedWidget_frame.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Control_label.setText(QCoreApplication.translate("MainWindow", u"                     \u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435", None))
        self.Button2.setText(QCoreApplication.translate("MainWindow", u"    \u041e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u0437\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.Button1.setText(QCoreApplication.translate("MainWindow", u"    \u0412\u043d\u0435\u0441\u0442\u0438 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e / \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.Button3.setText(QCoreApplication.translate("MainWindow", u"    \u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0437\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u043c\u0435\u0441\u044f\u0446", None))
        self.Button4.setText(QCoreApplication.translate("MainWindow", u"    \u0422\u0430\u0431\u043b\u0438\u0446\u0430 \u0437\u0430 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u0433\u043e\u0434", None))
        self.Current_option.setText("")
#if QT_CONFIG(tooltip)
        self.Button1_Rollup.setToolTip(QCoreApplication.translate("MainWindow", u"\u0421\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.Button1_Rollup.setText("")
#if QT_CONFIG(tooltip)
        self.Button2_Max.setToolTip(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u0432\u0435\u0440\u043d\u0443\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.Button2_Max.setText("")
#if QT_CONFIG(tooltip)
        self.Button3_Exit.setToolTip(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
#endif // QT_CONFIG(tooltip)
        self.Button3_Exit.setText("")
        self.Insert_info.setText("")
        self.Insert_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
        self.Insert_info_2.setText("")
        self.Insert_2_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.Insert_1_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e", None))
        self.Insert.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434 / \u0420\u0430\u0441\u0445\u043e\u0434", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434 / \u0420\u0430\u0441\u0445\u043e\u0434", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        ___qtablewidgetitem = self.Page2_Main.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u2116", None));
        ___qtablewidgetitem1 = self.Page2_Main.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434 / \u0420\u0430\u0441\u0445\u043e\u0434", None));
        ___qtablewidgetitem2 = self.Page2_Main.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None));
        ___qtablewidgetitem3 = self.Page2_Main.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None));
        ___qtablewidgetitem4 = self.Page2_Main.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430", None));
        ___qtablewidgetitem5 = self.Page2_Main.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None));
        self.Show2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434 \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u0443\u044e \u0438 \u043a\u043e\u043d\u0435\u0447\u043d\u0443\u044e \u0434\u0430\u0442\u0443 \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c\"", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0434\u0430\u0442\u0430", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u0434\u0430\u0442\u0430", None))
        self.Show3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c", None))
        ___qtablewidgetitem6 = self.Page3_Main.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0445\u043e\u0434 / \u0420\u0430\u0441\u0445\u043e\u0434", None));
        ___qtablewidgetitem7 = self.Page3_Main.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None));
        ___qtablewidgetitem8 = self.Page3_Main.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043c\u043c\u0430", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0442\u0430\u0431\u043b\u0438\u0446\u044b \u0437\u0430 \u043f\u0435\u0440\u0438\u043e\u0434 \u0432\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043d\u0430\u0447\u0430\u043b\u044c\u043d\u0443\u044e \u0438 \u043a\u043e\u043d\u0435\u0447\u043d\u0443\u044e \u0434\u0430\u0442\u0443 \u0438 \u043d\u0430\u0436\u043c\u0438\u0442\u0435 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0443 \"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c\"", None))
        self.Inc_pie.setText("")
        self.Ex_pie.setText("")
        self.IncEx_pie.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u0430\u044f \u0434\u0430\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0447\u043d\u0430\u044f \u0434\u0430\u0442\u0430", None))
        ___qtablewidgetitem9 = self.Page4_Main.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u044c\u044f", None));
        ___qtablewidgetitem10 = self.Page4_Main.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u042f\u043d\u0432\u0430\u0440\u044c", None));
        ___qtablewidgetitem11 = self.Page4_Main.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0435\u0432\u0440\u0430\u043b\u044c", None));
        ___qtablewidgetitem12 = self.Page4_Main.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0440\u0442", None));
        ___qtablewidgetitem13 = self.Page4_Main.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043f\u0440\u0435\u043b\u044c", None));
        ___qtablewidgetitem14 = self.Page4_Main.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0439", None));
        ___qtablewidgetitem15 = self.Page4_Main.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"\u0418\u044e\u043d\u044c", None));
        ___qtablewidgetitem16 = self.Page4_Main.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"\u0418\u044e\u043b\u044c", None));
        ___qtablewidgetitem17 = self.Page4_Main.horizontalHeaderItem(8)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0433\u0443\u0441\u0442", None));
        ___qtablewidgetitem18 = self.Page4_Main.horizontalHeaderItem(9)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0435\u043d\u0442\u0440\u044f\u0431\u0440\u044c", None));
        ___qtablewidgetitem19 = self.Page4_Main.horizontalHeaderItem(10)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0442\u044f\u0431\u0440\u044c", None));
        ___qtablewidgetitem20 = self.Page4_Main.horizontalHeaderItem(11)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u044f\u0431\u0440\u044c", None));
        ___qtablewidgetitem21 = self.Page4_Main.horizontalHeaderItem(12)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043a\u0430\u0431\u0440\u044c", None));
        ___qtablewidgetitem22 = self.Page4_Main.horizontalHeaderItem(13)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u043e\u0433", None));
    # retranslateUi

