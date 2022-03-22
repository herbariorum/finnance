from socket import send_fds
import string
import bcrypt

def criarHash(senhaString):
    hash = bcrypt.hashpw(password=senhaString.encode('utf-8'), salt=bcrypt.gensalt)
    return hash.decode('utf-8')

def validarSenha(senhaString, senhaComHash):
    return bcrypt.checkpw(senhaString.encode('utf-8'), senhaComHash.encode('utf-8'))
