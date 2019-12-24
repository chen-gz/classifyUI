from PySide2 import QtCore,QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtCharts import QtCharts
# import matplotlib.pyplot as plt

from main_window import Ui_MainWindow
import logging
import os
from classify import classify


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.imgGroupNumber = 0
        self.imgQuantity = 0
        self.preloadQuantity = 100
        self.ui.setupUi(self)
        self.groupSize, self.imgIndex = 5, 0
        self.imgLabels = [self.ui.image1, self.ui.image2,
                          self.ui.image3, self.ui.image4, self.ui.image5]
        self.classifier = classify()
        self.imageSet = {}
        self.classifyResult = []
        # self.chart = QtCharts.QtCharts()
        self.showClassifyChartAll()

    def showClassifyChartAll(self):
        # self.classifyImageAll()
        # x = list(range(1, self.imgQuantity + 1))
        # y = []
        # TODO  QChart View
        self.ui.chartView = QtCharts.QChartView()
        self.ui.chartView.setGeometry(QtCore.QRect(260, 40, 941, 311))
        self.ui.chartView.setObjectName("chartView")
        self.chart = QtCharts.QChart()
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
        self.series = QtCharts.QLineSeries()
        self.series.append(1, 1)
        self.series.append(2, 3)
        self.series.append(3, 4)
        self.chart.addSeries(self.series)
        self.ui.chartView.setChart(self.chart)
        self.ui.chartView.show()
        # self.axisX = QtCharts.QValueAxis()
        # self.axisX.setTickCount(1)
        # self.axisX.setLabelFormat("%d")
        # self.chart.addAxis(self.axisX, Qt.AlignBottom)
        # self.series.attachAxis(self.axisX)
        # # Setting Y-axis
        # self.axisY = QtCharts.QValueAxis()
        # self.axisY.setTickCount(1)
        # self.axisY.setLabelFormat("%d")
        # # self.axis_y.setTitleText("Magnitude")
        # self.chart.addAxis(self.axisY, Qt.AlignLeft)
        # self.series.attachAxis(self.axisY)
        #
        # for i in range(len(self.classifyAll)):
        #     self.series.append(i, int(self.classifyAll[i]))
        #
        # self.chart.addSeries(self.series)

        # self.ui.chartView = QtCharts.QChartView(self.chart)
        # self.ui.chartView.show()

        # self.chart.axisX()
        # plt.plot(x, y)
        # plt.savefig("classifyResult.png")
        # w, h = self.ui.classifyLable.width(), self.ui.classifyLable.height()
        # self.ui.classifyLable.setPixmap(
        #     QPixmap("classifyResult.png").scaled(w, h, QtCore.Qt.KeepAspectRatio))

    def preload(self):
        self.imageSet = {}
        for i in range(self.imgGroupNumber):
            for name in self.names[i]:
                self.imageSet[name] = QPixmap(self.filePath + '/' + name)

    def readImages(self):
        self.images = []
        for item in self.names[self.imgIndex]:
            self.images.append(self.imageSet[item])
            # if item in self.imageSet:
            #     self.images.append(self.imageSet[item])
            # else:
            #     self.images.append(QPixmap(self.filePath + '/' + item))

    def classifyImage(self):
        self.classifyResult = []
        for item in self.names[self.imgIndex]:
            self.classifyResult.append(
                self.classifier.getClass(self.filePath, item))

    def classifyImageAll(self):
        self.classifyAll = []
        for item1 in self.names:
            for item in item1:
                self.classifyAll.append(
                    self.classifier.getClass(self.filePath, item))

    def showImage(self):
        for i in range(len(self.images)):
            w, h = self.imgLabels[i].width(), self.imgLabels[i].height()
            self.imgLabels[i].setPixmap(
                self.images[i].scaled(w, h, QtCore.Qt.KeepAspectRatio))
        # self.showClassifyChartAll()

    def getPath(self):
        fileName = QFileDialog.getExistingDirectory(self, 'Open Directory')
        logging.info('open fold Directory' + fileName)
        self.filePath = fileName
        self.getImagesName()
        self.preload()
        self.showClassifyChartAll()

    def getImagesName(self):
        names = os.listdir(self.filePath)
        namesDuplicate = names.copy()
        for item in namesDuplicate:
            if not item.lower().endswith(".png") \
                    and not item.lower().endswith(".jpg"):
                names.remove(item)
        names.sort()
        self.imgQuantity = len(names)
        self.names = list([])
        for i in range(0, len(names), self.groupSize):
            tmp = []
            for j in range(self.groupSize):
                if i + j < len(names):
                    tmp.append(names[i + j])
            self.names.append(tmp)
        self.imgGroupNumber = len(self.names)

    def updateUI(self):
        for item in self.imgLabels:
            item.clear()
        if self.imgGroupNumber == 0:
            logging.error("no image")
            return None
        self.readImages()
        self.showImage()

    def addIndex(self, cnt):
        self.imgIndex += cnt
        if self.imgIndex >= self.imgGroupNumber:
            self.imgIndex = self.imgGroupNumber - 1
        if self.imgIndex <= 0:
            self.imgIndex = 0

    def goNext(self):
        self.addIndex(1)
        self.updateUI()

    def goBefore(self):
        self.addIndex(-1)
        self.updateUI()

    def goFarNext(self):
        self.addIndex(10)
        self.updateUI()

    def goFarBefore(self):
        self.addIndex(-10)
        self.updateUI()

    def goHome(self):
        self.addIndex(-99999)
        self.updateUI()

    def goEnd(self):
        self.addIndex(99999)
        self.updateUI()

    def openFoldButton(self):
        self.getPath()
        self.getImagesName()
        self.imgIndex = 0
        self.updateUI()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode='w',
                        format='%(asctime)s - %(levelname)s: %(message)s')
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
