from Database.LoginDataSet import LoginDataSet
from Entities.User import User
from libs.Seguranca import validarPassword


def validar_usuario(usuario, password):
    localizaEmail = LoginDataSet.selectByEmail(User, usuario)

    if not localizaEmail:
        return False

    seguranca = validarPassword(password, localizaEmail.password)
    if seguranca:
        return True
    return False



