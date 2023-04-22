import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
import os

# <-----------------------------------------------------frontend---------------------------------------------------------->
# <-----------------------------------------------------1 window---------------------------------------------------------->
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1080, 720))
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 1027, 200))
        self.label_2.setMinimumSize(QtCore.QSize(1027, 200))
        self.label_2.setMaximumSize(QtCore.QSize(1044, 200))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setToolTipDuration(-1)
        self.label_2.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.label_2.setObjectName("label_2")
        self.biton1 = QtWidgets.QPushButton(self.centralwidget)
        self.biton1.setGeometry(QtCore.QRect(30, 280, 111, 31))
        self.biton1.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; }\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 40); }")
        self.biton1.setObjectName("biton1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 721, 31))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Данное приложение позволит вам с помощью текста Руфье провести первичную диагностику вашего здоровья.\n"
"Проба ручье представляет собой нагрузочный комплекс ,предназначенный для оценки работоспособности сердца \n"
"при физической нагрузке. У испытуемого ,находиться в положении лежа на спине \n"
"в течение 5 минут, определяют частоту пульса за 15 секунд. Затем в течении 45 секунд испытуемый выполняет 30 приседаний.\n"
"После окончания нагрузки испытуемый ложится ,и у него вновь подсчитывается число пульсаций за первые 15 секунд, \n"
" а потом - за последние 15 секунд первой минуты периода восстанавления.\n"
"Важно! Если в процессе проведения испытания вы почуствуете себя плохо \n"
"(появиться головокружение ,шум в ушах, сильная отдышка и др.), то тест необходимо прервать и обратится к врачу."))
        self.biton1.setText(_translate("MainWindow", "начать тест"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать в программу по определению состояния здоровья!"))















# <-----------------------------------------------------2 window---------------------------------------------------------->
class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1080, 720)
        widget.setMinimumSize(QtCore.QSize(1080, 720))
        widget.setMaximumSize(QtCore.QSize(1080, 720))
        widget.setAutoFillBackground(False)
        widget.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(30, 40, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(30, 105, 91, 16))
        self.label_2.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 731, 16))
        self.label_3.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.label_3.setObjectName("label_3")
        self.biton2 = QtWidgets.QPushButton(widget)
        self.biton2.setGeometry(QtCore.QRect(23, 201, 161, 31))
        self.biton2.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; }\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 40); }")
        self.biton2.setObjectName("biton2")
        self.label_4 = QtWidgets.QLabel(widget)
        self.label_4.setGeometry(QtCore.QRect(30, 281, 881, 16))
        self.label_4.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.label_4.setObjectName("label_4")
        self.biton3 = QtWidgets.QPushButton(widget)
        self.biton3.setGeometry(QtCore.QRect(23, 310, 201, 32))
        self.biton3.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; }\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 40); }")
        self.biton3.setObjectName("biton3")
        self.label_5 = QtWidgets.QLabel(widget)
        self.label_5.setGeometry(QtCore.QRect(30, 353, 881, 71))
        self.label_5.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.label_5.setObjectName("label_5")
        self.biton4 = QtWidgets.QPushButton(widget)
        self.biton4.setGeometry(QtCore.QRect(23, 427, 181, 32))
        self.biton4.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; }\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 40); }")
        self.biton4.setObjectName("biton4")
        self.lineEdit = QtWidgets.QLineEdit(widget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 113, 21))
        self.lineEdit.setStyleSheet("color: white;\n"
"background-color: rgba(204, 204, 204, 15); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 130, 113, 21))
        self.lineEdit_2.setStyleSheet("color: white;\n"
"background-color: rgba(204, 204, 204, 15); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 240, 113, 21))
        self.lineEdit_3.setStyleSheet("color: white;\n"
"background-color: rgba(204, 204, 204, 15); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 470, 113, 21))
        self.lineEdit_4.setStyleSheet("color: white;\n"
"background-color: rgba(204, 204, 204, 15); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 500, 113, 21))
        self.lineEdit_5.setStyleSheet("color: white;\n"
"background-color: rgba(204, 204, 204, 15); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.biton5 = QtWidgets.QPushButton(widget)
        self.biton5.setGeometry(QtCore.QRect(430, 545, 181, 32))
        self.biton5.setStyleSheet("QPushButton {\n"
"color: white;\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; }\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 0, 40); }")
        self.biton5.setObjectName("biton5")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "trojan1"))
        self.label.setText(_translate("widget", "Введите Ф.И.О:"))
        self.label_2.setText(_translate("widget", "Полных лет:"))
        self.label_3.setText(_translate("widget", "Лягте на спину и замерите пульс за 15 секунд. Нажмите кнопку «Начать первый тест», чтобы запустить таймер."))
        self.biton2.setText(_translate("widget", "Начать первый тест:"))
        self.label_4.setText(_translate("widget", "Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку «Начать делать приседания», чтобы запустить счетчик приседаний."))
        self.biton3.setText(_translate("widget", "Начать делать приседания"))
        self.label_5.setText(_translate("widget", "Лягте на спину и замерите пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\n"
"Нажмите кнопку «Начать финальный тест », чтобы запустить таймер.\n"
"Зеленым обозначены секунды ,в течение которых необходимо проводить измерения, черным - минуты без замера пульсаций.\n"
"Результаты запишите в соответствующие поля."))
        self.biton4.setText(_translate("widget", "Начать финальный тест"))
        self.biton5.setText(_translate("widget", "Отправить результаты"))













# <-----------------------------------------------------3 window---------------------------------------------------------->
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1080, 720)
        Form.setMinimumSize(QtCore.QSize(1080, 720))
        Form.setMaximumSize(QtCore.QSize(1080, 720))
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(370, 210, 181, 21))
        self.label_2.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(450, 180, 101, 16))
        self.label.setStyleSheet("color: white;\n"
"background-color: rgba(255, 255, 255, 30); border: 1px solid rgba(255, 255, 255, 40); border-radius: 7px")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "trojan2"))
        self.label_2.setText(_translate("Form", "Работоспособность сердца:"))
        self.label.setText(_translate("Form", "Индекс Руфье:"))














# <-----------------------------------------------------back-end---------------------------------------------------------->
# 1 окно
class win1(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self.biton1.clicked.connect(self.next_click)

    def next_click(self):
        self.tw = Ui_widget()
        self.hide()


if __name__ == '__main__':
    app = QApplication([])
    widget = win1()
    widget.show()
    app.exec_()