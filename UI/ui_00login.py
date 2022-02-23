# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_00login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 481)
        self.comboBox_bandRate = QComboBox(Form)
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.addItem("")
        self.comboBox_bandRate.setObjectName(u"comboBox_bandRate")
        self.comboBox_bandRate.setGeometry(QRect(290, 190, 69, 22))
        self.comboBox_bandRate.setEditable(False)
        self.pushButton_devClose = QPushButton(Form)
        self.pushButton_devClose.setObjectName(u"pushButton_devClose")
        self.pushButton_devClose.setGeometry(QRect(300, 230, 75, 24))
        self.label_bandRate = QLabel(Form)
        self.label_bandRate.setObjectName(u"label_bandRate")
        self.label_bandRate.setGeometry(QRect(220, 190, 53, 16))
        self.pushButton_devOpen = QPushButton(Form)
        self.pushButton_devOpen.setObjectName(u"pushButton_devOpen")
        self.pushButton_devOpen.setGeometry(QRect(200, 230, 75, 24))
        self.comboBox_bandRate_devCOM = QComboBox(Form)
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.addItem("")
        self.comboBox_bandRate_devCOM.setObjectName(u"comboBox_bandRate_devCOM")
        self.comboBox_bandRate_devCOM.setGeometry(QRect(290, 150, 69, 22))
        self.comboBox_bandRate_devCOM.setEditable(False)
        self.label_bandRate_2 = QLabel(Form)
        self.label_bandRate_2.setObjectName(u"label_bandRate_2")
        self.label_bandRate_2.setGeometry(QRect(220, 150, 53, 16))

        self.retranslateUi(Form)
        self.comboBox_bandRate_devCOM.currentTextChanged.connect(Form.select_dev_comm)
        self.comboBox_bandRate.currentTextChanged.connect(Form.modify_dwBtr)
        self.pushButton_devOpen.clicked.connect(Form.devOpen)
        self.pushButton_devClose.clicked.connect(Form.devClose)

        self.comboBox_bandRate.setCurrentIndex(7)
        self.comboBox_bandRate_devCOM.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.comboBox_bandRate.setItemText(0, QCoreApplication.translate("Form", u"5Kbps", None))
        self.comboBox_bandRate.setItemText(1, QCoreApplication.translate("Form", u"10Kbps", None))
        self.comboBox_bandRate.setItemText(2, QCoreApplication.translate("Form", u"20Kbps", None))
        self.comboBox_bandRate.setItemText(3, QCoreApplication.translate("Form", u"50Kbps", None))
        self.comboBox_bandRate.setItemText(4, QCoreApplication.translate("Form", u"100Kbps", None))
        self.comboBox_bandRate.setItemText(5, QCoreApplication.translate("Form", u"125Kbps", None))
        self.comboBox_bandRate.setItemText(6, QCoreApplication.translate("Form", u"250Kbps", None))
        self.comboBox_bandRate.setItemText(7, QCoreApplication.translate("Form", u"500Kbps", None))
        self.comboBox_bandRate.setItemText(8, QCoreApplication.translate("Form", u"800Kbps", None))
        self.comboBox_bandRate.setItemText(9, QCoreApplication.translate("Form", u"1000Kbps", None))

        self.comboBox_bandRate.setCurrentText(QCoreApplication.translate("Form", u"500Kbps", None))
        self.pushButton_devClose.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.label_bandRate.setText(QCoreApplication.translate("Form", u"\u6ce2\u7279\u7387", None))
        self.pushButton_devOpen.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.comboBox_bandRate_devCOM.setItemText(0, QCoreApplication.translate("Form", u"USB1", None))
        self.comboBox_bandRate_devCOM.setItemText(1, QCoreApplication.translate("Form", u"USB2", None))
        self.comboBox_bandRate_devCOM.setItemText(2, QCoreApplication.translate("Form", u"USB3", None))
        self.comboBox_bandRate_devCOM.setItemText(3, QCoreApplication.translate("Form", u"USB4", None))
        self.comboBox_bandRate_devCOM.setItemText(4, QCoreApplication.translate("Form", u"USB5", None))
        self.comboBox_bandRate_devCOM.setItemText(5, QCoreApplication.translate("Form", u"USB6", None))
        self.comboBox_bandRate_devCOM.setItemText(6, QCoreApplication.translate("Form", u"USB7", None))
        self.comboBox_bandRate_devCOM.setItemText(7, QCoreApplication.translate("Form", u"USB8", None))
        self.comboBox_bandRate_devCOM.setItemText(8, QCoreApplication.translate("Form", u"USB9", None))
        self.comboBox_bandRate_devCOM.setItemText(9, QCoreApplication.translate("Form", u"USB10", None))
        self.comboBox_bandRate_devCOM.setItemText(10, QCoreApplication.translate("Form", u"USB11", None))
        self.comboBox_bandRate_devCOM.setItemText(11, QCoreApplication.translate("Form", u"USB12", None))
        self.comboBox_bandRate_devCOM.setItemText(12, QCoreApplication.translate("Form", u"USB13", None))
        self.comboBox_bandRate_devCOM.setItemText(13, QCoreApplication.translate("Form", u"USB14", None))
        self.comboBox_bandRate_devCOM.setItemText(14, QCoreApplication.translate("Form", u"USB15", None))
        self.comboBox_bandRate_devCOM.setItemText(15, QCoreApplication.translate("Form", u"USB16", None))

        self.comboBox_bandRate_devCOM.setCurrentText(QCoreApplication.translate("Form", u"USB1", None))
        self.label_bandRate_2.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3", None))
    # retranslateUi

