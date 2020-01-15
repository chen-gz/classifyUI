from PySide2.QtCore import Qt, QTime, QDateTime, QFileInfo, QThread, SIGNAL
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtGui import QPixmap, QPainter
from PySide2.QtCharts import QtCharts
from read_imu import imu
import csv

from main_window import Ui_MainWindow
import logging
import os
from classify import classify


class classifyBackground(QThread):
    def __init__(self, path, names):
        QThread.__init__(self)
        self.path = path
        self.names = names
        self.classifier = classify()

    def run(self):
        self.classifier.getAllClass(self.path, self.names)


# class loadImageBackground(QThread):
#     def __init__(self):
#         QThread.__init__(self)
#
#     def run(self):
#         return


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.msg = QMessageBox()

        self.imgQuantity, self.imgIndex = 0, 0
        self.imgSet, self.images = {}, []
        self.names, self.filePath = [], ''
        self.classifyResultSet, self.classifyResult = {}, []

        self.uiImageSize = 5
        self.imgLabels = [self.ui.image1, self.ui.image2,
                          self.ui.image3, self.ui.image4, self.ui.image5]

        self.classifier = classify()
        self.imu = imu()

    def showClassifyChart(self):
        # whole chart
        self.classifyImage()
        chart = QtCharts.QChart()
        series = QtCharts.QLineSeries()
        # add data
        for i in range(self.imgQuantity):
            series.append(i, int(self.classifyResultSet[self.names[i]]))
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        self.ui.chartView.setChart(chart)
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
                self.images[i].scaled(w, h, Qt.KeepAspectRatio))
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
            self.images = []

        # TODO: preload function should be move (other place). Maybe use new thread.
        self.preload()

    def done(self):
        self.ui.statusLabel.setText("Done! Result save in path + classify.csv")

    def analysis(self):
        # TODO: judgement folder size
        if self.imgQuantity >= 500:
            self.msg.setText(
                "this folder have {} images. Maybe too many pictures. "
                "Make sure the quantity of image is under 500".format(
                    self.imgQuantity))
            self.msg.show()
            return
        if QFileInfo.exists(self.filePath + '/classify.csv'):
            self.msg.setText('have file named classify.csv. it will be loaded')
            self.msg.show()
            with open(self.filePath + '/classify.csv') as csvFile:
                csv_reader = csv.reader(csvFile, delimiter=',')
                for row in csv_reader:
                    self.classifyResultSet[row[1]] = bool(row[2])
            self.showClassifyChart()
        else:
            self.msg.setText('csv file not found, classify begin')
            self.msg.show()
            # self.classifier.getAllClass(self.filePath, self.names)
            self.ui.analysisButton.setEnabled(False)
            self.classifyThread = classifyBackground(self.path, self.names)
            self.connect(self.classifyThread, SIGNAL('finished()'), self.done)
            self.classifyThread.start()

    def classifyDone(self):
        self.msg.setText('classification finished, show the result press analysis again')
        self.ui.analysisButton.setEnabled(True)
        self.msg.show()

    def getImuPath(self):
        fileName = QFileDialog.getOpenFileName(self, 'imu data', '', '*.hex')
        self.imu.setpath(fileName[0])

    def ImuDataAnalysis(self):
        self.imu.processImuData()
        # Acc
        chartAcc, seriesAcc = [], []
        chartViewAcc = [self.ui.chartViewAcc1, self.ui.chartViewAcc2, self.ui.chartViewAcc3]
        for i in range(3):
            chartAcc.append(QtCharts.QChart())
            seriesAcc.append(QtCharts.QLineSeries())
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
            axisY.setTitleText('acc ' + str(i + 1))
            chartAcc[i].addAxis(axisY, Qt.AlignLeft)
            seriesAcc[i].attachAxis(axisY)
            chartViewAcc[i].setChart(chartAcc[i])
            chartViewAcc[i].setRenderHint(QPainter.Antialiasing)
        # end of ACC
        # gyro
        chartGyro, seriesGyro = [], []
        chartViewGyro = [self.ui.chartViewGyro1, self.ui.chartViewGyro2, self.ui.chartViewGyro3]
        for i in range(3):
            chartGyro.append(QtCharts.QChart())
            seriesGyro.append(QtCharts.QLineSeries())
        # # add data
        # timestamp = QTime()
        # dateTime = QDateTime()
        for i in range(len(self.imu.gyro)):
            timestamp.setHMS(self.imu.timestamp[i][0], self.imu.timestamp[i][1], self.imu.timestamp[i][2])
            dateTime.setTime(timestamp)
            for j in range(3):
                seriesGyro[j].append(dateTime.toMSecsSinceEpoch(), self.imu.gyro[i][j])
        for i in range(3):
            chartGyro[i].legend().hide()
            chartGyro[i].addSeries(seriesGyro[i])
            # X axis setting
            axisX = QtCharts.QDateTimeAxis()
            axisX.setTickCount(10)
            axisX.setFormat("HH:mm:ss")
            axisX.setTitleText("Time")
            chartGyro[i].addAxis(axisX, Qt.AlignBottom)
            seriesGyro[i].attachAxis(axisX)
            # Y axis setting
            axisY = QtCharts.QValueAxis()
            axisY.setTickCount(1)
            axisY.setLabelFormat('%i')
            axisY.setTitleText('gyro ' + str(i + 1))
            chartGyro[i].addAxis(axisY, Qt.AlignLeft)
            seriesGyro[i].attachAxis(axisY)
            chartViewGyro[i].setChart(chartGyro[i])
            chartViewGyro[i].setRenderHint(QPainter.Antialiasing)
        # end of gyro
        # Mag
        chartMag, seriesMag = [], []
        chartViewMag = [self.ui.chartViewMag1, self.ui.chartViewMag2, self.ui.chartViewMag3]
        for i in range(3):
            chartMag.append(QtCharts.QChart())
            seriesMag.append(QtCharts.QLineSeries())
        # # add data
        # timestamp = QTime()
        # dateTime = QDateTime()
        for i in range(len(self.imu.mag)):
            timestamp.setHMS(self.imu.timestamp[i][0], self.imu.timestamp[i][1], self.imu.timestamp[i][2])
            dateTime.setTime(timestamp)
            for j in range(3):
                seriesMag[j].append(dateTime.toMSecsSinceEpoch(), self.imu.mag[i][j])
        for i in range(3):
            chartMag[i].legend().hide()
            chartMag[i].addSeries(seriesMag[i])
            # X axis setting
            axisX = QtCharts.QDateTimeAxis()
            axisX.setTickCount(10)
            axisX.setFormat("HH:mm:ss")
            axisX.setTitleText("Time")
            chartMag[i].addAxis(axisX, Qt.AlignBottom)
            seriesMag[i].attachAxis(axisX)
            # Y axis setting
            axisY = QtCharts.QValueAxis()
            axisY.setTickCount(1)
            axisY.setLabelFormat('%i')
            axisY.setTitleText('Mag ' + str(i + 1))
            chartMag[i].addAxis(axisY, Qt.AlignLeft)
            seriesMag[i].attachAxis(axisY)
            chartViewMag[i].setChart(chartMag[i])
            chartViewMag[i].setRenderHint(QPainter.Antialiasing)
        # end of Mag


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode='w',
                        format='%(asctime)s - %(levelname)s: %(message)s')
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
