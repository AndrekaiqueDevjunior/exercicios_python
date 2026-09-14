from fastapi import APIRouter,HTTPException
from app.data.vendas import vendas
from app.services.venda_service import listar_vendas, buscar_venda,adicionar_venda,atualizar_venda,deletar_venda
from app.schemas.vendas import VendaCreate


### pasta APP ( PRINCIPAL)
### pasta data ( sub-pasta  app/data)
### arquivo vendas.py, arquivo python dentro do

router = APIRouter(
    prefix="/vendas",
    tags=["vendas"]

)
#Quando estamos usando APIRouter, 
# quem recebe os decoradores HTTP é o objeto router.



#decorador @app

# LISTAR VENDAS
@router.get("/")
def listar():###funcao listar vendas
    return listar_vendas()



# BUSCAR VENDA
@router.get("/{cliente}")
def buscar(cliente: str):

    venda = buscar_venda(cliente)

    if venda is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"
        )
    return venda



#atualizarvenda
@router.put("/vendas/{cliente}")
def atualizar_venda(cliente: str,
                     novo_valor: int): # type hint client que recebe string
# como parametro

    for venda in vendas:
        if venda["cliente"] == cliente:# estamos puxando cliente que a funcao
            #atualizar_venda (cliente str) parametro cliente com a type hint STRING
            venda["valor"] = novo_valor

            return vendas 

        raise HTTPException(
            status_code=404,
            detail="cliente nao encontrado"
        )

#  raise
#→ dispare um erro

#HTTPException
#→ esse erro será uma resposta HTTP

#status_code=404
#→ código HTTP: recurso não encontrado

#detail="Cliente não encontrado"
#→ mensagem explicando o erro


###excluir venda
@router.delete("/vendas/{cliente}")
def excluir_venda(cliente: str):

    for venda in vendas:
        if venda["cliente"] == cliente:
            vendas.remove(venda)

            return vendas

        raise HTTPException(
            status_code=404,
            detail="cliente nao encontrado"
        )


@router.post("/")
def adicionar(venda: VendaCreate):
## estamos criando a funcao adicionar 
## que recebe como parametro vende e seu type hint VendaCreate
#O  VendaCreate deve ser uma variável que recebe os dados enviados pelo cliente.
    resultado = adicionar_venda(venda.cliente, venda.valor) ## adicionar venda vem de Service 

    return resultado
    

@router.put("/{cliente}") # Esse cliente veio da URL:
#Mas nesse PUT nós não queremos o cliente do objeto venda.
#  Queremos o cliente que veio no caminho da URL.
#Porque {cliente} é um parâmetro de caminho. 
def atualizar(cliente: str, venda: VendaCreate):
            
    resultado = atualizar_venda(cliente, venda.valor)
    #venda.valor veio Do JSON


    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Cliente não encontrado"        
            )
    #atualizar_venda vem de app/venda_service.py

    return resultado


@router.delete("/{cliente}")
#Se queremos acessar:
#DELETE /vendas/Carlos
def deletar(cliente:str):

    resultado = deletar_venda(vendas,cliente)
    #vendas  → lista de vendas
    #cliente → cliente recebido pela URL
    #resultado = excluir_vendas(vendas, "Carlos")
    # acessar lista venda e apontar para o cliente específico

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="cliente não encontrado"
        )

    return resultado

#cliente -> parametro
#str -> Tipo esperado -> string
#valor recebido -> Carlos - valor que o cliente digitou

#venda: Create
# venda é um objeto do tipo VendaCreate

#3. venda e valor
## venda -> objeto
## valor -> atributo


##portando venda.valor é um atributo do objeto venda





#$asyncio.run(main()

#@router.get("/")
#@router.get("/{cliente}/{id}")#futuramente meter um ID 
#@router.post("/")
#@router.put("/{cliente}")
#@router.delete("/{cliente}")



#app = FastAPI()
 #       │
  #      │ include_router()
   #     ▼
#routers/vendas.py

#router = APIRouter()
#        │
#        ├── @router.get()
#        ├── @router.post()
#        ├── @router.put()
#        └── @router.delete()
