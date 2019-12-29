from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import Qt, QTime, QDateTime
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtGui import QIcon, QPixmap, QPainter, QColor
from PySide2.QtCharts import QtCharts
from read_imu import imu

from main_window import Ui_MainWindow
import logging
import os
from classify import classify


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.msg = QMessageBox()

        self.imgQuantity, self.imgIndex = 0, 0
        self.imgSet = {}

        self.uiImageSize = 5
        self.imgLabels = [self.ui.image1, self.ui.image2,
                          self.ui.image3, self.ui.image4, self.ui.image5]

        self.classifier = classify()
        self.imu = imu()

    def showClassifyChart(self):
        # whole chart
        self.classifyImage()
        self.chart = QtCharts.QChart()
        self.series = QtCharts.QLineSeries()
        # add data
        for i in range(self.imgQuantity):
            self.series.append(i, int(self.classifyResultSet[self.names[i]]))
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        # TODO: X and Y axis setting
        self.chart.createDefaultAxes()
        self.ui.chartView.setChart(self.chart)
        self.ui.chartView.setRenderHint(QPainter.Antialiasing)

    def preload(self):
        self.imgSet = {}
        for name in self.names:
            self.imgSet[name] = QPixmap(self.filePath + '/' + name)

    def readImages(self):
        self.images = []
        for i in range(self.imgIndex, min(self.imgQuantity, self.imgIndex + 5)):
            self.images.append(self.imgSet[self.names[i]])
            if self.names[i] not in self.classifyResultSet:
                result = self.classifier.getClass(self.filePath, self.names[i])
                self.classifyResultSet[self.names[i]] = result

    def classifyImage(self):
        for item in self.names:
            if item not in self.classifyResultSet:
                result = self.classifier.getClass(self.filePath, item)
                self.classifyResultSet[item] = result

    def showImages(self):
        self.readImages()
        for i in range(len(self.images)):
            w, h = self.imgLabels[i].width(), self.imgLabels[i].height()
            self.imgLabels[i].setPixmap(
                self.images[i].scaled(w, h, QtCore.Qt.KeepAspectRatio))
        logging.info("move image to image label (show image success)")
        # clear useless table
        if len(self.images) < self.uiImageSize:
            for i in range(len(self.images), self.uiImageSize):
                self.imgLabels[i].clear()
            logging.info("clear unused image label success")

        # local chart
        chartLocal = QtCharts.QChart()
        seriesLocal = QtCharts.QLineSeries()
        # add data
        for i in range(self.imgIndex, min(self.imgQuantity, self.imgIndex + 5)):
            seriesLocal.append(i, self.classifyResultSet[self.names[i]])
        chartLocal.legend().hide()
        chartLocal.addSeries(seriesLocal)
        # TODO: X and Y axis setting
        chartLocal.createDefaultAxes()
        self.ui.chartView2.setChart(chartLocal)
        self.ui.chartView2.setRenderHint(QPainter.Antialiasing)

    def getImagesName(self):
        self.names = os.listdir(self.filePath)
        namesDuplicate = self.names.copy()
        for item in namesDuplicate:
            if not item.lower().endswith(".png") \
                    and not item.lower().endswith(".jpg"):
                self.names.remove(item)
        self.names.sort()
        self.imgQuantity = len(self.names)
        logging.info("get image name and quantity success")
        if self.imgQuantity == 0:
            logging.error("image quantity is zero")
        else:
            self.imgIndex = 0

    def updateUI(self):
        self.readImages()
        self.showImages()

    def addIndex(self, cnt):
        self.imgIndex += cnt * self.uiImageSize
        if self.imgIndex > self.imgQuantity:
            self.imgIndex = self.imgQuantity - (self.imgQuantity % self.uiImageSize)
        if self.imgIndex < 0:
            self.imgIndex = 0
        if self.imgQuantity == 0:
            self.imgIndex = -1

    def goNext(self):
        self.addIndex(1)
        self.showImages()

    def goBefore(self):
        self.addIndex(-1)
        self.showImages()

    def goFarNext(self):
        self.addIndex(10)
        self.showImages()

    def goFarBefore(self):
        self.addIndex(-10)
        self.showImages()

    def goHome(self):
        self.addIndex(-99999)
        self.showImages()

    def goEnd(self):
        self.addIndex(99999)
        self.showImages()

    # def openFoldButton(self):
    def getPath(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Open Directory')
        logging.info('open fold Directory' + fileName)
        self.filePath = fileName
        self.ui.statusbar.showMessage("path" + self.filePath)
        self.getImagesName()

        if self.imgQuantity == 0:
            self.msg.setText("No image in selected folder")
            self.msg.show()
            self.ui.showImageButton.setEnabled(False)
            return
        else:
            self.ui.showImageButton.setEnabled(True)
            self.ui.analysisButton.setEnabled(True)
            # TODO: clear all variable
            self.classifyResult = []
            self.classifyResultSet = {}

        # TODO: preload function should be move (other place). Maybe use new thread.
        self.preload()

    def analysis(self):
        # TODO: judgement folder size
        self.showClassifyChart()

    def getImuPath(self):
        fileName = QFileDialog.getOpenFileName(self, 'imu data', '', '*.hex')
        self.imu.setpath(fileName[0])

    def ImuDataAnalysis(self):
        self.imu.processImuData()
        chartAcc, seriesAcc = [], []
        chartView = [self.ui.chartViewAcc1,self.ui.chartViewAcc2,self.ui.chartViewAcc3]
        for i in range(3):
            chartAcc.append(QtCharts.QChart())
            seriesAcc.append(QtCharts.QLineSeries())
        # seriesAcc[0].setColor(QColor(255, 0, 0))
        # seriesAcc[1].setColor(QColor(0, 255, 0))
        # seriesAcc[2].setColor(QColor(0, 0, 255))
        # add data
        timestamp = QTime()
        dateTime = QDateTime()
        for i in range(len(self.imu.acc)):
            timestamp.setHMS(self.imu.timestamp[i][0], self.imu.timestamp[i][1], self.imu.timestamp[i][2])
            dateTime.setTime(timestamp)
            for j in range(3):
                seriesAcc[j].append(dateTime.toMSecsSinceEpoch(), self.imu.acc[i][j])
        for i in range(3):
            chartAcc[i].legend().hide()
            chartAcc[i].addSeries(seriesAcc[i])
            # X axis setting
            axisX = QtCharts.QDateTimeAxis()
            axisX.setTickCount(10)
            axisX.setFormat("HH:mm:ss")
            axisX.setTitleText("Time")
            chartAcc[i].addAxis(axisX, Qt.AlignBottom)
            seriesAcc[i].attachAxis(axisX)
            # Y axis setting
            axisY = QtCharts.QValueAxis()
            axisY.setTickCount(1)
            axisY.setLabelFormat('%i')
            axisY.setTitleText('acc ' + str(i+1))
            chartAcc[i].addAxis(axisY,Qt.AlignLeft)
            seriesAcc[i].attachAxis(axisY)
            chartView[i].setChart(chartAcc[i])
            chartView[i].setRenderHint(QPainter.Antialiasing)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode='w',
                        format='%(asctime)s - %(levelname)s: %(message)s')
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
