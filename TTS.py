from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QColor
from PyQt5.QtWidgets import *
import pyttsx3
from pathlib import Path


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(760, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelSpeed = QtWidgets.QLabel(self.centralwidget)
        self.labelSpeed.setObjectName("labelSpeed")
        self.horizontalLayout_5.addWidget(self.labelSpeed)
        self.comboBoxSpeed = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxSpeed.setObjectName("comboBoxSpeed")
        self.comboBoxSpeed.addItem("")
        self.comboBoxSpeed.setItemText(0, "")
        self.comboBoxSpeed.addItem("")
        self.comboBoxSpeed.addItem("")
        self.comboBoxSpeed.addItem("")
        self.comboBoxSpeed.addItem("")
        self.comboBoxSpeed.addItem("")
        self.comboBoxSpeed.addItem("")
        self.comboBoxSpeed.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBoxSpeed)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelVoice = QtWidgets.QLabel(self.centralwidget)
        self.labelVoice.setObjectName("labelVoice")
        self.horizontalLayout_4.addWidget(self.labelVoice)
        self.comboBoxVoice = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxVoice.setObjectName("comboBoxVoice")
        self.comboBoxVoice.addItem("")
        self.comboBoxVoice.setItemText(0, "")
        self.comboBoxVoice.addItem("")
        self.comboBoxVoice.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBoxVoice)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSpeed.setText(_translate("MainWindow", "Speed"))
        self.comboBoxSpeed.setItemText(1, _translate("MainWindow", "0.25x"))
        self.comboBoxSpeed.setItemText(2, _translate("MainWindow", "0.5x"))
        self.comboBoxSpeed.setItemText(3, _translate("MainWindow", "0.75x"))
        self.comboBoxSpeed.setItemText(4, _translate("MainWindow", "1x"))
        self.comboBoxSpeed.setItemText(5, _translate("MainWindow", "1.5x"))
        self.comboBoxSpeed.setItemText(6, _translate("MainWindow", "2x"))
        self.comboBoxSpeed.setItemText(7, _translate("MainWindow", "3x"))
        self.labelVoice.setText(_translate("MainWindow", "Voice"))
        self.comboBoxVoice.setItemText(1, _translate("MainWindow", "Male"))
        self.comboBoxVoice.setItemText(2, _translate("MainWindow", "Female"))
        self.pushButton.setText(_translate("MainWindow", "Go"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

        self.Update()
        self.pushButton.clicked.connect(self.Speak)
        self.actionSave_2.triggered.connect(self.Save)
        self.actionQuit.triggered.connect(self.Quit)

    def Update(self):
        self.comboBoxSpeed.setCurrentText('1x')
        self.comboBoxVoice.setCurrentText('Male')
        placeholderText = 'Enter your Text here'
        text = ''
        self.textEdit.setText(text)
        self.textEdit.setPlaceholderText(placeholderText)
        self.actionSave_2.setShortcut('ctrl+s')
        self.actionSave_2.setIcon(QIcon('Images/Save.png'))
        self.actionQuit.setShortcut('ctrl+q')
        self.actionQuit.setIcon(QIcon('Images/Quit.png'))

    def Speak(self):
        self.text = self.textEdit.toPlainText()
        self.speed = self.comboBoxSpeed.currentText()
        self.voiceid = self.comboBoxVoice.currentText()

        self.speed = self.speed[:-1]
        self.speed = float(self.speed)
        self.speed = self.speed * 100
        self.speed = int(self.speed)

        engine = pyttsx3.init()
        engine.setProperty('rate', self.speed)
        voice = engine.getProperty('voices')
        if self.voiceid == 'Male':
            voices = voice[0].id
        else:
            voices = voice[1].id
        engine.setProperty('voice', voices)
        engine.say(self.text)
        engine.runAndWait()

    def Save(self):
        name, _ = QFileDialog.getSaveFileName(caption='Save File', filter="Media(*.mp3)")
        path = Path(name)
        output_dir = Path(name)
        output_dir.mkdir(parents=True, exist_ok=True)

        filename1 = path.stem
        filename = f'{output_dir}/{filename1}.mp3'
        text = self.textEdit.toPlainText()
        engine = pyttsx3.init()
        engine.save_to_file(text=text, filename=filename)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QIcon('Images/Success.png'))
        msg.setText("Your Audio File has been Saved Successfully")
        msg.setInformativeText(f"Path {name}")
        msg.setWindowTitle("Success")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        self.textEdit.setText('')
        engine.runAndWait()

    def Quit(self):
        exit(0)




if __name__ == "__main__":
    import sys

    App = QtWidgets.QApplication(sys.argv)
    App.setStyle('Fusion')

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(190, 190, 190))
    palette.setColor(QPalette.WindowText, Qt.black)
    palette.setColor(QPalette.Base, QColor(0,0,0))
    palette.setColor(QPalette.AlternateBase, QColor(64, 128, 128))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.darkMagenta)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(190, 190, 190))
    palette.setColor(QPalette.ButtonText, Qt.black)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(0,0,0))
    palette.setColor(QPalette.HighlightedText, Qt.white)
    App.setPalette(palette)
    App.setStyleSheet("QToolTip { color: #ffffff; background-color: #ffffff; border: 1px solid white; }")

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('Text to Speech')
    MainWindow.setWindowIcon(QIcon('Images/Logo.png'))
    MainWindow.show()
    sys.exit(App.exec_())
