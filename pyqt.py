import os.path
import sys
import re
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
from components.functional.select_image import SelectImage

# TO DO:
# Add select_image, select_second_image, hide_message, read_message functional components
# Run test
# BuildS

# Do NOT change!
READ_MODE = "R"
HIDE_MODE = "H"
IMAGE_DIRECTORY = 'img/'
LINK_STYLE = 'style/style.css'
# Errors and texts
SET_MODE_READ = "read"
SET_MODE_HIDE = "hide"
TXT_OPEN_IMAGE = "Open Image File"
TXT_OPEN_SECOND_IMAGE = "Open Second Image File"
ERR_UPLOAD = "Upload an image!"
ERR_OUTPUT_FILE = "Enter output file!"
ERR_EXIST = "File already exist!"
ERR_INVALID_FILE = "No symbols / only .png!"
ERR_MESSAGE = "Message is reqired!"
ERR_INVALID_MESSAGE = "Message contains illegal symbols!"
ERR_MESSAGE_LENGTH = "Message is too long for this image!"


class SteganographyApp(QMainWindow):
    def __init__(self, window_title, window_x, window_y, window_width, window_height, file_pattern, msg_pattern):
        super().__init__()
        self.setWindowTitle(window_title)
        self.setGeometry(window_x, window_y, window_width, window_height)
        self.oimg = self.simg = self.msg = self.out = ""
        self.oi = self.si = False
        self.file_pattern = file_pattern
        self.msg_pattern = msg_pattern
        with open(LINK_STYLE, 'r') as file:
            self.setStyleSheet(""+file.read()+"")
        self.initUI()

    def initUI(self):
        self.mode_var = SET_MODE_READ
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
        self.mode_var = SET_MODE_HIDE
        SetMode(self, False)

    def set_read_mode(self):
        self.mode_var = SET_MODE_READ
        SetMode(self, True)

    def select_image(self):
        SelectImage(self, TXT_OPEN_IMAGE, ERR_UPLOAD)

    def select_second_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, TXT_OPEN_SECOND_IMAGE)
        pixmap = QPixmap(file_path).scaled(
            100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        if pixmap.isNull():
            self.handle_errors_and_text(self.label2, ERR_UPLOAD)
            self.si = False
            return
        self.si = True
        self.simg = file_path
        self.label2.setPixmap(pixmap)

    def hide_message(self):
        if self.oi == False:
            self.handle_errors_and_text(self.label, ERR_UPLOAD)
            return
        if self.out == "":
            self.input_label_warning.show()
            self.handle_errors_and_text(
                self.input_label_warning, ERR_OUTPUT_FILE)
            return
        if os.path.isfile(IMAGE_DIRECTORY + self.out):
            self.input_label_warning.show()
            self.handle_errors_and_text(
                self.input_label_warning, ERR_EXIST)
            return
        if not re.match(self.file_pattern, self.out):
            self.input_label_warning.show()
            self.handle_errors_and_text(
                self.input_label_warning, ERR_INVALID_FILE)
            return
        if self.msg == "":
            self.handle_errors_and_text(
                self.label_msg_warning, ERR_MESSAGE)
            self.label_msg_warning.show()
            return
        if not re.match(self.msg_pattern, self.msg):
            self.handle_errors_and_text(
                self.label_msg_warning, ERR_INVALID_MESSAGE)
            return self.label_msg_warning.show()
        try:
            solve(HIDE_MODE, self.oimg, "", self.msg, self.out, "")
        except:
            self.handle_errors_and_text(
                self.label_msg_warning, ERR_MESSAGE_LENGTH)
            return self.label_msg_warning.show()

    def read_message(self):
        if(self.oi == False):
            self.handle_errors_and_text(self.label, ERR_UPLOAD)
            return
        if(self.si == False):
            self.handle_errors_and_text(self.label2, ERR_UPLOAD)
            return
        result = solve(READ_MODE, self.oimg, self.simg, "", "", "")
        Save(self, result)
        self.handle_errors_and_text(self.msg_output, result)

    def handle_errors_and_text(self, target, error):
        target.setText(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    steganography_app = SteganographyApp(
        config.window_title, config.window_x, config.window_y, config.window_width, config.window_height, config.file_pattern, config.msg_pattern)
    steganography_app.show()
    sys.exit(app.exec())
