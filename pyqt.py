import os.path
import sys
import re  # regex
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from hideRead import solve  # app logic
import config.config as config  # app config
# Components for GUI layout and functionality:
from components.layout.mode_selector import ModeSelector
from components.layout.option_selector import OptionSelector
from components.layout.input_selector import InputSelector
from components.layout.image_selector import ImageSelector
from components.layout.message_editor import MessageEditor
from components.functional.save import Save
from components.functional.copy_to_clipboard import CopyToClipboard
from components.functional.on_input_change import OnInputChange
from components.functional.on_message_change import OnMessageChange
from components.functional.set_hide_read_mode import SetMode

#TO DO:
#Add error handling component line 109
#Add select_image, select_second_image, hide_message, read_message functional components
#Run test
#BuildS

class SteganographyApp(QMainWindow):
    def __init__(self, window_title, window_x, window_y, window_width, window_height, file_pattern, msg_pattern):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.oimg = self.simg = self.msg = self.out = ""
        self.oi = self.si = False
        self.file_pattern = file_pattern
        self.msg_pattern = msg_pattern
        with open('style/style.css', 'r') as file:
            self.setStyleSheet(""+file.read()+"")
        self.initUI()

    def initUI(self):
        self.mode_var = "read"
        ModeSelector(self)
        OptionSelector(self)
        InputSelector(self)
        ImageSelector(self)
        MessageEditor(self)

    def on_input_change(self, text):
        OnInputChange(self, text)

    def on_message_change(self, text):
        OnMessageChange(self, text)

    def copy_to_clipboard(self):
        CopyToClipboard(self)

    def set_hide_mode(self):
        self.mode_var = "hide"
        SetMode(self, False)

    def set_read_mode(self):
        self.mode_var = "read"
        SetMode(self, True)

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
        if os.path.isfile('img/' + self.out):
            self.input_label_warning.show()
            self.input_label_warning.setText("File already exist!")
            return
        if not re.match(self.file_pattern, self.out):
            self.input_label_warning.show()
            self.input_label_warning.setText(
                "No symbols / only .png!")
            return
        if self.msg == "":
            self.label_msg_warning.show()
            return
        if not re.match(self.msg_pattern, self.msg):
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
        Save(self, result)
        self.msg_output.setText(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    steganography_app = SteganographyApp(
        config.window_title, config.window_x, config.window_y, config.window_width, config.window_height, config.file_pattern, config.msg_pattern)
    steganography_app.show()
    sys.exit(app.exec())
