def ReadMessage(self, ERR_UPLOAD, solve, READ_MODE, Save):
    if(self.oi == False):
        self.handle_errors_and_text(self.label, ERR_UPLOAD)
        return
    if(self.si == False):
        self.handle_errors_and_text(self.label2, ERR_UPLOAD)
        return
    result = solve(READ_MODE, self.oimg, self.simg, "", "", "")
    Save(self, result)
    self.handle_errors_and_text(self.msg_output, result)
