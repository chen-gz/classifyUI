# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Mon Dec 23 20:23:53 2019
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCharts import QtCharts


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1359, 893)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(
            QtCore.QRect(260, 380, 941, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image1.setObjectName("image1")
        self.horizontalLayout.addWidget(self.image1)
        self.image2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image2.setObjectName("image2")
        self.horizontalLayout.addWidget(self.image2)
        self.image3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image3.setObjectName("image3")
        self.horizontalLayout.addWidget(self.image3)
        self.image4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image4.setObjectName("image4")
        self.horizontalLayout.addWidget(self.image4)
        self.image5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image5.setObjectName("image5")
        self.horizontalLayout.addWidget(self.image5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(820, 690, 336, 70))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonGoHome = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoHome.setFont(font)
        self.buttonGoHome.setObjectName("buttonGoHome")
        self.horizontalLayout_2.addWidget(self.buttonGoHome)
        self.buttonGoBefore = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoBefore.setFont(font)
        self.buttonGoBefore.setObjectName("buttonGoBefore")
        self.horizontalLayout_2.addWidget(self.buttonGoBefore)
        self.buttonGoNext = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoNext.setFont(font)
        self.buttonGoNext.setObjectName("buttonGoNext")
        self.horizontalLayout_2.addWidget(self.buttonGoNext)
        self.buttonGoEnd = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoEnd.setFont(font)
        self.buttonGoEnd.setObjectName("buttonGoEnd")
        self.horizontalLayout_2.addWidget(self.buttonGoEnd)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(
            QtCore.QRect(840, 780, 271, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setSizeConstraint(
            QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(
            self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(
            self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 110, 191, 191))
        self.label_2.setObjectName("label_2")
        self.classifyLable = QtWidgets.QLabel(self.centralwidget)
        self.classifyLable.setGeometry(QtCore.QRect(20, 450, 191, 141))
        self.classifyLable.setObjectName("classifyLable")
        self.chartView = QtCharts.QChartView(self.centralwidget)
        self.chartView.setGeometry(QtCore.QRect(260, 40, 941, 311))
        self.chartView.setObjectName("chartView")
        # self.chartView = QtWidgets.QGraphicsView(self.centralwidget)
        # self.chartView.setGeometry(QtCore.QRect(260, 40, 941, 311))
        # self.chartView.setObjectName("chartView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1359, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(
            "clicked()"), MainWindow.openFoldButton)
        QtCore.QObject.connect(self.buttonGoBefore, QtCore.SIGNAL(
            "clicked()"), MainWindow.goBefore)
        QtCore.QObject.connect(self.buttonGoNext, QtCore.SIGNAL(
            "clicked()"), MainWindow.goNext)
        QtCore.QObject.connect(self.buttonGoEnd, QtCore.SIGNAL(
            "clicked()"), MainWindow.goEnd)
        QtCore.QObject.connect(self.buttonGoHome, QtCore.SIGNAL(
            "clicked()"), MainWindow.goHome)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate(
            "MainWindow", "MainWindow", None, -1))
        self.image1.setText(QtWidgets.QApplication.translate(
            "MainWindow", "image1", None, -1))
        self.image2.setText(QtWidgets.QApplication.translate(
            "MainWindow", "image2", None, -1))
        self.image3.setText(QtWidgets.QApplication.translate(
            "MainWindow", "image3", None, -1))
        self.image4.setText(QtWidgets.QApplication.translate(
            "MainWindow", "image4", None, -1))
        self.image5.setText(QtWidgets.QApplication.translate(
            "MainWindow", "image5", None, -1))
        self.buttonGoHome.setText(
            QtWidgets.QApplication.translate("MainWindow", "<<", None, -1))
        self.buttonGoBefore.setText(
            QtWidgets.QApplication.translate("MainWindow", "<", None, -1))
        self.buttonGoNext.setText(
            QtWidgets.QApplication.translate("MainWindow", ">", None, -1))
        self.buttonGoEnd.setText(
            QtWidgets.QApplication.translate("MainWindow", ">>", None, -1))
        self.pushButton_2.setText(QtWidgets.QApplication.translate(
            "MainWindow", "open fold", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate(
            "MainWindow", "TextLabel", None, -1))
        self.classifyLable.setText(QtWidgets.QApplication.translate(
            "MainWindow", "TextLabel", None, -1))
