from fastapi import FastAPI, Request ## estamos importando o FastAPI e o Request da biblioteca fastapi 
from fastapi.templating import Jinja2Templates ## estamos importando o Jinja2Templates da biblioteca fastapi


app = FastAPI() # estamos criando uma instancia da classe FastAPI e atribuindo a ela a variavel app
## Criar uma instância da classe FastAPI, que representará nossa aplicação backend.


templates = Jinja2Templates(directory="templates") ## estamos criando uma instancia da classe Jinja2Templates e atribuindo a ela a variavel templates
## templates eh uma instancia da classe Jinja2Templates que recebe os parametros descricao, cliente e valor como parametro
# “Meus arquivos HTML estão dentro da pasta templates.”

## é bom depois colocar um login, registrar-se e logar-se 
## rotas como crud de ordens de servico
## rotas de login, registrar-se e logar-se
## get ordens de servicos | retornar todas as ordens de servicos
## post ordens de servicos | enviar uma ordem de servico
## put ordens de servicos | atualizar uma ordem de servico put quer dizer : atualizar 

## delete ordens de servicos  | deletar uma ordem de servico
## get ordens de servicos por id  | retoornar uma ordem de servico por id
## get ordens de servicos por status  | retornar todas as ordens de servicos por status

## 

@app.get("/ordens-servico") ## estamos criando uma rota que recebe os parametros descricao, cliente e valor como parametros
## o que é uma rota eh uma funcao que recebe os parametros numero, cliente,status  como parametros
#Essa linha registra um endpoint HTTP.

#Significa:

#Quando o navegador realizar uma requisição GET para /ordens-servico, execute a função listar_ordens.

def listar_ordens(request: Request): #request eh uma instancia da classe Request que recebe os parametros numero, cliente,status  como parametros
    # pra que serve request: 
    ordens = [
        {
            "numero": 1, ## estamos criando um dicionario que recebe os parametros numero, cliente,status  como parametros
            # o que é parametro : eh uma variavel que recebe um valor como parametro 
            "cliente": "André",
            "status": "ABERTA"

        },
        {
            "numero": 2, ## estamos criando um dicionario que recebe os parametros numero, cliente,status  como parametros
            # o que é parametro : eh uma variavel que recebe um valor como parametro 
            "cliente": "Kaique",
            "status": "FINALIZADA"

        }
    ]
    return templates.TemplateResponse( ## estamos criando uma instancia da classe TemplateResponse e atribuindo a ela a variavel templates
        request = request, ## estamos criando uma instancia da classe Request e atribuindo a ela a variavel request, por que estamos fazendo isso 
        # ? por que estamos fazendo isso ? porque estamos criando um template dinamico com o fastapi
        name="ordens_servico.html", # estamos criando um template dinamico com o fastapi
        # o que é response ? eh uma resposta que recebe os parametros numero, cliente,status  como parametros

        context={ # estamos criando um dicionario que recebe os parametros numero, cliente,status  como parametros
            
            "ordens": ordens  # 


        }
    )