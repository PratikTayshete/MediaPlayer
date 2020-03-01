# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mediaPlayerUI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.mainVideoFrame = QFrame(self.centralwidget)
        self.mainVideoFrame.setObjectName(u"mainVideoFrame")
        self.mainVideoFrame.setMaximumSize(QSize(16777215, 16777215))
        self.mainVideoFrame.setFrameShape(QFrame.StyledPanel)
        self.mainVideoFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.mainVideoFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.playerButtonsFrame = QFrame(self.mainVideoFrame)
        self.playerButtonsFrame.setObjectName(u"playerButtonsFrame")
        self.playerButtonsFrame.setMaximumSize(QSize(16777215, 45))
        self.playerButtonsFrame.setFrameShape(QFrame.StyledPanel)
        self.playerButtonsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.playerButtonsFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.playButton = QPushButton(self.playerButtonsFrame)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.playButton, 0, 0, 1, 1)

        self.pauseButton = QPushButton(self.playerButtonsFrame)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.pauseButton, 0, 1, 1, 1)

        self.stopButton = QPushButton(self.playerButtonsFrame)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_3.addWidget(self.stopButton, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.playerButtonsFrame, 1, 0, 1, 1)

        self.playerSliderFrame = QFrame(self.mainVideoFrame)
        self.playerSliderFrame.setObjectName(u"playerSliderFrame")
        self.playerSliderFrame.setMaximumSize(QSize(16777215, 35))
        self.playerSliderFrame.setFrameShape(QFrame.StyledPanel)
        self.playerSliderFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.playerSliderFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSlider = QSlider(self.playerSliderFrame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.playerSliderFrame, 2, 0, 1, 1)

        self.playerFrame = QFrame(self.mainVideoFrame)
        self.playerFrame.setObjectName(u"playerFrame")
        self.playerFrame.setMaximumSize(QSize(16777215, 500))
        self.playerFrame.setFrameShape(QFrame.StyledPanel)
        self.playerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.playerFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.playerLayout = QGridLayout()
        self.playerLayout.setObjectName(u"playerLayout")

        self.gridLayout_6.addLayout(self.playerLayout, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.playerFrame, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.mainVideoFrame, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 25))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Media Player v0.1", None))
        self.playButton.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pauseButton.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

