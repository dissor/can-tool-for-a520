# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
        Form.resize(640, 480)
        self.pushButton_devOpen = QPushButton(Form)
        self.pushButton_devOpen.setObjectName(u"pushButton_devOpen")
        self.pushButton_devOpen.setGeometry(QRect(40, 190, 75, 24))
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
        self.comboBox_bandRate.setGeometry(QRect(130, 150, 69, 22))
        self.comboBox_bandRate.setEditable(False)
        self.label_bandRate = QLabel(Form)
        self.label_bandRate.setObjectName(u"label_bandRate")
        self.label_bandRate.setGeometry(QRect(60, 150, 53, 16))
        self.pushButton_devClose = QPushButton(Form)
        self.pushButton_devClose.setObjectName(u"pushButton_devClose")
        self.pushButton_devClose.setGeometry(QRect(140, 190, 75, 24))
        self.pushButton_sendTest = QPushButton(Form)
        self.pushButton_sendTest.setObjectName(u"pushButton_sendTest")
        self.pushButton_sendTest.setGeometry(QRect(440, 140, 75, 24))

        self.retranslateUi(Form)
        self.comboBox_bandRate.textActivated.connect(Form.modify_dwBtr)
        self.pushButton_devOpen.clicked.connect(Form.devOpen)
        self.pushButton_devClose.clicked.connect(Form.devClose)
        self.pushButton_sendTest.clicked.connect(Form.test_sendData)

        self.comboBox_bandRate.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_devOpen.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
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
        self.label_bandRate.setText(QCoreApplication.translate("Form", u"\u6ce2\u7279\u7387", None))
        self.pushButton_devClose.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
        self.pushButton_sendTest.setText(QCoreApplication.translate("Form", u"\u53d1\u9001\u6d4b\u8bd5", None))
    # retranslateUi

