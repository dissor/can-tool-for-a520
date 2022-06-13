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

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.btn_top_setting.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # # SET CUSTOM THEME
        # # ///////////////////////////////////////////////////////////////
        # useCustomTheme = False
        # themeFile = "themes\light.qss"

        # # SET THEME AND HACKS
        # if useCustomTheme:
        #     # LOAD AND APPLY STYLE
        #     UIFunctions.theme(self, themeFile, True)

        #     # SET HACKS
        #     AppFunctions.setThemeHack(self)

    #     # SET HOME PAGE AND SELECT MENU
    #     # ///////////////////////////////////////////////////////////////
    #     widgets.stackedWidget.setCurrentWidget(widgets.home)
    #     widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))


    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_card":
            pass

        # SHOW WIDGETS PAGE
        if btnName == "btn_test":
            pass

        # SHOW NEW PAGE
        if btnName == "btn_upgrade":
            widgets.stackedWidget.setCurrentWidget(widgets.page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_number":
            pass

        if btnName == "btn_secret":
            pass

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # # RESIZE EVENTS
    # # ///////////////////////////////////////////////////////////////
    # def resizeEvent(self, event):
    #     # Update Size Grips
    #     UIFunctions.resize_grips(self)

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
