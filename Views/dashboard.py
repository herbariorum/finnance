from PySide6.QtWidgets import *
from PySide6.QtGui import (
    QScreen,
    QIcon,
    QFont,
    QRegularExpressionValidator,
)
from PySide6.QtCore import QSize, Qt, QRegularExpression
import libs.functons as functons
from validate_docbr import CPF


import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        # configurações da janela
        # --------------------------------------- #
        self.setWindowTitle("SysFinan :: Dashboard")
        self.setWindowFlag(Qt.FramelessWindowHint)
        # self.setGeometry(50, 50, 1080, 680) # esquerda, topo, largura e altura
        # dimensiono a janela com o tamanho do desktop
        screensize = QScreen.availableGeometry(QApplication.primaryScreen())
        # print(screensize)
        self.setGeometry(screensize)

        self.setAutoFillBackground(True)
        self.setStyleSheet("background-color: #8b8378")

        appIcon = QIcon("icons/dollar-sign.png")
        self.setWindowIcon(appIcon)
        # --------------------------------------- #
        # conteudo da janela
        # --------------------------------------- #
        self.initUI()
        # --------------------------------------- #
        # exibe a janela
        self.show()

    def initUI(self):

        self.font8 = QFont("fonts/Roboto/Roboto-Bold", 8)
        self.font10 = QFont("fonts/Roboto/Roboto-Regular", 10, QFont.Bold)
        self.font10TXT = QFont("fonts/Roboto/Roboto-Light", 10)
        self.headerImg = QIcon("icons/brown/pie-chart.svg")
        self.iconHome = QIcon("icons/brown/home.svg")
        self.styleButton = """QPushButton {padding: 10px; border-radius: 5px; background-color: rgba(33, 43, 51, 100); color: white;}
                         QPushButton:hover {background-color: rgb(120, 157, 186);}
                      """

        self.styleLineEdit = """
                        QLineEdit {padding: 1px; border-style: solid; border: 2px solid #474747; border-radius: 8px;}
                        QLineEdit:hover, QLineEdit:focus {border: 2px solid #00aaaa; }
                       """

        # menu esquerdo
        barraMenu = QFrame(self)
        barraMenu.setGeometry(0, 0, 200, 736)

        # logo e texto do header
        headerMenu = QFrame(barraMenu)
        headerMenu.setGeometry(0, 0, 200, 50)
        headerMenu.setStyleSheet("color: white;background-color: #154650;")
        headerMenu.setFrameShape(QFrame.NoFrame)
        headerMenu.setFrameShadow(QFrame.Raised)
        # Imagem do header
        headerIcon = QLabel()
        headerIcon.setMinimumSize(QSize(32, 32))
        headerIcon.setMaximumSize(QSize(32, 32))
        headerIcon.setPixmap(
            functons.setImagem(self.headerImg, 32, QIcon.Active)
        )
        headerIcon.setScaledContents(True)
        # texto do header
        headerLabel = QLabel("DASHBOARD")
        headerLabel.setFont(self.font10)
        headerLabel.setMinimumSize(QSize(0, 30))
        headerLabel.setMaximumSize(QSize(16777215, 30))
        headerLabel.setAlignment(Qt.AlignCenter)

        # gerencia o layout do headerMenu
        headerHBox = QHBoxLayout(headerMenu)
        headerHBox.setSpacing(10)
        headerHBox.setContentsMargins(0, 9, 0, 9)
        headerHBox.addWidget(headerIcon)
        headerHBox.addWidget(headerLabel)

        # botoes do menu
        self.barraDePushbutton = QFrame(barraMenu)
        self.barraDePushbutton.setObjectName(u"buttons")
        self.barraDePushbutton.setFrameShape(QFrame.NoFrame)
        self.barraDePushbutton.setFrameShadow(QFrame.Raised)
        # self.barraDePushbutton.setStyleSheet("background-color: green")
        self.barraDePushbutton.setGeometry(0, 50, 200, 250)
        self.verticalLayout_1 = QVBoxLayout(self.barraDePushbutton)
        self.verticalLayout_1.setSpacing(0)
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)

        # home button
        self.buttonHome = QPushButton(self.barraDePushbutton)
        self.buttonHome.setObjectName(u"btnHome")
        self.buttonHome.setText(u"Início")
        self.buttonHome.setObjectName(u"btnInicio")
        self.buttonHome.setIcon(self.iconHome)
        self.buttonHome.setFlat(True)
        self.buttonHome.setStyleSheet(self.styleButton)
        self.buttonHome.clicked.connect(self.homepage)

        # matricula alunos
        self.buttonMatricula = QPushButton(self.barraDePushbutton)
        self.buttonMatricula.setObjectName(u"btnMatricula")
        self.buttonMatricula.setIcon(QIcon("icons/brown/user-plus.svg"))
        self.buttonMatricula.setText("Matrícula")
        self.buttonMatricula.setFlat(True)
        self.buttonMatricula.setStyleSheet(self.styleButton)
        self.buttonMatricula.clicked.connect(self.matriculapage)
        # cadastro pais
        self.buttonResponsavel = QPushButton(self.barraDePushbutton)
        self.buttonResponsavel.setText("Responsável")
        self.buttonResponsavel.setObjectName(u"btnResponsavel")
        self.buttonResponsavel.setIcon(QIcon("icons/brown/watch.svg"))
        self.buttonResponsavel.setFlat(True)
        self.buttonResponsavel.setStyleSheet(self.styleButton)
        # relatórios
        self.buttonRelatorio = QPushButton(self.barraDePushbutton)
        self.buttonRelatorio.setText("Relatório")
        self.buttonRelatorio.setObjectName(u"btnRelatorio")
        self.buttonRelatorio.setIcon(QIcon("icons/brown/file-text.svg"))
        self.buttonRelatorio.setFlat(True)
        self.buttonRelatorio.setStyleSheet(self.styleButton)

        # sair
        self.buttonFechar = QPushButton(self.barraDePushbutton)
        self.buttonFechar.setText("Sair do APP")
        self.buttonFechar.setObjectName(u"btnFechar")
        self.buttonFechar.setIcon(QIcon("icons/brown/power.svg"))
        self.buttonFechar.setFlat(True)
        self.buttonFechar.setStyleSheet(self.styleButton)
        self.buttonFechar.clicked.connect(self.sairDoApp)

        # adiciona os buttons ao layout
        self.verticalLayout_1.addWidget(self.buttonHome)
        self.verticalLayout_1.addWidget(self.buttonMatricula)
        self.verticalLayout_1.addWidget(self.buttonResponsavel)
        self.verticalLayout_1.addWidget(self.buttonRelatorio)
        self.verticalLayout_1.addWidget(self.buttonFechar)

        """ FRAME HOME"""
        # conteudo direito
        self.frmHome = QFrame(self)
        self.frmHome.setGeometry(200, 0, 1166, 736)
        """ FIM HOME"""

        """ FRAME DE CRUD DE MATRICULA"""
        # conteudo direito
        self.frmMatricula = QFrame(self)
        self.frmMatricula.setGeometry(200, 0, 1166, 736)
        self.frmMatricula.setStyleSheet("background-color: #eadce0;")
        self.frmMatricula.setVisible(False)

        """ FIM CRUD DE ALUNOS"""

        global meus_frames
        self.meus_frames = (self.frmHome, self.frmMatricula)

        # inicializa a visão principal
        self.homepage()

    def ocultarFrames(self):
        global meus_frames
        for f in self.meus_frames:
            if f.isVisible() == True:
                f.setVisible(False)

    # cria o formulario inicial
    def homepage(self):
        self.ocultarFrames()
        frase = u"Área de notificações"

        self.observactions = QTextEdit(self.frmHome)
        self.observactions.setText(
            """
            21.03.2022 - Sempre ao realizar a matricular do Aluno, faça antes o cadastro do(s) Responsável(is) pelo mesmo.
            """
        )
        self.observactions.setGeometry(20, 50, 1166, 736)
        self.observactions.setStyleSheet(
            "background-color: #eae480; color: white"
        )
        self.observactions.setReadOnly(True)

        self.criarHeader(frase, self.frmHome)
        self.frmHome.setVisible(True)

    # cria o formulario de matricula
    def matriculapage(self):
        self.ocultarFrames()
        frase = u"Área de Cadastro/Edição/Pesquisa de Matrícula de Alunos"

        self.nomeValidator = QRegularExpressionValidator(
            QRegularExpression(r"^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$")
        )
        self.emailValidator = QRegularExpressionValidator(
            QRegularExpression(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$")
        )
        self.lblNome = QLabel(u"Nome", self.frmMatricula)
        self.lblNome.setGeometry(20, 70, 55, 16)
        self.txtNome = QLineEdit(self.frmMatricula)
        self.txtNome.setGeometry(80, 70, 721, 22)  # left top largura altura
        self.txtNome.setStyleSheet("background: none")
        self.txtNome.setValidator(self.nomeValidator)

        self.lblNick = QLabel(u"Nick", self.frmMatricula)
        self.lblNick.setGeometry(20, 110, 55, 16)
        self.txtNick = QLineEdit(self.frmMatricula)
        self.txtNick.setGeometry(80, 110, 200, 22)
        self.txtNick.setStyleSheet("background: none")
        self.lblEmail = QLabel(u"Email", self.frmMatricula)
        self.lblEmail.setGeometry(20, 150, 55, 16)
        self.txtEmail = QLineEdit(self.frmMatricula)
        self.txtEmail.setGeometry(80, 150, 721, 22)
        self.txtEmail.setStyleSheet("background: none")
        self.txtEmail.setValidator(self.emailValidator)
        self.txtEmail.textChanged.connect(self._adjustText)

        self.criarHeader(frase, self.frmMatricula)
        self.frmMatricula.setVisible(True)

    def _adjustText(self):
        if not self.txtEmail.hasAcceptableInput():
            self.txtEmail.setStyleSheet("color: red; background: none;")
        else:
            self.txtEmail.setStyleSheet("color: black; background: none;")

    def criarHeader(self, frase, form):
        self.frmHeader = QFrame(form)
        self.frmHeader.setGeometry(0, 0, 1366, 50)
        self.frmHeader.setStyleSheet("background-color: #154650; color: white")
        self.frmHeader.setFont(self.font10TXT)

        self.lblIconMessage = QLabel(self.frmHeader)
        self.lblIconMessage.setMinimumSize(QSize(32, 32))
        self.lblIconMessage.setMaximumSize(QSize(32, 32))
        self.lblIconMessage.setPixmap(
            functons.setImagem(
                QIcon("icons/brown/message-square.svg"), 32, QIcon.Active
            )
        )
        self.lblIconMessage.setScaledContents(True)
        self.lblIconMessage.setGeometry(20, 10, 32, 32)

        self.lblHeader = QLabel(frase, self.frmHeader)
        self.lblHeader.setGeometry(80, 10, 721, 22)

    def sairDoApp(self):
        self.close()


def executa():
    myApp = QApplication.instance()
    if myApp is None:
        myApp = QApplication(sys.argv)

    janela = Window()
    janela.show()

    myApp.exec()


# executa()
