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
        self.ui.addtonotate.clicked.connect(self.add_tag)
        self.ui.destroy_note.clicked.connect(self.del_teg)
        self.ui.search_teg.clicked.connect(self.search_by_tag)

    def show_note(self):
        self.name = self.ui.notate_bibliot.selectedItems()[0].text()
        self.ui.line_ss.setText(self.name)
        self.ui.text_Edit_big.setText(self.notes[self.name]["текст"])

    def save_note(self):
        tags = []
        for i in range(self.ui.biblio_teg.count()):
            tags.append(self.ui.biblio_teg.item(i).text())

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

    def add_tag(self):
        tag_name = self.ui.teg.toPlainText()
        if tag_name!="":
            if tag_name not in self.notes[self.name]["теги"]:
                self.notes[self.name]["теги"].append(tag_name)
                self.ui.biblio_teg.clear()
                self.ui.biblio_teg.addItems(self.notes[self.name]["теги"])


    def del_teg(self):
        if self.ui.biblio_teg.selectedItems():
            tag_name = self.ui.biblio_teg.selectedItems()[0].text()
            if tag_name in self.notes[self.name]["теги"]:
                self.notes[self.name]["теги"].remove(tag_name) 
                self.ui.biblio_teg.clear()
                self.ui.biblio_teg.addItems(self.notes[self.name]["теги"])

    def search_by_tag(self):

        tag = self.ui.teg.toPlainText()
        if tag:
            text_Edit_big = []
            for note_name in self.notes:
                if tag in self.notes[note_name]["теги"]:
                    text_Edit_big.append(note_name)
            self.ui.notate_bibliot.clear()
            self.ui.notate_bibliot.addItems(text_Edit_big)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()





































































