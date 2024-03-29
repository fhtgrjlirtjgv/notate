# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1009, 794)
        MainWindow.setStyleSheet("background:#bebebe ;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_ss = QtWidgets.QLineEdit(self.centralwidget)
        self.line_ss.setGeometry(QtCore.QRect(0, 20, 351, 21))
        self.line_ss.setStyleSheet("background:white;")
        self.line_ss.setObjectName("line_ss")
        self.notate_bibliot = QtWidgets.QListWidget(self.centralwidget)
        self.notate_bibliot.setGeometry(QtCore.QRect(390, 30, 251, 121))
        self.notate_bibliot.setStyleSheet("background:white;\n"
"border-radius: 10x;")
        self.notate_bibliot.setObjectName("notate_bibliot")
        self.text_Edit_big = QtWidgets.QTextEdit(self.centralwidget)
        self.text_Edit_big.setGeometry(QtCore.QRect(0, 50, 351, 461))
        self.text_Edit_big.setStyleSheet("background:white;")
        self.text_Edit_big.setObjectName("text_Edit_big")
        self.biblio_teg = QtWidgets.QListWidget(self.centralwidget)
        self.biblio_teg.setGeometry(QtCore.QRect(390, 290, 251, 121))
        self.biblio_teg.setStyleSheet("background:white;")
        self.biblio_teg.setObjectName("biblio_teg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 10, 74, 13))
        self.label.setObjectName("label")
        self.create_notate = QtWidgets.QPushButton(self.centralwidget)
        self.create_notate.setGeometry(QtCore.QRect(390, 170, 97, 41))
        self.create_notate.setStyleSheet("background:white;\n"
"\n"
"")
        self.create_notate.setObjectName("create_notate")
        self.delet_notate = QtWidgets.QPushButton(self.centralwidget)
        self.delet_notate.setGeometry(QtCore.QRect(540, 170, 97, 41))
        self.delet_notate.setStyleSheet("background:white;")
        self.delet_notate.setObjectName("delet_notate")
        self.save_notate = QtWidgets.QPushButton(self.centralwidget)
        self.save_notate.setGeometry(QtCore.QRect(470, 220, 97, 41))
        self.save_notate.setStyleSheet("background:white;")
        self.save_notate.setObjectName("save_notate")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 270, 64, 13))
        self.label_2.setObjectName("label_2")
        self.teg = QtWidgets.QTextEdit(self.centralwidget)
        self.teg.setGeometry(QtCore.QRect(390, 420, 251, 20))
        self.teg.setStyleSheet("background:white;")
        self.teg.setObjectName("teg")
        self.addtonotate = QtWidgets.QPushButton(self.centralwidget)
        self.addtonotate.setGeometry(QtCore.QRect(390, 450, 102, 23))
        self.addtonotate.setStyleSheet("background:white;")
        self.addtonotate.setObjectName("addtonotate")
        self.destroy_note = QtWidgets.QPushButton(self.centralwidget)
        self.destroy_note.setGeometry(QtCore.QRect(510, 450, 119, 23))
        self.destroy_note.setStyleSheet("background:white;")
        self.destroy_note.setObjectName("destroy_note")
        self.search_teg = QtWidgets.QPushButton(self.centralwidget)
        self.search_teg.setGeometry(QtCore.QRect(440, 480, 129, 23))
        self.search_teg.setStyleSheet("background:white;")
        self.search_teg.setObjectName("search_teg")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Список заміток"))
        self.create_notate.setText(_translate("MainWindow", "Створити замітку"))
        self.delet_notate.setText(_translate("MainWindow", "Видалити замітку"))
        self.save_notate.setText(_translate("MainWindow", "зберегти замітку"))
        self.label_2.setText(_translate("MainWindow", "Список тегів"))
        self.teg.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">введіть тег...</p></body></html>"))
        self.addtonotate.setText(_translate("MainWindow", "додати до замітки"))
        self.destroy_note.setText(_translate("MainWindow", "Відкріпити від замітки"))
        self.search_teg.setText(_translate("MainWindow", "Шукати замітки по тегу"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
