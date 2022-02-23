# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_02upgrade.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.pushButton_sendTest = QPushButton(Form)
        self.pushButton_sendTest.setObjectName(u"pushButton_sendTest")
        self.pushButton_sendTest.setGeometry(QRect(440, 140, 75, 24))

        self.retranslateUi(Form)
        self.pushButton_sendTest.clicked.connect(Form.test_sendData)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_sendTest.setText(QCoreApplication.translate("Form", u"\u53d1\u9001\u6d4b\u8bd5", None))
    # retranslateUi

