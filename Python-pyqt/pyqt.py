import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox, QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QRadioButton


class SteganographyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Steganography")
        self.setGeometry(100, 100, 500, 500)
        self.oi = False
        self.si = False
        self.style = "background-color: #3c3c3c; color: #ffffff; font: bold 10pt Helvetica;"
        self.setStyleSheet(self.style)

        self.initUI()

    def initUI(self):
        self.mode_label = QLabel("Select mode:", self)
        self.mode_label.move(10, 10)

        self.mode_var = "read"

        self.hide_button = QRadioButton("Hide message", self)
        self.hide_button.move(100, 10)
        self.hide_button.setMinimumWidth(400)
        self.hide_button.clicked.connect(self.set_hide_mode)

        self.read_button = QRadioButton("Read message", self)
        self.read_button.move(250, 10)
        self.read_button.setMinimumWidth(400)
        self.read_button.setChecked(True)
        self.read_button.clicked.connect(self.set_read_mode)

        self.select_button = QPushButton("Original image", self)
        self.select_button.move(10, 50)
        self.select_button.clicked.connect(self.select_image)

        self.select_second_button = QPushButton("Second image", self)
        self.select_second_button.move(10, 100)
        self.select_second_button.clicked.connect(self.select_second_image)

        self.read_button = QPushButton("Read message", self)
        self.read_button.move(10, 150)
        self.read_button.clicked.connect(self.read_message)

        self.label = QLabel(self)
        self.label.setGeometry(150, 50, 200, 100)

        self.label2 = QLabel(self)
        self.label2.setGeometry(280, 50, 200, 100)

    def set_hide_mode(self):
        self.mode_var = "hide"

    def set_read_mode(self):
        self.mode_var = "read"

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File")
        pixmap = QPixmap(file_path).scaled(
            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if pixmap.isNull():
            self.label.setText("Upload an image!")
            self.oi = False
            return
        self.oi = True
        self.label.setPixmap(pixmap)

    def select_second_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File")
        pixmap = QPixmap(file_path).scaled(
            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if pixmap.isNull():
            self.label2.setText("Upload an image!")
            self.si = False
            return
        self.si = True
        self.label2.setPixmap(pixmap)

    def hide_message(self):
        # Code to hide message in image goes here
        pass

    def read_message(self):
        if(self.oi == False):
            self.label.setText("Upload an image!")
            return
        if(self.si == False):
            self.label2.setText("Upload an image!")
            return
        # run from MIP


if __name__ == "__main__":
    app = QApplication(sys.argv)
    steganography_app = SteganographyApp()
    steganography_app.show()
    sys.exit(app.exec())
