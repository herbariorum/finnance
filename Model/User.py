from enum import unique
from peewee import *
from Database.BaseModel import BaseModel


class Usuarios(BaseModel):
    id = AutoField()
    nome = CharField(max_length=80)
    nick = CharField()
    email = CharField(unique=True)
    senha = CharField()
    criadoem = DateField()
