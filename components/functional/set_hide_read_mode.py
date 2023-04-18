def SetMode(self, option):
    self.option_label.setVisible(option)
    self.checkbox.setVisible(option)
    self.select_second_button.setVisible(option)
    self.read_button.setVisible(option)
    self.label2.setVisible(option)
    self.msg = ""
    self.copy.setVisible(option)
    if option == False:
        self.input_label.setVisible(True)
        self.input.setVisible(True)
        self.hide_button.setVisible(True)
        self.label_msg.setVisible(True)
        self.input_msg.setVisible(True)
        self.input_msg.setVisible(True)
        self.label_msg.setVisible(True)
    else:
        self.input_label.setVisible(False)
        self.input.setVisible(False)
        self.hide_button.setVisible(False)
        self.label_msg.setVisible(False)
        self.input_msg.setVisible(False)
        self.input_msg.setVisible(False)
        self.label_msg.setVisible(False)
    self.input_label_warning.setVisible(False)  # for both modes
    self.label_msg_warning.setVisible(False)  # for both modes
