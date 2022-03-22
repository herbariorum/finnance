from Database.Dataset import Dataset as dataset
from Model.User import Usuarios as usuario
from Seguranca.Seguranca import validarSenha

# valida o usuario e senha fornecidos
def validarUsuario(login, senha):
    # faz a busca por email e retorna os registros, caso tenha sucesso
    localizaEmail = dataset.selectByEmail(usuario, login)
    
    # caso não encontre registros na busca
    if not localizaEmail:
        return False
    
    # faz a validação da senha
    seguranca = validarSenha(senha, localizaEmail.senha)
    if seguranca:
        return True
    return False
