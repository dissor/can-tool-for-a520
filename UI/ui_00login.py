# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '_00login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QTabWidget, QTextBrowser,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(746, 638)
        Form.setAutoFillBackground(False)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayoutWidget_4 = QWidget(self.tab)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(140, 100, 341, 271))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_devOpen = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_devOpen.setObjectName(u"pushButton_devOpen")

        self.gridLayout_5.addWidget(self.pushButton_devOpen, 2, 0, 1, 1)

        self.label_bandRate_2 = QLabel(self.gridLayoutWidget_4)
        self.label_bandRate_2.setObjectName(u"label_bandRate_2")
        self.label_bandRate_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_bandRate_2, 0, 0, 1, 1)

        self.comboBox_bandRate_devCOM = QComboBox(self.gridLayoutWidget_4)
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
        self.comboBox_bandRate_devCOM.setEditable(False)

        self.gridLayout_5.addWidget(self.comboBox_bandRate_devCOM, 0, 1, 1, 1)

        self.pushButton_devClose = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_devClose.setObjectName(u"pushButton_devClose")

        self.gridLayout_5.addWidget(self.pushButton_devClose, 2, 1, 1, 1)

        self.comboBox_bandRate = QComboBox(self.gridLayoutWidget_4)
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
        self.comboBox_bandRate.setEditable(False)

        self.gridLayout_5.addWidget(self.comboBox_bandRate, 1, 1, 1, 1)

        self.label_bandRate = QLabel(self.gridLayoutWidget_4)
        self.label_bandRate.setObjectName(u"label_bandRate")
        self.label_bandRate.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_bandRate, 1, 0, 1, 1)

        self.cb_res = QCheckBox(self.gridLayoutWidget_4)
        self.cb_res.setObjectName(u"cb_res")

        self.gridLayout_5.addWidget(self.cb_res, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.pushButton = QPushButton(self.tab_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(360, 390, 75, 24))
        self.label_11 = QLabel(self.tab_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(80, 350, 111, 21))
        self.label_9 = QLabel(self.tab_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(80, 300, 91, 21))
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 40, 131, 21))
        self.label_4 = QLabel(self.tab_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 160, 91, 21))
        self.label_7 = QLabel(self.tab_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(80, 260, 101, 16))
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 220, 53, 16))
        self.label_6 = QLabel(self.tab_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(80, 240, 53, 16))
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 130, 53, 16))
        self.label_8 = QLabel(self.tab_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(80, 280, 81, 21))
        self.label_10 = QLabel(self.tab_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(80, 330, 91, 16))
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 17, 16))
        self.lb_sn = QLabel(self.tab_2)
        self.lb_sn.setObjectName(u"lb_sn")
        self.lb_sn.setGeometry(QRect(210, 10, 141, 21))
        self.lb_uuid = QLabel(self.tab_2)
        self.lb_uuid.setObjectName(u"lb_uuid")
        self.lb_uuid.setGeometry(QRect(240, 130, 191, 16))
        self.lb_okey = QLabel(self.tab_2)
        self.lb_okey.setObjectName(u"lb_okey")
        self.lb_okey.setGeometry(QRect(240, 160, 181, 21))
        self.lb_usrkey = QLabel(self.tab_2)
        self.lb_usrkey.setObjectName(u"lb_usrkey")
        self.lb_usrkey.setGeometry(QRect(230, 220, 211, 21))
        self.lb_usrdata = QLabel(self.tab_2)
        self.lb_usrdata.setObjectName(u"lb_usrdata")
        self.lb_usrdata.setGeometry(QRect(230, 240, 201, 21))
        self.lb_mkeya = QLabel(self.tab_2)
        self.lb_mkeya.setObjectName(u"lb_mkeya")
        self.lb_mkeya.setGeometry(QRect(230, 260, 191, 21))
        self.lb_mkeyb = QLabel(self.tab_2)
        self.lb_mkeyb.setObjectName(u"lb_mkeyb")
        self.lb_mkeyb.setGeometry(QRect(230, 280, 191, 21))
        self.lb_musrdata = QLabel(self.tab_2)
        self.lb_musrdata.setObjectName(u"lb_musrdata")
        self.lb_musrdata.setGeometry(QRect(230, 310, 231, 21))
        self.lb_muuid = QLabel(self.tab_2)
        self.lb_muuid.setObjectName(u"lb_muuid")
        self.lb_muuid.setGeometry(QRect(230, 330, 211, 16))
        self.lb_vmuuid = QLabel(self.tab_2)
        self.lb_vmuuid.setObjectName(u"lb_vmuuid")
        self.lb_vmuuid.setGeometry(QRect(230, 350, 211, 21))
        self.pushButton_4 = QPushButton(self.tab_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(460, 390, 75, 24))
        self.lb_state = QLabel(self.tab_2)
        self.lb_state.setObjectName(u"lb_state")
        self.lb_state.setGeometry(QRect(10, 60, 541, 31))
        self.lb_cardcnt = QLabel(self.tab_2)
        self.lb_cardcnt.setObjectName(u"lb_cardcnt")
        self.lb_cardcnt.setGeometry(QRect(420, 20, 151, 31))
        self.lb_temp = QLabel(self.tab_2)
        self.lb_temp.setObjectName(u"lb_temp")
        self.lb_temp.setGeometry(QRect(420, 50, 53, 16))
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lb_updatestate = QLabel(self.tab_3)
        self.lb_updatestate.setObjectName(u"lb_updatestate")
        self.lb_updatestate.setGeometry(QRect(160, 250, 181, 41))
        self.lb_progress = QLabel(self.tab_3)
        self.lb_progress.setObjectName(u"lb_progress")
        self.lb_progress.setGeometry(QRect(170, 360, 291, 141))
        self.gridLayoutWidget_3 = QWidget(self.tab_3)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(50, 270, 581, 71))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.progressBar = QProgressBar(self.gridLayoutWidget_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_4.addWidget(self.progressBar, 0, 2, 1, 1)

        self.pb_state = QPushButton(self.gridLayoutWidget_3)
        self.pb_state.setObjectName(u"pb_state")

        self.gridLayout_4.addWidget(self.pb_state, 0, 0, 1, 1)

        self.pb_state_2 = QPushButton(self.gridLayoutWidget_3)
        self.pb_state_2.setObjectName(u"pb_state_2")

        self.gridLayout_4.addWidget(self.pb_state_2, 0, 3, 1, 1)

        self.pb_selectbin = QPushButton(self.tab_3)
        self.pb_selectbin.setObjectName(u"pb_selectbin")
        self.pb_selectbin.setGeometry(QRect(60, 150, 75, 24))
        self.lb_binpath = QLabel(self.tab_3)
        self.lb_binpath.setObjectName(u"lb_binpath")
        self.lb_binpath.setGeometry(QRect(190, 150, 371, 16))
        self.lb_binpath.setMaximumSize(QSize(371, 16))
        self.lb_binsize = QLabel(self.tab_3)
        self.lb_binsize.setObjectName(u"lb_binsize")
        self.lb_binsize.setGeometry(QRect(190, 190, 171, 16))
        self.lb_binsize.setMaximumSize(QSize(171, 16))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.horizontalLayoutWidget = QWidget(self.tab_4)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(100, 50, 411, 121))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.horizontalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout.addWidget(self.label_13)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayoutWidget_2 = QWidget(self.tab_5)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(190, 180, 211, 111))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_12, 0, 0, 1, 1)

        self.comboBox = QComboBox(self.gridLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_3.addWidget(self.comboBox, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_3.addWidget(self.pushButton_5, 1, 1, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.pushButton_10 = QPushButton(self.tab_6)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(510, 130, 100, 24))
        self.pushButton_10.setMinimumSize(QSize(100, 0))
        self.textBrowser = QTextBrowser(self.tab_6)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(80, 120, 401, 171))
        self.label_17 = QLabel(self.tab_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 120, 31, 31))
        self.pushButton_9 = QPushButton(self.tab_6)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(510, 160, 100, 24))
        self.pushButton_9.setMinimumSize(QSize(100, 0))
        self.lineEdit_4 = QLineEdit(self.tab_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(80, 90, 400, 21))
        self.lineEdit_4.setMinimumSize(QSize(400, 0))
        self.label_15 = QLabel(self.tab_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 90, 48, 16))
        self.pushButton_7 = QPushButton(self.tab_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(510, 90, 75, 24))
        self.pushButton_6 = QPushButton(self.tab_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(510, 20, 71, 50))
        self.pushButton_6.setMinimumSize(QSize(0, 50))
        self.pushButton_6.setMaximumSize(QSize(16777215, 50))
        self.pushButton_8 = QPushButton(self.tab_6)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(580, 20, 75, 50))
        self.pushButton_8.setMinimumSize(QSize(0, 50))
        self.pushButton_8.setMaximumSize(QSize(16777215, 50))
        self.lineEdit_3 = QLineEdit(self.tab_6)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 50, 400, 21))
        self.lineEdit_3.setMinimumSize(QSize(400, 0))
        self.lineEdit_2 = QLineEdit(self.tab_6)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 20, 400, 21))
        self.lineEdit_2.setMinimumSize(QSize(400, 0))
        self.label_16 = QLabel(self.tab_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 50, 48, 16))
        self.label_14 = QLabel(self.tab_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 20, 46, 16))
        self.cb_p16 = QCheckBox(self.tab_6)
        self.cb_p16.setObjectName(u"cb_p16")
        self.cb_p16.setGeometry(QRect(490, 20, 21, 21))
        self.cb_a16 = QCheckBox(self.tab_6)
        self.cb_a16.setObjectName(u"cb_a16")
        self.cb_a16.setGeometry(QRect(490, 50, 21, 21))
        self.cb_k16 = QCheckBox(self.tab_6)
        self.cb_k16.setObjectName(u"cb_k16")
        self.cb_k16.setGeometry(QRect(490, 90, 21, 21))
        self.label_18 = QLabel(self.tab_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(490, 0, 53, 16))
        self.label_19 = QLabel(self.tab_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(20, 300, 48, 16))
        self.lineEdit_5 = QLineEdit(self.tab_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(80, 300, 400, 21))
        self.lineEdit_5.setMinimumSize(QSize(400, 0))
        self.pushButton_11 = QPushButton(self.tab_6)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(510, 300, 75, 24))
        self.tabWidget.addTab(self.tab_6, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.retranslateUi(Form)
        self.comboBox_bandRate.currentTextChanged.connect(Form.modify_dwBtr)
        self.pushButton_devOpen.clicked.connect(Form.devOpen)
        self.pushButton_3.clicked.connect(Form.writeNumber)
        self.pushButton_4.clicked.connect(Form.test_end)
        self.pushButton_devClose.clicked.connect(Form.devClose)
        self.pushButton.clicked.connect(Form.test_start)
        self.comboBox_bandRate_devCOM.currentTextChanged.connect(Form.select_dev_comm)
        self.cb_res.clicked.connect(Form.set_dev_res)
        self.pushButton_2.clicked.connect(Form.peika_start)
        self.pushButton_5.clicked.connect(Form.peika_stop)
        self.comboBox.currentTextChanged.connect(Form.peika_mode)
        self.pushButton_8.clicked.connect(Form.write_card_id)
        self.pushButton_6.clicked.connect(Form.read_card_id)
        self.pushButton_7.clicked.connect(Form.write_ic_id)
        self.pushButton_9.clicked.connect(Form.delete_all_uid)
        self.pb_state_2.clicked["bool"].connect(Form.update_term)
        self.pb_selectbin.clicked.connect(Form.openBinFile)
        self.pb_state.clicked.connect(Form.startUpgrade)
        self.pushButton_10.clicked.connect(Form.read_all_uid)
        self.cb_p16.clicked.connect(Form.select_picc_16)
        self.cb_a16.clicked.connect(Form.select_app_16)
        self.cb_k16.clicked.connect(Form.select_ic_16)
        self.pushButton_11.clicked.connect(Form.write_uid_single)

        self.tabWidget.setCurrentIndex(5)
        self.comboBox_bandRate_devCOM.setCurrentIndex(0)
        self.comboBox_bandRate.setCurrentIndex(7)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u6d4b\u8bd5\u5de5\u5177", None))
        self.pushButton_devOpen.setText(QCoreApplication.translate("Form", u"\u6253\u5f00", None))
        self.label_bandRate_2.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3", None))
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
        self.pushButton_devClose.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
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
        self.cb_res.setText(QCoreApplication.translate("Form", u"\u7ec8\u7aef\u7535\u963b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u5f00\u542f\u8bbe\u5907", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u6a21\u62df\u5361\uff35\uff35\uff29\uff24", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\uff2d\u5361\u7528\u6237\u6570\u636e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5361\u7247\u4fe1\u606f\u5916\u8bbe\u72b6\u6001", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u5916\u90e8\u8ba4\u8bc1\u5bc6\u94a5", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"M\u5361\u5bc6\u94a5A", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u5bc6\u94a5", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u6570\u636e", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"UUID", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"M\u5361\u5bc6\u94a5B", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\uff2d\u5361\uff35\uff35\uff29\uff24", None))
        self.label.setText(QCoreApplication.translate("Form", u"SN", None))
        self.lb_sn.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_uuid.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_okey.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_usrkey.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_usrdata.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_mkeya.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_mkeyb.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_musrdata.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_muuid.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_vmuuid.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u7ed3\u675f", None))
        self.lb_state.setText(QCoreApplication.translate("Form", u"\u7a7a", None))
        self.lb_cardcnt.setText(QCoreApplication.translate("Form", u"\u5237\u5361\u7d2f\u8ba1\uff1a0", None))
        self.lb_temp.setText(QCoreApplication.translate("Form", u"\u6e29\u5ea6\uff1a0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u6d4b\u8bd5", None))
        self.lb_updatestate.setText("")
        self.lb_progress.setText("")
        self.pb_state.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.pb_state_2.setText(QCoreApplication.translate("Form", u"\u4e2d\u6b62", None))
        self.pb_selectbin.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.lb_binpath.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u8def\u5f84", None))
        self.lb_binsize.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5927\u5c0f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u5347\u7ea7", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"SN \u53f7", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u5199\u5165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u5199\u53f7", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u914d\u5361\u6a21\u5f0f", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u5b9e\u4f53\u5361", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u6a21\u62df\u5361", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u89e3\u7ed1\u5361", None))

        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u914d\u5361", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6\u6240\u6709UID", None))
        self.textBrowser.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">NULL</p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"UID", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u6240\u6709UID", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u5199IC\u5bc6\u94a5", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"\u5199\u5165", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"\u5199\u5165", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"AppKey:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"PiccKey:", None))
        self.cb_p16.setText("")
        self.cb_a16.setText("")
        self.cb_k16.setText("")
        self.label_18.setText(QCoreApplication.translate("Form", u"16 B", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u5199UID", None))
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"\u5199\u5165", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u5bc6\u94a5", None))
    # retranslateUi

