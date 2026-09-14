from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class OrdemCreate(BaseModel):
    cliente: str = Field(min_length=3, max_length=100) # minimo de 3 e maximo de 100
    descricao: str = Field(min_length=5, max_length=300) # minimo de 5 e maximo de 300
    valor: float = Field(gt=0) # maior que zero Greater than maior que zero


@app.post("/ordens")
def criar_ordem(ordem: OrdemCreate): # ordem: OrdemCreate. Estamos criando um objeto chamado ordem que recebe a classe OrdemCreate
    return ordem

#agora imagine esta request.

{

    "cliente": "Andre Kaique",
    "descricao": "Troca de SSD",
    "valor": 350.90
}

#fluxo:

Post /ordens
     ↓
Body JSON
     ↓
OrdemCreate
     ↓
Pydantic Valida
     ↓

cliente 
str?
tamanho válido?


descricao
str?
tamanho válido?


valor  
float?
maior que 0 ?


 ↓
criar_ordem(...)

#fastAPI le o JSON, converte os tipos quando aplicavel, valida contrao o modelo Pydantic e entrega o objeto validado para a funcao a da rota.

## mas agora mande :

##nem recebe um modelo válido; a validação acontece antes da execução normal do endpoint.
#FastAPI retorna uma resposta de erro de validação indicando os campos problemáticos


#campo opcional

## também podemos combinar Field() com None:

observacao: str | None = Field(
    default = None, # padrao  padrao igual há None, none significa que o campo eh opcional ou nulo
    max_length = 500 # maximo de 500
)
##um modelo mais realista:

class OrdemCreate(BaseModel): # BaseModel eh uma classe da biblioteca pydantic
    cliente: str = Field(
        min_length=3,
        max_length=100     
    ) # minimo de 3 e maximo de 100 

    descricao: str = Field(
        min_length=5,
        max_length=300   
    ) # minimo de 5 e maximo de 300 

    valor: float = Field(
        gt=0
    ) # maior que zero 

    observacao: str | None = Field(
        default=None,
        max_length=500
    ) # maximo de 500 




##pattern,field_validator

#1. pattern: validar formato de texto

#pattern é usado quando uma str precisa seguir um formato específico.
#O FastAPI/Pydantic suporta esse tipo de validação para strings

from pydantic import BaseModel, Field


class ClienteCreate(BaseModel):
    telefone: str = Field( # telefone: str = Field(
          
        pattern=r"^\d{11}$" # padrao de 11 digitos

    )

#essa regra significa:

## o telefone deve conter exatamente 11 numeros


## então: 

#11999998888 ✅

#11999-98888 ❌
#abc123      ❌
#123         ❌

#raio x do Pattern


#temos:

#^
#↓
#inicio da string

#\d
#↓
#um dígito


# {11} 
# ↓
# exatamente 11 vezes

#$
# ↓
#final da string

#portanto:

#^ \d {11} $

#significa:
# do começo ao fim, quero exatamente 11 dígitos

## isso é uma expressão regular, ou Regex


## 2. outro exemplo perfeito para ordem de Serviço:

## outro exemplo: codigo da OS.

#suponha que todasas ordens tenham este formato:

# OS-1234 

#podemos fazeR:

class OrdemCreate(BaseModel):
    codigo: str = Field(

        pattern=r"^OS-\d{4}$"
    )


#aceita:

#OS-1234
#OS-9999

# a regra:

# OS-\d{4}$


##3. mas Field() tem limite
#imagina uma regra:
# o valor da OS não pode ser menor que R$ 50, se ela for urgente

#isso depende de dois campos.

#urgente
#valor

## 4. field_validator

#no pydantic atual existe o decorador:

# @field_validator(...)

##ele permite criar uma funcao de validacao personalizada para um campo

##exemplo simples:

from pydantic import BaseModel, field_validator 


class OrdemCreate(BaseModel):
    cliente: str 

    @field_validator("cliente")

    @classmethod # classmethod quer dizer: essa funcao eh uma funcao de classe 
    # quer dizer 
    def validar_cliente(cls,valor): 
        if valor.lower() == "teste" # lower quer dizer  tudo em minusculo. valor.lower()  quer dizer == "teste"
            raise ValueError("Cliente não pode se chamar teste")

        return valor

#agora:

OrdemCreate(cliente="Carlos")

#válido


#mas:

OrdemCreate(cliente="Teste")

##gera erro de validation error( validação )


#raio X do validator

#esta parte

@field_validator("cliente")

#é um decorador.

#voce ja estudou decoredores no FASTAPI.

## aqui ele significa 

## aplique ea funcao abaixar para validar o campo Cliente.

#depois:

@classmethod # classmethod quer dizer: essa funcao eh uma funcao de classe específica (CLS)


#indica que o método pertence á classe.

#E:

def validar_cliente(cls,valor):
#é a função que fará a validação 

#O:

#valor

# é o valor recebido 

#se chegou:

{
    "cliente": "Carlos"
}

#a funcao recebe algo equivalente a :

valor = "carlos"



#6. raise ValueError

#aqui:

if valor.lower() == "teste"
    raise ValueError("Cliente não pode se chamar teste")


#voce está dizendo:
# se essa condicao, for verdadeira, interrompa, a validação porque o valor é invalido

#7. e por que existe return valor ?

## isso aqui é muito importante:

return valor 

## se o campoi passou pela validação, voce precisa devolver o valor validado

#fluxo:

"Carlos"
   ↓
validar_cliente()
   ↓
é "teste"?
   ↓
não
   ↓
return "Carlos"
   ↓
Pydantic continua


#8. Podemos também modificar o valor

#Validators não servem apenas para rejeitar.

#Podemos normalizar dados:

from pydantic import BaseModel, field_validator

class ClienteCreate(BaseModel):


    nome: str
    @field_validator("nome")
    @classmethod
    def limpar_nome(cls, valor): # cls vem de classmethod
        return valor.strip()

    #se chegar

    "  Carlos  "

    #a funcao vai devolver:

    "Carlos"

#isso pode ser util para normalizacao.


# 9-field() vs field_validator()

# essa distinção vale guardar:

# field()

# regra simples


#exemplo:

valor: float = Field(gt=0)

#ou 

nome: str = Field(min_lenght=3)

#ou:

codigo: str = Field(
    pattern=r"^OS-\d{4}$"
)


#já 
#field_validator

#regra personalizada

#exemplo:


@field_validator("cliente")
@classmethod

def validar_cliente(cls, valor) # funcao validar cliente, com parametro cls de class method e parametro valor
    if valor_lower() == "teste"
        raise ValueError(...)
    return valor

# o que essa funcao quer dizer: se o campo cliente for teste, interrompa a validação.@#@#@#@#@#@#@# 


## o proximo tema é model_validator, por que ele entra exatamenter quando a regra depende maisd de um campo ao mesmo tempo.

# penmsa assim.
#field_validator
# valida UM campo

#model_validator
#VALIDA O OBJETO INTEIRO
#exemplo de objeto inteiro

# obj = Objeto(

#     campo1="algo",
#     campo2="algo",
#     campo3="algo",
#     campo4="algo",
#     campo5="algo",
# ) 

# exemplo de validação de um objeto inteiro:

@model_validator("objeto")


from pydantic import BaseModel, model_validator 

class OrdemCreate(baseModel):


    valor: float# numeros quebrados
    urgente: bool# true ou false 

    @model_validator(mode="after") # model validator eh um decorador que valida um objeto inteiro 
    # mode quer dizer = depois da validação
    def validar_ordem(self): # self eh o objeto inteiro 

        if self.urgente and self.valor <50: # se a ordem for urgente e o valor for menor que 50
            raise ValueError(
                "Uma Ordem urgen precisa ter valor mínimo de R 50  "

            )

        return self 


#agora vamos fazer o Raio X 

@model_validator(mode="after") #é um decorador do pydantic que valida um objeto inteiro

# ele e esta dizendo:

#depois que os campos forem criados e validados individualmente, execute esta validação do modelo inteiro.

#por isso:

mode="after"

#significa:

#depois da validação normal dos campos.

def validar_ordem(self):

#aqui self representa a instancia do modelo.

# entao conseguios acessar:
self.valor
self.urgente

##assim como em POO:

self.nome
self.idade

#agora a regra

if self.urgente and self.valor < 50:

#leia:
#se a ordem for urgente E o valor for menor que 50


#entao:

raise ValueError(...) 
#faz o pydantic considerar o modelo inválido

#exemplo válido:


{

    "valor": 100,
    "urgente": true
}

#porque: 
urgente = True
valor = 100 

100 < 50 ? 
NotADirectoryError

✅ válido

#agora:

{
    "valor": 20,
    "urgente": true

}

#temos: 

#urgente = True
#valor = 20

#20 < 50?

# INvalido#

# mas isto:

{
    "valor": 20,
    "urgente": false

}

#poderia ser valido, por que nossa regra especial só vale para ordens urgentes.

# a diferença fica bem clara:

class OrdemCreate(BaseModel):

    valor: float
    urgente: bool


# se eu quiser dizer:

# valor sempre precisa ser maior que zero

# uso:

valor : float = Field(gt=0)

#se eu quiser dizer:

# valor precisa respeitar uma regra dependendo de urgente.

# uso: 
@model_validator(mode="after") #decorador de validacao do pydantic que valida um objeto inteiro   

#field()

#regra simple sobre UM campo


#field_validator

#regra personalizada sobre um campo


#model_validastor

#regra envovlendo o modelo inteiro


#um exemplo ainda mais clássico é senha:


from pydantic import BaseModel, model_validator 


class Cadastro(BaseModel): # classe de cadastro

    senha: str # 
    confirmar_senha: str

    @model_validator(mode="after")
    def validar_senhas(self)

        if self.senha != self.confirmar_senha:
            raise ValueError(
                "As senhas não são iguais. Digite as senhas novamente"
                "Verifique se estão iguais."
            )

        return self

#aqui nao da para validar direito olhando apenas:

senha:

# ou apenas:

confirmar_senha

#voce precisa comparar os dois

# por isso MODEL_VALIDATOR


###

from pydantic import BaseModel, field

class Veiculo(BaseModel): # classe de veiculo(basemodel) = parametro BaseModel = veiculo 


    id: int = field(default=None, gt=0)
    placa: str = field(min_length=7, max_length=7)
    cor: str = field(min_length=3, max_length=20)
    motorização: str = field(min_length=3, max_length=20)
    ano: int = field(gt=0) # greather than 0 Maior que 0
    combustivel: str = field(min_length=3, max_length=20)
    nome_veiculo: str = field(min_length=3, max_length=20) 


class VeiculoCreate(BaseModel):

    placa: str = field(min_length=7, max_length=7)
    cor: str = field(min_length=3, max_length=20)
    motorização: str = field(min_length=3, max_length=20)
    ano: int = field(gt=0) # greather than 0 Maior que 0
    combustivel: str = field(min_length=3, max_length=20)
    nome_veiculo: str = field(min_length=3, max_length=20)


#Rota fictícia
@app.post("/veiculos")
def criar_veiculo(veiculo: VeiculoCreate):  #veiculo: VeiculoCreate criamos um veicul do tipo VeiculoCreate
    # isso quer dizer que estamos criando um veiculo do tipo VeiculoCreate 
    return veiculo
#O FastAPI interpreta esse modelo como Request Body e valida os dados antes de executar normalmente a função.

class VeiculoUpdate(BaseModel):

    placa: str | None = None # Agora todos são opcionais.
    cor: str | None = None # Agora todos são opcionais.
    motorização: str | None = None # Agora todos são opcionais.
    ano: int | None = None # Agora todos são opcionais.
    combustivel: str | None = None # Agora todos são opcionais.
    nome_veiculo: str | None = None # Agora todos são opcionais.


class VeiculoResponse(BaseModel):

    id: int = field(default=None, gt=0)
    placa: str = field(min_length=7, max_length=7)
    cor: str = field(min_length=3, max_length=20)
    motorização: str = field(min_length=3, max_length=20)
    ano: int = field(gt=0) # greather than 0 Maior que 0
    combustivel: str = field(min_length=3, max_length=20)
    nome_veiculo: str = field(min_length=3, max_length=20)


#Mentalmente:

#VeiculoCreate:
#
#O que preciso para criar ?



#veiculoUpdate:
#
# o que posso Alterar ?


#VeiculoResponse:
#
#O que  A API pode devolver ?



#json:

{
    placa: "CSB-0H87",
    cor: "Cinza Steel",
    motorização: "Gasolina",
    ano: 1998,
    combustivel: "Gasolina",
    nome_veiculo: "Palio Ex 1998"

}


#Raio-X
#valor: float | None = None

#significa:

#valor
#↓
#campo


#float | None
#↓
#pode ser float OU None


#= None
#↓
#se não vier, o padrão é None


#4. Por que isso combina com PATCH?

#Porque PATCH normalmente representa uma atualização parcial.


#ordem.model_dump(exclude_unset=True) # 

# serve para trabalhar apenas com campos efetivamente enviados na atualização, 
# um padrão mostrado pela própria documentação do FastAPI para updates parciais.

#Exemplo:

#dados = ordem.model_dump(exclude_unset=True)