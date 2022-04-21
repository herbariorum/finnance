from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import qtawesome as qta

from libs.uteis import Uteis
import Controller.LoginController as loginController
import sys


class Login(QWidget):
    global logou

    logou = False

    def __init__(self):
        super().__init__()
        self.tentativas = 0
        self.initUI()

    def initUI(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setFixedSize(300, 500)
        self.setWindowTitle('Login')
        self.setAutoFillBackground(True)
        self.setObjectName(u'formulario')
        appIcon = QIcon(u'static/img/logo.png')
        self.setWindowIcon(appIcon)

        self.centralizarJanela()

        self.btnIconClose = QPushButton(self.tr('X'), self)
        self.btnIconClose.setAttribute(Qt.WA_TranslucentBackground)
        self.btnIconClose.setObjectName(u'close')
        self.btnIconClose.move(270, 5)
        self.btnIconClose.setFixedWidth(25)
        self.btnIconClose.clicked.connect(self.fecharJanela)

        self.lblLogo = QLabel(self)
        self.lblLogo.move(86, 70)
        self.iconLogo = qta.icon('fa.user-circle', color='black')
        self.lblLogo.setPixmap(self.iconLogo.pixmap(QSize(128, 128)))

        self.txtUsuario = QLineEdit(self)
        self.txtUsuario.setObjectName(u'usuario')
        self.txtUsuario.setAlignment(Qt.AlignCenter)
        self.txtUsuario.setGeometry(24, 250, 250, 25)
        self.txtUsuario.setPlaceholderText(u'Entre com o Email')

        self.txtPassword = QLineEdit(self)
        self.txtPassword.setObjectName(u'password')
        self.txtPassword.setAlignment(Qt.AlignCenter)
        self.txtPassword.setGeometry(25, 310, 250, 24)
        self.txtPassword.setPlaceholderText(u'Entre com a Senha')
        self.txtPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.btnLogar = QPushButton(self.tr('Verificar'), self)
        self.btnLogar.setFixedWidth(70)
        self.btnLogar.setObjectName(u'button_logar')
        self.btnLogar.move(117, 390)
        self.btnLogar.clicked.connect(
            lambda x: self.verificar_login(self.txtUsuario.text(), self.txtPassword.text())
        )

        self.linkCadastro = QLabel(self)
        self.linkCadastro.setObjectName(u'link')
        self.linkCadastro.setText(
            '''<a style=text-decoration:none; href='http://google.com'>Solicitar senha</a>'''
        )
        self.linkCadastro.setOpenExternalLinks(True)
        self.linkCadastro.move(25, 340)

    def centralizarJanela(self):
        minhaJanela = QScreen.availableGeometry(QApplication.primaryScreen()).center()
        geo = self.frameGeometry()
        geo.moveCenter(minhaJanela)
        self.move(geo.topLeft())

    def fecharJanela(self):
        info = QMessageBox.question(
            self,
            'Confirmaçao',
            'Voce realmente deseja sair do apliativo?',
            QMessageBox.Yes | QMessageBox.No,
        )
        if info == QMessageBox.Yes:
            self.close()

    def verificar_login(self, usuario, password):
        global tentativas, logou

        if not Uteis.is_not_blank(usuario) or not Uteis.check(usuario):
            QMessageBox.about(self, 'Aviso', 'Digite um email válido')
            self.txtUsuario.setFocus()
            return
        if not Uteis.is_not_blank(password) or len(password) < 6:
            QMessageBox.about(self, 'Aviso', 'A senha deve conter no mínimo 6 digitos')
            self.txtPassword.setFocus()
            return
        if loginController.validar_usuario(usuario, password):
            logou = True
            self.close()
        else:
            if self.tentativas < 3:
                QMessageBox.about(self, 'Aviso', 'Login ou senha incorretos')
                self.tentativas += 1
                if self.tentativas == 3:
                    sys.exit(0)


def executa():
    global logou

    try:
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)

        with open('static/css/login.css', 'r') as f:
            style = f.read()
            app.setStyleSheet(style)

        janela = Login()
        janela.show()

        app.exec()
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Fechando Janela...")
    except Exception:
        print(sys.exc_info()[1])
    finally:
        return logou
