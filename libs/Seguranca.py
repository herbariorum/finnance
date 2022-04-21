import bcrypt


def criarHash(senhaString):
    hash = bcrypt.hashpw(password=senhaString.encode('utf-8'), salt=bcrypt.gensalt())
    return hash.decode('utf-8')


def validarPassword(senhaString, senhaComHash):
    return bcrypt.checkpw(senhaString.encode('utf-8'), senhaComHash.encode('utf-8'))