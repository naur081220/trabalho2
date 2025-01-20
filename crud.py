from fastapi_crudrouter import SQLAlchemyCRUDRouter
from models import Roupa, Fornecedor, Cliente, Pedido, ItensPedido
from database import get_db
from pydantic import BaseModel
from datetime import date

class RoupaSchema(BaseModel):
    id: int
    nome: str
    tamanho: str
    cor: str
    preco: float
    fornecedor_id: int

    class Config:
        orm_mode = True

roupaRouter = SQLAlchemyCRUDRouter(
    schema=RoupaSchema,
    db_model=Roupa,
    db=get_db
)

class FornecedorSchema(BaseModel):
    id: int
    nome: str
    telefone: str
    email: str
    cidade: str

    class Config:
        orm_mode = True

fornecedorRouter = SQLAlchemyCRUDRouter(
    schema=FornecedorSchema,
    db_model=Fornecedor,
    db=get_db
)

class ClienteSchema(BaseModel):
    id: int
    nome: str
    cpf: str
    telefone: str
    data_nascimento: date

    class Config:
        orm_mode = True

clienteRouter = SQLAlchemyCRUDRouter(
    schema=ClienteSchema,
    db_model=Cliente,
    db=get_db
)

class PedidoSchema(BaseModel):
    id: int
    data: date
    cliente_id: int
    status: str
    valor_total: float

    class Config:
        orm_mode = True

pedidoRouter = SQLAlchemyCRUDRouter(
    schema=PedidoSchema,
    db_model=Pedido,
    db=get_db
)

class ItensPedidoSchema(BaseModel):
    id: int
    pedido_id: int
    roupa_id: int
    quantidade: int
    preco_unitario: float

    class Config:
        orm_mode = True

itensPedidoRouter = SQLAlchemyCRUDRouter(
    schema=ItensPedidoSchema,
    db_model=ItensPedido,
    db=get_db
)