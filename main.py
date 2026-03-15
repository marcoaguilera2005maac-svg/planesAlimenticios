import sys
from PyQt6 import QWidgets, uic
from PyQt6.QtCore import pyqtSignal
from controllers.login_controller import LoginController
class login(QtWidgets.QMainWindow):
    login_successfull = pyqtSignal()
    def init (self):
        super(). init()
        uic.loadUI("./Views/login.ui" , self)
        self.controller = LoginController(self, None)
class Dashboard(QtWidgets.QMainWindo) :
    request_ficha = pyqtSignal()
    def init (self):
        super().innit ()
        uic.loadUI("./views/dashboard.ui" , self)
        #Boton para ir a la ficha(objectname:btn_nuevo)
        self.btn_nuevo.clicked.connect(lambda: self.request_ficha.emit())
class Ficha(Qtwidgets.QMainWindow):
    request_plan = pyqtSignal()
    def innit (self):
        super().innit()
        uic.loadUI("./views/ficha.ui",self)
        #boton para el plan (objectName:btn_generar)
        self.btn_generar.clicked.connect(lambda : self.request_plan.emit())
class plan(Qtwidgets.QMainWindow):
    finalizado = pyqtSignal()
    def innit (self):
        super(). innit ()
        uic.loadUi("./views/receta.ui",self)
        self.btn_finalizar.clicked.connect(lambda: self.finalizado.emit())
#administrador de la app
class AppManager:
    def innit (self):
        self.w_login= Login()
        self.w_dash = Dashboard()
        self.w_ficha = Ficha()
        self.w_plan = Plan ()
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
        self.w_dash.show()
        self.w_login.close()
        self.w_plan.close()

    def ir_a_plan(self):
        self.w_plan.show()
        self.w_ficha.close()

if name == "main":
    app = Qtwidgets.QApplication(sys.argv)
    manager = AppManager()
    sys.exit(app.exec())