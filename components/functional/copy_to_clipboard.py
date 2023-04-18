import pyperclip  # copy to clipboard


def CopyToClipboard(self):
    text = self.msg_output.text().replace('\x00', '')
    pyperclip.copy(text)
