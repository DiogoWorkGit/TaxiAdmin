from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = "USERS"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    EMAIL = db.Column(db.String(120), unique=True, nullable=False)
    SENHA = db.Column(db.String(100), nullable=False)
    CARGO = db.Column(db.String(50))
    TOKEN_VALIDACAO = db.Column(db.String(25))
    TOKEN_EXPIRA = db.Column(db.DateTime)
    CONTA_ATIVA = db.Column(db.Boolean, default=False)
    ULTIMO_LOGIN = db.Column(db.DateTime)
    TENTATIVAS_LOGIN = db.Column(db.Integer, default=0)
    USER_ATIVO = db.Column(db.Boolean, default=True)
    DT_CRIACAO = db.Column(db.DateTime, default=lambda: datetime.now(datetime.UTC))
    DT_ATUALIZACAO = db.Column(db.DateTime, default=lambda: datetime.now(datetime.UTC), onupdate=lambda: datetime.now(datetime.UTC))

    corridas = db.relationship('Corridas', backref='user', lazy=True)

    def __repr__(self):
        return '<Users %r>' % self.ID


class Corridas(db.Model):
    __tablename__ = "CORRIDAS"

    ID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    USER_ID = db.Column(db.Integer, db.ForeignKey('USERS.ID'), nullable=False)
    END_ORIGEM = db.Column(db.String(255))
    END_DESTINO = db.Column(db.String(255))
    DT_EMBARQUE = db.Column(db.DateTime)
    DT_DESEMBARQUE = db.Column(db.DateTime)
    DISTANCIA_KM = db.Column(db.Float)
    VALOR_VIAGEM = db.Column(db.Float)
    NOME_CLIENTE = db.Column(db.String(255))
    OBS = db.Column(db.Text)
    TIPO = db.Column(db.String(255))
    DT_CRIACAO = db.Column(db.DateTime, default=lambda: datetime.now(datetime.UTC))

    def __repr__(self):
        return '<Corridas %r>' % self.ID
