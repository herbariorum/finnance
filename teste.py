# import bcrypt
#
# passwd = '123456'
#
# salt = bcrypt.gensalt()
# hashed = bcrypt.hashpw(passwd.encode('utf-8'), salt)
#
# print(salt)
# print(hashed.decode('utf-8'))

from libs.Seguranca import *
hashed = criarHash('123456')
print(hashed)
