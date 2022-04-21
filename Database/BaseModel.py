from peewee import *

# db = PostgresqlDatabase('finance', user='postgres', password='bot901', host='localhost', port=5432)
db = SqliteDatabase('finance.db')


class BaseModel(Model):
    class Meta:
        database = db
