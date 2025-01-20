from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Roupa, Cliente, Fornecedor, Pedido, ItensPedido
from database import SessionLocal

# Conexão com o PostgreSQL
POSTGRES_DATABASE_URL = "postgresql+psycopg2://postgres:1005@localhost/dbmigration"
postgres_engine = create_engine(POSTGRES_DATABASE_URL)

# Copiar dados de SQLite para PostgreSQL
def migrate_data():
    sqlite_session = SessionLocal()
    postgres_session = sessionmaker(bind=postgres_engine)()

    roupas = sqlite_session.query(Roupa).all()
    for roupa in roupas:
        new_roupa = Roupa(id=roupa.id, nome= roupa.nome, tamanho=roupa.tamanho, cor = roupa.cor, preco = roupa.preco) 
        postgres_session.add(new_roupa)

    fornecedores = sqlite_session.query(Fornecedor).all()
    for fornecedor in fornecedores:
        new_fornecedor = Fornecedor(id=fornecedor.id, nome= fornecedor.nome, telefone=fornecedor.telefone, email = fornecedor.email, cidade = fornecedor.cidade) 
        postgres_session.add(new_fornecedor)

    clientes = sqlite_session.query(Cliente).all()
    for cliente in clientes:
        new_cliente = Cliente(id=cliente.id, nome= cliente.nome, cpf=cliente.cpf, telefone = cliente.telefone, data_nascimento = cliente.data_nascimento) 
        postgres_session.add(new_cliente)

    pedidos = sqlite_session.query(Pedido).all()
    for pedido in pedidos:
        new_pedido = Pedido(id=pedido.id, data= pedido.data, cliente_id= pedido.cliente_id, status = pedido.status, valor_total = pedido.valor_total) 
        postgres_session.add(new_pedido)        
   
    itensPedidos = sqlite_session.query(ItensPedido).all()
    for itenspedido in itensPedidos:
        new_itempedido = ItensPedido(id=itenspedido.id, pedido_id= itenspedido.pedido_id, roupa_id=itenspedido.roupa_id, quantidade = itenspedido.quantidade, preco_unitario = itenspedido.preco_unitario) 
        postgres_session.add(new_itempedido)    

    postgres_session.commit()

    sqlite_session.close()
    postgres_session.close()

if __name__ == "__main__":
    migrate_data()