from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtSvgWidgets import *
from PySide6.QtSvg import *
import libs.functons as functons
import Controller.loginController as clogin

import sys


class Login(QWidget):
    global tentativas, logou
    tentativas = 0
    logou = False

    def __init__(self):
        super().__init__()
        # configurações da janela
        # --------------------------------------- #
        self.setWindowFlag(Qt.FramelessWindowHint)
        # dimensiono a janela com o tamanho do desktop
        self.setFixedSize(300, 500)  # fixa o tamanho da janela
        self.setWindowTitle("Login")
        # habilita pintar o blackground
        self.setAutoFillBackground(True)
        # pinta o blackground
        self.setStyleSheet("background-color: #ffffff; color: #505e6c")
        # self.setToolTip("Aplicativo de Finanças Personalizado")
        appIcon = QIcon("icons/dollar-sign.svg")
        self.setWindowIcon(appIcon)

        self.initUI()
        self.centralizarJanela()

    def initUI(self):
        global txtUsuario, txtPassword
        # font8 = 'font: 8pt Arial bold; color: #485976;'
        font8 = QFont("fonts/Roboto/Roboto-Bold", 8)
        # font12 = 'font: 10pt Arial; color: #000000;'
        font12 = QFont("fonts/Roboto/Roboto-Regular", 10, QFont.Bold)
        font12TXT = QFont("fonts/Roboto/Roboto-Light", 11)

        # botão fechar janela
        btnIconClose = QPushButton(self.tr('X'), self)
        btnIconClose.setObjectName("close")
        btnIconClose.move(270, 5)
        btnIconClose.setFixedWidth(25)
        btnIconClose.setStyleSheet(
            'color: #ffffff; background-color: #dc3545; border-color: #dc3545;'
        )
        btnIconClose.clicked.connect(self.fecharJanela)

        # cria o logotipo
        lblLogo = QLabel(self)
        lblLogo.move(81, 70)
        lblLogo.setPixmap(
            functons.setImagem("icons/user-139.svg", 139, QIcon.Active)
        )

        # cria o label e a caixa de texto de usuario
        lblUsuario = QLabel('Usuário', self)
        lblUsuario.move(25, 230)
        lblUsuario.setFont(font12)
        txtUsuario = QLineEdit(self)
        txtUsuario.setGeometry(25, 250, 250, 25)
        txtUsuario.setPlaceholderText('Email')
        txtUsuario.setFont(font12TXT)
        txtUsuario.setStyleSheet(
            'QLineEdit {padding: 1px; border-style: solid; border: 2px solid #474747; border-radius: 8px;}'
            + 'QLineEdit:hover, QLineEdit:focus {border: 2px solid #00aaaa; }'
        )
        # cria o label e a caixa de texto de senha
        lblPassword = QLabel('Senha', self)
        lblPassword.move(25, 290)
        lblPassword.setFont(font12)
        txtPassword = QLineEdit(self)
        txtPassword.setGeometry(25, 310, 250, 25)
        txtPassword.setPlaceholderText('Senha')
        txtPassword.setEchoMode(QLineEdit.EchoMode.Password)
        txtPassword.setFont(font12TXT)
        txtPassword.setStyleSheet(
            'QLineEdit {padding: 1px; border-style: solid; border: 2px solid #474747; border-radius: 8px;}'
            + 'QLineEdit:hover, QLineEdit:focus {border: 2px solid #00aaaa; }'
        )

        # cria o botão para logar
        btnLogar = QPushButton(self.tr('&Verificar'), self)
        btnLogar.setDefault(True)
        btnLogar.setFixedWidth(70)
        btnLogar.move(117, 390)
        btnLogar.setObjectName(u"verificar")
        btnLogar.setStyleSheet(
            'QPushButton {color: #fff; background-color: #102940; text-align: center;'
            + 'border-color: #102940; min-height: 25px;'
            + 'min-width: 70px; padding: 0 6px 0 6px; border-radius: 4px;}'
            + 'QPushButton:hover {color: #fff; background-color: #397E95; border-color: #397E95;} '
            + 'QPushButton:pressed {border: 3px solid #102940;}'
        )
        btnLogar.clicked.connect(
            lambda x: self.validar_login(txtUsuario.text(), txtPassword.text())
        )

        # link para cadastro
        linkCadastro = QLabel(self)
        linkCadastro.setText(
            '''<a href='http://google.com'>Solicitar senha</a>'''
        )
        linkCadastro.setOpenExternalLinks(True)
        linkCadastro.move(25, 340)
        linkCadastro.setFont(font8)

        # cria label de copyright
        lblCopyright = QLabel(self.tr('@Elias Gomes - 2021'), self)
        lblCopyright.move(90, 470)
        lblCopyright.setFont(font8)
        lblCopyright.setStyleSheet("color: #485976;")
        lblContato = QLabel(self.tr('Contato: (63)991111196'), self)
        lblContato.move(85, 485)
        lblContato.setFont(font8)
        lblContato.setStyleSheet("color: #485976;")

    def validar_login(self, email, senha):
        global tentativas, logou
        global txtUsuario, txtPassword
       
        if (self.is_not_blank(email)) == False:
            txtUsuario.setFocus()
            return
        if (self.is_not_blank(senha)) == False or len(senha) < 6:
            msg = QMessageBox()
            msg.setText('A senha deve ter no mínimo 6 digitos')
            msg.exec()
            txtPassword.setFocus()
            return

        if clogin.validarUsuario(email, senha):
            logou = True
            self.close()
        else:
            if tentativas < 3:
                msg = QMessageBox()
                msg.setText('Login ou senha incorretos')
                msg.exec()
                tentativas += 1
                if tentativas == 3:
                    sys.exit(0)

    def fecharJanela(self):
        info = QMessageBox.question(
            self,
            'Confirmação',
            'Você realmente deseja sair do aplicativo?',
            QMessageBox.Yes | QMessageBox.No,
        )
        if info == QMessageBox.Yes:
            self.close()

    def centralizarJanela(self):
        minhaJanela = QScreen.availableGeometry(
            QApplication.primaryScreen()
        ).center()  # 0, 32, 1366, 736
        geo = self.frameGeometry()  # 0, 0, 400, 600
        geo.moveCenter(minhaJanela)
        self.move(geo.topLeft())  # move para o centro da tela

    def is_not_blank(self, s):
        return bool(s and not s.isspace())


def executa():
    global logou

    myApp = QApplication.instance()
    if myApp is None:
        myApp = QApplication(sys.argv)

    # with open('css/login.qss', 'r') as f:
    #     style = f.read()
    #     myApp.setStyleSheet(style)

    janela = Login()
    janela.show()

    myApp.exec()

    return logou
