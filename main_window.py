# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui',
# licensing of 'main_window.ui' applies.
#
# Created: Sat Dec 28 20:22:14 2019
#      by: pyside2-uic  running on PySide2 5.14.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets, QtCharts


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1178, 888)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 350, 941, 281))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image1.setAutoFillBackground(True)
        self.image1.setObjectName("image1")
        self.horizontalLayout.addWidget(self.image1)
        self.image2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image2.setAutoFillBackground(True)
        self.image2.setObjectName("image2")
        self.horizontalLayout.addWidget(self.image2)
        self.image3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image3.setAutoFillBackground(True)
        self.image3.setObjectName("image3")
        self.horizontalLayout.addWidget(self.image3)
        self.image4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image4.setAutoFillBackground(True)
        self.image4.setObjectName("image4")
        self.horizontalLayout.addWidget(self.image4)
        self.image5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.image5.setAutoFillBackground(True)
        self.image5.setObjectName("image5")
        self.horizontalLayout.addWidget(self.image5)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(620, 640, 340, 70))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonGoHome = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoHome.setFont(font)
        self.buttonGoHome.setObjectName("buttonGoHome")
        self.horizontalLayout_2.addWidget(self.buttonGoHome)
        self.buttonGoBefore = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(36)
        self.buttonGoBefore.setFont(font)
        self.buttonGoBefore.setObjectName("buttonGoBefore")
        self.horizontalLayout_2.addWidget(self.buttonGoBefore)
        self.buttonGoNext = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
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
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(580, 730, 421, 61))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.getPathButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.getPathButton.sizePolicy().hasHeightForWidth())
        self.getPathButton.setSizePolicy(sizePolicy)
        self.getPathButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.getPathButton.setFont(font)
        self.getPathButton.setObjectName("getPathButton")
        self.horizontalLayout_3.addWidget(self.getPathButton)
        self.showImageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.showImageButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.showImageButton.sizePolicy().hasHeightForWidth())
        self.showImageButton.setSizePolicy(sizePolicy)
        self.showImageButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.showImageButton.setFont(font)
        self.showImageButton.setObjectName("showImageButton")
        self.horizontalLayout_3.addWidget(self.showImageButton)
        self.analysisButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.analysisButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analysisButton.sizePolicy().hasHeightForWidth())
        self.analysisButton.setSizePolicy(sizePolicy)
        self.analysisButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.analysisButton.setFont(font)
        self.analysisButton.setObjectName("analysisButton")
        self.horizontalLayout_3.addWidget(self.analysisButton)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 10, 821, 311))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        # self.chartView = QtWidgets.QGraphicsView(self.tab)
        self.chartView = QtCharts.QtCharts.QChartView(self.tab)
        self.chartView.setGeometry(QtCore.QRect(0, 0, 821, 281))
        self.chartView.setObjectName("chartView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        # self.chartView2 = QtWidgets.QGraphicsView(self.tab_2)
        self.chartView2 = QtCharts.QtCharts.QChartView(self.tab_2)
        self.chartView2.setGeometry(QtCore.QRect(0, 0, 821, 281))
        self.chartView2.setObjectName("chartView2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 811, 271))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        # self.chartViewAcc1 = QtWidgets.QGraphicsView(self.tab_6)
        self.chartViewAcc1 = QtCharts.QtCharts.QChartView(self.tab_6)
        self.chartViewAcc1.setGeometry(QtCore.QRect(0, 0, 821, 251))
        self.chartViewAcc1.setObjectName("chartViewAcc1")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        # self.chartViewAcc2 = QtWidgets.QGraphicsView(self.tab_8)
        self.chartViewAcc2 = QtCharts.QtCharts.QChartView(self.tab_8)
        self.chartViewAcc2.setGeometry(QtCore.QRect(0, 0, 811, 241))
        self.chartViewAcc2.setObjectName("chartViewAcc2")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        # self.chartViewAcc3 = QtWidgets.QGraphicsView(self.tab_7)
        self.chartViewAcc3 = QtCharts.QtCharts.QChartView(self.tab_7)
        self.chartViewAcc3.setGeometry(QtCore.QRect(0, 0, 821, 251))
        self.chartViewAcc3.setObjectName("chartViewAcc3")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.chartViewGyro = QtWidgets.QGraphicsView(self.tab_4)
        self.chartViewGyro.setGeometry(QtCore.QRect(0, 0, 821, 281))
        self.chartViewGyro.setObjectName("chartViewGyro")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.chartViewMag = QtWidgets.QGraphicsView(self.tab_5)
        self.chartViewMag.setGeometry(QtCore.QRect(0, 0, 821, 281))
        self.chartViewMag.setObjectName("chartViewMag")
        self.tabWidget.addTab(self.tab_5, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1178, 20))
        self.menubar.setObjectName("menubar")
        self.menuimu = QtWidgets.QMenu(self.menubar)
        self.menuimu.setObjectName("menuimu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.getImuPath = QtWidgets.QAction(MainWindow)
        self.getImuPath.setObjectName("getImuPath")
        self.imuDataAnalysis = QtWidgets.QAction(MainWindow)
        self.imuDataAnalysis.setObjectName("imuDataAnalysis")
        self.menuimu.addAction(self.getImuPath)
        self.menuimu.addAction(self.imuDataAnalysis)
        self.menubar.addAction(self.menuimu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QObject.connect(self.buttonGoBefore, QtCore.SIGNAL("clicked()"), MainWindow.goBefore)
        QtCore.QObject.connect(self.buttonGoNext, QtCore.SIGNAL("clicked()"), MainWindow.goNext)
        QtCore.QObject.connect(self.buttonGoEnd, QtCore.SIGNAL("clicked()"), MainWindow.goEnd)
        QtCore.QObject.connect(self.buttonGoHome, QtCore.SIGNAL("clicked()"), MainWindow.goHome)
        QtCore.QObject.connect(self.getPathButton, QtCore.SIGNAL("clicked()"), MainWindow.getPath)
        QtCore.QObject.connect(self.showImageButton, QtCore.SIGNAL("clicked()"), MainWindow.showImages)
        QtCore.QObject.connect(self.analysisButton, QtCore.SIGNAL("clicked()"), MainWindow.analysis)
        QtCore.QObject.connect(self.getImuPath, QtCore.SIGNAL("triggered()"), MainWindow.getImuPath)
        QtCore.QObject.connect(self.imuDataAnalysis, QtCore.SIGNAL("triggered()"), MainWindow.ImuDataAnalysis)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.image1.setText(QtWidgets.QApplication.translate("MainWindow", "image1", None, -1))
        self.image2.setText(QtWidgets.QApplication.translate("MainWindow", "image2", None, -1))
        self.image3.setText(QtWidgets.QApplication.translate("MainWindow", "image3", None, -1))
        self.image4.setText(QtWidgets.QApplication.translate("MainWindow", "image4", None, -1))
        self.image5.setText(QtWidgets.QApplication.translate("MainWindow", "image5", None, -1))
        self.buttonGoHome.setText(QtWidgets.QApplication.translate("MainWindow", "<<", None, -1))
        self.buttonGoBefore.setText(QtWidgets.QApplication.translate("MainWindow", "<", None, -1))
        self.buttonGoNext.setText(QtWidgets.QApplication.translate("MainWindow", ">", None, -1))
        self.buttonGoEnd.setText(QtWidgets.QApplication.translate("MainWindow", ">>", None, -1))
        self.getPathButton.setText(QtWidgets.QApplication.translate("MainWindow", "get path", None, -1))
        self.showImageButton.setText(QtWidgets.QApplication.translate("MainWindow", "Show image", None, -1))
        self.analysisButton.setText(QtWidgets.QApplication.translate("MainWindow", "Analysis", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QtWidgets.QApplication.translate("MainWindow", "Tab 1", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QtWidgets.QApplication.translate("MainWindow", "local", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6),
                                    QtWidgets.QApplication.translate("MainWindow", "Tab 1", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8),
                                    QtWidgets.QApplication.translate("MainWindow", "Page", None, -1))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7),
                                    QtWidgets.QApplication.translate("MainWindow", "Tab 2", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),
                                  QtWidgets.QApplication.translate("MainWindow", "acc", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4),
                                  QtWidgets.QApplication.translate("MainWindow", "gyro", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5),
                                  QtWidgets.QApplication.translate("MainWindow", "mag", None, -1))
        self.menuimu.setTitle(QtWidgets.QApplication.translate("MainWindow", "imu", None, -1))
        self.getImuPath.setText(QtWidgets.QApplication.translate("MainWindow", "imu path", None, -1))
        self.imuDataAnalysis.setText(QtWidgets.QApplication.translate("MainWindow", "imu data analysis", None, -1))

