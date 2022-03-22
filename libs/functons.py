from PySide6.QtGui import QPixmap, QIcon


def setImagem(iconNome, iconSize, iconState):
        icone = QIcon(iconNome)
        pixmap = icone.pixmap(iconSize, iconSize, iconState)
        return pixmap