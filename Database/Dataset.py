from peewee import DoesNotExist


class Dataset:
    # retorna todos os dados contidos na tabela
    @staticmethod
    def select(model):
        return model.select()

    # caso encontre o email, retorna Verdadeiro
    # se não encontrar, retorna Falso
    @staticmethod
    def selectByEmail(model, email):
        try:
            usuarios = model.select().where(model.email == email).get()
        except DoesNotExist:
            return False
        return usuarios