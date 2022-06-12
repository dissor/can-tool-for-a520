# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.style_sheet = QWidget(MainWindow)
        self.style_sheet.setObjectName(u"style_sheet")
        self.style_sheet.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.style_sheet)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.bkgd_app = QFrame(self.style_sheet)
        self.bkgd_app.setObjectName(u"bkgd_app")
        self.bkgd_app.setFrameShape(QFrame.NoFrame)
        self.bkgd_app.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.bkgd_app)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.bkgd_menu = QFrame(self.bkgd_app)
        self.bkgd_menu.setObjectName(u"bkgd_menu")
        self.bkgd_menu.setMinimumSize(QSize(60, 0))
        self.bkgd_menu.setMaximumSize(QSize(60, 16777215))
        self.bkgd_menu.setFrameShape(QFrame.NoFrame)
        self.bkgd_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.bkgd_menu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.bkgd_menu)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(0, 50))
        self.logo.setMaximumSize(QSize(16777215, 50))
        self.logo.setStyleSheet(u"image: url(:/images/images/images/128.png);")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.logo)

        self.menu = QFrame(self.bkgd_menu)
        self.menu.setObjectName(u"menu")
        self.menu.setFrameShape(QFrame.NoFrame)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_toggle = QFrame(self.menu)
        self.menu_toggle.setObjectName(u"menu_toggle")
        self.menu_toggle.setMinimumSize(QSize(0, 0))
        self.menu_toggle.setMaximumSize(QSize(16777215, 45))
        self.menu_toggle.setFrameShape(QFrame.NoFrame)
        self.menu_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.menu_toggle)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.menu_toggle)
        self.btn_toggle.setObjectName(u"btn_toggle")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setMinimumSize(QSize(0, 45))
        self.btn_toggle.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_toggle.setMouseTracking(True)
        self.btn_toggle.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.btn_toggle)


        self.verticalLayout_3.addWidget(self.menu_toggle)

        self.menu_top = QFrame(self.menu)
        self.menu_top.setObjectName(u"menu_top")
        self.menu_top.setEnabled(True)
        self.menu_top.setMaximumSize(QSize(16777215, 16777215))
        self.menu_top.setCursor(QCursor(Qt.ArrowCursor))
        self.menu_top.setFrameShape(QFrame.NoFrame)
        self.menu_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.menu_top)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_test = QPushButton(self.menu_top)
        self.btn_test.setObjectName(u"btn_test")
        sizePolicy.setHeightForWidth(self.btn_test.sizePolicy().hasHeightForWidth())
        self.btn_test.setSizePolicy(sizePolicy)
        self.btn_test.setMinimumSize(QSize(0, 45))
        self.btn_test.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_test.setMouseTracking(True)
        self.btn_test.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.btn_test)

        self.btn_upgrade = QPushButton(self.menu_top)
        self.btn_upgrade.setObjectName(u"btn_upgrade")
        sizePolicy.setHeightForWidth(self.btn_upgrade.sizePolicy().hasHeightForWidth())
        self.btn_upgrade.setSizePolicy(sizePolicy)
        self.btn_upgrade.setMinimumSize(QSize(0, 45))
        self.btn_upgrade.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upgrade.setMouseTracking(True)
        self.btn_upgrade.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.btn_upgrade)

        self.btn_number = QPushButton(self.menu_top)
        self.btn_number.setObjectName(u"btn_number")
        sizePolicy.setHeightForWidth(self.btn_number.sizePolicy().hasHeightForWidth())
        self.btn_number.setSizePolicy(sizePolicy)
        self.btn_number.setMinimumSize(QSize(0, 45))
        self.btn_number.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_number.setMouseTracking(True)

        self.verticalLayout_5.addWidget(self.btn_number)

        self.btn_card = QPushButton(self.menu_top)
        self.btn_card.setObjectName(u"btn_card")
        sizePolicy.setHeightForWidth(self.btn_card.sizePolicy().hasHeightForWidth())
        self.btn_card.setSizePolicy(sizePolicy)
        self.btn_card.setMinimumSize(QSize(0, 45))
        self.btn_card.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_card.setMouseTracking(True)

        self.verticalLayout_5.addWidget(self.btn_card)

        self.btn_secret = QPushButton(self.menu_top)
        self.btn_secret.setObjectName(u"btn_secret")
        sizePolicy.setHeightForWidth(self.btn_secret.sizePolicy().hasHeightForWidth())
        self.btn_secret.setSizePolicy(sizePolicy)
        self.btn_secret.setMinimumSize(QSize(0, 45))
        self.btn_secret.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_secret.setMouseTracking(True)

        self.verticalLayout_5.addWidget(self.btn_secret)


        self.verticalLayout_3.addWidget(self.menu_top, 0, Qt.AlignTop)

        self.menu_botton = QFrame(self.menu)
        self.menu_botton.setObjectName(u"menu_botton")
        self.menu_botton.setMaximumSize(QSize(16777215, 16777215))
        self.menu_botton.setFrameShape(QFrame.NoFrame)
        self.menu_botton.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.menu_botton)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_setting = QPushButton(self.menu_botton)
        self.btn_setting.setObjectName(u"btn_setting")
        sizePolicy.setHeightForWidth(self.btn_setting.sizePolicy().hasHeightForWidth())
        self.btn_setting.setSizePolicy(sizePolicy)
        self.btn_setting.setMinimumSize(QSize(0, 45))
        self.btn_setting.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_8.addWidget(self.btn_setting, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.menu_botton, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.menu)


        self.horizontalLayout.addWidget(self.bkgd_menu)

        self.bkgd_extra = QFrame(self.bkgd_app)
        self.bkgd_extra.setObjectName(u"bkgd_extra")
        self.bkgd_extra.setMaximumSize(QSize(0, 16777215))
        self.bkgd_extra.setFrameShape(QFrame.NoFrame)
        self.bkgd_extra.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bkgd_extra)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.bkgd_extra)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_9.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.bkgd_extra)

        self.bkgd_content = QFrame(self.bkgd_app)
        self.bkgd_content.setObjectName(u"bkgd_content")
        self.bkgd_content.setStyleSheet(u"")
        self.bkgd_content.setFrameShape(QFrame.NoFrame)
        self.bkgd_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bkgd_content)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content_top = QFrame(self.bkgd_content)
        self.content_top.setObjectName(u"content_top")
        self.content_top.setMinimumSize(QSize(0, 50))
        self.content_top.setMaximumSize(QSize(16777215, 50))
        self.content_top.setFrameShape(QFrame.NoFrame)
        self.content_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.content_top)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.box_left = QFrame(self.content_top)
        self.box_left.setObjectName(u"box_left")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.box_left.sizePolicy().hasHeightForWidth())
        self.box_left.setSizePolicy(sizePolicy1)
        self.box_left.setFrameShape(QFrame.NoFrame)
        self.box_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.box_left)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.title_info = QLabel(self.box_left)
        self.title_info.setObjectName(u"title_info")
        self.title_info.setMaximumSize(QSize(16777215, 45))

        self.horizontalLayout_3.addWidget(self.title_info)


        self.horizontalLayout_2.addWidget(self.box_left)

        self.box_right = QFrame(self.content_top)
        self.box_right.setObjectName(u"box_right")
        self.box_right.setMinimumSize(QSize(0, 28))
        self.box_right.setFrameShape(QFrame.NoFrame)
        self.box_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.box_right)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 10, 0)
        self.btn_top_setting = QPushButton(self.box_right)
        self.btn_top_setting.setObjectName(u"btn_top_setting")
        self.btn_top_setting.setMinimumSize(QSize(28, 28))
        self.btn_top_setting.setMaximumSize(QSize(28, 28))
        self.btn_top_setting.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_setting.setMouseTracking(True)
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_top_setting.setIcon(icon)
        self.btn_top_setting.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_top_setting)

        self.btn_min = QPushButton(self.box_right)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(28, 28))
        self.btn_min.setMaximumSize(QSize(28, 28))
        self.btn_min.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_min.setMouseTracking(True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_min.setIcon(icon1)
        self.btn_min.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.box_right)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(28, 28))
        self.btn_max.setMaximumSize(QSize(28, 27))
        self.btn_max.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_max.setMouseTracking(True)
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_max.setIcon(icon2)
        self.btn_max.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.box_right)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setMouseTracking(True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)
        self.btn_close.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_close)


        self.horizontalLayout_2.addWidget(self.box_right, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.content_top)

        self.content_bottom = QFrame(self.bkgd_content)
        self.content_bottom.setObjectName(u"content_bottom")
        self.content_bottom.setFrameShape(QFrame.StyledPanel)
        self.content_bottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.content_bottom)


        self.horizontalLayout.addWidget(self.bkgd_content)


        self.verticalLayout.addWidget(self.bkgd_app)

        MainWindow.setCentralWidget(self.style_sheet)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5", None))
        self.btn_upgrade.setText(QCoreApplication.translate("MainWindow", u"\u5347\u7ea7", None))
        self.btn_number.setText(QCoreApplication.translate("MainWindow", u"\u5199\u53f7", None))
        self.btn_card.setText(QCoreApplication.translate("MainWindow", u"\u5237\u5361", None))
        self.btn_secret.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u94a5", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.title_info.setText(QCoreApplication.translate("MainWindow", u"\u90ed\u5efa\u6587\u7684\u6d4b\u8bd5\u5de5\u5177", None))
        self.btn_top_setting.setText("")
        self.btn_min.setText("")
        self.btn_max.setText("")
        self.btn_close.setText("")
    # retranslateUi

