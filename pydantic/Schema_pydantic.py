##schema pydantic.

##exemplo:

from pydantic import BaseModel, Field 

class OrdemCreate(BaseModel):

    cliente : str 

    descricao : str 

    valor : float  = Field (gt=0)
###esse schema responde:

# quais dados eu aceito na criacao de uma ordem

# se chegar:


{
    "cliente" : "Carlos",

    "descricao" "Troca de Memoria RAM E SSD"

    "valor": 490
}

# O pydantic valida esses dados.

# ele nao cria a tabela no POSTGRESQL

# ele nao salva nada no banco.

# ele cuida principalmente do contrato e validação de dados



#MODEL SQLALCHEMY

#agora imagine:

from sqlalchemy.orm import Declarative, Mapped, mapped_column
from sqlalchemy import String

class Base(DeclarativeBase): # percebemos que estamos criando uma classe de nome generico Base, que recebe o parametro DeclarativeBase 
    pass # nao faça nada


class Ordem(Base):

    __table__name = "Ordens" # criando o nome da tabela como Ordens


    id: Mapped[int] = mapped_column(primary_key = True) # estamos criando um id com chave primaria 


    cliente: Mapped[str] = mapped_column(String(100)) # estamos criando um cliente que recebe até 100 caracteres.


    valor: Mapped[float]

##esse codigo esta preocupado com o banco de dados

# aqui aparecem conceitos como:

__tablename__
primary_key
String(100)
mapped_column
Mapped # Mapeada ?

#isso responde perguntas diferentes:

qual tabela?
qual coluna?
qual primary Key ?
qual tipo de coluna ?
qual relacionamento ?
qual constraint ?


# comparando lado a lado

#Pydantic

class OrdemCreate(BaseModel): #classe 
    cliente: str #dados da API 
    descricao: str #dados da API 
    valor: float #dados da API 

#representa:
#dados da API 


#SQLALCHEMY

class Ordem(Base):
    __tablename__ = "ordens"

    id: Mapped[int] = mapped_column( #ID nomeado/MAPPEADA como chave primaria, mapeado como um numero inteiro: 1,2,3,4,5,6
        primary_key=True
    )

    cliente: Mapped[str] # campo de formulario Cliente, mapeado como string, ex: "Andre"

    descricao: Mapped[str] # campo  de formulario descricao, mapeado como String , ex: "Computador Lento"

    valor: Mapped[float] # campo  de formulario valor, mapeado como float, valores quebrados 3,14



#representa:


#registro/tabela no banco

entao:

[Pydantic]                | SQL ALCHEMY
API                       |Banco de dados
valida dados              | persiste dados
request                   | tabela
Response                  | coluna
BaseModel                 | DeclarativeBase
Field()                   |mapped_column
Contrato da API           |Mapeamento ORM 


#para anotar:

pydantic schema
↓
Validacao e contrato da API

exemplos:
OrdemCreate
OrdemUpdate
OrdemResponse

SQLALCHEMY MODEL 
↓
REPRESENTACAO E PERSISTENCIA NO BaseExceptionGroup
EXEMPLO:
Ordem
Usuario
Cliente 

frase importante:

SCHEMA: Representa os dados que  atravessam   a fronteira da api.
MODELS: Representa a entidade persistida no banco de dados 


## ordem é um objeto Pydantic

# voce pode fazer:

# print(ordem.cliente)
# resultado:

Carlos

#mas isso ainda nao é um objeto SQLALchemy

#Imagine:

class Ordem(Base):
    __tablename__ = "ordens"


    id: Mapped[int] = mapped_column(primary_key=True)
    cliente: Mapped[str]
    descricao: Mapped[str]
    valor: Mapped[float]

#O SQLAlchemy conhece:
Ordem

#como entidade ligada á tabela: 
ordens

# mas ele nao conhece OrdemCreate como uma entidade do banco


#entao isto:

session.add(ordem)

#nao é o fluxo correto se ordem é uma instancia pydantic


# 3. entao entra o model_dump()

#temos:
Ordem
# que é aproximadamente

OrdemCreate(
    cliente="carlinhos feijoada",
    descricao="Troca de memoria ram e processador",
    valor = 540
)

#agora fazemos:
dados = ordem.model_dump()
# pegue os atributos deste objeto pydantic e me entregue como um dicionário Python

#entao 

#O objeto dados vira

{
    "cliente": "Carlinhos Chupa Manga",
    "descricao": "Troca de SSD",
    "valor": 350
}

#perceba a mudança:

#ordem
#= objeto Pydantic
#= dados que chegaram pela API e foram validados


#ordem.model_dump()
#= pega os dados do objeto Pydantic
#= retorna um dict


#**dados
#= desempacota o dict
#= transforma chaves em argumentos nomeados


#Ordem(**dados)
#= cria uma instância do Model SQLAlchemy


#ordem_db
#= objeto SQLAlchemy
#= objeto que poderá ser salvo no banco


#9. código passo a passo, sem atalhos
#eu começaria aprendendo assim:

@app.post("/ordens")
def criar_ordem(ordem: OrdemCreate)#criando um objeto chamado ordem, que recbee como parametro OrdemCreate ( PYDANTIC ).


    ordem_db = Ordem( # criação de um objeto chamado ordem_db que recebe Ordem 
        cliente=ordem.cliente,
        descricao=ordem.descricao,
        valor=ordem.valor

    )

    return ordem_db
#aqui fica extremamente claro:

ordem.cliente
    ↓
vai para 
    ↓
ordem_db.cliente

#depois ique isso estiver natural, voce reduz:
ordem.cliente
#significa:

#o objeto ordem acessando o atributo cliente.

#Então o ponto . serve para acessar coisas que pertencem ao objeto, como atributos e métodos.

#objeto = OrdemCreate().

#objeto.OrdemCreate
#“Acesse alguma coisa que pertence ou está disponível nesse objeto.”


pessoa.nome

significa
#Pegue o atributo nome do objeto pessoa.
#resultado:
#Carlos


#exemplo 2: mais de um atributo

class Carro:
    def __init__(self, marca,modelo):
        self.marca = marca
        self.modelo = modelo


carro = Carro("Toyota", "Corolla")

# agora podemos acessar:

#carro.marca 

Carro = Classe 
marca = atributo da classe 

#Exemplo 4: FastAPI

#Agora olha uma linha que você já vê bastante:

app.get("/ordens")

#Lembra?

app = FastAPI()

#app é um objeto.

#Então:

#app.get

#significa:

#acesse get que está disponível no objeto app.

#exemplo 5. SQLALCHEMY

#mais para frente você vê

#session.add(ordem_db)

#session
#↓
#objeto

#.
#↓
#acesse algo pertencente/disponível nesse objeto

#add
#↓
#método

#(ordem_db)
#↓
#argumento passado para o método

#então:

session.add(ordem_db)

#Pode ser lido como:

# use o metodo add do objeto session e passe ordem_db para ele

class Repository:
    def salvar(self, ordem):
        print("Ordem salva:", ordem)


class Service:
    def __init__(self):
        self.repository = Repository()



#criamos o objeto:

services = Service()

#nesse momento, mentalmente temos:

service
    |
    |_____repository
        |
        |______objeto Repository

#então:

service.Repository
#significa:

#pegue o repository que está dentro do objeto service

# acesse o self.repository que está dentro do objeto service.

# esse resulltado é um objeto Repository.

### se guardar só uma frase, guarde esta:

Cada (.) significa "entra/acessa o proximo nivel desse objeto"