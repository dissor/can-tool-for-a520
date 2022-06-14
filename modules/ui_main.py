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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 720)
        self.style_sheet = QWidget(MainWindow)
        self.style_sheet.setObjectName(u"style_sheet")
        self.style_sheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"")
        self.app_margins = QVBoxLayout(self.style_sheet)
        self.app_margins.setSpacing(0)
        self.app_margins.setObjectName(u"app_margins")
        self.app_margins.setContentsMargins(10, 10, 10, 10)
        self.bkgd_app = QFrame(self.style_sheet)
        self.bkgd_app.setObjectName(u"bkgd_app")
        self.bkgd_app.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"")
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
        self.bkgd_menu.setStyleSheet(u"background-color: rgb(33, 37, 43);")
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
        self.logo.setStyleSheet(u"")
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.logo)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 5, 42, 42))
        self.frame_2.setMinimumSize(QSize(42, 42))
        self.frame_2.setMaximumSize(QSize(42, 42))
        self.frame_2.setStyleSheet(u"image: url(:/images/images/images/512.png);")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.lb_title_left_app = QLabel(self.logo)
        self.lb_title_left_app.setObjectName(u"lb_title_left_app")
        self.lb_title_left_app.setGeometry(QRect(70, 8, 160, 20))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.lb_title_left_app.setFont(font)
        self.lb_title_left_app.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.lb_title_left_desc = QLabel(self.logo)
        self.lb_title_left_desc.setObjectName(u"lb_title_left_desc")
        self.lb_title_left_desc.setGeometry(QRect(70, 27, 160, 16))
        self.lb_title_left_desc.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.logo)

        self.menu = QFrame(self.bkgd_menu)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"QPushButton {\n"
"  background-position: center left;\n"
"  background-repeat: no-repeat;\n"
"  border-left: 22px solid red;\n"
"  text-align: left;\n"
"  padding-left: 44px;\n"
"}\n"
"\n"
"")
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
        self.btn_toggle.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);\n"
"")

        self.verticalLayout_4.addWidget(self.btn_toggle)


        self.verticalLayout_3.addWidget(self.menu_toggle)

        self.menu_top = QFrame(self.menu)
        self.menu_top.setObjectName(u"menu_top")
        self.menu_top.setEnabled(True)
        self.menu_top.setMaximumSize(QSize(16777215, 16777215))
        self.menu_top.setCursor(QCursor(Qt.ArrowCursor))
        self.menu_top.setStyleSheet(u"")
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
        self.btn_test.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-speedometer.png);")

        self.verticalLayout_5.addWidget(self.btn_test)

        self.btn_upgrade = QPushButton(self.menu_top)
        self.btn_upgrade.setObjectName(u"btn_upgrade")
        sizePolicy.setHeightForWidth(self.btn_upgrade.sizePolicy().hasHeightForWidth())
        self.btn_upgrade.setSizePolicy(sizePolicy)
        self.btn_upgrade.setMinimumSize(QSize(0, 45))
        self.btn_upgrade.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_upgrade.setMouseTracking(True)
        self.btn_upgrade.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chevron-double-up.png);")

        self.verticalLayout_5.addWidget(self.btn_upgrade)

        self.btn_number = QPushButton(self.menu_top)
        self.btn_number.setObjectName(u"btn_number")
        sizePolicy.setHeightForWidth(self.btn_number.sizePolicy().hasHeightForWidth())
        self.btn_number.setSizePolicy(sizePolicy)
        self.btn_number.setMinimumSize(QSize(0, 45))
        self.btn_number.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_number.setMouseTracking(True)
        self.btn_number.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-pencil.png);")

        self.verticalLayout_5.addWidget(self.btn_number)

        self.btn_card = QPushButton(self.menu_top)
        self.btn_card.setObjectName(u"btn_card")
        sizePolicy.setHeightForWidth(self.btn_card.sizePolicy().hasHeightForWidth())
        self.btn_card.setSizePolicy(sizePolicy)
        self.btn_card.setMinimumSize(QSize(0, 45))
        self.btn_card.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_card.setMouseTracking(True)
        self.btn_card.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-credit-card.png);")

        self.verticalLayout_5.addWidget(self.btn_card)

        self.btn_secret = QPushButton(self.menu_top)
        self.btn_secret.setObjectName(u"btn_secret")
        sizePolicy.setHeightForWidth(self.btn_secret.sizePolicy().hasHeightForWidth())
        self.btn_secret.setSizePolicy(sizePolicy)
        self.btn_secret.setMinimumSize(QSize(0, 45))
        self.btn_secret.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_secret.setMouseTracking(True)
        self.btn_secret.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-lock-locked.png);")

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
        self.btn_setting.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_settings.png);")

        self.verticalLayout_8.addWidget(self.btn_setting)


        self.verticalLayout_3.addWidget(self.menu_botton, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.menu)


        self.horizontalLayout.addWidget(self.bkgd_menu)

        self.bkgd_extra = QFrame(self.bkgd_app)
        self.bkgd_extra.setObjectName(u"bkgd_extra")
        self.bkgd_extra.setMinimumSize(QSize(0, 0))
        self.bkgd_extra.setMaximumSize(QSize(0, 16777215))
        self.bkgd_extra.setFrameShape(QFrame.NoFrame)
        self.bkgd_extra.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.bkgd_extra)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.extra_top = QFrame(self.bkgd_extra)
        self.extra_top.setObjectName(u"extra_top")
        self.extra_top.setMinimumSize(QSize(0, 50))
        self.extra_top.setMaximumSize(QSize(16777215, 50))
        self.extra_top.setFrameShape(QFrame.NoFrame)
        self.extra_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.extra_top)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.extra_top_grid = QGridLayout()
        self.extra_top_grid.setObjectName(u"extra_top_grid")
        self.extra_top_grid.setHorizontalSpacing(10)
        self.extra_top_grid.setVerticalSpacing(0)
        self.extra_top_grid.setContentsMargins(10, -1, 10, -1)
        self.btn_extral_close = QPushButton(self.extra_top)
        self.btn_extral_close.setObjectName(u"btn_extral_close")
        self.btn_extral_close.setMinimumSize(QSize(28, 28))
        self.btn_extral_close.setMaximumSize(QSize(28, 28))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_extral_close.setIcon(icon)
        self.btn_extral_close.setIconSize(QSize(20, 16))

        self.extra_top_grid.addWidget(self.btn_extral_close, 0, 2, 1, 1)

        self.lb_extra = QLabel(self.extra_top)
        self.lb_extra.setObjectName(u"lb_extra")
        self.lb_extra.setMinimumSize(QSize(150, 0))

        self.extra_top_grid.addWidget(self.lb_extra, 0, 1, 1, 1)

        self.extra_icon = QFrame(self.extra_top)
        self.extra_icon.setObjectName(u"extra_icon")
        self.extra_icon.setMinimumSize(QSize(20, 0))
        self.extra_icon.setMaximumSize(QSize(20, 20))
        self.extra_icon.setStyleSheet(u"image: url(:/icons/images/icons/icon_settings.png);")
        self.extra_icon.setFrameShape(QFrame.NoFrame)
        self.extra_icon.setFrameShadow(QFrame.Raised)

        self.extra_top_grid.addWidget(self.extra_icon, 0, 0, 1, 1)


        self.verticalLayout_9.addLayout(self.extra_top_grid)


        self.verticalLayout.addWidget(self.extra_top)

        self.extra_content = QFrame(self.bkgd_extra)
        self.extra_content.setObjectName(u"extra_content")
        self.extra_content.setFrameShape(QFrame.StyledPanel)
        self.extra_content.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.extra_content)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 120, 53, 16))
        self.cb_set_usb = QComboBox(self.extra_content)
        self.cb_set_usb.addItem("")
        self.cb_set_usb.addItem("")
        self.cb_set_usb.addItem("")
        self.cb_set_usb.addItem("")
        self.cb_set_usb.addItem("")
        self.cb_set_usb.addItem("")
        self.cb_set_usb.addItem("")
        self.cb_set_usb.addItem("")
        self.cb_set_usb.setObjectName(u"cb_set_usb")
        self.cb_set_usb.setGeometry(QRect(110, 120, 101, 21))
        self.label_5 = QLabel(self.extra_content)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 160, 53, 16))
        self.cb_set_bps = QComboBox(self.extra_content)
        self.cb_set_bps.addItem("")
        self.cb_set_bps.addItem("")
        self.cb_set_bps.addItem("")
        self.cb_set_bps.addItem("")
        self.cb_set_bps.addItem("")
        self.cb_set_bps.addItem("")
        self.cb_set_bps.addItem("")
        self.cb_set_bps.addItem("")
        self.cb_set_bps.addItem("")
        self.cb_set_bps.addItem("")
        self.cb_set_bps.setObjectName(u"cb_set_bps")
        self.cb_set_bps.setGeometry(QRect(110, 160, 101, 21))
        self.btn_set_open = QPushButton(self.extra_content)
        self.btn_set_open.setObjectName(u"btn_set_open")
        self.btn_set_open.setGeometry(QRect(40, 200, 75, 24))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-link-alt.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_set_open.setIcon(icon1)
        self.btn_set_close = QPushButton(self.extra_content)
        self.btn_set_close.setObjectName(u"btn_set_close")
        self.btn_set_close.setEnabled(False)
        self.btn_set_close.setGeometry(QRect(130, 200, 75, 24))
        self.btn_set_close.setIcon(icon)
        self.btn_set_close.setCheckable(False)
        self.btn_set_close.setAutoDefault(False)
        self.btn_set_close.setFlat(False)

        self.verticalLayout.addWidget(self.extra_content)


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
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_top_setting.setIcon(icon2)
        self.btn_top_setting.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_top_setting)

        self.btn_min = QPushButton(self.box_right)
        self.btn_min.setObjectName(u"btn_min")
        self.btn_min.setMinimumSize(QSize(28, 28))
        self.btn_min.setMaximumSize(QSize(28, 28))
        self.btn_min.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_min.setMouseTracking(True)
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_min.setIcon(icon3)
        self.btn_min.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_min)

        self.btn_max = QPushButton(self.box_right)
        self.btn_max.setObjectName(u"btn_max")
        self.btn_max.setMinimumSize(QSize(28, 28))
        self.btn_max.setMaximumSize(QSize(28, 27))
        self.btn_max.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_max.setMouseTracking(True)
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_max.setIcon(icon4)
        self.btn_max.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_max)

        self.btn_close = QPushButton(self.box_right)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(28, 28))
        self.btn_close.setMaximumSize(QSize(28, 28))
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_close.setMouseTracking(True)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(20, 20))

        self.horizontalLayout_4.addWidget(self.btn_close)


        self.horizontalLayout_2.addWidget(self.box_right, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.content_top)

        self.content_bottom = QFrame(self.bkgd_content)
        self.content_bottom.setObjectName(u"content_bottom")
        self.content_bottom.setFrameShape(QFrame.NoFrame)
        self.content_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.content_bottom)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.centent = QFrame(self.content_bottom)
        self.centent.setObjectName(u"centent")
        self.centent.setFrameShape(QFrame.NoFrame)
        self.centent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.centent)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.box_pages = QFrame(self.centent)
        self.box_pages.setObjectName(u"box_pages")
        self.box_pages.setFrameShape(QFrame.StyledPanel)
        self.box_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.box_pages)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.box_pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_test = QWidget()
        self.page_test.setObjectName(u"page_test")
        self.label_2 = QLabel(self.page_test)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 190, 81, 81))
        self.stackedWidget.addWidget(self.page_test)
        self.page_update = QWidget()
        self.page_update.setObjectName(u"page_update")
        self.label_3 = QLabel(self.page_update)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 180, 111, 61))
        self.stackedWidget.addWidget(self.page_update)
        self.page_number = QWidget()
        self.page_number.setObjectName(u"page_number")
        self.label = QLabel(self.page_number)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(330, 150, 101, 71))
        self.stackedWidget.addWidget(self.page_number)
        self.page_secret = QWidget()
        self.page_secret.setObjectName(u"page_secret")
        self.stackedWidget.addWidget(self.page_secret)
        self.page_card = QWidget()
        self.page_card.setObjectName(u"page_card")
        self.stackedWidget.addWidget(self.page_card)

        self.verticalLayout_12.addWidget(self.stackedWidget)


        self.horizontalLayout_6.addWidget(self.box_pages)

        self.box_extra_right = QFrame(self.centent)
        self.box_extra_right.setObjectName(u"box_extra_right")
        self.box_extra_right.setMaximumSize(QSize(0, 16777215))
        self.box_extra_right.setFrameShape(QFrame.StyledPanel)
        self.box_extra_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.box_extra_right)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.top = QFrame(self.box_extra_right)
        self.top.setObjectName(u"top")
        self.top.setMaximumSize(QSize(16777215, 3))
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.top)

        self.setting = QFrame(self.box_extra_right)
        self.setting.setObjectName(u"setting")
        self.setting.setFrameShape(QFrame.NoFrame)
        self.setting.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.setting)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.menus = QFrame(self.setting)
        self.menus.setObjectName(u"menus")
        self.menus.setFrameShape(QFrame.StyledPanel)
        self.menus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.menus)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_msg = QPushButton(self.menus)
        self.btn_msg.setObjectName(u"btn_msg")
        self.btn_msg.setMinimumSize(QSize(0, 45))
        self.btn_msg.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_msg.setMouseTracking(True)

        self.verticalLayout_11.addWidget(self.btn_msg)

        self.btn_print = QPushButton(self.menus)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setMouseTracking(True)

        self.verticalLayout_11.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.menus)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setMouseTracking(True)

        self.verticalLayout_11.addWidget(self.btn_logout)


        self.verticalLayout_10.addWidget(self.menus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.setting)


        self.horizontalLayout_6.addWidget(self.box_extra_right)


        self.verticalLayout_13.addWidget(self.centent)

        self.bar_bottom = QFrame(self.content_bottom)
        self.bar_bottom.setObjectName(u"bar_bottom")
        self.bar_bottom.setMinimumSize(QSize(0, 22))
        self.bar_bottom.setMaximumSize(QSize(16777215, 22))
        self.bar_bottom.setFrameShape(QFrame.NoFrame)
        self.bar_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bar_bottom)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.lb_credits = QLabel(self.bar_bottom)
        self.lb_credits.setObjectName(u"lb_credits")
        self.lb_credits.setMaximumSize(QSize(16777215, 16))

        self.horizontalLayout_5.addWidget(self.lb_credits)

        self.lb_version = QLabel(self.bar_bottom)
        self.lb_version.setObjectName(u"lb_version")
        self.lb_version.setMaximumSize(QSize(16777215, 16))
        self.lb_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.lb_version)

        self.frame_size_grip = QFrame(self.bar_bottom)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_13.addWidget(self.bar_bottom)


        self.verticalLayout_6.addWidget(self.content_bottom)


        self.horizontalLayout.addWidget(self.bkgd_content)


        self.app_margins.addWidget(self.bkgd_app)

        MainWindow.setCentralWidget(self.style_sheet)

        self.retranslateUi(MainWindow)

        self.btn_set_close.setDefault(False)
        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lb_title_left_app.setText(QCoreApplication.translate("MainWindow", u"\u90ed\u5efa\u6587\u7684\u6d4b\u8bd5\u5de5\u5177", None))
        self.lb_title_left_desc.setText(QCoreApplication.translate("MainWindow", u"\u8fd9\u662f\u8f6f\u4ef6\u7684\u63cf\u8ff0", None))
        self.btn_toggle.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.btn_test.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5", None))
        self.btn_upgrade.setText(QCoreApplication.translate("MainWindow", u"\u5347\u7ea7", None))
        self.btn_number.setText(QCoreApplication.translate("MainWindow", u"\u5199\u53f7", None))
        self.btn_card.setText(QCoreApplication.translate("MainWindow", u"\u5237\u5361", None))
        self.btn_secret.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u94a5", None))
        self.btn_setting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.btn_extral_close.setText("")
        self.lb_extra.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3", None))
        self.cb_set_usb.setItemText(0, QCoreApplication.translate("MainWindow", u"USB1", None))
        self.cb_set_usb.setItemText(1, QCoreApplication.translate("MainWindow", u"USB2", None))
        self.cb_set_usb.setItemText(2, QCoreApplication.translate("MainWindow", u"USB3", None))
        self.cb_set_usb.setItemText(3, QCoreApplication.translate("MainWindow", u"USB4", None))
        self.cb_set_usb.setItemText(4, QCoreApplication.translate("MainWindow", u"USB5", None))
        self.cb_set_usb.setItemText(5, QCoreApplication.translate("MainWindow", u"USB6", None))
        self.cb_set_usb.setItemText(6, QCoreApplication.translate("MainWindow", u"USB7", None))
        self.cb_set_usb.setItemText(7, QCoreApplication.translate("MainWindow", u"USB8", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387", None))
        self.cb_set_bps.setItemText(0, QCoreApplication.translate("MainWindow", u"5Kbps", None))
        self.cb_set_bps.setItemText(1, QCoreApplication.translate("MainWindow", u"10Kbps", None))
        self.cb_set_bps.setItemText(2, QCoreApplication.translate("MainWindow", u"20Kbps", None))
        self.cb_set_bps.setItemText(3, QCoreApplication.translate("MainWindow", u"50Kbps", None))
        self.cb_set_bps.setItemText(4, QCoreApplication.translate("MainWindow", u"100Kbps", None))
        self.cb_set_bps.setItemText(5, QCoreApplication.translate("MainWindow", u"125Kbps", None))
        self.cb_set_bps.setItemText(6, QCoreApplication.translate("MainWindow", u"250Kbps", None))
        self.cb_set_bps.setItemText(7, QCoreApplication.translate("MainWindow", u"500Kbps", None))
        self.cb_set_bps.setItemText(8, QCoreApplication.translate("MainWindow", u"800Kbps", None))
        self.cb_set_bps.setItemText(9, QCoreApplication.translate("MainWindow", u"1000Kbps", None))

        self.btn_set_open.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.btn_set_close.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.title_info.setText(QCoreApplication.translate("MainWindow", u"\u90ed\u5efa\u6587\u7684\u6d4b\u8bd5\u5de5\u5177", None))
        self.btn_top_setting.setText("")
        self.btn_min.setText("")
        self.btn_max.setText("")
        self.btn_close.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel 1", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel 2", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel 3", None))
        self.btn_msg.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lb_credits.setText(QCoreApplication.translate("MainWindow", u"By: \u90ed\u5efa\u6587", None))
        self.lb_version.setText(QCoreApplication.translate("MainWindow", u"v1.0.3", None))
    # retranslateUi

