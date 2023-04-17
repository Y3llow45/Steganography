from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtWidgets import QLineEdit, QApplication, QMainWindow, QLabel, QPushButton, QFileDialog, QRadioButton, QCheckBox
from time import gmtime, strftime
from hideRead import solve  # here is the logic
import os.path
import sys
import pyperclip
import re

#window_title = "Steganography"
#window_geometry = 100, 100, 500, 500


def save(self, result):
    if self.checkbox.isChecked():
        output_file = str(strftime("%Y-%m-%d-%H-%M-%S", gmtime()))
        with open(f"{output_file}.txt", "w") as f:
            f.write(result)


class SteganographyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Steganography")
        self.setGeometry(100, 100, 500, 500)
        self.oimg = ""
        self.simg = ""
        self.msg = ""
        self.out = ""
        self.oi = False
        self.si = False
        self.pattern = r"^[a-zA-Z0-9][a-zA-Z0-9_\-. ]*\.(png)$"
        self.msgpattern = r'^[A-Za-z0-9 !@#$%^&*()_=+\-`\'"\\{}\[\]<>.,/]+$'
        # HEX Codes: #EDF4F2, #7C8363, #31473A
        self.style = """
    QWidget {
        background-color: #EDF4F2;
        color: #000000;
        font-family: 'Montserrat', sans-serif;
        font-size: 13px;
    }
    QPushButton {
        background-color: #31473A;
        color: #FFFFFF;
        border: none;
        border-radius: 3px;
        font-family: 'Montserrat', sans-serif;
        font-size: 13px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #31473A;
    }
    QLabel {
        font-family: 'Montserrat', sans-serif;
        font-size: 13px;
        font-weight: bold;
    }
    QRadioButton {
        font-family: 'Montserrat', sans-serif;
        border-radius: 3px;
        font-size: 13px;
        font-weight: bold;
    }
    QLineEdit {
        background-color: #FFFFFF;
        border: 1px solid #7C8363;
        border-radius: 3px;
        font-family: 'Montserrat', sans-serif;
        font-size: 13px;
        font-weight: bold;
    }
    QRadioButton::indicator {
        width: 20px;
        height: 20px;
        border-radius: 3px;
        border: 1px solid #31473A;
    }
    QRadioButton::indicator:checked {
        background-color: #7C8363;
        border: 1px solid #676d52;
        border-radius: 3px;
        border: 1px solid #31473A;
    }
    QCheckBox {
        color: #000000;
        font-family: 'Montserrat', sans-serif;
        font-size: 13px;
        font-weight: bold;
    }
    QCheckBox::indicator:hover {
        border: 1px solid #31473A;
    }
    QCheckBox::indicator {
        border: 1px solid #31473A;
    }
    QCheckBox::indicator::unchecked {
        border: 1px solid #31473A;
        border-radius: 3px;
    }
    QCheckBox::indicator::checked {
        background-color: #7C8363;
        border-radius: 3px;
    }
"""

        self.setStyleSheet(self.style)

        self.initUI()

    def initUI(self):
        self.mode_var = "read"
        self.mode_label = QLabel("Select mode:", self)
        self.mode_label.move(10, 10)
        self.hide_button = QRadioButton("Hide message", self)
        self.hide_button.move(100, 10)
        self.hide_button.setMinimumWidth(400)
        self.hide_button.clicked.connect(self.set_hide_mode)
        self.read_button = QRadioButton("Read message", self)
        self.read_button.move(250, 10)
        self.read_button.setMinimumWidth(400)
        self.read_button.setChecked(True)
        self.read_button.clicked.connect(self.set_read_mode)

        self.input_label = QLabel("Output image: ", self)
        self.input_label.move(10, 50)
        self.input_label.hide()
        self.input = QLineEdit(self)
        self.input.setMinimumWidth(110)
        self.input.textChanged.connect(self.on_input_changed)
        self.input.move(110, 50)
        self.input.hide()
        self.input_label_warning = QLabel("", self)
        self.input_label_warning.move(230, 50)
        self.input_label_warning.setMinimumWidth(240)
        self.input_label_warning.hide()

        self.option_label = QLabel("Select option:", self)
        self.option_label.move(10, 50)
        self.checkbox = QCheckBox("Save to file", self)
        self.checkbox.move(113, 50)
        self.checkbox.setFixedWidth(self.checkbox.fontMetrics(
        ).boundingRect(self.checkbox.text()).width() + 41)

        self.select_button = QPushButton("Original image", self)
        self.select_button.move(10, 100)
        self.select_button.clicked.connect(self.select_image)
        self.select_second_button = QPushButton("Second image", self)
        self.select_second_button.move(10, 150)
        self.select_second_button.clicked.connect(self.select_second_image)
        self.read_button = QPushButton("Read message", self)
        self.read_button.move(10, 200)
        self.read_button.clicked.connect(self.read_message)
        self.hide_button = QPushButton("Hide message", self)
        self.hide_button.move(10, 150)
        self.hide_button.clicked.connect(self.hide_message)
        self.hide_button.hide()

        self.label = QLabel(self)
        self.label.setGeometry(150, 100, 200, 100)
        self.label2 = QLabel(self)
        self.label2.setGeometry(280, 100, 200, 100)

        self.msg_output = QLabel(self)
        self.msg_output.setGeometry(15, 230, 470, 500)
        self.msg_output.setWordWrap(True)
        self.msg_output.setFixedHeight(200)
        self.copy = QPushButton("Copy message", self)
        self.copy.move(10, 460)
        self.copy.clicked.connect(self.copy_to_clipboard)

        self.label_msg = QLabel("Message: ", self)
        self.label_msg.move(15, 200)
        self.label_msg.hide()
        self.label_msg_warning = QLabel("Message is reqired!", self)
        self.label_msg_warning.move(85, 200)
        self.label_msg_warning.setMinimumWidth(200)
        self.label_msg_warning.hide()
        self.input_msg = QLineEdit(self)
        self.input_msg.textChanged.connect(self.on_message_changed)
        self.input_msg.move(15, 230)
        self.input_msg.setMinimumWidth(470)
        self.input_msg.hide()

    def on_message_changed(self, text):
        self.msg = str(text)
        self.label_msg_warning.hide()

    def on_input_changed(self, text):
        self.out = str(text)
        self.input_label_warning.hide()

    def copy_to_clipboard(self):
        text = self.msg_output.text().replace('\x00', '')
        pyperclip.copy(text)

    def set_hide_mode(self):
        self.mode_var = "hide"
        self.option_label.hide()
        self.checkbox.hide()
        self.select_second_button.hide()
        self.read_button.hide()
        self.label2.hide()
        self.msg = ""
        self.copy.hide()
        self.input_label.show()
        self.input.show()
        self.hide_button.show()
        self.label_msg.show()
        self.input_msg.show()
        self.input_msg.show()
        self.label_msg.show()
        self.input_label_warning.hide()
        self.label_msg_warning.hide()

    def set_read_mode(self):
        self.mode_var = "read"
        self.option_label.show()
        self.checkbox.show()
        self.select_second_button.show()
        self.read_button.show()
        self.label2.show()
        #self.msg = ""
        self.copy.show()
        self.input_label.hide()
        self.input.hide()
        self.hide_button.hide()
        self.label_msg.hide()
        self.input_msg.hide()
        self.input_msg.hide()
        self.label_msg.hide()
        self.input_label_warning.hide()
        self.label_msg_warning.hide()

    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File")
        pixmap = QPixmap(file_path).scaled(
            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if pixmap.isNull():
            self.label.setText("Upload an image!")
            self.oi = False
            return
        self.oi = True
        self.oimg = file_path
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
        self.simg = file_path
        self.label2.setPixmap(pixmap)

    def hide_message(self):
        if self.oi == False:
            self.label.setText("Upload an image!")
            return
        if self.out == "":
            self.input_label_warning.show()
            self.input_label_warning.setText("Enter output file!")
            return
        if os.path.isfile(self.out):
            self.input_label_warning.show()
            self.input_label_warning.setText("File already exist!")
            return
        # .replace('\x00', '')
        if not re.match(self.pattern, self.out):
            self.input_label_warning.show()
            self.input_label_warning.setText(
                "No symbols / only .png!")
            return
        if self.msg == "":
            self.label_msg_warning.show()
            return
        if not re.match(self.msgpattern, self.msg):
            return self.label_msg_warning.show()
        try:
            solve("H", self.oimg, "", self.msg, self.out, "")
        except:
            self.label_msg_warning.show()
            print("length error")

    def read_message(self):
        if(self.oi == False):
            self.label.setText("Upload an image!")
            return
        if(self.si == False):
            self.label2.setText("Upload an image!")
            return
        result = solve("R", self.oimg, self.simg, "", "", "")
        save(self, result)
        self.msg_output.setText(result)
        # print(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    steganography_app = SteganographyApp()
    steganography_app.show()
    sys.exit(app.exec())
