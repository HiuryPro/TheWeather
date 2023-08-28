import datetime
from mongoengine import Document, fields, EmbeddedDocument
from django import forms
from django.utils import timezone
import django.utils


class Usuario(Document):
    nome = fields.StringField(max_length=100)
    email = fields.EmailField()
    password = fields.StringField(max_length=10)


class DadosMetereologicos(EmbeddedDocument):
    temperatura = fields.IntField()
    umidade = fields.DecimalField()


class Regiao(Document):
    regiao = fields.StringField(max_length=200)
    dados_metereologicos = fields.ListField(
        fields.EmbeddedDocumentField(DadosMetereologicos))
