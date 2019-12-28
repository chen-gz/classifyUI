from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtGui import QIcon, QPixmap, QPainter
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
        self.ui.setupUi(self)
        self.msg = QMessageBox()

        self.imgQuantity, self.imgIndex = 0, 0
        self.imgSet = {}

        self.uiImageSize = 5
        self.imgLabels = [self.ui.image1, self.ui.image2,
                          self.ui.image3, self.ui.image4, self.ui.image5]

        # self.classifier = classify()
        # self.classifyResult = []

    # def showClassifyChartAll(self):
    #     self.classifyImageAll()
    #     self.chart = QtCharts.QChart()
    #     self.series = QtCharts.QLineSeries()
    #     # add data
    #     for i in range(self.imgQuantity):
    #         self.series.append(i, int(self.classifyResult[i]))
    #     self.chart.legend().hide()
    #     self.chart.addSeries(self.series)
    #     # TODO: X and Y axis setting
    #     self.chart.createDefaultAxes()
    #     self.ui.chartView.setChart(self.chart)
    #     self.ui.chartView.setRenderHint(QPainter.Antialiasing)

    def preload(self):
        self.imgSet = {}
        for name in self.names:
            self.imgSet[name] = QPixmap(self.filePath + '/' + name)

    def readImages(self):
        self.images = []
        for i in range(self.imgIndex, min(self.imgQuantity, self.imgIndex + 5)):
            self.images.append(self.imgSet[self.names[i]])

    # def classifyImage(self):
    #     self.classifyResult = []
    #     for item in self.names[self.imgIndex]:
    #         self.classifyResult.append(
    #             self.classifier.getClass(self.filePath, item))

    # def classifyImageAll(self):
    #     self.classifyResult = []
    #     for item1 in self.names:
    #         for item in item1:
    #             self.classifyResult.append(
    #                 self.classifier.getClass(self.filePath, item))

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
        self.getImagesName()
        if self.imgQuantity == 0:
            self.msg.setText("No image in selected folder")
            self.msg.show()
            self.ui.showImageButton.setEnabled(False)
            return
        else:
            self.ui.showImageButton.setEnabled(True)

        # TODO: preload function should be move (other place). Maybe use new thread.
        self.preload()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='log.log', filemode='w',
                        format='%(asctime)s - %(levelname)s: %(message)s')
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
