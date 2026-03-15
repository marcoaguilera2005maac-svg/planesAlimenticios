import sys
from PyQt6 import QtWidgets,uic
from PyQt6.QtCore import pyqtSignal
<<<<<<< Updated upstream
from controller.login_controller import LoginController

class Login(QtWidgets.QDialog):
    login_successfull = pyqtSignal()
    def __init__ (self):
        super().__init__()
        uic.loadUi("./views/login.ui", self)
        self.controller = LoginController(self, None)

class Dashboard(QtWidgets.QMainWindow) :
    request_ficha = pyqtSignal()
    def __init__ (self):
        super().__init__()
        uic.loadUi("./views/dashboard.ui", self)
        self.btn_nuevo.clicked.connect(lambda: self.request_ficha.emit())

class Ficha(QtWidgets.QMainWindow):
    request_plan = pyqtSignal()
    def __init__ (self):
        super().__init__()
        uic.loadUi("./views/ficha.ui", self)
        self.btn_generar.clicked.connect(lambda : self.request_plan.emit())

class Plan(QtWidgets.QMainWindow):
    finalizado = pyqtSignal()
    def __init__ (self):
        super().__init__()
        uic.loadUi("./views/receta.ui", self)
        self.btn_finalizar.clicked.connect(lambda: self.finalizado.emit())

class AppManager:
    def __init__ (self):
        self.w_login = Login()
        self.w_dash = Dashboard()
        self.w_ficha = Ficha()
        self.w_plan = Plan()
        self.w_login.login_successfull.connect(self.ir_a_dash)
        self.w_dash.request_ficha.connect(self.ir_a_ficha)
        self.w_ficha.request_plan.connect(self.ir_a_plan)
        self.w_plan.finalizado.connect(self.ir_a_dash)

        self.w_login.show()

    def ir_a_dash(self):
        self.w_dash.show()
        self.w_login.close()
        self.w_plan.close()

    def ir_a_ficha(self):
        self.w_ficha.show()
        self.w_login.close()
        self.w_plan.close()

    def ir_a_plan(self):
        self.w_plan.show()
        self.w_ficha.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    manager = AppManager()
    sys.exit(app.exec())
=======
from controllers.login_controller import LoginController

>>>>>>> Stashed changes
