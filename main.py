import json
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.notes = {
            "Перша замітка":{
                "текст": "Це текст першої замітки",
                "теги":[]
            }
        }
        self.ui.notate_bibliot.addItems(self.notes)
        self.ui.notate_bibliot.itemClicked.connect(self.show_note)
        self.ui.save_notate.clicked.connect(self.save_note)
    def show_note(self):
        name = self.ui.notate_bibliot.selectedItems()[0].text()
        self.ui.line_ss.setText(name)
        self.ui.text_Edit_big.setText(self.notes[name]["текст"])

    def save_note(self):
        self.notes[self.ui.line_ss.text()] = self.ui.text_Edit_big.toPlainText()
        with open("notes.json", "w", encoding="utf-8" ) as file:
            json.dump(self.notes, file)






app = QApplication([])
ex = Widget()
ex.show()
app.exec_()

