import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import (
    QScreen,
    QIcon,
    QFont, QPixmap,
    QRegularExpressionValidator, QStandardItemModel, QStandardItem
)
from PySide6.QtCore import QSize, Qt, QRegularExpression

from validate_docbr import CPF
import qtawesome as qta


class Dashboard(QWidget):
    def __init__(self):
        super(Dashboard, self).__init__()

        self.initUI()

    
    def initUI(self):
        self.setWindowTitle(f"SysFinan")
        self.setWindowFlag(Qt.FramelessWindowHint)
        screenzise = QScreen.availableGeometry(QApplication.primaryScreen())
        self.setGeometry(screenzise)
        self.setAutoFillBackground(True)
        self.setObjectName(u'dashboard')

        appIcon = QIcon(u'static/img/logo.png')
        self.setWindowIcon(appIcon)

        iconAluno = qta.icon('fa.user', color='black')
        iconPais = qta.icon('ei.adult', color='black')

        vbox = QVBoxLayout(self)
        vbox.setSpacing(0)
        vbox.setContentsMargins(0, 0, 0, 0)

        # barra do topo
        frameTop = QFrame(self)
        hbox = QHBoxLayout(frameTop)
        hbox.setSpacing(0)
        hbox.setContentsMargins(0, 0, 0, 0)

        # exibe o logo
        self.lblLogo = QLabel()
        self.lblLogo.setMinimumSize(QSize(32,32))
        self.lblLogo.setMaximumSize(QSize(32, 32))
        lblPix = QPixmap(u'static/img/logo.png')
        self.lblLogo.setPixmap(lblPix)
        self.lblLogo.setScaledContents(True)        
        hbox.addWidget(self.lblLogo)
        
        self.lblLogoText = QLabel(u'DASHBOARD')
        self.lblLogoText.setMinimumSize(QSize(0, 30))
        self.lblLogoText.setMaximumSize(QSize(200, 30))
        hbox.addWidget(self.lblLogoText)
        
        vbox.addWidget(frameTop)

        frameContent = QFrame(self)
        hbox = QHBoxLayout(frameContent)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)
        # adiciono o menu
        self.listMenu = QListView(frameContent)
        self.listMenu.setMaximumWidth(250)
        self.item = QStandardItemModel()
        self.listMenu.setSpacing(0)

        item1 = QStandardItem(iconAluno, 'Matricula')
        item2 = QStandardItem(iconPais, 'Responsável')
        
        self.item.appendRow(item1)
        self.item.appendRow(item2)
        self.listMenu.setModel(self.item) 

        hbox.addWidget(self.listMenu)

        # aciono o conteudo
        self.conteudo = QStackedWidget(frameContent)
        hbox.addWidget(self.conteudo)

        vbox.addWidget(frameContent)
        

def executa():
    try:
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        with open('static/css/dashboard.css', 'r') as f:
            style = f.read()
            app.setStyleSheet(style)

        janela = Dashboard()
        janela.show()

        app.exec()
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Fechando Janela...")
    except Exception:
        print(sys.exc_info()[1])