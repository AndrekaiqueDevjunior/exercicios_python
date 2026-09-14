## SQL ALCHEMY 
## COMO O SQL ALCHEMYU SALVA UM OBJETO NO BANCO

## SESSION.ADD(ORDEM_DB)
## SESSION.COMMIT()
## SESSION.REFRESH(ORDEM_DB)


## e tambem:

##session.rollback() # reverter


## voce ja entende que:

ordem_db = Ordem(**dados)

## cria um objeto SQLALCHEMY;

## mas criar o objeto ainda nao significa que ele foi salvo no PostgreSQL

o fluxo é : 

ordem_db

objeto SQLALCHEMY criado na memória
↓
session.add(ordem_db)

SQLALCHEMY passa a acompanhar esse objeto
↓
session.commit()
↓
confirma a operação no BaseExceptionGroup


session.refresh(ordem_db)
↓
busca novamente os dados atualizados no banco


#session.add(ordem_db) # SQLALCHEMY PASS A ACOMPANHA ESSE OBJETO
#session.add(ordem_db) # session, adicione esse objeto para ser persistido


#session.commit() # confirma a operação no banco

#raio-x
#↓
#session 
#objeto que gerencia a conversa com o banco


#.add
#↓
# é o metodo que  prepara isso para salvar:


#ordem_db
#↓
#objeto SQLALCHEMY que queremos salvar


#importante: o add() não [é o commit]


#mentalmente:

#add()
# -> prepare isso para salvar


#commit()
# -> confirme de verdade



#session.commit()



#agora estamos dizendo:

#confirme as alteracoes no banco

# é aqui que entra o conceito de transação


#imagine:


#antes

#banco:
#nenhuma OS 

#        ↓
#session.add(ordem_db) ### -> prepare isso para salvar



#SQLALCHEMY:
#"Tenho uma nova OS para inserir"

#        ↓
#session.commit() ## # -> confirme de verdade


#PosgreSQL:
#INSERT REALIZADO


##session.refresh()

#depois do commit, o banco pode tert criado informacoes que seu objeto ainda precisa atualizar

#session.refresh(ordem_db)

#agora o objeto  fica sincronizado com os dados atuais do banco.




#rollback()

#agora imagina que deu erro:

try:
    session.add(ordem_db)
    session.commit()

except Exception:
    session.rollback()

#rollback() significa:
# "Desfaça a transação atual e volte ao estado anterior."


#mentalmente:

#tentou salvar
 #   ↓
# deu erro
   # ↓
# rollback()
  #  ↓
#cancela a transação

## isso conecta diretamente com acid e trransacoes que sao conceitos muitos importante em backend.


# o fluxo inteiro


class OrdemRepository:

    def salvar(self, ordem): # criacao de um construtor que passa o self e ordem como parametro.
        self.session.add(ordem)
        self.session.commit() # commit é a funcao
        self.session.refresh(ordem)

        return ordem
#aqui o repository sabe como salvar uma ordem no banc

# ja o servbice pode cuuuidar da regra de negocio:

class OrdemService:

    def __init__(self, repository):
        self.repository = repository

    def criar_ordem(self, ordem):

        if ordem.valor <= 0:
            raise ValueError("Valor Invalido")


        ordem_salva = self.repository.salvar(ordem)

        return ordem_salva


#observe a separação:

SERVICE: 
'Posso criar essa ordem ?'


REPOSITORY:

"Como eu salvo essa ordem ?"


#destrinchando 
def criar_ordem(ordem: OrdemCreate):

def = criando uma função

criar_ordem = nome da função

ordem = nome do parametro

: OrdemCreate = type hint que inidica que ordem deve ser  um objeto do tipo OrdemCreate 

def criar_ordem(ordem: OrdemCreate):

    print(ordem.cliente) # ordem acesse o parametro cliente de OrdemCreate(BaseModel)
    print(ordem.descricao)#ordem acesseo parametro descricao de OrdemCreate(BaseModel)
    print(ordem.valor)# ordem acesse o parametro valor de OrdemCreate(BaseModel)

#aqui voce pode pensar:

#ordem
#↓
#objeto OrdemCreate


#ordem.cliente
#↓
#pegue o atribute cliente deste objeto

#entao sua frase estava quase perfeitrra. eu só ajustaria de:

# parametro ordem que Recebe OrdemCreate

para:

#Parametro ordem, que deve ser do tipo OrdemCreate



session.add(ordem) # session prepare essa ordem para ser salva


#depois:

session.commit # session, confirme as alteracoes no banco.


# e:


session.refresh # session, busque novamente os dados atualizados dessa ordem no banco

#um exemplo completo:

def salvar(self, ordem):
    self.session.add(ordem)
    self.session.commit()
    self.session.refresh(ordem)


    return ordem


#o fluxo é:

#ordem
#↓
#session.add(ordem)
#↓
#SQLALCHEMY começa a rastrear o objeto
#↓
#session.commit()
#↓
#dados sao confirmados no banco
#↓
#session.refresh(ordem)
#↓
#objeto recebe os dados atualizados do banco



session.commit # confirma essa transacao no banco


#então: 
# 
# 
# session.add(ordem) # prepare essa ordem para ser salva
#session.commit() # confirme as alterações no banco
#pode ser lido como:

#add()
#↓
#quero salvar isso


#commit()
#↓
#agora confirme de verdade


#veja este repository:

class OrdemRepository:

    def __init__(self, session): 
        self.session = session 

    def salvar(self, ordem): # funcao ordem que recebe como parametro chamado ordem
        self.session.add(ordem) # # prepare essa ordem para ser salva
        self.session.commit() # # #session.commit() # confirme as alterações no banco


        return ordem # retorne a ordem 

#vamos ver linha por linha

def salvar(self, ordem):
    #crie um metodo chamado salvar que recebe um parametro chamado ordem.


#depois:

self.session

#leia:
#Pegue a session que pertence a este objeto Repository:

#depois:

#self.session.add

#pegue o metodo add dessa session. PEGUE O METODO  add  DESSA SESSION


# e finalmente: 
#self.session.add(ordem)

# execute o método add, passando o objeto ordem

# Ou naquele formato que você estava treinando:

#self
#  ↓
#este REPOSITORY

#self.session
#  ↓
#pegue a Session do REPOSITORY

#self.session.add
#  ↓
#pegue o método add da session


#self.session.add(ordem)
#  ↓
#execute add passando ordem

#FRASE BOA PARA GUARDAR:
#session.add(objeto) coloca o objeto sob gerenciamento da session.
#session.commit() confirma as alterações no banco.

# e existe uma distinção que vale decorar desde ja:

#.add = preparar / rastrear
#.commit = confirmar

#session nao [é o banco, ele é o intermediário]


#refresh serve tambem para, não só ID:

##id
##timestamps
##defaults
## campos alterados pelo banco
## outros valores atuais da linha

# o trio principal

#guarda isso:
session.add(ordem) # "Session, gerencie esse objeto"

session.commit() # "Confirme as alterações no banco"

session.refresh(ordem) # "Busque a versão atual no banco
#e atualize meu objeto"

#Resumo de uma linha:

#Repository = conversa com o banco

#Session = Gerencia as operacoes com o banco

#add = coloca o objeto sob gerenciammento

#commit = confirma a transação

#refresh = recarrega os dados atuais no banco

#1.
#self.session.add(ordem)  = este objeto repository, pegue a session deste repository, pegue o metodo da Session, execute add passando ordem

#2.
#self.session.commit() = este objeto repository, pegue a session deste repository, pegue o metodo da session, execute commmit que confirma a transação.

#3.
#self.session.refresh(ordem) = este objeto repository, pegue a session deste repository, pegue o metodo da session, execute refresh que recarrega os 
# os dados atuais no banco passando ordem como parametro do argumento ( ordem )


#4.ordem_salva = self.repository.salvar(ordem) 
# crianos um objeto chamado ordem_salva, que recebe  este objeto repository, que pega o metodo salvar passando ordemm como parametro do argumento

#5.cliente = ordem.cliente 
# instanciando  o objeto cliente que recebe ordem. cliente, que server para acessar o cliente da ordem 

#exemplo de correção:

def refresh(objeto):

    #aqui:
#objeto = parametro 

#quando fazemos:

#refresh(ordem)
#aqui:
#ordem = argumento

#guarde:
#PARAMETRO
#↓
#APARECE NA DEFINIÇÃO DA FUNÇÃO def refresh(objeto)

#ARGUMENTO
#↓
#APARECE QUANDO CHAMAMOS A FUNÇÃO ordem = argumento


#correção 4. ordem_salva = self.repository.salvar(ordem)

# nao estamos criando um objeto, estamos criando uma variavel chamado (ordem_salva)

##leia assim: 

#self
#↓
#este objeto atual

#self.repository
#↓
#pegue o repository deste objeto

#self.repository.salvar
#↓
#pegue o metodo salvar do repository

#self.repository.salvar(ordem)
#↓
#execute salvar, passando ordem como argumento (COMO ARGUMENTO) salvar(ordem) = salvar função, ordem = argumento

#ordem_salva =
# ↓
# guarde o resultado retornado na variável ordem_salva

ordem_salva = self.repository.salvar(ordem) 

# significa
# execute salvar(ordem) e guarde o resultado na variável ordem_salva
#
#  RESULTADO 
#  _____________    
# |             |
# | ordem_salva | = self.repository.salvar(ordem)
# |             |
# |_____________| guardamos o resultado na variável ordem_salva 

#5. cliente = ordem.cliente

#aqui também tem uma pequena correção.

# voce nao está necessariamente

## instancioando  o objeto cliente.

## voce está criando uma variável chamada cliente.

## cliente = ordem.cliente

## leia:
## pegue o atributo cliente do objeto ordem e guarde seu valor na variavel cliente

#compare:
ordem.calcular_total # sem ()  
# significa Pegue o metodo, catch the method

#com
ordem.calcular_total() # com () 
#significa Execute o método, execute the method


