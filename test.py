import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QTextEdit, QMessageBox, QFileDialog
)
from main import process

class FileViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Conversor')
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()
        
        self.label = QLabel("Arrastra archivo excel a convertir")
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        
        # Add components to layout
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text_edit)
        
        self.setLayout(self.layout)

        # Allow drag & drop
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.open_file(file_path)
            # self.process_file(file_path)

    def process_file(self, filepath):
        if os.path.isfile(filepath):
            return process(filepath)
        else:
            QMessageBox.warning(self, "Warning", "No es un archivo")
            return "nope"

    def open_file(self, filepath):
        if os.path.isfile(filepath):
            # with open(filepath, 'r') as file:
            #     content = file.read()
                
            content = f"ÉXITO {filepath}"
            try:
                content += " " + self.process_file(filepath)
            except Exception as ex:
                content = f"FALLO {filepath}" + str(ex)
            self.text_edit.setPlainText(content)
        else:
            QMessageBox.warning(self, "Warning", "The dropped item is not a valid file.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileViewer()
    window.show()
    sys.exit(app.exec_())