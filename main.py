import json
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_notes()
        self.ui.notate_bibliot.addItems(self.notes)
        self.ui.notate_bibliot.itemClicked.connect(self.show_note)
        self.ui.save_notate.clicked.connect(self.save_note)
        self.ui.create_notate.clicked.connect(self.create_notate)
        self.ui.delet_notate.clicked.connect(self.delete_note)



    def show_note(self):
        self.name = self.ui.notate_bibliot.selectedItems()[0].text()
        self.ui.line_ss.setText(self.name)
        self.ui.text_Edit_big.setText(self.notes[self.name]["текст"])

    def save_note(self):
        self.notes[self.ui.line_ss.text()] = {
                "текст":self.ui.text_Edit_big.toPlainText(),
                "теги": []
        }
        with open("notes.json", "w", encoding="utf-8" ) as file:
            json.dump(self.notes, file)
        self.ui.notate_bibliot.clear()
        self.ui.notate_bibliot.addItems(self.notes)

    def clear(self):
        self.ui.line_ss.clear()
        self.ui.text_Edit_big.clear()

    def create_notate(self):
        self.clear()
        
    def read_notes(self):
        try:
            with open("notes.json", "r" , encoding="utf-8" ) as file:
                self.notes = json.load(file)
        except:
            self.notes = {
                "Перша замітка":{
                    "текст": "Це текст першої замітки",
                    "теги": []
                }

            }


    def delete_note(self):
        try:
            del self.notes[self.name]
            self.clear()
            self.ui.line_ss.clear()
            self.ui.text_Edit_big.clear()
            self.save_note()
        except:
            print("помилка видалення")

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()





































































