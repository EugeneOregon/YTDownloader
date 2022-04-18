# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(975, 505)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(236, 255, 45, 255), stop:1 rgba(255, 255, 160, 255));\n"
            "color:  rgb(155, 155, 155);\n"
            "border-radius: 5%;\n"
            "font: 12pt \"MS Shell Dlg 2\";")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Ukrainian, QtCore.QLocale.Ukraine))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.placeHolderChoice = QtWidgets.QToolButton(self.centralwidget)
        self.placeHolderChoice.setGeometry(QtCore.QRect(930, 60, 31, 31))
        self.placeHolderChoice.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.placeHolderChoice.setStyleSheet("QToolButton {\n"
                                             "    background-color: rgb(80, 80, 80);\n"
                                             "    color:  rgb(255, 255, 0);\n"
                                             "    border-radius: 5%;\n"
                                             "}\n"
                                             "\n"
                                             "QToolButton:hover {\n"
                                             "    background-color: rgb(120, 120, 120);\n"
                                             "    color:  rgb(255, 255, 255);\n"
                                             "    border-radius: 5%;\n"
                                             "    transition: all 0.3s ease 0s;\n"
                                             "}")
        self.placeHolderChoice.setObjectName("placeHolderChoice")
        self.downloadAudio = QtWidgets.QPushButton(self.centralwidget)
        self.downloadAudio.setGeometry(QtCore.QRect(780, 360, 181, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.downloadAudio.setFont(font)
        self.downloadAudio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downloadAudio.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(80, 80, 80);\n"
                                         "    font: 75 12pt \"MS Shell Dlg 2\";\n"
                                         "    color:  rgb(255, 255, 0);\n"
                                         "    border-radius: 5%;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(120, 120, 120);\n"
                                         "    font: 75 12pt \"MS Shell Dlg 2\";\n"
                                         "    color:  rgb(255, 255, 255);\n"
                                         "    border-radius: 5%;\n"
                                         "    transition: all 0.3s ease 0s;\n"
                                         "}")
        self.downloadAudio.setObjectName("downloadAudio")
        self.downloadVideo = QtWidgets.QPushButton(self.centralwidget)
        self.downloadVideo.setEnabled(True)
        self.downloadVideo.setGeometry(QtCore.QRect(780, 270, 181, 71))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.downloadVideo.setFont(font)
        self.downloadVideo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.downloadVideo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.downloadVideo.setStyleSheet("QPushButton {\n"
                                         "    background-color: rgb(80, 80, 80);\n"
                                         "    font: 75 12pt \"MS Shell Dlg 2\";\n"
                                         "    color:  rgb(255, 255, 0);\n"
                                         "    border-radius: 5%;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(120, 120, 120);\n"
                                         "    font: 75 12pt \"MS Shell Dlg 2\";\n"
                                         "    color:  rgb(255, 255, 255);\n"
                                         "    border-radius: 5%;\n"
                                         "    transition: all 0.3s ease 0s;\n"
                                         "}")
        self.downloadVideo.setObjectName("downloadVideo")
        self.placeHolder = QtWidgets.QTextBrowser(self.centralwidget)
        self.placeHolder.setGeometry(QtCore.QRect(540, 60, 381, 31))
        self.placeHolder.setStyleSheet("QTextBrowser {\n"
                                       "    background-color: rgb(80, 80, 80);\n"
                                       "    color:  rgb(255, 255, 0);\n"
                                       "    border-radius: 5%;\n"
                                       "    font: 8pt \"MS Shell Dlg 2\";\n"
                                       "    text-align: center;\n"
                                       "    padding-top: 2px;\n"
                                       "}\n"
                                       "\n"
                                       "")
        self.placeHolder.setObjectName("placeHolder")
        self.linkYouTube = QtWidgets.QPushButton(self.centralwidget)
        self.linkYouTube.setEnabled(True)
        self.linkYouTube.setGeometry(QtCore.QRect(540, 10, 421, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.linkYouTube.setFont(font)
        self.linkYouTube.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.linkYouTube.setFocusPolicy(QtCore.Qt.NoFocus)
        self.linkYouTube.setStyleSheet("QPushButton {\n"
                                       "    background-color: rgb(80, 80, 80);\n"
                                       "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                       "    color: rgb(255, 255, 0);\n"
                                       "    border-radius: 5%;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {\n"
                                       "    background-color: rgb(120, 120, 120);\n"
                                       "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                       "    color:  rgb(255, 255, 255);\n"
                                       "    border-radius: 5%;\n"
                                       "    transition: all 0.3s ease 0s;\n"
                                       "}")
        self.linkYouTube.setObjectName("linkYouTube")
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setGeometry(QtCore.QRect(30, 10, 81, 81))
        self.labelLogo.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("ytlogo.png"))
        self.labelLogo.setObjectName("labelLogo")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(40, 440, 711, 21))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.progressBar.setFont(font)
        self.progressBar.setMouseTracking(False)
        self.progressBar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setToolTipDuration(-1)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    background-color: rgb(90, 90, 90);\n"
                                       "    font: 75 10pt \"MS Shell Dlg 2\";\n"
                                       "    color: white;\n"
                                       "    border-radius: 5%;\n"
                                       "    text-align: center;\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    background-color: ;\n"
                                       "    background-color:qlineargradient(spread:pad, x1:0.136, y1:0.0905455, x2:0.966, y2:0.0625, stop:0 rgba(108, 255, 168, 245), stop:0.943182 rgba(0, 212, 41, 241));\n"
                                       "    border-radius: 5%;\n"
                                       "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 460, 711, 20))
        self.lineEdit.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 120, 731, 321))
        self.label.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("boombox.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 351, 61))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(255, 255, 255, 0));\n"
            "font: 24pt \"Ink Free\";")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.placeHolderChoice.raise_()
        self.downloadAudio.raise_()
        self.downloadVideo.raise_()
        self.placeHolder.raise_()
        self.linkYouTube.raise_()
        self.labelLogo.raise_()
        self.progressBar.raise_()
        self.lineEdit.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube Downloader"))
        MainWindow.setWindowIcon(QtGui.QIcon('YTDicon.png'))
        self.placeHolderChoice.setText(_translate("MainWindow", "..."))
        self.downloadAudio.setText(_translate("MainWindow", "Завантажити Аудіо"))
        self.downloadVideo.setText(_translate("MainWindow", "Завантажити Відео"))
        self.placeHolder.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Вкажіть шлях, де зберегти файл</p></body></html>"))
        self.linkYouTube.setText(_translate("MainWindow", "Вказати посилання для завантаження"))
        self.label_2.setText(_translate("MainWindow", "YouTube Downloader"))
