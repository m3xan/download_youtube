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
    QMainWindow, QPushButton, QSizePolicy, QWidget)
from icon import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(443, 343)
        icon = QIcon()
        icon.addFile(u":/icon/YouTube_full-color_icon__2017_.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.action_path = QAction(MainWindow)
        self.action_path.setObjectName(u"action_path")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_image = QLabel(self.centralwidget)
        self.label_image.setObjectName(u"label_image")

        self.gridLayout.addWidget(self.label_image, 1, 0, 1, 2)

        self.line_edit_url = QLineEdit(self.centralwidget)
        self.line_edit_url.setObjectName(u"line_edit_url")

        self.gridLayout.addWidget(self.line_edit_url, 2, 0, 1, 2)

        self.push_button_download = QPushButton(self.centralwidget)
        self.push_button_download.setObjectName(u"push_button_download")

        self.gridLayout.addWidget(self.push_button_download, 3, 0, 1, 1)

        self.push_button_settings = QPushButton(self.centralwidget)
        self.push_button_settings.setObjectName(u"push_button_settings")
        self.push_button_settings.setAutoDefault(True)

        self.gridLayout.addWidget(self.push_button_settings, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Downloader", None))
        self.action_path.setText(QCoreApplication.translate("MainWindow", u"Path", None))
        self.label_image.setText("")
        self.line_edit_url.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insert video url her", None))
        self.push_button_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.push_button_settings.setText(QCoreApplication.translate("MainWindow", u"settings", None))
    # retranslateUi

