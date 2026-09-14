#SCHEMAS SEPARADOS
# CREATE
#UPDATE
#RESPONSE
from pydantic import field, BaseModel
class Ordem(BaseModel):

    id: int
    cliente: str
    descricao: str
    valor: float
    status: str


#ordem create

#serve para os dados necessários na criação.
from pydantic import BaseModel, Field

class OrdemCreate(BaseModel):
    cliente: str = Field(min_length=3, max_length=100)

    descrição: str = Field(min_lenght=5)

    valor: float = Field(gt=0)


#então:

#OrdemCreate
#↓
#o que o usuário pode/deve mandar ao criar

#rota:

@app.post("/ordens")
def criar_ordem(ordem: OrdemCreate): # ordem: OrdemCreate. Estamos criando um objeto chamado ordem que recebe a classe OrdemCreate
    return ordem

#3. ordemUpdate

class OrdemCreate(BaseModel):
    cliente: str 

    descricao: str 

    valor: float 

    #ele exigiria todoso s campos

    ## isso é ruim para um PATCH

    ## entao criamos:


class OrdemUpdate(BaseModel):
    cliente: str | None = None# | None significa que o campo pode ser nulo isso é bom pra patch pois pode atualizar PARCIALMENTE 

    descricao: str | None = None # | None significa que o campo pode ser nulo

    valor: float | None = Field(default=None, gt=0) # | None significa que o campo pode ser nulo

#agora todos sao opcionais

#voce pode mandar:

{
    "valor": 450
}

#valor
#↓
#campo

#float | None
#↓
#pode ser float OU None

#= None
#↓
#se não vier, o padrão é None


# ordem.model_dump(exclude_unset=True) .

#model_dump() gera uma representação em dicionário do modelo Pydantic.

#E:

#para que serve exclude_unset=True 

#exclude_unset=True
#↓
#exclui o campo se ele for nulo
#serve para trabalhar apenas com campos efetivamente enviados na atualização,
#  um padrão mostrado pela própria documentação do FastAPI para updates parciais.


#exemplo: 
dados = ordem.model_dump(exclude_unset=True)

 #se chegou

{
    "valor": 450
}
dados fica aproximadamente assim:

{
    "valor": 450

}

#em vez de: 


{
    "cliente": None,
    "descricao": None,
    "valor": 450
}

#isso é importantíssimo


#5.OrdemResponse

#agora temos outra situação:

# o que a API pode DEVOLVER ? 

#podemos criar:

class OrdemResponse(BaseModel):

    id: int 
    cliente: str
    descricao: str
    valor: float
    status: str
#
# 
# observe: id : int
# existe no Response, mas nao precisav existir no Create.
# 
# 
# #entao:
# 
# CREATE:
# cliente
# descricao
# valor
# 
# RESPONSE:
# id
# cliente
# descricao
# valor
# status 


# USANDO O RESPONSE_MODEL

# NO FASTAPI:
@app.post(/"ordens", response_model=OrdemResponse)

def criar_ordem(ordem: OrdemCreate): 
    ...

## esse trecho

response_model=OrdemResponse
#significa: A resposta desse endpoint deve seguir o formato de dados de OrdemResponse

#o FastAPI usa response_model para:
#  documentação, validação, serialização e também para fdiltrar a saide ocnforme o modelo declarado


# temos: 


#@app.post
#↓
#metodo HTTP


#"/ordens"
#↓
#rota


#response_model=OrdemResponse
#↓
#formato esperado da response_model

#Ordem
#↓
#parametro da funcao

#: OrdemCreate 
#↓
#schema esperado no Request body


#entao essa rotap ode ser mentalmente lida:

# receba um OrdemCreate e devolva um OrdemResponse.



#8. os três juntos

from pydantic import BaseModel, Field 

class OrdemCreate(BaseModel):
    cliente: str
    descricao: str
    valor: float = Field(gt=0)


class OrdemUpdate(BaseModel):
    cliente : str | None = None
    descricao : str | None = None 
    valor: float | None = Field(default=None, gt=0) #gt significa = greather than


class OrdemResponse(BaseModel):
    id: int
    cliente: str
    descricao: str
    valor: float 
    status: str 


#Mentalmente

#OrdemCreaste
#↓
#O que eu preciso para criar ?

#OrdemUpdate
#↓
#O que posso Alterar ?


#OrdemResponse
#↓
#O que a API pode devolver ?