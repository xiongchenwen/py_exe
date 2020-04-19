# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TSP_Ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1374, 855)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 291, 851))
        self.tabWidget.setStyleSheet("font: 9pt \"宋体\";")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 24, 271, 31))
        self.label.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(30, 60, 231, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"background-color: rgb(194, 194, 194);\n"
"color:rgb(85, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(129, 129, 129);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(30, 140, 231, 31))
        self.label_2.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 180, 241, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"宋体\";\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"宋体\";\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 1, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"宋体\";\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(30, 370, 231, 31))
        self.label_15.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_15.setObjectName("label_15")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 420, 256, 381))
        self.textBrowser_2.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(10, 0, 261, 31))
        self.label_16.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_16.setObjectName("label_16")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(10, 30, 266, 181))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_26 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_26.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_26.setIndent(10)
        self.label_26.setObjectName("label_26")
        self.gridLayout_7.addWidget(self.label_26, 2, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_27.setMaximumSize(QtCore.QSize(90, 16777215))
        self.label_27.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_27.setIndent(10)
        self.label_27.setObjectName("label_27")
        self.gridLayout_7.addWidget(self.label_27, 0, 0, 1, 1)
        self.radioButton_13 = QtWidgets.QRadioButton(self.gridLayoutWidget_7)
        self.radioButton_13.setCheckable(True)
        self.radioButton_13.setChecked(False)
        self.radioButton_13.setObjectName("radioButton_13")
        self.gridLayout_7.addWidget(self.radioButton_13, 5, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_29.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_29.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_29.setIndent(11)
        self.label_29.setObjectName("label_29")
        self.gridLayout_7.addWidget(self.label_29, 4, 0, 1, 2)
        self.radioButton_14 = QtWidgets.QRadioButton(self.gridLayoutWidget_7)
        self.radioButton_14.setObjectName("radioButton_14")
        self.gridLayout_7.addWidget(self.radioButton_14, 5, 1, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_15.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_15.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_15.setText("")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_7.addWidget(self.lineEdit_15, 0, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_25.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_25.setIndent(10)
        self.label_25.setObjectName("label_25")
        self.gridLayout_7.addWidget(self.label_25, 1, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_17.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_17.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_17.setText("")
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_7.addWidget(self.lineEdit_17, 1, 1, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_18.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_18.setText("")
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_7.addWidget(self.lineEdit_18, 2, 1, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_46.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_46.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_46.setObjectName("label_46")
        self.gridLayout_7.addWidget(self.label_46, 0, 2, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_47.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_47.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_47.setObjectName("label_47")
        self.gridLayout_7.addWidget(self.label_47, 1, 2, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.gridLayoutWidget_7)
        self.label_48.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_48.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_48.setObjectName("label_48")
        self.gridLayout_7.addWidget(self.label_48, 2, 2, 1, 1)
        self.gridLayout_7.setColumnStretch(0, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 510, 181, 51))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"background-color: rgb(194, 194, 194);\n"
"    font: 12pt \"宋体\";\n"
"color:rgb(85, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(129, 129, 129);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(20, 570, 261, 16))
        self.label_30.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_30.setObjectName("label_30")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 590, 256, 221))
        self.textBrowser_4.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.radioButton_12 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_12.setGeometry(QtCore.QRect(10, 390, 258, 21))
        self.radioButton_12.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_12.setObjectName("radioButton_12")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(10, 230, 261, 16))
        self.label_24.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_24.setObjectName("label_24")
        self.gridLayoutWidget_11 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_11.setGeometry(QtCore.QRect(10, 410, 261, 80))
        self.gridLayoutWidget_11.setObjectName("gridLayoutWidget_11")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.radioButton_10 = QtWidgets.QRadioButton(self.gridLayoutWidget_11)
        self.radioButton_10.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton_10.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButton_10.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_10.setObjectName("radioButton_10")
        self.gridLayout_12.addWidget(self.radioButton_10, 0, 0, 1, 1)
        self.radioButton_11 = QtWidgets.QRadioButton(self.gridLayoutWidget_11)
        self.radioButton_11.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_11.setObjectName("radioButton_11")
        self.gridLayout_12.addWidget(self.radioButton_11, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_11)
        self.label_23.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_23.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_23.setObjectName("label_23")
        self.gridLayout_12.addWidget(self.label_23, 1, 0, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.gridLayoutWidget_11)
        self.comboBox_5.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"宋体\";\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.gridLayout_12.addWidget(self.comboBox_5, 1, 1, 1, 1)
        self.gridLayoutWidget_12 = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget_12.setGeometry(QtCore.QRect(10, 260, 261, 119))
        self.gridLayoutWidget_12.setObjectName("gridLayoutWidget_12")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.gridLayoutWidget_12)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_45 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_45.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_45.setObjectName("label_45")
        self.gridLayout_13.addWidget(self.label_45, 1, 2, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.gridLayoutWidget_12)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_16.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_16.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_16.setText("")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_13.addWidget(self.lineEdit_16, 2, 1, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.gridLayoutWidget_12)
        self.lineEdit_22.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_22.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_22.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_13.addWidget(self.lineEdit_22, 1, 1, 1, 1)
        self.radioButton_17 = QtWidgets.QRadioButton(self.gridLayoutWidget_12)
        self.radioButton_17.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_17.setChecked(True)
        self.radioButton_17.setObjectName("radioButton_17")
        self.gridLayout_13.addWidget(self.radioButton_17, 0, 0, 1, 3)
        self.label_44 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_44.setMaximumSize(QtCore.QSize(180, 16777215))
        self.label_44.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_44.setObjectName("label_44")
        self.gridLayout_13.addWidget(self.label_44, 1, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_28.setMinimumSize(QtCore.QSize(100, 0))
        self.label_28.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_28.setIndent(10)
        self.label_28.setObjectName("label_28")
        self.gridLayout_13.addWidget(self.label_28, 2, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget_12)
        self.label_31.setMinimumSize(QtCore.QSize(100, 0))
        self.label_31.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_31.setIndent(10)
        self.label_31.setObjectName("label_31")
        self.gridLayout_13.addWidget(self.label_31, 3, 0, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.gridLayoutWidget_12)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_19.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_19.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_19.setText("")
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_13.addWidget(self.lineEdit_19, 3, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(30, 40, 218, 131))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_32.setMinimumSize(QtCore.QSize(70, 0))
        self.label_32.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_32.setObjectName("label_32")
        self.gridLayout_4.addWidget(self.label_32, 2, 0, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_39.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_39.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_39.setObjectName("label_39")
        self.gridLayout_4.addWidget(self.label_39, 2, 2, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_37.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_37.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_37.setObjectName("label_37")
        self.gridLayout_4.addWidget(self.label_37, 1, 2, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_19.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 1, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_18.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_18.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_17.setMinimumSize(QtCore.QSize(70, 0))
        self.label_17.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 3, 0, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_36.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_36.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_36.setObjectName("label_36")
        self.gridLayout_4.addWidget(self.label_36, 0, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_5.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_4.addWidget(self.lineEdit_5, 0, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_6.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_4.addWidget(self.lineEdit_6, 1, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_7.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_7.setText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_4.addWidget(self.lineEdit_7, 2, 1, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_8.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_4.addWidget(self.lineEdit_8, 3, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(10, 210, 261, 16))
        self.label_20.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_20.setObjectName("label_20")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(20, 380, 251, 91))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.radioButton.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton.setObjectName("radioButton")
        self.gridLayout_5.addWidget(self.radioButton, 1, 0, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_2.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout_5.addWidget(self.radioButton_2, 1, 1, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_4.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_5.addWidget(self.radioButton_4, 2, 1, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget_5)
        self.radioButton_3.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_5.addWidget(self.radioButton_3, 2, 0, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_42.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_42.setObjectName("label_42")
        self.gridLayout_5.addWidget(self.label_42, 0, 0, 1, 2)
        self.label_21 = QtWidgets.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.label_21.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(10, 570, 261, 16))
        self.label_22.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_22.setObjectName("label_22")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 610, 256, 181))
        self.textBrowser_3.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.tab_3)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(20, 230, 251, 148))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_9.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_8.addWidget(self.lineEdit_9, 0, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_35.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_35.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_35.setObjectName("label_35")
        self.gridLayout_8.addWidget(self.label_35, 2, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_33.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_33.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_33.setObjectName("label_33")
        self.gridLayout_8.addWidget(self.label_33, 0, 0, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_40.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_40.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_40.setObjectName("label_40")
        self.gridLayout_8.addWidget(self.label_40, 2, 2, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_12.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_8.addWidget(self.lineEdit_12, 1, 2, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_10.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_8.addWidget(self.lineEdit_10, 0, 2, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_38.setMaximumSize(QtCore.QSize(150, 16777215))
        self.label_38.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_38.setObjectName("label_38")
        self.gridLayout_8.addWidget(self.label_38, 5, 0, 1, 2)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_11.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_8.addWidget(self.lineEdit_11, 1, 1, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_13.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_13.setText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_8.addWidget(self.lineEdit_13, 2, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget_8)
        self.label_34.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_34.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_34.setObjectName("label_34")
        self.gridLayout_8.addWidget(self.label_34, 1, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_14.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_14.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_14.setText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_8.addWidget(self.lineEdit_14, 5, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 510, 161, 41))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"background-color: rgb(194, 194, 194);\n"
"    font: 12pt \"宋体\";\n"
"color:rgb(85, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(129, 129, 129);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.label_6.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(10, 240, 261, 16))
        self.label_7.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_7.setObjectName("label_7")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 248, 171))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_50 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_50.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_50.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_50.setObjectName("label_50")
        self.gridLayout_2.addWidget(self.label_50, 2, 2, 1, 1)
        self.radioButton_6 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_6.setObjectName("radioButton_6")
        self.gridLayout_2.addWidget(self.radioButton_6, 6, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_9.setIndent(20)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_2.addWidget(self.radioButton_5, 6, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_3.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_4.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_10.setIndent(20)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_8.setIndent(20)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_11.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_11.setIndent(10)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 2)
        self.label_51 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_51.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_51.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_51.setObjectName("label_51")
        self.gridLayout_2.addWidget(self.label_51, 3, 2, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_49.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label_49.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_49.setObjectName("label_49")
        self.gridLayout_2.addWidget(self.label_49, 0, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 510, 181, 51))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"background-color: rgb(194, 194, 194);\n"
"    font: 12pt \"宋体\";\n"
"color:rgb(85, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(232, 232, 232);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(129, 129, 129);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(20, 570, 261, 16))
        self.label_12.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 11pt \"宋体\";")
        self.label_12.setObjectName("label_12")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_4)
        self.textBrowser.setGeometry(QtCore.QRect(20, 590, 256, 211))
        self.textBrowser.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayoutWidget_9 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_9.setGeometry(QtCore.QRect(20, 270, 261, 119))
        self.gridLayoutWidget_9.setObjectName("gridLayoutWidget_9")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_9)
        self.label_13.setMinimumSize(QtCore.QSize(100, 0))
        self.label_13.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_13.setIndent(10)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 2, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.gridLayoutWidget_9)
        self.label_41.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_41.setObjectName("label_41")
        self.gridLayout_9.addWidget(self.label_41, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_2.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_9.addWidget(self.lineEdit_2, 2, 1, 1, 1)
        self.radioButton_16 = QtWidgets.QRadioButton(self.gridLayoutWidget_9)
        self.radioButton_16.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_16.setChecked(True)
        self.radioButton_16.setObjectName("radioButton_16")
        self.gridLayout_9.addWidget(self.radioButton_16, 0, 0, 1, 3)
        self.label_43 = QtWidgets.QLabel(self.gridLayoutWidget_9)
        self.label_43.setMaximumSize(QtCore.QSize(180, 16777215))
        self.label_43.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_43.setObjectName("label_43")
        self.gridLayout_9.addWidget(self.label_43, 1, 0, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_21.setMaximumSize(QtCore.QSize(40, 16777215))
        self.lineEdit_21.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_9.addWidget(self.lineEdit_21, 1, 1, 1, 1)
        self.label_52 = QtWidgets.QLabel(self.gridLayoutWidget_9)
        self.label_52.setMinimumSize(QtCore.QSize(100, 0))
        self.label_52.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_52.setIndent(10)
        self.label_52.setObjectName("label_52")
        self.gridLayout_9.addWidget(self.label_52, 3, 0, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_20.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_20.setMaximumSize(QtCore.QSize(50, 16777215))
        self.lineEdit_20.setStyleSheet("background-color: transparent;\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.lineEdit_20.setText("")
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_9.addWidget(self.lineEdit_20, 3, 1, 1, 1)
        self.radioButton_7 = QtWidgets.QRadioButton(self.tab_4)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 400, 258, 21))
        self.radioButton_7.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_7.setObjectName("radioButton_7")
        self.gridLayoutWidget_10 = QtWidgets.QWidget(self.tab_4)
        self.gridLayoutWidget_10.setGeometry(QtCore.QRect(20, 420, 261, 80))
        self.gridLayoutWidget_10.setObjectName("gridLayoutWidget_10")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.gridLayoutWidget_10)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.radioButton_8 = QtWidgets.QRadioButton(self.gridLayoutWidget_10)
        self.radioButton_8.setMinimumSize(QtCore.QSize(100, 0))
        self.radioButton_8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.radioButton_8.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_8.setObjectName("radioButton_8")
        self.gridLayout_11.addWidget(self.radioButton_8, 0, 0, 1, 1)
        self.radioButton_9 = QtWidgets.QRadioButton(self.gridLayoutWidget_10)
        self.radioButton_9.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.radioButton_9.setObjectName("radioButton_9")
        self.gridLayout_11.addWidget(self.radioButton_9, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_10)
        self.label_14.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_14.setStyleSheet("color:rgb(85, 0, 0);\n"
"font: 10pt \"宋体\";")
        self.label_14.setObjectName("label_14")
        self.gridLayout_11.addWidget(self.label_14, 1, 0, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.gridLayoutWidget_10)
        self.comboBox_4.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 10pt \"宋体\";\n"
"border: none;\n"
"border-bottom: 1px solid lightgray;")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout_11.addWidget(self.comboBox_4, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(290, 0, 1071, 851))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_3)
        MainWindow.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.radioButton_5)
        MainWindow.setTabOrder(self.radioButton_5, self.radioButton_6)
        MainWindow.setTabOrder(self.radioButton_6, self.radioButton_16)
        MainWindow.setTabOrder(self.radioButton_16, self.lineEdit_21)
        MainWindow.setTabOrder(self.lineEdit_21, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.radioButton_7)
        MainWindow.setTabOrder(self.radioButton_7, self.radioButton_8)
        MainWindow.setTabOrder(self.radioButton_8, self.radioButton_9)
        MainWindow.setTabOrder(self.radioButton_9, self.comboBox_4)
        MainWindow.setTabOrder(self.comboBox_4, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.textBrowser_4)
        MainWindow.setTabOrder(self.textBrowser_4, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        MainWindow.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        MainWindow.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        MainWindow.setTabOrder(self.lineEdit_8, self.radioButton)
        MainWindow.setTabOrder(self.radioButton, self.radioButton_2)
        MainWindow.setTabOrder(self.radioButton_2, self.radioButton_4)
        MainWindow.setTabOrder(self.radioButton_4, self.radioButton_3)
        MainWindow.setTabOrder(self.radioButton_3, self.textBrowser_3)
        MainWindow.setTabOrder(self.textBrowser_3, self.lineEdit_9)
        MainWindow.setTabOrder(self.lineEdit_9, self.lineEdit_12)
        MainWindow.setTabOrder(self.lineEdit_12, self.lineEdit_10)
        MainWindow.setTabOrder(self.lineEdit_10, self.lineEdit_11)
        MainWindow.setTabOrder(self.lineEdit_11, self.lineEdit_13)
        MainWindow.setTabOrder(self.lineEdit_13, self.lineEdit_14)
        MainWindow.setTabOrder(self.lineEdit_14, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.radioButton_14)
        MainWindow.setTabOrder(self.radioButton_14, self.lineEdit_15)
        MainWindow.setTabOrder(self.lineEdit_15, self.comboBox_3)
        MainWindow.setTabOrder(self.comboBox_3, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.lineEdit_18)
        MainWindow.setTabOrder(self.lineEdit_18, self.lineEdit_16)
        MainWindow.setTabOrder(self.lineEdit_16, self.lineEdit_17)
        MainWindow.setTabOrder(self.lineEdit_17, self.textBrowser_2)
        MainWindow.setTabOrder(self.textBrowser_2, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.comboBox_2)
        MainWindow.setTabOrder(self.comboBox_2, self.radioButton_13)
        MainWindow.setTabOrder(self.radioButton_13, self.textBrowser)
        MainWindow.setTabOrder(self.textBrowser, self.radioButton_10)
        MainWindow.setTabOrder(self.radioButton_10, self.radioButton_11)
        MainWindow.setTabOrder(self.radioButton_11, self.comboBox_5)
        MainWindow.setTabOrder(self.comboBox_5, self.lineEdit_22)
        MainWindow.setTabOrder(self.lineEdit_22, self.radioButton_17)
        MainWindow.setTabOrder(self.radioButton_17, self.radioButton_12)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "  ------地块信息导入--------"))
        self.pushButton.setText(_translate("MainWindow", "导入现实地块（kml文件）"))
        self.label_2.setText(_translate("MainWindow", "--------颜色选择---------"))
        self.label_3.setText(_translate("MainWindow", "地块边界线"))
        self.comboBox.setItemText(0, _translate("MainWindow", "green"))
        self.comboBox.setItemText(1, _translate("MainWindow", "red"))
        self.comboBox.setItemText(2, _translate("MainWindow", "orange"))
        self.comboBox.setItemText(3, _translate("MainWindow", "yellow"))
        self.comboBox.setItemText(4, _translate("MainWindow", "blue"))
        self.comboBox.setItemText(5, _translate("MainWindow", "purple"))
        self.comboBox.setItemText(6, _translate("MainWindow", "gray"))
        self.comboBox.setItemText(7, _translate("MainWindow", "white"))
        self.comboBox.setItemText(8, _translate("MainWindow", "black"))
        self.label_5.setText(_translate("MainWindow", "车辆边界线"))
        self.label_4.setText(_translate("MainWindow", "车辆路线"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "blue"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "green"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "red"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "orange"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "yellow"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "purple"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "gray"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "white"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "black"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "red"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "green"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "orange"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "yellow"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "blue"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "purple"))
        self.comboBox_3.setItemText(6, _translate("MainWindow", "gray"))
        self.comboBox_3.setItemText(7, _translate("MainWindow", "white"))
        self.comboBox_3.setItemText(8, _translate("MainWindow", "black"))
        self.label_15.setText(_translate("MainWindow", "--------使用说明---------"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:11pt; font-weight:600;\">华中农业大学-工学院B103</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "地块导入"))
        self.label_16.setText(_translate("MainWindow", "----------车辆信息----------"))
        self.label_26.setText(_translate("MainWindow", "转弯半径"))
        self.label_27.setText(_translate("MainWindow", "工作幅宽"))
        self.radioButton_13.setText(_translate("MainWindow", "牵引式"))
        self.label_29.setText(_translate("MainWindow", "车辆行走方式"))
        self.radioButton_14.setText(_translate("MainWindow", "自走式"))
        self.label_25.setText(_translate("MainWindow", "车辆幅宽"))
        self.label_46.setText(_translate("MainWindow", "M（米）"))
        self.label_47.setText(_translate("MainWindow", "M（米）"))
        self.label_48.setText(_translate("MainWindow", "M（米）"))
        self.pushButton_4.setText(_translate("MainWindow", "路径求解"))
        self.label_30.setText(_translate("MainWindow", "----------结果展示----------"))
        self.radioButton_12.setText(_translate("MainWindow", "是否预留转弯空间"))
        self.label_24.setText(_translate("MainWindow", "--------求解参数设定---------"))
        self.radioButton_10.setText(_translate("MainWindow", "最短路线"))
        self.radioButton_11.setText(_translate("MainWindow", "最小重漏"))
        self.label_23.setText(_translate("MainWindow", " 选择算法"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "经验算法"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "贪婪算法"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "google OR-Tools"))
        self.label_45.setText(_translate("MainWindow", "°（度）"))
        self.radioButton_17.setText(_translate("MainWindow", "自动选择最优作业方向"))
        self.label_44.setText(_translate("MainWindow", "手动作业方向"))
        self.label_28.setText(_translate("MainWindow", "偏置次数"))
        self.label_31.setText(_translate("MainWindow", "初始行"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "播种"))
        self.label_32.setText(_translate("MainWindow", "机具速度"))
        self.label_39.setText(_translate("MainWindow", "M/S"))
        self.label_37.setText(_translate("MainWindow", "M（米）"))
        self.label_19.setText(_translate("MainWindow", "安全距离"))
        self.label_18.setText(_translate("MainWindow", "工作幅宽"))
        self.label_17.setText(_translate("MainWindow", "机具数量"))
        self.label_36.setText(_translate("MainWindow", "M（米）"))
        self.label_20.setText(_translate("MainWindow", "--------求解参数设定---------"))
        self.radioButton.setText(_translate("MainWindow", "经验算法"))
        self.radioButton_2.setText(_translate("MainWindow", "贪婪算法"))
        self.radioButton_4.setText(_translate("MainWindow", "其它算法"))
        self.radioButton_3.setText(_translate("MainWindow", "OR-Tools"))
        self.label_42.setText(_translate("MainWindow", "算法选择："))
        self.label_21.setText(_translate("MainWindow", "---------无人机参数----------"))
        self.label_22.setText(_translate("MainWindow", "----------结果展示----------"))
        self.label_35.setText(_translate("MainWindow", "总能量"))
        self.label_33.setText(_translate("MainWindow", "起航点"))
        self.label_40.setText(_translate("MainWindow", "Kw"))
        self.label_38.setText(_translate("MainWindow", "单次航行所需能量"))
        self.label_34.setText(_translate("MainWindow", "补给点"))
        self.pushButton_3.setText(_translate("MainWindow", "路径求解"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "无人机"))
        self.label_6.setText(_translate("MainWindow", "----------车辆信息----------"))
        self.label_7.setText(_translate("MainWindow", "--------求解参数设定---------"))
        self.label_50.setText(_translate("MainWindow", "M（米）"))
        self.radioButton_6.setText(_translate("MainWindow", "牵引式"))
        self.label_9.setText(_translate("MainWindow", "车辆幅宽"))
        self.lineEdit.setText(_translate("MainWindow", "4"))
        self.radioButton_5.setText(_translate("MainWindow", "自走式"))
        self.lineEdit_4.setText(_translate("MainWindow", "2"))
        self.label_10.setText(_translate("MainWindow", "转弯半径"))
        self.label_8.setText(_translate("MainWindow", "工作幅宽"))
        self.label_11.setText(_translate("MainWindow", "车辆行走方式选择："))
        self.label_51.setText(_translate("MainWindow", "M（米）"))
        self.label_49.setText(_translate("MainWindow", "M（米）"))
        self.pushButton_2.setText(_translate("MainWindow", "路径求解"))
        self.label_12.setText(_translate("MainWindow", "----------结果展示----------"))
        self.label_13.setText(_translate("MainWindow", "偏置次数"))
        self.label_41.setText(_translate("MainWindow", "°（度）"))
        self.lineEdit_2.setText(_translate("MainWindow", "2"))
        self.radioButton_16.setText(_translate("MainWindow", "自动选择最优作业方向"))
        self.label_43.setText(_translate("MainWindow", "手动作业方向"))
        self.label_52.setText(_translate("MainWindow", "初始位置"))
        self.radioButton_7.setText(_translate("MainWindow", "是否预留转弯空间"))
        self.radioButton_8.setText(_translate("MainWindow", "最短路线"))
        self.radioButton_9.setText(_translate("MainWindow", "最小重漏"))
        self.label_14.setText(_translate("MainWindow", " 选择算法"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "经验算法"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "贪婪算法"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "google OR-Tools"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "收获"))
