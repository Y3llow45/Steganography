import re
import os.path


def HideMessage(self, ERR_UPLOAD, ERR_OUTPUT_FILE, IMAGE_DIRECTORY, ERR_EXIST, ERR_INVALID_FILE, ERR_MESSAGE, ERR_INVALID_MESSAGE, solve, HIDE_MODE, ERR_MESSAGE_LENGTH):
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
