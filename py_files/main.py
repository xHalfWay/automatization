import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from menu import Ui_Window_SmartHome
from livingroom import Ui_Window_Living_room
from kitchen import Ui_Window_Kitchen
from garage import Ui_MainWindow_garage
from bedroom import Ui_MainWindow_bedroom
from bathroom import Ui_MainWindow_bathroom

app = QtWidgets.QApplication(sys.argv)

Window_SmartHome = QtWidgets.QMainWindow()
ui = Ui_Window_SmartHome()
ui.setupUi(Window_SmartHome)
Window_SmartHome.show()

# button
def openKitchenWindow():
    global Window_Kitchen
    Window_Kitchen = QtWidgets.QMainWindow()
    ui = Ui_Window_Kitchen()
    ui.setupUi(Window_Kitchen)
    Window_SmartHome.close()
    Window_Kitchen.show()

    def returnToMain():
        Window_Kitchen.close()
        Window_SmartHome.show()

    ui.pushButton_back_to_menu.clicked.connect(returnToMain)

ui.pushButton_kitchen.clicked.connect(openKitchenWindow)

def openLivingRoom():
    global Window_Living_room
    Window_Living_room = QtWidgets.QMainWindow()
    ui = Ui_Window_Living_room()
    ui.setupUi(Window_Living_room)
    Window_SmartHome.close()
    Window_Living_room.show()

    def returnToMain():
        Window_Living_room.close()
        Window_SmartHome.show()

    ui.pushButton_back_to_menu.clicked.connect(returnToMain)

ui.pushButton_living_room.clicked.connect(openLivingRoom)

def openGarage():
    global MainWindow_garage
    MainWindow_garage = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_garage()
    ui.setupUi(MainWindow_garage)
    Window_SmartHome.close()
    MainWindow_garage.show()

    def returnToMain():
        MainWindow_garage.close()
        Window_SmartHome.show()

    ui.pushButton_back_to_menu.clicked.connect(returnToMain)

ui.pushButton_garage.clicked.connect(openGarage)

def openBedroom():
    global MainWindow_bedroom
    MainWindow_bedroom = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_bedroom()
    ui.setupUi(MainWindow_bedroom)
    Window_SmartHome.close()
    MainWindow_bedroom.show()

    def returnToMain():
        MainWindow_bedroom.close()
        Window_SmartHome.show()

    ui.pushButton_back_to_menu.clicked.connect(returnToMain)

ui.pushButton_bedroom.clicked.connect(openBedroom)

def openBathroom():
    global MainWindow_bathroom
    MainWindow_bathroom = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_bathroom()
    ui.setupUi(MainWindow_bathroom)
    Window_SmartHome.close()
    MainWindow_bathroom.show()

    def returnToMain():
        MainWindow_bathroom.close()
        Window_SmartHome.show()

    ui.pushButton_back_to_menu.clicked.connect(returnToMain)

ui.pushButton_bathroom.clicked.connect(openBathroom)

def closeMenu():
    Window_SmartHome.close()

ui.pushButton_exit_programm.clicked.connect(closeMenu)

sys.exit(app.exec())