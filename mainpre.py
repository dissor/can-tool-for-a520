# ///////////////////////////////////////////////////////////////
#
# BY: guojianwenjonas@foxmail.com
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "怎么隐藏这个标题栏，将 ENABLE_CUSTOM_TITLE_BAR 改为 True"
        description = "描述：这是郭建文的工具箱"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.title_info.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.btn_toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

    #     # QTableWidget PARAMETERS
    #     # ///////////////////////////////////////////////////////////////
    #     widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_card.clicked.connect(self.buttonClick)
        widgets.btn_test.clicked.connect(self.buttonClick)
        widgets.btn_upgrade.clicked.connect(self.buttonClick)
        widgets.btn_number.clicked.connect(self.buttonClick)
        widgets.btn_secret.clicked.connect(self.buttonClick)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.btn_setting.clicked.connect(openCloseLeftBox)
        widgets.btn_extral_close.clicked.connect(openCloseLeftBox)

        # EXTRA LEFT SETTINGS
        widgets.btn_set_open.clicked.connect(self.buttonClick)
        widgets.btn_set_close.clicked.connect(self.buttonClick)

        # TEST PAGE

        widgets.btn_test_start.clicked.connect(self.buttonClick)
        widgets.btn_test_stop.clicked.connect(self.buttonClick)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.btn_top_setting.clicked.connect(openCloseRightBox)

        # UPDATED SETTINGS
        widgets.btn_update_open.clicked.connect(self.buttonClick)
        widgets.btn_update_start.clicked.connect(self.buttonClick)
        widgets.btn_update_stop.clicked.connect(self.buttonClick)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.page_test)
        widgets.btn_test.setStyleSheet(UIFunctions.selectMenu(widgets.btn_test.styleSheet()))


    # BUTTONS CLICK
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_card":
            widgets.stackedWidget.setCurrentWidget(widgets.page_card) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # SHOW WIDGETS PAGE
        if btnName == "btn_test":
            widgets.stackedWidget.setCurrentWidget(widgets.page_test) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        # SHOW NEW PAGE
        if btnName == "btn_upgrade":
            widgets.stackedWidget.setCurrentWidget(widgets.page_update) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_number":
            widgets.stackedWidget.setCurrentWidget(widgets.page_number) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_secret":
            widgets.stackedWidget.setCurrentWidget(widgets.page_secret) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_set_open":
            CANFunctions.open(self)
        if btnName == "btn_set_close":
            CANFunctions.close(self)

        if btnName == "btn_test_start":
            CANFunctions.buttonClick(self, btnName)
        if btnName == "btn_test_stop":
            CANFunctions.buttonClick(self, btnName)

        if btnName == "btn_update_open":
            CANFunctions.openUpdateFile(self)
        if btnName == "btn_update_start":
            CANFunctions.startUpdate(self)
        if btnName == "btn_update_stop":
            CANFunctions.stopUpdate(self)

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
