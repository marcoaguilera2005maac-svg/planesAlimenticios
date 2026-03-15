from PyQt6 import QtWidgets
class LoginController:
    def __init__(self, window, model=None):
        self.window = window
        self.model = model
        self.window.btn_login.clicked.connect(self.handle_login)

    def handle_login(self):
        user = self.window.text_username.text()
        pas = self.window.txt_password.text()
        if user == "nutriologo" and pas == "12345":
            self.window.login_successfull.emit()
            print("Login correcto")
        else:
            QtWidgets.QMessageBox.warning(self.window, "Error", "Usuario o contraseña incorrectos")