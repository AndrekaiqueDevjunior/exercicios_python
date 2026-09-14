####'1. Primeiro: o que é Pydantic?

#Pydantic é uma biblioteca de validação e transformação de dados baseada principalmente nos Type Hints do Python. 
#Você define como os dados deveriam ser, e o Pydantic cria/valida uma instância que respeite essa estrutura.

from pydantic import BaseModel # importa a classe BaseModel da biblioteca pydantic 


class Ordem(BaseModel): # cria uma classe chamada Ordem que herda da classe BaseModel

    cliente: str # 
    valor : float #  



###aqui estamos dizendo:

## uma ordem precisa ter:

## cliente -> str

## valor -> float 


## 2. o que é base model 

## olha esta linha:

from pydantic import BaseModel

## base Model é uma classe do Pydantic


## e fazemos:

##class Ordem(BaseModel):

## aqui entra um conceito de POO que voce ja estudou: heranca


## a classe Ordem herda da classe BaseModel

## BaseModel
#   ↑
 #  │ herança
   #│
#
## Ordem


## ou seja:
## ordem é uma classe que herda funcionalidades do BaseModel.

## os modelos do Pydantic normalmentes sao classes que herdam de BaseModel e declaram seus campos usando atributos anotados com Type Hints.


# 5 . criando um objeto Pydantic

## lembra de poo ? = 

## podemos fazer:

## instancia de um objeto chamado ordem que recebe a classe OrdemCreate(

## que recebe argumentos como, cliente,descricao,valor.
#))


ordem = OrdemCreate(
    cliente="André",
    descricao="Manutencao do computador",
    valor=250
)

## 6. por que usar pydantic 

## por que os dados de uma API VEM DE FORa.

## o frontend pode mandar um JSON:

##{
##    "cliente": "André",
##    "descricao": "Manutencao do computador",
##    "valor": 250
##}

## mas também pode mandar coisa errada:

{
    "cliente": "Carlos",

    "descricao": "Troca de SSD",

    "Valor": "Batata"
}

## nos declaramos que Ordem Create recebe o typehint com o Float.

## entao o pydantic vai reclamar: 

## TypeError: value is not a valid float
##entao o pydantic tenta validar / converter os dados para que o objeto resultante respeite os tipos declarados:
## quando isso nao é possivel, ocorre um erro de validacao:

## por isso usamos o pydantic


## agora entra o FASTAPI


## aqui aonde as coisas começam a se conectar:

from fastapi import FastAPI #
from pydantic import BaseModel


##objeto app que recebe a classe FastAPI.

app = FastAPI()

class OrdemCreate(BaseModel):
    cliente: str
    descricao: str
    valor: float 


@app.post("/ordens")
def criar_ordem(ordem: OrdemCreate): # ordem: OrdemCreate. Estamos criando um objeto chamado ordem que recebe a classe OrdemCreate
    return ordem# estamos trazendo a classe OrdemCreate que possui como parametro o Base MODEL., que possui os atributos cliente, descricao e valor
# que serve para indicar que estamos criando um metodo de instancia que recebe um parametro ordem que recebe a classe OrdemCreate

#entao a function def criar_ordem recebe um parametro ordem que recebe a classe OrdemCreate que possui os atributos cliente, descricao e valor


#voce ja sabe que:

#def
#
#função


#criar_ordem
#
#nome da função

#ordem
#
#parâmetro 


#mas agora:

#ordem: OrdemCreate

#é muito importante.

# isso é um type Hint.

# só que o tipo não é :

#str
#int
#float

#o tipo agora é uma clase que nós criamos:
#OrdemCreate

#portanto:

#ordem: OrdemCreate

#Significa Aproximadamente:

#o parametro ordem deve seguir o Modelo OrdemCreate.

# 8 . FASTAPI entende que isso é Body.

# quando FASTAPI Vê um parâmetro tipado com um modelo Pydantic:


def criar_ordem(ordem: OrdemCreate):

#ele entende que os dados devem ser extraídos do Request Body e validadso de acordo com asquele modelo

# então o cliente manda:

POST /ordens

#BODY:

{
    "cliente": "Carlos",
    "descricao": "Troca de SSD",
    "Valor": 350.90
}

# o fluxo fica:

CLIENTE
   │
   │ POST /ordens
   │
   │ Body JSON
   ▼
FastAPI
   │
   ▼
OrdemCreate
   │
   ├── cliente precisa ser str
   ├── descricao precisa ser str
   └── valor precisa ser float
   │
   ▼
Pydantic valida
   │
   ▼
objeto OrdemCreate
   │
   ▼
criar_ordem(ordem)












## 5. criando um objeto Pydantic

## lembra de POO ? 


##podemos fazer:

ordem = OrdemCreate(
    cliente="Carlos",
    descricao="Troca de SSD",
    valor=350.90
)

## aqui

## ordemcreate
## ↓
## classe

# OrdemCreate(...)
##↓
##instancia a classe OrdemCreate


## ordem
## ↓
## variável que guarda o objeto


##9 e dentro da função 

## depois da validação, ordem é um objeto OrdemCreate


## entao podemos fazer:


def criar_ordem(ordem: OrdemCreate): # ordem: OrdemCreate. Estamos criando um objeto chamado ordem que recebe a classe OrdemCreate

   print(ordem.cliente) # acessando o atributo cliente do objeto ordem
   print(ordem.descricao) # acessando o atributo descricao do objeto ordem
   print(ordem.valor)  # acessando o atributo valor do objeto ordem

   return ordem # retornando o objeto ordem para o frontend (ou para o banco de dados) 

## perceba o :

ordem.cliente
## isso é POO  novamente.

#ordem
#↓
#objeto

#.

#cliente
#↓
#atributo


#assim como:

pessoa.nome

#agora temos:

ordem.cliente


#transformando em dicionário
#no pydantic atual, existe:


ordem.model_dump() # transformando em dicionário o objeto ordem 

## ele retorna os campos do modelo como um dict = dicionário


#Exemplo:

dados = ordem.model_dump() # transformando em dicionário o objeto ordem 
{
    "cliente": "André kaique ",
    "descricao": "Troca de Cooler",
    "valor": 250.00
}

## e lemhbra do **kwargs que acabamos de conversar ?

## é por isso que futuramente você verá:


dados = ordem.model_dump() # transformando em dicionário o objeto ordem 
ordem_db = Ordem(**dados) # criando um objeto Ordem com os dados do dicionário


## observe o ** dados

**dados

#desempacota o dicionário

# se :

dados = {
    "cliente": "André kaique ",
    "descricao": "Troca de Cooler",
    "valor": 250.00
}

##então:

Ordem(**dados) 

#é semelhante á criar um objeto tipo 
objeto = Ordem(
    cliente="André kaique ", 
    descricao="Troca de Cooler", 
    valor=250.00
    )


Ordem(
   cliente= "Carlos",
   valor = 350.90
)

##essa conexao vai ficar muito importante quando entrarmos em Pydantic+ SQLALCHEMY


##11. um detalhe muito importante: obrigatório x opcional

veja:

class OrdemCreate(BaseModel):
   cliente: str
   descricao: str
   valor: float

#os três sao obrigatorios.

#agora:

class Ordem(BaseModel):
   cliente: str
   descricao: str | None = None # o | None significa que o atributo descricao eh opcional
   valor: float

#aqui descricao : str | None = None

significa:

#descricao pode ser str ou None, e tem None como valor Padrão