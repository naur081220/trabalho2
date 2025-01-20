from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from database import Base

class Roupa(Base):
    __tablename__ = 'roupas'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tamanho = Column(String)
    cor = Column(String)
    preco = Column(Float)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"))
    fornecedor = relationship("Fornecedor", back_populates="roupas")

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    telefone = Column(String)
    email = Column(String)
    cidade = Column(String)
    roupas = relationship("Roupa", back_populates="fornecedor")

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    cpf = Column(String, unique=True)
    telefone = Column(String)
    data_nascimento = Column(Date)
    pedidos = relationship("Pedido", back_populates="cliente")

class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    status = Column(String)
    valor_total = Column(Float)
    cliente = relationship("Cliente", back_populates="pedidos")
    itens_pedido = relationship("ItensPedido", back_populates="pedido")

class ItensPedido(Base):
    __tablename__ = 'itens_pedido'
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    roupa_id = Column(Integer, ForeignKey("roupas.id"))
    quantidade = Column(Integer)
    preco_unitario = Column(Float)
    pedido = relationship("Pedido", back_populates="itens_pedido")
    roupa = relationship("Roupa")