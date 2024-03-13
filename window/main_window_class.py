# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(499, 468)
        self.action_path = QAction(MainWindow)
        self.action_path.setObjectName(u"action_path")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.push_button_download = QPushButton(self.centralwidget)
        self.push_button_download.setObjectName(u"push_button_download")

        self.gridLayout.addWidget(self.push_button_download, 3, 0, 1, 1)

        self.label_image = QLabel(self.centralwidget)
        self.label_image.setObjectName(u"label_image")

        self.gridLayout.addWidget(self.label_image, 0, 0, 1, 3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)

        self.line_edit_url = QLineEdit(self.centralwidget)
        self.line_edit_url.setObjectName(u"line_edit_url")

        self.gridLayout.addWidget(self.line_edit_url, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 499, 22))
        self.menusettings = QMenu(self.menubar)
        self.menusettings.setObjectName(u"menusettings")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menusettings.menuAction())
        self.menusettings.addAction(self.action_path)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Downloader", None))
        self.action_path.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.push_button_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_image.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Insert video url her", None))
        self.menusettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

