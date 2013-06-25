from unicodedata import normalize

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

class Nome(Base):
    __tablename__ = 'nomes'

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    nome_normalizado = Column(String, index=True) # nome sem acentos, todo em caixa baixa
    nome_invertido = Column(String, index=True)   # normalizado inverido (reversed)
    genero_masculino = Column(Float, index=True, default=0)
    genero_feminino = Column(Float, index=True, default=0)
    genero_ambos = Column(Float, index=True, default=0)   # nomes unisex, ex: Darcy
    conhece_zero = Column(Integer, index=True, default=0) # pessoas que não conhecem ninguém com este nome
    conhece_uma = Column(Integer, index=True, default=0)  # pessoas que conhecem uma pessoa com este nome
    conhece_mais = Column(Integer, index=True, default=0) # pessoas que conhecem mais de uma pessoa com este nome

    def __init__(self, nome):
        self.nome = nome
        self.normalizar()

    def normalizar(self):
        sem_acentos = normalize('NFKD', self.nome).encode('ASCII', 'ignore').decode('ASCII')
        self.nome_normalizado = sem_acentos.lower()
        self.nome_invertido = self.nome_normalizado[::-1]

