import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import (
    QScreen,
    QIcon,
    QFont,
    QRegularExpressionValidator,
)
from PySide6.QtCore import QSize, Qt, QRegularExpression

from validate_docbr import CPF


class Dashboard(QWidget):
    def __init__(self):
        super(Dashboard, self).__init__()


def executa():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)

    janela = Dashboard()
    janela.show()

    app.exec()

