from PySide6.QtWidgets import QLabel, QPushButton, QLineEdit


def OutputViewer(self):
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
