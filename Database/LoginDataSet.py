from peewee import DoesNotExist


class LoginDataSet:

    @staticmethod
    def selectByEmail(model, email):
        try:
            usuario = model.select().where(model.email == email).get()
        except DoesNotExist:
            return False
        return usuario