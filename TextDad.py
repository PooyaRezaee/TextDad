from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
import calender
import info
import sys
import threading
import font
import json
from datetime import datetime

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 615)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.viewport().setProperty(
            "cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.plainTextEdit.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1009, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuPut = QtWidgets.QMenu(self.menuTools)
        self.menuPut.setObjectName("menuPut")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuThem = QtWidgets.QMenu(self.menuSetting)
        self.menuThem.setObjectName("menuThem")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_on_This = QtWidgets.QAction(MainWindow)
        self.actionSave_on_This.setObjectName("actionSave_on_This")
        self.actionSave_To = QtWidgets.QAction(MainWindow)
        self.actionSave_To.setObjectName("actionSave_To")
        self.actionClose_Window = QtWidgets.QAction(MainWindow)
        self.actionClose_Window.setObjectName("actionClose_Window")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCalender = QtWidgets.QAction(MainWindow)
        self.actionCalender.setObjectName("actionCalender")
        self.actionDate = QtWidgets.QAction(MainWindow)
        self.actionDate.setObjectName("actionDate")
        self.actionTime = QtWidgets.QAction(MainWindow)
        self.actionTime.setObjectName("actionTime")
        self.actionFont = QtWidgets.QAction(MainWindow)
        self.actionFont.setObjectName("actionFont")
        self.actionLight = QtWidgets.QAction(MainWindow)
        self.actionLight.setCheckable(True)
        self.actionLight.setChecked(True)
        self.actionLight.setObjectName("actionLight")
        self.actionDark = QtWidgets.QAction(MainWindow)
        self.actionDark.setCheckable(True)
        self.actionDark.setObjectName("actionDark")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionReport_Problem = QtWidgets.QAction(MainWindow)
        self.actionReport_Problem.setObjectName("actionReport_Problem")
        self.menuSave.addAction(self.actionSave_on_This)
        self.menuSave.addAction(self.actionSave_To)
        self.menuFile.addAction(self.actionNew_Window)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_Window)
        self.menuFile.addAction(self.actionExit)
        self.menuPut.addAction(self.actionDate)
        self.menuPut.addAction(self.actionTime)
        self.menuTools.addAction(self.menuPut.menuAction())
        self.menuTools.addAction(self.actionCalender)
        self.menuThem.addAction(self.actionLight)
        self.menuThem.addAction(self.actionDark)
        self.menuSetting.addAction(self.menuThem.menuAction())
        self.menuSetting.addAction(self.actionFont)
        self.menuHelp.addAction(self.actionReport_Problem)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ========================= coding =============================
        try:
            with open("setting.json", "r") as File:
                my_dict = json.load(File)

                font = QtGui.QFont()
                font.setPointSize(my_dict["size_font"])
                font.setFamily(my_dict["type_font"])

                self.plainTextEdit.setFont(font)
        except:
            pass

        if self.checker_them() == "dark":
            self.actionLight.setChecked(False)
            self.actionDark.setChecked(True)
        #=========================== Status Bar =========================
        self.statusbar.setStatusTip("Dont Touch me")
        self.actionExit.setStatusTip("EXIT")
        self.actionDate.setStatusTip("Put Date now")
        self.actionTime.setStatusTip("Put Time now")
        self.actionFont.setStatusTip("Setting Font")
        self.actionClose_Window.setStatusTip("Close This window")
        self.actionNew_Window.setStatusTip("Open a new Window")
        self.actionSave_on_This.setStatusTip("Save on File Entered")
        self.actionSave_To.setStatusTip("Save To ...")
        self.actionOpen.setStatusTip("Open New File")
        self.actionCalender.setStatusTip("Open Calender")
        self.actionAbout.setStatusTip("About program and Developer")
        
        self.plainTextEdit.setStatusTip(f"| TextDad | {str(datetime.now())[0:10]} |")
        # ========================= Dialogs ============================
        self.actionFont.triggered.connect(self.dialog_font)
        self.actionCalender.triggered.connect(self.open_calender)
        self.actionReport_Problem.triggered.connect(self.massage_box_report)
        self.actionAbout.triggered.connect(self.dialog_about)
        # ============================ PUT =============================
        self.actionDate.triggered.connect(lambda: self.put_date("Date"))
        self.actionTime.triggered.connect(lambda: self.put_date("time"))
        # ============================ File =============================
        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave_To.triggered.connect(self.save_in_file)
        self.actionSave_on_This.triggered.connect(self.save_on_this)
        self.actionExit.triggered.connect(sys.exit)
        # ============================== Them =======================
        self.actionLight.triggered.connect(
            lambda: self.controler_them("light"))
        self.actionDark.triggered.connect(lambda: self.controler_them("dark"))



    def _statusbar_(self):
        pass

    def checker_them(self):
        try:
            with open("them.txt", "r") as File:
                if File.read() == "dark":
                    return "dark"
                elif File.read() == "light":
                    return "light"
        except:
            return "light"

    def dialog_about(self):
        dialog = QtWidgets.QDialog()

        dialog.ui = info.Ui_Dialog()
        dialog.ui.setupUi(dialog)

        dialog.ui.pushButton.clicked.connect(dialog.close)

        dialog.exec_()

    def massage_box_report(self):
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Report Problem")
        self.msg.setText(
            "If You See a problem or Bug\nPlease Rport This to\nEmail:Pooyarezaiy909@gmail.com")
        self.msg.show()

    def controler_them(self, them):
        if them == "light":
            self.actionLight.setChecked(True)
            self.actionDark.setChecked(False)
            with open("them.txt", "w") as File:
                File.write("light")
        elif them == "dark":
            self.actionLight.setChecked(False)
            self.actionDark.setChecked(True)
            with open("them.txt", "w") as File:
                File.write("dark")

    def put_date(self, Type):
        date = str(datetime.now())
        dates = date.split(" ")
        if Type == "Date":
            a = dates[0]
            self.plainTextEdit.appendPlainText(a)
        elif Type == "time":
            a = dates[1][0:5]
            self.plainTextEdit.appendPlainText(a)

    def open_file(self):
        try:
            self.path = QtWidgets.QFileDialog.getOpenFileName()[0]
            with open(self.path, "r") as File:
                text = File.read()
                self.plainTextEdit.setPlainText(text)
        except:
            pass

    def save_in_file(self):
        try:
            self.path = QtWidgets.QFileDialog.getSaveFileName()[0]
            with open(self.path, "w") as File:
                text = self.plainTextEdit.toPlainText()
                File.write(text)
        except:
            pass

    def save_on_this(self):
        try:
            with open(self.path, "w") as File:
                text = self.plainTextEdit.toPlainText()
                File.write(text)
        except:
            pass

    def open_calender(self):
        dialog = QtWidgets.QDialog()
        dialog.ui = calender.Ui_Form()
        dialog.ui.setupUi(dialog)

        dialog.exec_()

    def dialog_font(self):
        dialog = QtWidgets.QDialog()

        dialog.ui = font.Ui_Form()
        dialog.ui.setupUi(dialog)

        def set_font():
            self.font = dialog.ui.getter_font()
            with open("setting.json", "w") as File:
                font_json = json.dumps(self.font)
                File.write(font_json)

            self.plainTextEdit.setFont(dialog.ui.maker_font())

            dialog.close()

        dialog.ui.btn_cancel.clicked.connect(dialog.close)
        dialog.ui.btn_save.clicked.connect(set_font)

        dialog.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TextDad"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuPut.setTitle(_translate("MainWindow", "Put"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.menuThem.setTitle(_translate("MainWindow", "Them"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave_on_This.setText(
            _translate("MainWindow", "Save"))
        self.actionSave_To.setText(_translate("MainWindow", "Save as"))
        self.actionClose_Window.setText(
            _translate("MainWindow", "Close Window"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionCalender.setText(_translate("MainWindow", "Calender"))
        self.actionDate.setText(_translate("MainWindow", "Date"))
        self.actionTime.setText(_translate("MainWindow", "Time"))
        self.actionFont.setText(_translate("MainWindow", "Font"))
        self.actionLight.setText(_translate("MainWindow", "Light"))
        self.actionDark.setText(_translate("MainWindow", "Dark"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionReport_Problem.setText(
            _translate("MainWindow", "Report Problem"))


def checker_them():
    try:
        with open("them.txt", "r") as File:
            if File.read() == "dark":
                return "dark"
            elif File.read() == "light":
                return "light"
    except:
        return "light"
 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    if checker_them() == "dark":
        app.setStyleSheet(qdarkstyle.load_stylesheet_from_environment())
    MainWindow.show()

    sys.exit(app.exec_())
