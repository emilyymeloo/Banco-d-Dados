
import sqlite3
connection = sqlite3.connect("pizza_app.sqlite")
     
Executa uma instrução no SQL recebida como string


cursor.execute("INSERT INTO data VALUES ('queijo', 4.5);")
     
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
/tmp/ipykernel_10861/2823559680.py in <cell line: 0>()
----> 1 cursor.execute("INSERT INTO data VALUES ('queijo', 4.5);")

NameError: name 'cursor' is not defined
Coloca placeholders à string e preenche em parameters


execute(sql: str, parameters: tuple = ())
# exemplo com placeholders nomeados:
dic = ({'ing': 'queijo', 'preco': 4.5})
cursor.execute("INSERT INTO data VALUES(:ing, :preco)", dic)
     
Repete a execução dada com cada um dos parameters


executemany(sql: str, parameters: Sequence[tuple])
# exemplo com ? placeholders
rows = [("queijo", 4.5), ("azeitona", 1)]
cursor.executemany("INSERT INTO data VALUES(?, ?)", rows)
     
Executa scripts sql


executescript(sql_script: str)
# exemplo
cursor.executescript("""
    BEGIN;
    CREATE TABLE person(firstname, lastname, age);
    CREATE TABLE book(title, author, published);
    COMMIT;
""")
     
executa sql com tratamento de erros


from sqlite3 import Error

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)

        # commit necessário para alterações no banco
        connection.commit() ###

        print(f"Query executada.")
        if cursor.rowcount != -1:
            print(f"{cursor.rowcount} linha(s) afetadas")

    except Error as e:
        print(f"Erro: '{e}'")
     
Executa a query de cada tabela


# Cria a tabela produto #
create_produto_table = \
"""CREATE TABLE produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo VARCHAR(50),
    desc_item VARCHAR(100),
    vl_preco DECIMAL(10, 2)
);"""

execute_query(connection, create_produto_table)
#########################

# Cria a tabela pedido #
create_pedido_table = \
"""CREATE TABLE pedido (
    id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
    dt_pedido DATE,
    fl_ketchup BOOLEAN,
    desc_uf CHAR(2),
    txt_recado TEXT
);"""

execute_query(connection, create_pedido_table)
#########################

# Cria a tabela item_pedido #
create_item_pedido_table = \
"""CREATE TABLE item_pedido (
    id_pedido INT NOT NULL,
    id_produto INT NOT NULL,
    quantidade INT NOT NULL,
    PRIMARY KEY (id_pedido, id_produto),
    FOREIGN KEY (id_pedido) REFERENCES pedido(id_pedido),
    FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);"""
execute_query(connection, create_item_pedido_table)
#########################
     
Insere produtos manualmente


## Inserindo registros manualmente

# Inserindo produto #
insert_produto = \
"""INSERT INTO
produto (tipo, desc_item, vl_preco)
VALUES
('ingrediente', 'camarão', 6),
('massa', 'tradicional', 9.25),
('borda', 'tradicional', 0),
('queijo', 'muçarela', 4),
('bebida', 'refrigerante', 5);
"""
execute_query(connection, insert_produto)
######################

# Inserindo pedido
insert_pedido = \
"""INSERT INTO
pedido (dt_pedido, fl_ketchup, desc_uf, txt_recado)
VALUES
('2023-06-01', TRUE, 'MG', 'Capricha no queijo!');
"""
execute_query(connection, insert_pedido)
######################
     
Automatiza grande volume de alterações


# Inserindo item_pedido
itens = (
    {'id_pedido': 1, 'id_produto': 2, 'qtd': 1},
    {'id_pedido': 1, 'id_produto': 3, 'qtd': 1},
    {'id_pedido': 1, 'id_produto': 1, 'qtd': 1},
    {'id_pedido': 1, 'id_produto': 4, 'qtd': 2},
    {'id_pedido': 1, 'id_produto': 5, 'qtd': 3}
)

insert_item_pedido = \
"""INSERT INTO item_pedido (id_pedido, id_produto, quantidade)
VALUES(:id_pedido, :id_produto, :qtd);"""

cursor = connection.cursor()
cursor.executemany(insert_item_pedido, itens)
connection.commit() # necessário para inserções
cursor.close()
     
Retorna a próxima linha do resultado da consulta


fetchone() -> tuple
     
Retorna uma lista de tuplas com todas as linhas resultantes da consulta


fetchall() -> list[tuple]
     
Retorna o próximo conjunto de linhas da consulta, de acordo com parâmetro size


fetchmany(size: int = cur.arraysize) -> list[tuple]
     

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()

        return result
    except Error as e:
        print(f"Erro: '{e}'")
     

tabela = 'produto'
query = f"SELECT * FROM {tabela}"
resultado = execute_read_query(connection, query)

print(f"Tabela: {tabela}")
for res in resultado:
    print(res)
     
Tabela que armazena o esquema desse banco de dados


CREATE TABLE sqlite_schema(
  type text,
  name text,
  tbl_name text,
  rootpage integer,
  sql text
);
     
Cria uma query para ler o nome de todas as tabelas registradas no esquema


SELECT name FROM sqlite_schema WHERE type='table';
     

select_table_names = \
"SELECT name FROM sqlite_schema WHERE type='table';"
tables = execute_read_query(connection, select_table_names)
print(tables, '\n')

for table in tables:
    select_all = f"SELECT * FROM {table[0]}"
    res = execute_read_query(connection, select_all)
    print(f"{table[0]}: {res}")
     
Exclui todos os registros de todas as tabelas que criamos manualmente


execute_query(connection, "DELETE FROM item_pedido;")
execute_query(connection, "DELETE FROM pedido;")
execute_query(connection, "DELETE FROM produto;")
     
Baixa a versão modificada dos dados do Pizza Query.


! wget https://raw.githubusercontent.com/camilalaranjeira/python-intermediario/main/pizza_query/item_pedido.csv
! wget https://raw.githubusercontent.com/camilalaranjeira/python-intermediario/main/pizza_query/pedido.csv
! wget https://raw.githubusercontent.com/camilalaranjeira/python-intermediario/main/pizza_query/produto.csv
     
Cria tabelas parecidas com o excel


import pandas as pd
df_pedido = pd.read_csv(f'pedido.csv')
display(df_pedido.head())
     
Carrega tabelas em bancos sqlite


df.to_sql(table_name, connection, if_exists='fail', index=False)
     

cursor = connection.cursor()
cursor.execute(f"SELECT * FROM pedido WHERE id_pedido < 5;")
result = cursor.fetchall()
     

df_pedido.to_sql('pedido', connection, if_exists='append', index=False)

count_rows = "SELECT COUNT(id_pedido) as count_id FROM pedido;"
print(execute_read_query(connection, count_rows))

select_all = f"SELECT * FROM pedido WHERE id_pedido < 5;"
execute_read_query(connection, select_all)
     

con.connect();
con.query("SELECT * FROM customers WHERE address = 'Park Lane 38'",
         (err, result) => {
  if (err) throw err;
  console.log(result);
});
     

# df_pedido.to_sql('pedido', connection, if_exists='replace', index=False)
res = execute_read_query(connection, "SELECT sql FROM sqlite_schema")
for r in res:
    print(r[0])
     
Instala sqlmodel


!pip install sqlmodel
     

from datetime import datetime
from sqlmodel import (
    SQLModel, Field, Relationship,
    create_engine, Session, select
)

## Definição de classes/tabelas
class Equipe(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    pessoas: list["Pessoa"] = Relationship(back_populates="equipe")

class Pessoa(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    apelido: str
    data_nasc: datetime

    id_equipe: int | None = Field(default=None, foreign_key="equipe.id")
    equipe: Equipe | None = Relationship(back_populates="pessoas")

# Iniciando a conexão com o banco (SQLite)
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)

# Criando as tabelas
SQLModel.metadata.create_all(engine)

# Inserindo dados (isso estaria em uma função)
with Session(engine) as session:
    pessoa1 = Pessoa(nome="André Augusto", apelido="Melhor amigo",
                      data_nasc=datetime(2007, 2, 8))
    pessoa2 = Pessoa(nome="Gabriel Felipe", apelido="Tilipe",
                      data_nasc=datetime(2005, 10, 19))

    session.add(pessoa1)
    session.add(pessoa2)
    session.commit()

# Fazendo consultas
with Session(engine) as session:
    statement = select(Pessoa).where(Pessoa.apelido == "Tilipe")
    pessoa = session.exec(statement).first()
    print(pessoa.id, pessoa.nome)
     

df_pedido.to_sql('pedido', connection, if_exists='replace', index=False)
res = execute_read_query(connection, "SELECT sql FROM sqlite_schema")
for r in res:
    print(r[0])
     

query="""
SELECT desc_uf, COUNT(*) as count_pedidos
FROM pedido
GROUP BY desc_uf
ORDER BY count_pedidos DESC
LIMIT 5
"""
pd.read_sql_query(query, connection)
     
